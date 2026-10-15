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

## TechMate (dealer troubleshooting tool)

Bruno's dealer portal (brunopartner.com → **TECHMATE**) has an
interactive troubleshooter for stairlifts and VPLs. It's a serial-number
lookup followed by multiple-choice decision trees with photos and
videos. The stairlift half is ingested as
[[TechMate Stairlift Troubleshooter]] and condensed into
[[Stairlift-Troubleshooting]]. The VPL half (35 trees) is pulled to
`MANUALS/Bruno/TechMate/VPL/` but not ingested yet. Its "Contact Bruno"
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

Nothing — all Bruno-authored manuals on disk have been ingested, including
a third ingest pass that added [[ASL-250]] (found via a check of an
out-of-repo `MANUALS/Bruno/` drop).

**Missing manuals:** the **SRE-5000** (added 2026-10-15, see TechMate
above). The Chariot, Joey and Curb-Sider manuals were added 2026-10-08
(ticked off at [[index#Missing manuals]]).

## See also

[[Warranty]], [[Staircase-Measuring-System]], [[Diagnostic-Codes]],
[[Vehicle-Lift-Power-Wiring]], [[Docking-Devices]], [[Gate-and-Door-Interlocks]], [[Hitch-Adapters]],
[[Stairlift-Troubleshooting]], [[Troubleshooting]]
