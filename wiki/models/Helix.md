---
type: model
manufacturer: Harmar
model: Helix (CSL Series)
tags: [stairlift, harmar, curved-rail]
---

# Helix (CSL Series)

Harmar's curved-rail residential stairlift — "Helix" is the marketing name
for the **CSL500, CSL510, CSL511, CSL560, CSL570, CSL589, CSL590, CSL595**
series models (named together in the owner's manual's warranty section;
individual model differences aren't documented in the one manual on
file). Harmar's curved-rail counterpart to Bruno's [[CRE-2110]] — see
[[Staircase-Measuring-System]] for how the two manufacturers' custom-rail
ordering/measuring processes compare.

## Specs / key features
- 350 lb max payload
- Folds at parking position; Harmar claims smaller rail-to-wall clearance
  and a higher max incline angle than competing stairlifts (no numeric
  angle given in this manual)
- Retractable seat belt, footrest obstruction sensors, rail/step
  obstruction sensors, folding armrests/seat/footrest
- Optional: emergency stop button, key lock
- 3-color chassis status light: red = major fault, yellow = obstruction,
  green = ready
- Diagnostic port (connector present, no field-service procedure
  documented in the owner's manual on file)

## Remotes (Oct 2021 change)
Per [[Harmar Product Insights (2021-2023)]]: a new-look remote shipped from **October 2021**, same
functions, **25% more range**, better encoding, no repeaters needed.
Fits older Helix lifts **only if the chassis circuit board is replaced
with the remotes**. Same housing as Pinnacle remotes but **not
interchangeable**. Helix team: helix@harmar.com, 800-833-0478.

## Documents on file
- [[Harmar Product Insights (2021-2023)]] — new remote (dealer sheet)
- [[Helix Owner's Manual]] — end-user manual (2021 Rev D)
- [[Helix Install Manual]] — dealer install/service manual (2021 Rev D)
- [[Helix Photo Measuring Manual (2023, Rev C)]] — Helix PhotoMap
  staircase-measuring kit, a newer revision of the doc misfiled as
  [[CSL Series Photo Measuring Manual]] under Bruno's folder
- [[Harmar Wiring Schematics]] — Helix III (2014) and OSG (2021)
  electronics schematics

**Harmar training videos** (timestamped; the manuals win any conflict):
- [[Video - How to Measure for a Helix Stair Lift]] — PhotoMap camera kit: markers, shooting order, common mistakes
- [[Video - How to Install a Helix Stair Lift]] — full install, rail to final checks
- [[Video - Correct Position of the Lower Roller Assembly (Helix)]] — **false final limit at the bottom = flipped lower roller**; plunger above the bottom track
- [[Video - Helix Curved Stairlift Diagnostic]] — laptop diagnostic software on the chassis port; switch-by-switch screen
- [[Video - How to Change the Helix Batteries]] — series jumper, black/red leads
- [[Video - How to Change the Helix Board]] — board terminals (C±, M1 red / M2 black, B±, BK1/BK2, 30-pin), anti-static strap
- [[Video - How to Use the Helix Sales Demo Kit]] — sales points: ~7 in from the wall, 8 lb/ft rail, bottom-mounted (lubricated) gear rack

## Overspeed mechanism
Confirmed **standard equipment** (not optional) on both commercial and
residential Helix installs per its order form, ASME 18.1-2017 compliant.
Mechanically it is **a jammer, not a centrifugal governor**: moving a
release arm drops a jammer between the gear rack and sprocket, and a
limit switch cuts power. Field-resettable by pushing the jammer back into
place — a genuinely different mechanism from Bruno's centrifugal governor,
Prism's motor-replacement design, and Harmar's own HighlanderII OSG
switch. See [[Overspeed-Safety-Brake]] for the full manufacturer
comparison. Note: wiring schematics show Harmar's internal naming for
this assembly shifted from "Parachute Centrifugal Brake" (2014, "Helix
III" hardware) to "Overspeed Safety Switch"/"OSG" (2021) — see
[[Harmar Wiring Schematics]]; not fully reconciled with the jammer
mechanism described above.

## Diagnostics
Beep-code major-fault table shared with SL300/SL600 (near-identical, one
extra code) — see [[Harmar-Stairlift-Beep-Codes]].

## On PMS's VA FSS contract

On Supply's 65 II A contract ([[PMS FSS Price List 65 II A (2021-2026)]]): CSL590-18 (90° turn, 18 ft rail), CSL580-18 (180° turn, 18 ft rail), the 90° and 180° parks (CSL011 / CSL012) and extra track over 20 ft (CSL030, per foot). **The CSL580 isn't in the owner's manual's model list**; it's almost certainly the 180° Helix, but nothing on file confirms it. Curved stairlifts can't be returned on PMS's FSS terms.

## Warranty
Limited lifetime on motor/gearbox/rail, 2yr other parts, 1yr batteries —
see [[Harmar-Warranty]].

## See also
[[Harmar]], [[Pinnacle-SL300]], [[Pinnacle-SL600]],
[[Harmar-Stairlift-Beep-Codes]], [[Harmar-Warranty]],
[[Staircase-Measuring-System]], [[Overspeed-Safety-Brake]]

Site evaluation: [[Stairlift-Evaluation]] (PMS stair lift evaluation form and photo guide).
