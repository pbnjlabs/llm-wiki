---
type: concept
manufacturer: Bruno
tags: [bruno, parts, ipb, ordering, serial-number]
---

# Bruno parts lookup and parts drawings

How to find a Bruno part number.

## 1. The portal lookup (best for a specific unit)

Brunopartner → **Service → Parts Lookup by Serial #**
(`/er26ya59sp/parts.aspx`):
- It takes an **exact serial number only**. Partial numbers and model
  names return nothing.
- It returns the order and model code, and **View details** opens the
  unit's **parts list as built**: every assembly with part number,
  revision, description and the dealer's price. Each part number links
  to its drawing PDF.
- The list has checkboxes and a **Submit** button that **emails Bruno a
  parts availability inquiry**. Don't tick or submit them unless you mean
  to send the inquiry.
- **Parts Pricing & Ordering** (`parts-search.aspx`) is the ordering
  side. Portal prices are **manufacturer suggestions**, not PMS rates.
- Serial format and product codes: [[Bruno-Serial-Numbers]].

## 2. The parts drawings on file (no serial needed)

Bruno's assembly drawings are public at
`/Uploads/Public/Documents/Drawings/<part>.pdf`. On 2026-10-22 the
wiki pulled **252 of them** into `MANUALS/Bruno/Parts/`, starting from
each model's top-level drawing and going three assembly levels down
(manifest `MANUALS/Bruno/Parts/_manifest.md`). Each family page lists the
drawings and a **key service parts** table: motors, boards, chargers,
batteries, belts, brakes, actuators, switches, remotes, harnesses, ACME
screws and nuts, bearings, springs and wheels.

| Family | Page |
|---|---|
| SRE-5000 Elan | [[Parts Drawings - SRE-5000 Elan]] |
| SRE-3050 / SRE-3000 Elan | [[Parts Drawings - SRE-3050 Elan]] |
| SRE-2010 Elite | [[Parts Drawings - SRE-2010 Elite]] |
| CRE-2110 Elite Curve | [[Parts Drawings - CRE-2110 Elite Curve]] |
| VPL-3153B/3175B and AC 3153/3175 | [[Parts Drawings - VPL Residential Short (3153-3175)]] |
| VPL-3210B/3212B/3214B | [[Parts Drawings - VPL Residential Tall (3210B-3214B)]] |
| VPL-3353B/3375B, 3310B–3314B | [[Parts Drawings - VPL Commercial (3353B-3375B, 3310B-3314B)]] |
| Vehicle lifts (Out-Sider, Chariot, Out-Rider, Stow-Away, Joey, Curb-Sider, Big-Lifter, Lifter, Back-Saver) | [[Parts Drawings - Vehicle Lifts]] |

**Caveats:**
- The drawings are **Bruno's current revision**. Older units may have
  different parts (for example, the Elite gear motor changed in Feb 2025
  and the SRE-5000 board changed in Aug 2026). For an older unit, run the
  serial on the portal.
- **540 referenced part numbers have no drawing on Bruno's server**
  (all checked: 404). These are mostly single parts and hardware; their
  descriptions are still in the parent drawing's table.
- SRE-2010 and SRE-5000 have no model-level drawing. Their pages start
  from the carriage, seat and rail part numbers in the manuals' exploded
  views. The outdoor SRE-2010OS has none at all.
- Valet seat parts were skipped.

**Common cross-model parts** (from the drawings):

| Part | What it is | Used on |
|---|---|---|
| **BCR-24020** | 24 VDC 5 A charger | All battery VPLs |
| **BTR-12001** | 12 V 33 Ah U1 battery | Tall residential and commercial VPLs |
| **BTR-12002** | 12 V 7 Ah | SRE-2010, CRE-2110 |
| **BTR-12008** | 12 V 3 Ah | SRE-3050 |
| **BTR-12010** | 12 V 3.2 Ah AGM | SRE-5000 |
| **BCR-24024** | 24 VDC 2 A charger | Elite and Elite Curve |
| **TMR-00004** | IR remote (2 AA) | SRE-2010, SRE-3050, SRE-5000 |
| **CBK-30004** | 30 A breaker with aux switch | Elite carriages |
| **SRE-27391** | Seat user interface PCB | Elite and Elite Curve |
| **VPL-31119** | Manual lowering handwheel | All VPLs |

## See also

[[Bruno]], [[Bruno-Serial-Numbers]], [[VPL-Drive-Service]], [[Stairlift-Troubleshooting]], [[VPL-Troubleshooting]]
