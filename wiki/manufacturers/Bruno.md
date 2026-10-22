---
type: manufacturer
manufacturer: Bruno
tags: [manufacturer, stairlift, vehicle-lift]
---

# Bruno

Independent Living Aids manufacturer — stair lifts, vehicle/porch lifts, and
vertical platform lifts (VPL).

## Product lines

- **Bruno Curved SL** — curved-rail stair lifts. **Fully ingested.**
  - [[CRE-3110]] — newer curved rail (2026 spec sheet only): 300 lb,
    0–65°, Smart Swivel for 26 in stairs
  - [[CRE-2110]] ("Elite Curve") — custom curved rail; shares
    [[Rail-Mounting-Guidance]] and [[Diagnostic-Codes]] with the straight
    Elite/Elan line; overspeed brake is optional (not standard like the
    straight-rail line); reset by cranking the motor shaft CCW (8 mm) and
    turning the trip plate back to neutral (2026 manuals; the 2018
    two-lever reset is superseded) — see [[Overspeed-Safety-Brake]].
  - Ordering the custom rail uses Bruno's [[Staircase-Measuring-System]]
    (Picture Perfect / StairsChecker 3.0 camera kit) — a dealer tool, not
    part of the stairlift.
  - One document found in this folder (`HARMAR Camera Measuring Manual.pdf`)
    turned out to belong to a different manufacturer entirely — see
    [[Harmar]]. Likely misfiled; not moved since raw sources are
    immutable.
  - Also found: an "Elite 2010 conversion" doc that's actually
    [[SRE-2010]] content (opposite-hand conversion), not curved-rail —
    folded into the SRE-2010 page instead.
  - The general Bruno stairlift warranty (5yr major components/2yr parts;
    **limited lifetime** on SRE-3000/2010/2010C made after 2 Apr 2018, per
    [[Bruno Warranty Summary]]) is documented once at [[Warranty]] rather
    than per-model.
