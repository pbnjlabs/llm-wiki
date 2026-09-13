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

## Documents on file
- [[Helix Owner's Manual]] — end-user manual (2021 Rev D)
- [[Helix Install Manual]] — dealer install/service manual (2021 Rev D)
- [[Helix Photo Measuring Manual (2023, Rev C)]] — Helix PhotoMap
  staircase-measuring kit, a newer revision of the doc misfiled as
  [[CSL Series Photo Measuring Manual]] under Bruno's folder
- [[Harmar Wiring Schematics]] — Helix III (2014) and OSG (2021)
  electronics schematics

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

## Warranty
Limited lifetime on motor/gearbox/rail, 2yr other parts, 1yr batteries —
see [[Harmar-Warranty]].

## See also
[[Harmar]], [[Pinnacle-SL300]], [[Pinnacle-SL600]],
[[Harmar-Stairlift-Beep-Codes]], [[Harmar-Warranty]],
[[Staircase-Measuring-System]], [[Overspeed-Safety-Brake]]
