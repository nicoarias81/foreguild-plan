# -*- coding: utf-8 -*-
"""
field_stats.py — Muestreo reproducible del "campo" real de bounties en poidh.xyz/Base.

VENTANA Y CORTE (documentados):
  Ventana  : todos los bounties listados en poidh.xyz/base cuyo campo `createdAt`
             (del endpoint /data del frontend, ver LIMITACIONES) cae dentro de los
             WINDOW_DAYS dias previos a la corrida.
  Corte    : CUTOFF = fecha de corrida (UTC) - WINDOW_DAYS dias. Se imprime al correr.
  Enumeracion: IDs descendentes de frontend desde el maximo ID visible en la home
             de poidh.xyz/base. Los IDs son globales (compartidos entre cadenas);
             se conservan solo los que /data reporta con chainId == 8453 (Base).
             Se detiene al encontrar el primer bounty con createdAt < CUTOFF o al
             agotar MAX_IDS intentos (lo que ocurra primero; se reporta cual).

FUENTES:
  1) https://poidh.xyz/base/bounty/{id}/data  (via proxy de lectura r.jina.ai,
     el host no puede alcanzar poidh.xyz directamente). JSON del frontend:
     status, amount (wei), claims[], createdAt, onChainId, etc.
  2) Base mainnet RPC (base.publicnode.com) para `acceptedAt`: evento
     ClaimAccepted(uint256 indexed bountyId, uint256 indexed claimId,
     address indexed claimIssuer, address bountyIssuer, uint256 bountyAmount,
     uint256 payout, uint256 fee) del contrato v3 0x5555Fa783936C260f77385b4E153B9725feF1719
     (ABI real del frontend: github.com/picsoritdidnthappen/poidh-app, prod).
     Se matchea por (bountyId == onChainId) y (claimIssuer == issuer del claim aceptado).

USO (fases cacheadas en field/cache/):
  python field_stats.py crawl    # descarga /data por id (reanudable)
  python field_stats.py chain    # escanea logs on-chain de aceptacion
  python field_stats.py report   # agrega y escribe field_stats.json + resumen
  python field_stats.py all      # las tres

LIMITACIONES (resumen; detalle en FIELD.md):
  - `createdAt` de /data es la fecha de alta en el sitio, no la del evento
    BountyCreated on-chain (puede diferir por dias/semanas).
  - claims[] del frontend no trae timestamps por claim; acceptedAt sale solo
    del evento on-chain y solo para bounties v3 (id frontend > 986).
  - Muestra de listado: sesga hacia bounties visibles hoy en /base.
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone

import requests

# ----------------------------- configuracion ---------------------------------
CHAIN_SLUG = 'base'
CHAIN_ID = 8453
WINDOW_DAYS = 30
MAX_IDS = 400          # techo de intentos de IDs en el crawl
JINA = 'https://r.jina.ai/'
RPC = 'https://base.publicnode.com'
V3_CORE = '0x5555Fa783936C260f77385b4E153B9725feF1719'
FRONTEND_V2_TO_V3_OFFSET = 986   # id frontend <= 986 => contrato v2 (sin lookup v3)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(BASE_DIR)              # .../foreguild/data
CACHE = os.path.join(BASE_DIR, 'cache')
OUT_JSON = os.path.join(DATA_DIR, 'field_stats.json')

os.makedirs(CACHE, exist_ok=True)

# topic0s del ABI real del frontend (derivados de src/constant/abi/abi.ts)
TOPIC_CLAIM_ACCEPTED = '0x46fffb589554d79a52571e78a5a713b327069bbc5afd8b997c7ca512ab38070a'
TOPIC_BOUNTY_CREATED = '0xd265c5d6a9224c4853317e9e3262b0605b45f0e87c8bfd17d020e54a87c439af'

RUN_TS = datetime.now(timezone.utc)
CUTOFF = (RUN_TS - timedelta(days=WINDOW_DAYS)).replace(hour=0, minute=0, second=0, microsecond=0)

_session = requests.Session()


def log(msg):
    print(f'[{datetime.now(timezone.utc):%H:%M:%S}] {msg}', flush=True)


# ----------------------------- helpers HTTP ----------------------------------
def _get(url, timeout=75, tries=5):
    """GET con backoff ante 429/5xx del proxy jina."""
    last = None
    for i in range(tries):
        try:
            r = _session.get(url, timeout=timeout)
            if r.status_code == 200:
                return r
            last = f'HTTP {r.status_code}'
        except Exception as e:
            last = f'{type(e).__name__}: {e}'
        time.sleep(min(30, 3 * (i + 1) ** 2))
    raise RuntimeError(f'GET {url} fallo ({last})')


def fetch_bounty_data(frontend_id):
    """Devuelve dict /data o None si el id no existe (o no esta publicado)."""
    cache = os.path.join(CACHE, f'data_{CHAIN_SLUG}_{frontend_id}.json')
    if os.path.exists(cache):
        with open(cache, encoding='utf8') as f:
            return json.load(f)
    url = f'{JINA}https://poidh.xyz/{CHAIN_SLUG}/bounty/{frontend_id}/data'
    r = _get(url)
    m = re.search(r'Markdown Content:\s*\n(.*)', r.text, re.S)
    body = m.group(1).strip() if m else r.text
    try:
        data = json.loads(body)
    except Exception:
        data = {'_unparseable': body[:200]}
    with open(cache, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data


# ----------------------------- fase 1: crawl ---------------------------------
def max_front_end_id():
    """Maximo ID de bounty base visible en la home (cacheado por dia)."""
    cache = os.path.join(CACHE, f'home_{CHAIN_SLUG}.json')
    if os.path.exists(cache):
        with open(cache, encoding='utf8') as f:
            return json.load(f)['max_id']
    r = _get(f'{JINA}https://poidh.xyz/{CHAIN_SLUG}', timeout=90)
    ids = [int(m) for m in re.findall(r'poidh\.xyz/%s/bounty/(\d+)' % CHAIN_SLUG, r.text)]
    if not ids:
        raise RuntimeError('home sin IDs de bounty')
    max_id = max(ids)
    with open(cache, 'w') as f:
        json.dump({'max_id': max_id, 'fetched_at': RUN_TS.isoformat()}, f)
    return max_id


def phase_crawl():
    max_id = max_front_end_id()
    log(f'max frontend id en home: {max_id}; cutoff={CUTOFF:%Y-%m-%d %H:%M} UTC '
        f'({WINDOW_DAYS} dias)')
    sampled, stopped_at, attempts = [], None, 0
    fid = max_id
    while fid > 0 and attempts < MAX_IDS:
        attempts += 1
        d = fetch_bounty_data_safe(fid)
        if d and 'id' in d and d.get('chainId') == CHAIN_ID:
            created = int(d.get('createdAt') or 0)
            rec = {
                'frontendId': fid,
                'onChainId': d.get('onChainId'),
                'chainId': d.get('chainId'),
                'title': (d.get('title') or '')[:120],
                'amountWei': d.get('amount'),
                'amountEth': (int(d['amount']) / 1e18) if d.get('amount') else None,
                'priceUsd': d.get('priceUsd'),
                'status': d.get('status'),
                'statusLabel': d.get('statusLabel'),
                'isCanceled': d.get('isCanceled'),
                'isMultiplayer': d.get('isMultiplayer'),
                'inProgress': d.get('inProgress'),
                'createdAtData': d.get('createdAt'),
                'createdAtIso': (datetime.fromtimestamp(int(d['createdAt']), timezone.utc).isoformat()
                                 if d.get('createdAt') else None),
                'nClaims': len(d.get('claims') or []),
                'nAccepted': sum(1 for c in (d.get('claims') or []) if c.get('isAccepted')),
                'acceptedIssuers': [c['issuerAddress'].lower() for c in (d.get('claims') or [])
                                    if c.get('isAccepted')],
                'issuer': d.get('issuer'),
            }
            sampled.append(rec)
            if created and created < CUTOFF.timestamp():
                stopped_at = fid
                log(f'id {fid} creado {rec["createdAtIso"]} < cutoff -> corte')
                break
        fid -= 1
    log(f'attempted={attempts} sampled={len(sampled)} (id inicial {max_id}, '
        f'ultimo revisado {fid})')
    with open(os.path.join(CACHE, 'sample_meta.json'), 'w') as f:
        json.dump({'runTs': RUN_TS.isoformat(), 'cutoff': CUTOFF.isoformat(),
                   'windowDays': WINDOW_DAYS, 'maxFrontendId': max_id,
                   'attempts': attempts, 'stoppedAtId': stopped_at,
                   'lastCheckedId': fid}, f, indent=1)
    return sampled


def fetch_bounty_data_safe(fid):
    try:
        d = fetch_bounty_data(fid)
        if d and '_unparseable' in d:
            return None
        return d
    except Exception as e:
        log(f'  id {fid}: ERROR {type(e).__name__} {str(e)[:80]}')
        return None


def load_sample():
    """Reconstruye la muestra desde el cache (sin re-fetch)."""
    ids = []
    meta_p = os.path.join(CACHE, 'sample_meta.json')
    max_id = 1543
    if os.path.exists(meta_p):
        with open(meta_p, encoding='utf8') as f:
            meta = json.load(f)
        max_id = meta.get('maxFrontendId', meta['lastCheckedId'])
    for fid in range(1, max_id + 2):
        p = os.path.join(CACHE, f'data_{CHAIN_SLUG}_{fid}.json')
        if not os.path.exists(p):
            continue
        with open(p, encoding='utf8') as f:
            d = json.load(f)
        if isinstance(d, dict) and d.get('chainId') == CHAIN_ID and d.get('createdAt'):
            if int(d['createdAt']) >= CUTOFF.timestamp():
                ids.append((fid, d))
    return ids


# ----------------------------- fase 2: chain ---------------------------------
def rpc(method, params, tries=6):
    for i in range(tries):
        try:
            r = _session.post(RPC, json={'jsonrpc': '2.0', 'id': 1, 'method': method,
                                         'params': params}, timeout=60)
            j = r.json()
            if 'error' not in j:
                return j
        except Exception:
            pass
        time.sleep(min(20, 1.5 * (i + 1)))
    raise RuntimeError(f'RPC {method} agoto reintentos')


def block_ts(b):
    cache = os.path.join(CACHE, f'block_{b}.json')
    if os.path.exists(cache):
        with open(cache, encoding='utf8') as f:
            return json.load(f)['ts']
    res = rpc('eth_getBlockByNumber', [hex(b), False])['result']
    ts = int(res['timestamp'], 16)
    with open(cache, 'w') as f:
        json.dump({'ts': ts}, f)
    return ts


def phase_chain():
    cache_p = os.path.join(CACHE, 'chain_events.json')
    if os.path.exists(cache_p):
        with open(cache_p, encoding='utf8') as f:
            prev = json.load(f)
        log(f'chain_events.json existente ({len(prev["accepted"])} accepts) -> skip scan')
        return
    sample = load_sample()
    latest = int(rpc('eth_blockNumber', [])['result'], 16)
    ts_latest = block_ts(latest)
    # inicio del escaneo: createdAt(/data) mas viejo de la muestra menos margen
    # (el alta en DB puede ser bastante posterior al evento on-chain)
    min_created = min(int(d['createdAt']) for _, d in sample)
    scan_start_ts = min_created - 40 * 86400
    # bloque inicial por bisect
    lo, hi = latest - int(1.2 * (ts_latest - scan_start_ts) / 2), latest
    lo = max(lo, 1)
    while lo < hi:
        mid = (lo + hi) // 2
        if block_ts(mid) < scan_start_ts:
            lo = mid + 1
        else:
            hi = mid
    log(f'escaneando eventos desde bloque {lo} (ts {block_ts(lo)}) hasta {latest}')

    pad = lambda n: '0x' + hex(n)[2:].rjust(64, '0')
    accepted, created_ev = {}, {}
    b = lo
    while b < latest:
        hi2 = min(b + 10000, latest)
        j = rpc('eth_getLogs', [{
            'fromBlock': hex(b), 'toBlock': hex(hi2), 'address': V3_CORE,
            'topics': [[TOPIC_CLAIM_ACCEPTED, TOPIC_BOUNTY_CREATED]]}])
        for lg in j.get('result', []):
            bn = int(lg['blockNumber'], 16)
            if lg['topics'][0] == TOPIC_CLAIM_ACCEPTED and len(lg['topics']) >= 4:
                bid = int(lg['topics'][1], 16)
                issuer = '0x' + lg['topics'][3][26:]
                accepted.setdefault(bid, []).append({
                    'claimId': int(lg['topics'][2], 16),
                    'issuer': issuer, 'block': bn})
            elif lg['topics'][0] == TOPIC_BOUNTY_CREATED and len(lg['topics']) >= 2:
                created_ev.setdefault(int(lg['topics'][1], 16), []).append(int(lg['blockNumber'], 16))
        b = hi2
        if b % 200000 < 10000:
            log(f'  progreso: bloque {b}/{latest} ({len(accepted)} accepts, '
                f'{len(created_ev)} creations)')
    out = {'scanFromBlock': lo, 'scanToBlock': latest, 'accepted': accepted,
           'createdBlocks': created_ev}
    with open(os.path.join(CACHE, 'chain_events.json'), 'w') as f:
        json.dump(out, f)
    log(f'eventos: {len(accepted)} bounties con accept, {len(created_ev)} con creation')


# ----------------------------- fase 3: report --------------------------------
def median(xs):
    xs = sorted(xs)
    n = len(xs)
    if not n:
        return None
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def phase_report():
    sample = load_sample()
    with open(os.path.join(CACHE, 'sample_meta.json'), encoding='utf8') as f:
        meta = json.load(f)
    chain = {}
    chain_p = os.path.join(CACHE, 'chain_events.json')
    if os.path.exists(chain_p):
        with open(chain_p, encoding='utf8') as f:
            chain = json.load(f)

    bounties = []
    for fid, d in sample:
        claims = d.get('claims') or []
        accepted_issuers = {c['issuerAddress'].lower() for c in claims
                            if c.get('isAccepted')}
        onchain = d.get('onChainId')
        accepted_at = None
        if onchain is not None and accepted_issuers:
            for ev in chain.get('accepted', {}).get(str(onchain), []):
                if ev['issuer'].lower() in accepted_issuers:
                    accepted_at = block_ts(ev['block'])
                    break
        created = int(d.get('createdAt') or 0)
        bounties.append({
            'id': fid,
            'onChainId': onchain,
            'amount': (int(d['amount']) / 1e18) if d.get('amount') else None,
            'amountUsd': d.get('priceUsd'),
            'entries': len(claims),
            'status': d.get('status'),
            'isCanceled': d.get('isCanceled'),
            'isMultiplayer': d.get('isMultiplayer'),
            'createdAt': (datetime.fromtimestamp(created, timezone.utc).isoformat()
                          if created else None),
            'createdAtData': d.get('createdAt'),
            'acceptedAt': (datetime.fromtimestamp(accepted_at, timezone.utc).isoformat()
                           if accepted_at else None),
            'hasAcceptedClaim': bool(accepted_issuers),
            'issuer': d.get('issuer'),
            'title': (d.get('title') or '')[:120],
        })

    # ---- agregados ----
    entries = [b['entries'] for b in bounties]
    amounts = [b['amount'] for b in bounties if b['amount'] is not None]
    closed = [b for b in bounties if b['status'] != 'in_progress']
    won = [b for b in closed if b['hasAcceptedClaim'] and not b['isCanceled']]
    closed_nowin = [b for b in closed if not b['hasAcceptedClaim'] and not b['isCanceled']]
    canceled = [b for b in closed if b['isCanceled']]
    zero = [b for b in bounties if b['entries'] == 0]

    verdict_hours = []
    for b in bounties:
        if b['acceptedAt'] and b['createdAt']:
            t1 = datetime.fromisoformat(b['createdAt'])
            t2 = datetime.fromisoformat(b['acceptedAt'])
            verdict_hours.append(round((t2 - t1).total_seconds() / 3600, 2))

    # entries por ETH: solo bounties con amount > 0 y > 0 entries
    e_per_eth = [(b['entries'] / b['amount'], b['amount'])
                 for b in bounties if b['amount'] and b['amount'] > 0 and b['entries'] > 0]
    amt_med = median(amounts) if amounts else None
    small = [x for x in e_per_eth if x[1] < amt_med]
    large = [x for x in e_per_eth if x[1] >= amt_med]

    status_counts = {}
    for b in bounties:
        key = f"{b['status']}" + ('/canceled' if b['isCanceled'] else '')
        status_counts[key] = status_counts.get(key, 0) + 1

    result = {
        'meta': {
            'chain': 'base', 'source': 'poidh.xyz /data via r.jina.ai + Base RPC (publicnode)',
            'runAtUtc': RUN_TS.isoformat(),
            'cutoffUtc': CUTOFF.isoformat(),
            'windowDefinition': (f'bounties de poidh.xyz/base con createdAt(/data) >= '
                                 f'{CUTOFF:%Y-%m-%d %H:%M} UTC ({WINDOW_DAYS} dias), '
                                 f'enumerando IDs de frontend desde {meta["maxFrontendId"]} '
                                 f'hacia abajo; intentos={meta["attempts"]}, '
                                 f'corte por: ' + ('cutoff' if meta['stoppedAtId'] else 'MAX_IDS')),
            'nSample': len(bounties),
            'onChainScan': {k: chain.get(k) for k in ('scanFromBlock', 'scanToBlock')} if chain else None,
            'v3Contract': V3_CORE,
        },
        'bounties': bounties,
        'aggregates': {
            'n': len(bounties),
            'entries': {'mean': round(sum(entries) / len(entries), 2) if entries else None,
                        'median': median(entries), 'max': max(entries) if entries else None,
                        'pct_bounties_with_10plus_entries':
                            round(100 * sum(1 for e in entries if e >= 10) / len(entries), 1)
                            if entries else None},
            'zero_entries': {'count': len(zero), 'pct': round(100 * len(zero) / len(bounties), 1)
                             if bounties else None},
            'settlement': {'closed_total': len(closed),
                           'closed_won': len(won),
                           'closed_no_winner': len(closed_nowin),
                           'canceled': len(canceled),
                           'win_rate_of_closed_pct':
                               round(100 * len(won) / len(closed), 1) if closed else None,
                           'win_rate_of_closed_noncanceled_pct':
                               round(100 * len(won) / (len(closed) - len(canceled)), 1)
                               if (len(closed) - len(canceled)) else None,
                           'status_counts': status_counts},
            'time_to_verdict_hours': {
                'n_measurable': len(verdict_hours),
                'median': median(verdict_hours),
                'min': min(verdict_hours) if verdict_hours else None,
                'max': max(verdict_hours) if verdict_hours else None,
                'values': verdict_hours},
            'entries_per_eth': {
                'n': len(e_per_eth),
                'median': round(median([x[0] for x in e_per_eth]), 2) if e_per_eth else None,
                'split_by': f'median amount = {amt_med} ETH',
                'small_half': {'n': len(small),
                               'median': round(median([x[0] for x in small]), 2) if small else None},
                'large_half': {'n': len(large),
                               'median': round(median([x[0] for x in large]), 2) if large else None}},
            'entries_by_amount_half': {
                'split_by': f'median amount = {amt_med} ETH',
                'small_half': {'n': sum(1 for b in bounties if b['amount'] is not None
                                        and b['amount'] < amt_med),
                               'median_entries': median([b['entries'] for b in bounties
                                                         if b['amount'] is not None
                                                         and b['amount'] < amt_med])},
                'large_half': {'n': sum(1 for b in bounties if b['amount'] is not None
                                        and b['amount'] >= amt_med),
                               'median_entries': median([b['entries'] for b in bounties
                                                         if b['amount'] is not None
                                                         and b['amount'] >= amt_med])}},
        },
    }
    with open(OUT_JSON, 'w', encoding='utf8') as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
    log(f'escrito {OUT_JSON}')
    return result


if __name__ == '__main__':
    phase = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if phase in ('crawl', 'all'):
        phase_crawl()
    if phase in ('chain', 'all'):
        phase_chain()
    if phase in ('report', 'all'):
        r = phase_report()
        print(json.dumps(r['aggregates'], indent=1)[:2500])
