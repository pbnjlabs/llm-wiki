---
type: concept
tags: [diagnostics, harmar, stairlift, beep-codes]
---

# Harmar Stairlift Beep Codes

[[Helix]], [[Pinnacle-SL300]], and [[Pinnacle-SL600]] all use the same
beeps-only major-fault diagnostic scheme (no separate LED status light
carries fault detail — Helix and SL300 both do have a basic 3-color
chassis/armrest light, but neither documents distinct light **patterns**
per fault the way Harmar's [[HighlanderII]] VPL does). Confirmed
**near-identical, not quite identical** across the three straight/curved
stairlift models — worth checking against an install manual if one is
ever ingested, since only owner's manuals are on file for all three so
far.

## Major fault table (beeps counted after the first power-on beep)

| Beeps | Fault | Helix | SL300 | SL600 |
|---|---|---|---|---|
| 1 | Runaway | ✓ | ✓ | ✓ |
| 2 | No 12V power on board / No power | ✓ | ✓ | ✓ |
| 3 | Conflicting FOOTREST UP / FOOTREST DOWN | ✓ | ✓* | ✓ |
| 4 | Conflicting OBSTRUCTION UP / OBSTRUCTION DOWN | ✓ | ✓* | ✓ |
| 5 | Conflicting FOOTREST UP / OBSTRUCTION DOWN | ✓ | ✓* | ✓ |
| 6 | Conflicting FOOTREST DOWN / OBSTRUCTION UP | ✓ | ✓* | ✓ |
| 7 | Conflicting STOP UP / STOP DOWN both detected | ✓ | ✓ | ✓ |
| 8 | Conflicting STOP UP / STOP DOWN both NOT detected | ✓ | ✓ | ✓ |
| 9 | FINAL LIMIT switch detected | ✓ | — | ✓ |

\* SL300's manual marks beeps 3-6 "if configured for your model" — the
only one of the three to caveat these codes as option-dependent.

**SL300 has no code 9** — its table stops at 8. Not confirmed whether
SL300 genuinely lacks a final-limit-switch fault or the code table is
simply incomplete in that manual.

## Minor faults (SL300/SL600 only — not broken out separately in the
Helix manual)
Single long beep, self-clears once resolved: seat swiveled out of
position, edge/obstruction safety triggered, footrest fault, current
overload, low battery voltage. SL300 additionally documents Power
Swivel- and Power Footrest-specific fault/recovery procedures (self-
resetting fuses, 1-2 minute reset waits) not applicable to SL600, since
those options aren't mentioned in its manual.

## Charging-related beeping (all three)
An intermittent beep (not a fault code — no LED/fault state) sounds when
the lift is stopped somewhere other than a charge strip; it repeats every
5 minutes until the lift is returned to a charging position at either end
of the rail.

## See also
[[Helix]], [[Pinnacle-SL300]], [[Pinnacle-SL600]], [[Harmar]],
[[Diagnostic-Codes]] (Bruno's equivalent scheme — unrelated, not
compatible)