- **Bruno Straight SL** — straight-rail stair lifts. **Fully ingested.**
  - [[SRE-2010]] ("Elite") — recommended for scoot-pivot transfers / leg
    weakness that Elan can't safely handle
  - [[SRE-3050]] ("Elan") — current generation, successor to SRE-3000
  - [[SRE-3000]] ("Elan", legacy) — same platform as SRE-3050, only a 2015
    manual on file
  - [[SRE-5000]] ("Elan", 2026) — newest straight rail; full manual set
    (install, owner's, TSG, power options, folding rail) pulled 2026-10-22
  - **2026 power folding rail update** (Bruno dealer email, clipped
    2026-10-13): board PCB-00193 replaces PCB-00157 on future SRE-3050 and
    SRE-2010 power folding rails. See [[SRE-3050 and SRE-2010 Power Folding Rail Logic Board Update]].
  - Both model lines share [[Overspeed-Safety-Brake]], [[Folding-Rail]],
    and [[Rail-Mounting-Guidance]] — Bruno reuses the same safety
    mechanisms, folding-rail hardware family, and anchoring guidance
    across the whole Straight SL line.
- **Vehicle Lifts** — **Fully ingested.**
  - [[PUL-1100]] ("Out-Rider") — truck-bed-mounted arm lift for storing an
    empty wheelchair/scooter
  - [[ASL-275]] ("Out-Sider"/Out-Sider with Swing-Away) — hitch-mounted
    platform lift for scooters/powerchairs
  - [[ASL-250]] ("Out-Sider"/Out-Sider with Swing-Away, legacy) —
    ASL-275's predecessor (2019 manual); same branding, different
    platform lineup including a ramped "HTP" variant not documented on
    ASL-275
  - [[ASL-700]] ("Chariot") — **wheeled** hitch-mounted platform carrier
    with its own tires, lights and VIN (title paperwork); Class I/II
    1.25 in hitch only, 350 lb
  - [[VSL-4400]] ("Joey") — inside platform lift for vans, minivans and
    SUVs; mandatory door safety switch; 350 lb
  - [[VSL-6000-6900]] ("Curb-Sider") — boom/hoist lift for minivans,
    SUVs and pickups; 6900 adds a power-telescoping head; 250–450 lb
  - Added 2026-10-22 from Brunopartner Service Docs:
    - [[VSL-570]] ("Big-Lifter"): 400 lb in-vehicle boom hoist, the
      Curb-Sider's predecessor generation.
    - [[AWL-150]] ("Lifter"): 200 lb in-vehicle hoist for a manual chair
      stored upright.
    - [[AWL-1600]] ("Back-Saver"): hitch lift for a folded manual chair,
      with the Hold-Tite clamp.
    - [[PUL-1850]] ("Stow-Away"): under-vehicle **transfer seat** for
      pickups, 300 lb user, runs only with the door open.
    - Operator manuals for the ASL-275, ASL-250, PUL-1100 and VSL-4400,
      plus the legacy VSL-4000HW Joey manuals.
  - All three original lifts share [[Vehicle-Lift-Power-Wiring]] (battery routing/wiring
    pattern — ASL-250 confirms the inline fuse is specifically ATO 30A)
    and a 3-year vehicle-lift variant of [[Warranty]] — distinct terms
    from the stairlift warranty (3yr flat vs. 5yr/2yr split).
- **VPL** — vertical platform lifts. **Fully ingested.**
  - [[VPL-3100B]] — smaller porch/deck lift, 53"/75" max floor-to-floor,
    hand-wheel-only emergency operation
  - [[VPL-3200B]] — larger hoistway lift, up to 123" (3.1m) floor-to-floor,
    electrical emergency lowering kit + hand wheel, two-section tower
    joined on site
  - [[VPL-3153-3175]] — the **AC** low-rise VPL (no "B"): 2025 install
    and 2024 operator manuals (pulled 2026-10-22), plus tech tips. PCB-00143
    90 V board, LEDs E1–E18 and fault flash codes
  - [[VPL-3300B]]: the **commercial** line (VPL-3353B/3375B,
    VPL-3310B/3312B/3314B): install and operator manuals, 3-gate and
    enclosure supplements (pulled 2026-10-22), plus ILS sheets
  - [[VPL-3200B]] also has a **flood zone tower** (VPL-3210B-OFZ; it won't run in
    more than 3 in of standing water)
  - Drive work for all of them: [[VPL-Drive-Service]]; schedules and
    inspections: [[VPL-Maintenance]] (ILS-01444)
  - Both share [[Top-Landing-Gate-Installation]] and
    [[Battery-Charger-LED-Diagnostics]] — same gate hardware/procedure and
    charger diagnostics reused verbatim across both install manuals.

## Tech Tips (dealer-portal library)

Bruno's dealer portal (brunopartner.com → Service → **Tech Tips**) is a
searchable library of short Bruno Technical Service documents. All 165
entries were listed on 2026-10-21; 107 stairlift, VPL, vehicle lift and
general files were downloaded to `MANUALS/Bruno/Tech Tips/`
(manifest in `_manifest.md` there). Valet turning seats were skipped,
and three VPL links were broken on Bruno's server.

**Stairlifts: ingested 2026-10-21** (46 files, 33 source pages titled
"Tech Tip - …"). Most date from 2013–2016 and were written for the
SRE-3000 Elan, the SRE-2010 Elite and the CRE-2110; none name the
SRE-3050. Highlights: the Elan brake kit SRV-3000-016, motor-lead
voltages, the SRE-2010C drop test, gear rack and clamp part numbers,
ride-out, folding-rail fixes, and serial number decoding
([[Bruno-Serial-Numbers]]). Yearly service is summarized on
[[Stairlift-Maintenance]].

**VPL: ingested 2026-10-21** (49 files, 25 source pages). Older step
guides for units TechMate doesn't support (pre-2012 low-rise and tall,
AC before 2017), the AC PCB-00143 board's fault flash codes, shipping
jumper sheets, drive work (screw, nuts, bearing, belts, guide pads),
timers and interlock wiring, tall-VPL rigging notes, and a 2011 VPL-3200B
lower-interlock field notice. New pages: [[VPL-Drive-Service]] and
[[VPL-3153-3175]] (the AC low-rise VPL). Three VPL tips are broken links
on Bruno's server (Electric Strike Offerings, Von Duprin 6211, Fuse &
Circuit Breaker Listing).

