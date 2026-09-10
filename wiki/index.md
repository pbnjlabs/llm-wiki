---
type: index
---

# Index

Entry point for every query — check here first before opening raw manuals.

## Manufacturers

| Manufacturer | Page | Manuals on disk | Ingested |
|---|---|---|---|
| Bruno | [[Bruno]] | 20 | 10 |
| Golden | [[Golden]] | 66 | 0 |
| Pride | [[Pride]] | 10 | 0 |
| Prism | [[Prism]] | 1 | 0 |

## Models

| Model | Manufacturer | Page |
|---|---|---|
| SRE-2010 (Elite) | Bruno | [[SRE-2010]] |
| SRE-3000 (Elan, legacy) | Bruno | [[SRE-3000]] |
| SRE-3050 (Elan) | Bruno | [[SRE-3050]] |
| VPL-3100B | Bruno | [[VPL-3100B]] |
| VPL-3200B (VPL-3210B) | Bruno | [[VPL-3200B]] |

## Concepts

| Concept | Page |
|---|---|
| Overspeed safety governor | [[Overspeed-Safety-Brake]] |
| Folding rail (manual/power) | [[Folding-Rail]] |
| Rail mounting/anchoring guidance | [[Rail-Mounting-Guidance]] |
| Top landing gate installation (VPL) | [[Top-Landing-Gate-Installation]] |
| Battery charger LED diagnostics (VPL) | [[Battery-Charger-LED-Diagnostics]] |

Other candidates flagged but not yet written: Brake-Replacement,
Joystick-Controllers, Seat-Systems, Troubleshooting (general,
non-Bruno-specific).

## Sources

Bruno Straight SL (6 of 6 ingested) — see `wiki/sources/Bruno/Bruno Straight SL/`:
2010-TS Tech Support Guide, 3050-I Install Manual, 3050-O Operator Manual,
3050-TS Tech Support Guide, SRE-2010 Folding Rail Install Manual,
SRE-3000 Installation Manual.

Bruno VPL (4 of 4 ingested) — see `wiki/sources/Bruno/VPL/`: VPL-3100B
Install Manual, VPL-3100B Operator Manual, VPL-3200B Install Manual,
VPL-3200B Operator Manual.

Everything else below is still backlog, not ingested.

## Ingestion backlog

### Bruno (10 of 20 files remaining)
- Bruno Curved SL/ — 2110-TS Tech Support Guide, Bruno Camera Overview,
  Bruno Elite 2010 conversion, Bruno Stair Lift Warranty, CRE-2110 Elite
  Curve Installation, HARMAR Camera Measuring Manual, Picture Perfect
  Instructions, Picture Perfect Stairs Checker 3.0
- Vehicle Lifts/ — 1100-I PUL-1100 Installation, 275-I ASL-275 Install Manual

### Golden (66 files)
See [[Golden]] for the model-family breakdown. Full file list:
`MANUALS/Golden/*.pdf` (flat directory, ~60 accessory/model docs covering
GA541, GB1xx Buzzaround, GC2xx-4xx Companion/LiteRider, GL1xx LiteRider,
GP1xx/GP6xx Compass/Alante/Envy, plus chargers and cross-model accessory
installs).

### Pride (10 files)
J6 (3), Q6 Edge 3 Stretto (3), Q-Logic/Q-Logic 3 (3), Tru-Balance 3 (1). See
[[Pride]].

### Prism (1 file)
C-450/C-625 tech manual. See [[Prism]].

## How to use this wiki

1. **Querying?** Start here, follow links into `manufacturers/`, `models/`,
   or `concepts/` pages. If nothing covers your question yet, say so — the
   PDF backlog above is the fallback.
2. **Ingesting a new manual (or an existing backlog one)?** Follow the
   workflow in `/CLAUDE.md` — pick one manual or a tight cluster, read it,
   write/update its `sources/` page, its `models/` page, any `concepts/`
   pages it touches, then update this file and `log.md`.
