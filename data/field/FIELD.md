# Campo real de poidh en Base — muestreo de 30 días

Corrida: **2026-11-09** (`field_stats.py`, reproducible con `python field_stats.py all`).
Ventana: **los 58 bounties de poidh.xyz/base con `createdAt` (alta en el sitio) entre
2026-10-12 16:11 y 2026-11-08 03:59 UTC** — corte definido como `createdAt >= 2026-10-10 00:00 UTC`
(30 días antes de la corrida). Enumeración por IDs de frontend descendentes desde 1540;
el corte se activó solo (id 1482 creado 2026-10-09 17:29 UTC < cutoff).
Datos crudos por bounty: `../field_stats.json` (`bounties[]`), cache crudo en `field/cache/`.

## Resultados

| Métrica | Valor |
|---|---|
| **1. Entries por bounty** | media **10.4**, mediana **6.5**, máximo **77** (bounty 1500, 0.0935 ETH); bounties con ≥10 entries: **41.4%** |
| **2. Settlement** (36 vencidos/cerrados) | **30 con claim aceptado (won), 0 cerrados sin ganador, 6 cancelados** → 100% de los completados tuvieron ganador (83.3% si los cancelados cuentan como "cerrados sin ganador") |
| **3. Tiempo a veredicto** | mediana **90.8 h** (~3.8 días), media 118.5 h, rango 0.01–366 h; medible en **30/30** bounties completados (evento on-chain `ClaimAccepted`) |
| **4. Entries por ETH** | mediana global **1628 entries/ETH**; mitad chica (<0.0025 ETH): **4000**/ETH; mitad grande: **909**/ETH. En términos absolutos, bounties grandes reciben más entries: mediana **8 entries** (grandes) vs **3** (chicos) |
| **5. Sin ningún entry** | **6 de 58 (10.3%)** |

22 de 58 (37.9%) seguían `in_progress` al corte y siguen acumulando entries.

## Metodología

- Fuente web: `GET poidh.xyz/base/bounty/{id}/data` vía proxy de lectura `r.jina.ai`
  (el host no alcanza poidh.xyz directo). De ahí salen `status`, `amount` (wei),
  `claims[]` (entries), `createdAt`, `onChainId`.
- Fuente on-chain: eventos `ClaimAccepted(uint256 indexed bountyId, uint256 indexed claimId,
  address indexed claimIssuer, ...)` del contrato v3 de poidh en Base
  (`0x5555Fa783936C260f77385b4E153B9725feF1719`, ABI real del repo del frontend), escaneados
  con `eth_getLogs` sobre `base.publicnode.com` desde el bloque 51,623,299 al 55,134,351.
  El `acceptedAt` se matchea por `bountyId == onChainId` **y** `claimIssuer == issuer del claim
  aceptado en /data`. Los 30 completados matchearon 1:1; verificación de referencia:
  bounty frontend 1533 (on-chain 547) → claim 4095, issuer `0xad0442...`, bloque 5,387,043.

## Limitaciones

1. **Muestra chica y de un corte**: 58 bounties en 30 días; un solo snapshot. Los abiertos
   (37.9%) aún pueden recibir entries, por lo que la media de entries está subestimada para
   bounties jóvenes.
2. **Sesgo de listado**: sólo se ven bounties publicados hoy en el sitio. Un bounty creado
   on-chain y nunca listado (o retirado) no aparece. El `createdAt` de /data es la **alta en
   la DB del sitio**, no el evento `BountyCreated` on-chain: la diferencia puede ser de días o
   semanas (ej. bounty 1533: creado on-chain ~2026-10-10, alta en el sitio 2026-11-06).
   Consecuencia: el tiempo a veredicto mide *alta-en-el-sitio → aceptación on-chain*, lo que
   **subestima** el tiempo desde creación on-chain.
3. **`acceptedAt` sólo existe on-chain**: los claims del endpoint /data no traen timestamps.
   Bounties del contrato v2 (id de frontend ≤ 986) no tienen lookup; no afecta esta ventana
   (ids 1483–1540, todos v3).
4. **Cuatro veredictos < 1 h** (0.01–0.06 h): self-claims — el issuer acepta segundos después
   de publicar. Son legítimos pero distorsionan el mínimo; la mediana es robusta a ellos.
5. **entries/ETH es muy sensible a premios minúsculos** (mínimo 0.001 ETH): la mediana global
   (1628) está dominada por bounties chicos; por eso también se reporta entries absolutos por
   mitad de tamaño (3 vs 8).
6. **No se puede saber con estos datos**: (a) por qué un bounty termina sin ganador (0 casos en
   la ventana, así que el punto es menor); (b) si el sitio oculta claims baneados o spam — se
   cuenta lo que `claims[]` expone; (c) bounties cancelados *antes* de listar; (d) claims
   on-chain que el frontend no refleja (los IDs de claim de la DB del sitio difieren de los del
   contrato; la comparación se hace por issuer).
7. **Monotonía asumida del `createdAt` con el ID** para el corte por cutoff: si un id menor
   hubiera sido listado después del cutoff, quedaría fuera de la muestra (efecto marginal).