**Vehicle lift and general tips: ingested 2026-10-21** (12 files, 9
source pages): Chariot spec sheet, lights and wiring, certificate
replacement; PUL-1100 dimensions; the older **VSL-4000HW Joey**
troubleshooting guide (now on [[VSL-4400]]); the trunk-lift motor note;
the Auto Meter RC-300 battery tester; Bruno's return goods policy; and
the 2018 serial number list ([[Bruno-Serial-Numbers]]). **All 107
downloaded tech tips are now ingested.**

**Legacy vehicle lifts:** the **VSL-4000HW** Joey (before the VSL-4400;
its 2017 install and 2013 operator manuals arrived 2026-10-22, see
[[VSL-4400]]), and the older **AWL-100/125/160 and VSL-175** trunk lifts
(hoist motor MDC-12009; see
[[Tech Tip - Trunk Lift Motor MDC-12009 Replacement]]). The current
**AWL-150** has its own page ([[AWL-150]]).

They're manufacturer-authored, so they rank like TechMate: above
clippings, **below the manuals**. Where they disagree, the pages say so.

## Legacy stairlifts

Older Bruno models still in the field. Their 2007–2011 manuals were
pulled from Brunopartner Service Docs on 2026-10-22.
- [[CRE-2100]] **Electra-Ride III**: the curved rail before the CRE-2110
  (2009 install and operator manuals, 2001 spec sheet).
- [[SRE-2000]] **Electra-Ride Elite**: 400 lb straight rail before the
  SRE-2010. It has a two-lever overspeed reset and a DIP #4 coast delay.
- [[SRE-2750]] **Electra-Ride LT**: 275 lb, ½ hp, aluminum channel rail
  (clamp bolts only 10 ft-lb). It came before the Elan.
- [[SRE-1550]] **Electra-Ride II** (and SRE-1540): 350 lb, steel channel
  rail, belt-and-pulley drive (seat comparison, duct-tape overspeed
  test).
- [[SRE-3000]] Elan: the 2019 trilingual install and operator manuals
  supersede the 2015 install manual.

See [[Tech Tip - Legacy SRE-1540, SRE-1550 and SRE-2000]] and
[[ILS - Legacy Stairlift Sheets (SRE-2000, Decals, Molding Standard)]].

## TechMate (dealer troubleshooting tool)

Bruno's dealer portal (brunopartner.com → **TECHMATE**) has an
interactive troubleshooter for stairlifts and VPLs. It's a serial-number
lookup followed by multiple-choice decision trees with photos and
videos. The stairlift half is ingested as
[[TechMate Stairlift Troubleshooter]] and condensed into
[[Stairlift-Troubleshooting]]. The VPL half is ingested as
[[TechMate VPL Troubleshooter]] and condensed into [[VPL-Troubleshooting]];
it also covers the AC and commercial VPL models (VPL-3153/3175,
VPL-3353B/3375B, VPL-3310B/3312B/3314B), whose manuals arrived 2026-10-22. Its "Contact Bruno"
and "order a part" buttons send the session to Bruno, so only click them
on purpose.

TechMate also covers the **SRE-5000**, a newer Bruno straight stairlift
with three carriage terminal switches, its own beep codes and its own
folding rail. PMS sells and services it (per the human, 2026-10-15). Its
manuals and tech support guide were pulled from Brunopartner on
2026-10-22 ([[SRE-5000]]).

## Drawings (ILS instruction sheet library)

Brunopartner → **Drawings** is Bruno's library of numbered instruction
sheets (**ILS-xxxxx**) and part drawings: 4,601 entries. On 2026-10-21
the 1,368 ILS entries were pulled, classified from their own title pages,
and **636 relevant sheets** saved to `MANUALS/Bruno/Drawings/`
(Stairlifts 161, VPL 134, Vehicle Lifts 277, Docking Devices 60,
General 3; manifest `_manifest.md`). Skipped: Valet seats, kits for
discontinued vehicle lifts, image-only scans and part drawings.

**Stairlifts ingested 2026-10-21** (161 sheets, 31 "ILS - …" source
pages). Headlines: the **ILS-01446 maintenance control plan**, SRE-5000
and CRE-3110 specs, brake kits for every carriage, the Feb 2025 Elite gear
motor change, SRE-3050 Service Bulletin 81 seat fixes, folding rail
install numbers, flood sensor and USB kits, and current spec sheets for
every model.

