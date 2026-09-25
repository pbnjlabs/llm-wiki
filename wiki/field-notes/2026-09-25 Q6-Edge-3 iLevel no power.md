---
type: field-note
manufacturer: Pride
model: Q6-Edge-3
date: 2026-09-25
status: open
tags: [pride, quantum, q6-edge, ilevel, no-power, field-note]
---

# 2026-09-25 — Q6 Edge 3 (standard) with iLevel: no power

**Status: open.** Replaced both batteries. The chair powers on, and on the return visit it passed the full function test and the charger completed a full cycle. Why the old batteries ran down is still unknown. On the same visit the joystick was found with a frayed cable and is being replaced. Check the chair after the joystick swap, then close the note.

## Unit

- Quantum (Pride) **Q6 Edge 3, standard** — *not* the Stretto. The wiki
  has no manual or model page for the standard Edge 3; the closest is
  [[Q6-Edge-3-Stretto]]. Don't assume Stretto specs carry over.
- Options: **iLevel** power seat elevator.
- Controller: joystick part # **CTL143976**. Family (Q-Logic 3 or other)
  TBD; the Stretto ships with Q-Logic 3.
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
- **Battery age: less than 1 year.** Worn-out batteries don't explain this,
  so something ran them down.

## Root cause

**Confirmed: the batteries were discharged to nearly zero.** At 4 V there's
far too little voltage for the controller to power up, which explains the
completely dark joystick. The chair powered on as soon as new batteries went in.

From the Edge 3 Stretto OM, which we assume also applies to the standard
Edge 3 since both use the same 24 V two-battery system:
- The chair's charger **will not operate once the batteries are discharged
  to nearly zero volts** (OM p. 16 of the PDF). So plugging in the charger
  won't bring these back.
- Batteries that are deeply discharged or stored without a full charge
  "may be permanently damaged" (OM p. 19 of the PDF).

**Why they ran down: unknown.** The cause wasn't found on this job. The batteries are less than a year old, so
look at how they were charged or stored. Things to rule out, from
[[Q6 Edge Basic Troubleshooting]] (p. 1) and the OM:
- The charger plugged into an outlet controlled by a wall switch that
  was turned off.
- An extension cord (Pride prohibits them for charging).
- Charged too rarely or too briefly. Pride says to charge overnight
  (8–14 hrs) with daily use, and for 12–14 hrs at least once a week even
  when the chair isn't used.
- The chair stored or left sitting without being charged or unplugged
  from the batteries.
- The charger itself not working. Test it on the new batteries: its
  output, and whether it finishes a charge.
- Something draining the batteries while the chair is off. This is a
  guess, not from any source; the wiki doesn't cover it.

## Fix

Replaced both batteries. **The chair powered on.**

Function test on the return visit, after the new batteries charged:
**passed, all functions working** (drive, controller, iLevel up/down,
other seat functions). **The charger completed a full cycle** on the new
batteries, so a charger that doesn't work at all is ruled out as the
cause.

**Joystick replaced (return visit).** The joystick cable was frayed. It
was replaced with a new joystick with the same part number, **CTL143976**.
The **SD card from the old joystick was moved into the new one**, so the
customer's programming and settings carry over. **On power-up with the
old SD card, the new joystick forced an update.** Details (what was
updated, how long it took, whether it finished cleanly) TBD. Post-swap
check: **pending**.

## Parts used

- 2 × **Interstate DCM0055**, 12 V 55 Ah
  - 55 Ah is one of the two capacities listed for the Edge 3 Stretto (40 or
    55 Ah; see [[Q6-Edge-3-Stretto]]). The wiki has no spec sheet for the
    standard Edge 3.
- 1 × joystick controller, **CTL143976** (same part number as the one
  removed). The old joystick's SD card was reused.

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
- **New batteries (less than a year old) dead at 4 V: find the cause
  before closing the job.** Otherwise the replacement set will die the
  same way. The wiki has no Pride battery warranty terms, so ask Pride or
  the battery supplier about coverage.
- **Joystick replacement: move the SD card from the old joystick into the
  new one** so the customer's configuration stays the same. This is PMS
  field practice; the wiki's sources don't cover the SD card. Check the
  new part number matches the old one first (here both were CTL143976).
  **Expect a forced update** when the new joystick first powers up with the
  old SD card, and let it finish before testing. The wiki's sources don't
  cover joystick updates.
- **Inspect the joystick cable on any service visit.** The frayed cable
  here wasn't related to the no-power complaint and was found during the
  function test visit.
- More TBD. Note anything the manual's checklist missed, especially
  anything iLevel-specific.

## See also

- [[Q6-Edge-3-Stretto]]
- [[Q6 Edge Basic Troubleshooting]]
- [[Joystick-Controllers]]
- [[Tru-Balance-3-Power-Positioning]]
