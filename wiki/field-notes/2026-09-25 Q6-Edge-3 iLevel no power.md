---
type: field-note
manufacturer: Pride
model: Q6-Edge-3
date: 2026-09-25
status: open
tags: [pride, quantum, q6-edge, ilevel, no-power, field-note]
---

# 2026-09-25 — Q6 Edge 3 (standard) with iLevel: no power

**Status: open** — job in progress.

## Unit

- Quantum (Pride) **Q6 Edge 3, standard** — *not* the Stretto. The wiki
  has no manual or model page for the standard Edge 3; the closest is
  [[Q6-Edge-3-Stretto]]. Don't assume Stretto specs carry over.
- Options: **iLevel** power seat elevator.
- Controller: TBD (Stretto ships with Q-Logic 3; confirm on this unit).
- Serial / customer ref: TBD

## Symptom

Completely dark. Pressing on/off gives no joystick light and nothing on the
display. No error code shown.

## Checked

Starting point is the "dead system" checklist from
[[Q6 Edge Basic Troubleshooting]] (p. 1):

- [x] Batteries installed and wired correctly: OK
- [x] Battery terminal connections tight: OK
- [ ] Battery quick-disconnect harness fully joined
- [x] Main circuit breaker reset button pushed in: not tripped
- [ ] Joystick fully connected to the power module
- **Battery voltage: 4 V per battery**, measured directly at each battery's
  terminals with a multimeter on the 200 V DC range. Normal is about 12 V
  per battery, or about 24 V for the pair.

## Root cause

**Likely: the batteries were discharged to nearly zero.** At 4 V there's
far too little voltage for the controller to power up, which explains the
completely dark joystick. Not yet confirmed that new batteries bring it
back.

From the Edge 3 Stretto OM, which we assume also applies to the standard
Edge 3 since both use the same 24 V two-battery system:
- The chair's charger **will not operate once the batteries are discharged
  to nearly zero volts** (OM p. 16 of the PDF). So plugging in the charger
  won't bring these back.
- Batteries that are deeply discharged or stored without a full charge
  "may be permanently damaged" (OM p. 19 of the PDF).

## Fix

TBD. Expected: replace both batteries as a pair. Then check whether the
chair powers up and iLevel works.

## Parts used

TBD

## Takeaways

- **Main circuit breaker location (standard Edge 3):** above the **left
  drive motor**. The troubleshooting sheet says to reset it but doesn't
  say where it is.
- **Dark chair + 4 V batteries = over-discharged batteries.** The charger
  can't recover them. Check battery voltage early, before chasing wiring.
- **Two ways to check voltage:**
  1. **At each battery:** measure across each battery's terminals, with the
     meter on a DC range above 24 V (e.g. 200 V). This is what was done here.
     It shows each battery separately, so a single dead battery stands out.
  2. **At the charger port:** measure the whole pack (about 24 V) without
     removing the shrouds. It's quicker, but it only shows the total, so a
     low reading doesn't tell you which battery is bad. The wiki has no
     pinout for the Q-Logic 3 charger port, so find the +/− pins before
     probing.
- More TBD. Note anything the manual's checklist missed, especially
  anything iLevel-specific.

## See also

- [[Q6-Edge-3-Stretto]]
- [[Q6 Edge Basic Troubleshooting]]
- [[Joystick-Controllers]]
- [[Tru-Balance-3-Power-Positioning]]