**VPL ingested 2026-10-21** (134 sheets, 15 source pages). Headlines:
the **ILS-01444 maintenance control plan** ([[VPL-Maintenance]]: weekly,
6-month/yearly, 5-year; **Mobil Aviation Grease SHC 100**; belts about
½ in, which conflicts with the 2016 tip's ⅛ in, and the newer ILS
wins), 2026 spec sheets for VPL-3100 and VPL-3210B plus the VPL-3353B
commercial sheet ([[VPL-3300B]]), application drawings for every
layout, gate and flush-door details, ACME screw/nut/pin service
including the nut safety switch test tool, AC brake retrofits,
interlock wiring (24 VAC vs 24 VDC), timers and door operators (DS-4H
codes), 3-stop and redundant limit kits, cold-weather kits, electrical
retrofits (PCB-00164, aux disconnect, 240 V), travelling cable, flood
sensors, shipping.

**Vehicle lifts ingested 2026-10-21** (277 sheets, 8 source pages). Most
are **vehicle fitment**: [[ILS - Curb-Sider Sub-Base Fitment by Vehicle]]
(144 bases), [[ILS - Joey Mounting Kit Fitment by Vehicle]] (60 kits) and
[[ILS - Pickup Truck Bases and Stow-Away Mounting Kits]]. The rest are
service sheets per lift: Curb-Sider (lift belt, head assembly, controller
retrofit, capacity decal), Joey (belt, motors, wheels, VSL-4000HW
override), Out-Sider (hitch adapters, platform setup, fold cam, trailer
wiring and resistor kits, camera), Chariot (linkage, actuator, latch,
wheels, camera), Out-Rider and the **PUL-1850 Stow-Away**.

**Docking devices and general notices ingested 2026-10-22** (63 sheets):
[[ILS - Docking Device Fitment by Mobility Device]] (60 sheets, mostly
1999–2015 scooters and chairs) and
[[ILS - General Install Notices (Hybrid Vehicles, ESD, Dielectric Grease)]].
**All 636 downloaded Drawings sheets are now ingested.**

Bruno also publishes Australian-market addenda for its G models
([[ILS - Stairlift Australian Addenda]]); they're not US requirements.

ILS sheets are Bruno's own installation and service documents (the same
series the manuals are built from), so they rank **with the manuals**:
where they disagree, the newer revision wins.

Bruno Technical Service: 1-800-656-0552.

## VA FSS

Bruno's own VA FSS price list (65 II A: CRE, SRE and VPL units and
options, government warranty, returns): [[Bruno VA FSS Price List (2021-2026)]]. PMS's Bruno dealer (Solutions) has an FSS contract for
Bruno **vehicle lifts only** (65 II F); it doesn't handle 65 II A. See
[[VA-FSS-Contracts]].

## Not yet ingested

All Bruno-authored manuals on disk have been ingested, including
a third ingest pass that added [[ASL-250]] (found via a check of an
out-of-repo `MANUALS/Bruno/` drop). All 107 dealer-portal tech tips in
`MANUALS/Bruno/Tech Tips/` were ingested 2026-10-21 (46 stairlift, 49
VPL, 9 vehicle lift, 3 general).

**Missing manuals:** the **SRE-5000** install, operator and tech support
manuals (added 2026-10-15; the ILS sheets cover specs and service but the
manuals are still needed). Bruno's **ILS-01446** maintenance control plan
was found in the Drawings library and ingested 2026-10-21. The Chariot, Joey and Curb-Sider manuals were added 2026-10-08
(ticked off at [[index#Missing manuals]]).

## See also

[[Warranty]], [[Staircase-Measuring-System]], [[Diagnostic-Codes]],
[[Vehicle-Lift-Power-Wiring]], [[Docking-Devices]], [[Gate-and-Door-Interlocks]], [[Hitch-Adapters]],
[[Stairlift-Troubleshooting]], [[VPL-Troubleshooting]], [[Troubleshooting]],
[[Stairlift-Maintenance]], [[Bruno-Serial-Numbers]], [[CRE-2100]]
