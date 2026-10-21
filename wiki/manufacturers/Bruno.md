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
  - [[CRE-2110]] ("Elite Curve") — custom curved rail; shares
    [[Rail-Mounting-Guidance]] and [[Diagnostic-Codes]] with the straight
    Elite/Elan line; overspeed brake is optional (not standard like the
    straight-rail line) and uses a different two-lever reset — see
    [[Overspeed-Safety-Brake]].
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

**VPL, vehicle lift and general tips: downloaded, not yet ingested.**

They're manufacturer-authored, so they rank like TechMate: above
clippings, **below the manuals**. Where they disagree, the pages say so.

## Legacy stairlifts (tech tips only)

Older Bruno models that appear only in tech tips. No manuals are on file.
- [[CRE-2100]] **Electra-Ride III**: the curved rail before the CRE-2110
  (2001 spec sheet).
- **SRE-1540 / SRE-1550**: older straight lifts with belt-and-pulley
  drives (seat comparison, duct-tape overspeed test).
- **SRE-2000**: overspeed test fixture and cam reset shared with the
  CRE-2100/2110.
- **SRE-2750**: mentioned only as the Elan's predecessor for battery
  range (10–15 trips).

See [[Tech Tip - Legacy SRE-1540, SRE-1550 and SRE-2000]].

## TechMate (dealer troubleshooting tool)

Bruno's dealer portal (brunopartner.com → **TECHMATE**) has an
interactive troubleshooter for stairlifts and VPLs. It's a serial-number
lookup followed by multiple-choice decision trees with photos and
videos. The stairlift half is ingested as
[[TechMate Stairlift Troubleshooter]] and condensed into
[[Stairlift-Troubleshooting]]. The VPL half is ingested as
[[TechMate VPL Troubleshooter]] and condensed into [[VPL-Troubleshooting]];
it also covers AC and commercial VPL models the wiki has no manuals for
(VPL-3153/3175, VPL-3353B/3375B, VPL-3310B/3312B/3314B). Its "Contact Bruno"
and "order a part" buttons send the session to Bruno, so only click them
on purpose.

TechMate also covers the **SRE-5000**, a newer Bruno straight stairlift
with three carriage terminal switches, its own beep codes and its own
folding rail. **No SRE-5000 manual is on file.** PMS sells and services
it (per the human, 2026-10-15), so it's on the index's
[[index#Missing manuals]] checklist.

Bruno Technical Service: 1-800-656-0552.

## VA FSS

Bruno's own VA FSS price list (65 II A: CRE, SRE and VPL units and
options, government warranty, returns): [[Bruno VA FSS Price List (2021-2026)]]. PMS's Bruno dealer (Solutions) has an FSS contract for
Bruno **vehicle lifts only** (65 II F); it doesn't handle 65 II A. See
[[VA-FSS-Contracts]].

## Not yet ingested

All Bruno-authored manuals on disk have been ingested, including
a third ingest pass that added [[ASL-250]] (found via a check of an
out-of-repo `MANUALS/Bruno/` drop). **Pending:** 61 dealer-portal tech
tips in `MANUALS/Bruno/Tech Tips/` (VPL 49, Vehicle Lifts 9, General 3);
the 46 stairlift tips were ingested 2026-10-21.

**Missing manuals:** the **SRE-5000** (added 2026-10-15, see TechMate
above), and Bruno's **ILS-01446** Maintenance Control Plan for CRE/SRE
chair lifts (ASME A18.1-2017 units; added 2026-10-21, see
[[Stairlift-Maintenance]]). The Chariot, Joey and Curb-Sider manuals were added 2026-10-08
(ticked off at [[index#Missing manuals]]).

## See also

[[Warranty]], [[Staircase-Measuring-System]], [[Diagnostic-Codes]],
[[Vehicle-Lift-Power-Wiring]], [[Docking-Devices]], [[Gate-and-Door-Interlocks]], [[Hitch-Adapters]],
[[Stairlift-Troubleshooting]], [[VPL-Troubleshooting]], [[Troubleshooting]],
[[Stairlift-Maintenance]], [[Bruno-Serial-Numbers]], [[CRE-2100]]
