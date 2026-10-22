---
type: concept
manufacturer: Bruno
tags: [stairlift, bruno, power-swivel, power-footrest, options, install]
---

# Stairlift power options (power swivel and power footrest)

Bruno's two powered seat options across the straight and curved
stairlifts. Power folding rails are on [[Folding-Rail]]. Symptom-first
fixes are on [[Stairlift-Troubleshooting]] §13.

## How the rider uses them

| | SRE-2010 Elite / CRE-2110 Elite Curve | SRE-3050 / SRE-3000 Elan | SRE-5000 Elan |
|---|---|---|---|
| **Power swivel** | At the top, **release the paddle and press it again** (same direction). The seat swivels to its stop and beeps. DOWN or the remote returns it. | Same: **press again** after the stop. | **Keep holding** the paddle at the top and the seat turns. The remote returns it. |
| Swivel range | 0–90° at the top only. On the CRE-2110 the **small cam sets the stop anywhere from 30° to 90°** (large cam = home switch, factory set). | 0–90° at the top | Up to **85°** at the top |
| **Power footrest** | Follows the seat: **raise the seat to fold, lower it to unfold**. | Same | Same; the footrest has a **magnetic break-away** |
| Jams | The swivel won't turn if it senses a jam. The footrest returns to its last position. | Same | Same |

**Never fold a power footrest by hand**: it can damage the unit. The
2026 Elite and Curve owner's manuals show **A6 = seat jammed** and
**A7 = footrest jammed** under the seat ([[Diagnostic-Codes]]).

## Installing (kits, harnesses, torques)

| | Elite (SRE-2010) | Elite Curve (CRE-2110) | Elan (SRE-3050) | Elan (SRE-5000) |
|---|---|---|---|---|
| Guide | [[SRE-2010 Power Seat and Footrest Install (2022)]] | [[CRE-2110 Power Options Install Guide]] | [[SRE-3050 Power Options Install Guide]] | [[SRE-5000 Power Options Install Guide]] |
| Kits | SRE-K-2078WG (swivel seat), SRE-K-2086WG (footrest seat) | per ILS-00937 | SRE-K-3094 (swivel hardware) | per ILS-01616 |
| Footrest to carriage | Kit M10 flat-heads, **50 ft-lb**, as low as possible | Kit M10 flat-heads, **40 ft-lb (54 Nm)** | **40 ft-lb (55 Nm)** with swivel / **50 ft-lb** footrest only (the guide gives both) | Flat-heads **40 ft-lb**, hex **50 ft-lb** |
| Footrest harness to main board | Orange to **"PWR FOOTREST AUX"** | 2-pin to the carriage plug **"FOOTREST"**; 3-pin grey safety harness down into the footrest | Footrest/aux harness to the main PCB | **J1 "PWR FOOTREST AUX"**; aux 3-pin to **J10**, fold switch to **J8 "F-FOLD"** on the footrest PCB |
| Swivel harness | Orange to **"PWR SWV AUX"**; 6- and 12-pin carriage to swivel | Orange to orange, 3-pin, display PCB | AUX 3-pin orange to the large header, swivel 2-pin to the small header | 8-pin carriage jumper out, swivel harness in |
| Seat to swivel | **4 × M6, 150 in-lb** | **4 × M6, 150 in-lb** | Lock plate **6.7 ft-lb**; **drill out the inner countersunk hole** to take out play | 2 × M6 lock plate plus a T25 |
| Seat parts removed | Display PCB detached (hook and loop) and refitted | Same | Release lever, **seat safety switch**, spring, plate. Fit switch PBS-00148. | Swivel lever, spring, **seat safety switch** |
| Seat height | Power footrest: factory 21.8/18.3 in; power seat: 24.3/21.5 in. Bracket **SRE-20710WG** for the highest settings. | M8 flat-heads before mounting | — | Seat adjusts **2 in** (3 in without options) |

**Common to all:**
- **Keep the shipping jumpers** (3-, 6-, 12- or 8-pin). The Elite guide
  says to slide them onto the carriage harness so they're there for
  service calls.
- **Grease the thrust washers** (Elan) or nylon washers on both faces, or
  the seat squeaks as it turns.
- Check the hand (LH or RH) of the swivel assembly before mounting. Elan
  harness holes: c1 LH, c2 RH; footrest-only offset holes H1 LH, H2 RH.
- Route harnesses **clear of the IR/RF eyes** (CRE) and so nothing is
  pinched when the actuator pivots.
- **Never lift the footrest or seat by the actuator** (CRE guide).
- Test: lift the seat and the footrest folds; lower it and the footrest
  drops. At the top, swivel out to the stop (beep), then return.

## Parts (from Bruno's drawings)

| Part | What | Model |
|---|---|---|
| **PCB-00178** / **PCB-00179** | Power swivel / power footrest aux PCBs | SRE-5000 |
| **ADC-24008** | 24 VDC 40 mm footrest actuator | SRE-5000 |
| **SRE-30608** | Power swivel actuator assembly | SRE-3050 (also used on the SRE-5000) |
| **PCB-00127** | Aux power swivel PCB | SRE-3050 |
| **SRE-30211** / **SRE-30021** | Power footrest aux PCB / footrest actuator | SRE-3050 |
| SRE-21358WG | Seat frame, power swivel and power footrest | Elite and Curve |

Sources: [[Parts Drawings - SRE-5000 Elan]], [[Parts Drawings - SRE-3050 Elan]],
[[Parts Drawings - SRE-2010 Elite]], [[Parts Drawings - CRE-2110 Elite Curve]].

## See also

[[SRE-2010]], [[CRE-2110]], [[SRE-3050]], [[SRE-5000]],
[[Stairlift-Troubleshooting]], [[Folding-Rail]], [[Bruno-Parts-Lookup]]
