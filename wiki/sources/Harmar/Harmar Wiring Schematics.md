---
type: source
manufacturer: Harmar
doc_type: Engineering Wiring Schematics
tags: [harmar, wiring-schematic, helix, sl600, vpl400-x, pinnacle]
---

# Harmar Wiring Schematics

Six engineering wiring-diagram/schematic drawings, grouped into one
source page (drafting-standard diagrams, not narrative documentation).

## Helix — two overspeed-terminology generations
- `Harmar-640-00008_D.pdf` ("SCHEMATIC, HELIX III", DWG 640-00008 Rev D,
  24-Nov-14) — an older Helix electronics schematic (for a "Helix III"
  hardware generation not named elsewhere) labels the overspeed assembly
  a **"PARACHUTE CENTRIFUGAL BRAKE"**.
- `Harmar-640-00028-REVA.pdf` ("HELIX OSG SCHEMATIC", DWG 640-00028 Rev A,
  13JUL21 — seven years newer) labels the same general assembly an
  **"OVERSPEED SAFETY SWITCH"**, and titles the whole drawing "OSG" —
  the same term Harmar uses for [[HighlanderII]]'s Over-Speed Governor
  switch. **Not fully reconciled** with the jammer mechanism described in
  [[Helix Install Manual]]: it's plausible the trigger is centrifugal
  (hence "parachute centrifugal brake") while the stopping action is the
  rack/sprocket jammer the install manual documents, and that Harmar's
  internal naming shifted from "parachute brake" to "OSG" between 2014
  and 2021 without the mechanism necessarily changing — but this isn't
  confirmed from parts diagrams alone. See [[Overspeed-Safety-Brake]].

## VPL400-X wiring set
- `Harmar-640-00033-_Rev-B.pdf` ("VPL400-X BLOCK DIAGRAM", DWG 640-00033
  Rev B, 11-MAR-2024) and the 6-sheet `Harmar-650-00010-_Rev-B.pdf`
  ("VPL400-X Main Wiring Diagram / Cab Control / Landings / Limit
  Switches / Trailing Cable") — confirm the combined OSG/pit/bottom-final
  switch circuit and platform-gate interlock wiring matches
  [[VPL400-X Install Manual]]'s description exactly.

## Pinnacle SL300/SL600 control PCB
- `Harmar-650-00001-01_K.pdf` ("SCHEMATIC, PINNACLE CS PCB", DWG
  650-00001-01 Rev K) — its connector configuration table names **four
  SL600 chassis sub-variants: STD, RAVE, LLSL, and HD** (matching the
  "RAVEII"/"LLSL" data-label variants seen in
  [[Harmar Parts Diagrams]] and independently corroborating "SL600HD"
  from [[Bulletin - Pinnacle Rail Length Change]] as a real variant, not
  a typo), plus SL300 FR/COS and an unexplained "IPL" configuration.

## SL600 Power Swivel / EZ-Footrest wiring
- `Harmar-650-00011-_REV_A.pdf` ("Wiring Diagram SL600 Easy Footrest and
  Power Swivel Option", DWG 650-00011 Rev A, 21JUN23) — confirms Harmar's
  internal name for the power footrest option is **"EZ-Footrest"**, and
  that this wiring existed by June 2023, well before
  [[Pinnacle Power Swivel and Power Footrest Install Supplement]]
  (Oct 2025) documented the install procedure.

## Feeds into
[[Helix]], [[HighlanderII]], [[Pinnacle-SL600]], [[Overspeed-Safety-Brake]]
