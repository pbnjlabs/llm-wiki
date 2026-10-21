---
type: concept
tags: [vpl, bruno, maintenance, inspection, grease, belts, batteries, asme-a18-1, joint-commission]
---

# VPL Maintenance (Bruno)

Preventive maintenance and inspection on Bruno vertical platform lifts.
The main source is Bruno's **ILS-01444 Maintenance Control Plan for
VPLs** (08/01/22,
[[ILS-01444 Maintenance Control Plan for VPLs]]). The 2025
[[VPL-3100B Install Manual]] and [[VPL-3200B Install Manual]] (p.41 / p.52)
both point to it and say Bruno **recommends it for every unit, whatever
code year it was installed under**. Keep a copy **with the unit's
manuals** for inspectors.

PMS follows the Joint Commission DMEPOS standards: maintenance **at the
manufacturer's intervals, with a record** ([[Joint-Commission-DMEPOS]]).
For a Bruno VPL, that means the schedule below.

## How often

| What | How often | Source |
|---|---|---|
| Operational checklist (16 items: controls, stops within ½ in, E-stop, alarm, charger LEDs, gates and interlocks, safety pans, emergency lowering) | **Weekly** for commercial (A18.1 Section 2) lifts; optional for residential (Section 5) | ILS-01444 |
| Door interlocks hold (electronic: won't move with a door open; **GAL: moves no more than 2 in** off the landing); **safety pans** work | **Every 2 months** | 3100B / 3200B manuals |
| Drive (belts and tension, pulleys and keys, motor, ACME screw and nuts, screw grease, pads and rollers, bearing), batteries, stops within ½ in, controls, wiring, cleanliness ("not uncommon to remove mouse nests"), **mechanical upper gate lock lubricated**, **battery load test** | **Every 12 months**, more often under hard use | 3100B / 3200B manuals |
| Routine inspection (A18.1-2017 10.2) | **6 months commercial, 1 year residential** | ILS-01444 |
| Periodic tests: safeties, terminal stops (10.3.1) | **Yearly** | ILS-01444 |
| Acceptance and 5-year test: **bottom stop with 125% load**, top stop empty, speed (10.3.3) | **Every 5 years** | ILS-01444 |
| **Coastal / salt-air sites**: inspect and lubricate | **Every 4 months** | ILS-01444 |
| Checklist log and maintenance/repair log | **Keep 5 years** | ILS-01444 |

## The drive

- **Grease the ACME screw with Mobil Aviation Grease SHC 100 (Bruno
  LUB-00114)**: degrease first (Super Clean or similar). The manuals,
  ILS-01444 and the 2022 tall screw/nut sheet all name it.
  **Bearings:** Mobil Epic EP 102 through the zerk, 1–2 squirts.
  **Guide rails are not lubricated.**
- **Nuts:** drive (top) nut and safety (bottom) nut **about ½ in
  apart**; the four drive-nut bolts have **at least ¼ in of play**. Check
  for brass filings and nut-to-screw wear. **Test the nut safety switch
  with tool VPL-32422** (ILS-01544): if the tool won't fit between the
  plate and the switch, the drive nut has dropped: **replace both nuts**.
  **Never bypass the switch.** Details: [[VPL-Drive-Service]].
- **Tall VPLs:** the screw joint pins about 8 ft up must sit below the
  thread root. If they're proud, use pin kit SRV-3200-001 (ILS-01185) and
  nut kit SRV-3200-002.
- **Belts: about ½ in deflection** halfway between the pulleys, one belt
  at a time. Tall units: **idler set with a torque wrench at 60 in-lb**.
  ⚠️ The 2016 tech tip says **⅛ in at 2½–3½ lb**
  ([[Tech Tip - VPL Field Tensioning of Belts]]). The two may be the same
  tension measured differently (the tip specifies a force; ILS-01444
  doesn't), but they're written differently. **ILS-01444 is newer and
  ranks with the manuals, so use ½ in.** Use the tip's force figure only
  with a belt tension gauge, and never leave a belt loose enough to slip
  under load.
- **Brake:** **commercial and newer residential VPLs have no separate
  brake**; older residential units have one on top of the tower. Check it
  releases and holds. AC VPL-3153/3175 units with drift problems may have
  the 2013 brake retrofit
  ([[ILS - VPL Brake Retrofit Kits (AC VPL-3153-3175)]]).

## Switches and safeties

Lower, middle and upper **limits**; **final limit** (stops it, won't run
up); gate **enable switches**; **top cover switch** (three positions);
**safety pans** (press each side in 3 spots, going down it must stop);
**E-stop**; **flood sensor** if fitted (a damp cloth across the pins stops
it, [[ILS - VPL Flood Sensor Kits]]); **redundant landing limits** if
fitted (either switch stops it, [[ILS - VPL 3-Stop and Redundant Limit Switch Kits]]).
Gates and doors must **lock within 2 in** of the platform leaving the
landing ([[Gate-and-Door-Interlocks]]).

## Batteries (DC units)

AGM, **17 Ah or 34 Ah** pairs. Load test (e.g. RC-300); **replace below
70%**. House standard: **replace both batteries as a matched set**
([[Mobility-Batteries]]). Dielectric grease on connections exposed to
weather. Charger LEDs: **solid red = AC on, flashing red = no AC, yellow
= charging, green = full**; the full table is on
[[Battery-Charger-LED-Diagnostics]]. Cold climates: heater pads below
20 °F ([[ILS - VPL Cold Weather and Battery Kits]]).

## Site checks

Lighting **50 lx** at the landings; **sill gap 3/8–3/4 in**; headroom
**79 in** (80 in ADA); door operator holds the door **at least 20 s**;
fascia sound. A plywood fascia delaminating after 6 years jammed a
3100B ([[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]]).

## Finish

Treat rust early. **Touch-up paint is free under warranty** (champagne
PNT-00107 / SPC-00105, graphite PPN-00104 / SPC-00104, tan PPN-00107 /
SPC-00107). Wax the paint, and keep salt and de-icer off the lift.

## Joint Commission

Record every visit: date, checks done, parts, batteries, who did it.
ILS-01444's weekly checklist log and maintenance/repair log (5 years) are
a ready-made format. Evacuation steps (lower landing: push the gate rod
up or use the bypass key; upper landing: push the actuator wheel up)
belong in owner training ([[Joint-Commission-DMEPOS]]).

## See also

[[VPL-Drive-Service]], [[VPL-Troubleshooting]], [[VPL-3100B]],
[[VPL-3200B]], [[VPL-3300B]], [[VPL-3153-3175]], [[Stairlift-Maintenance]],
[[Bruno]]
