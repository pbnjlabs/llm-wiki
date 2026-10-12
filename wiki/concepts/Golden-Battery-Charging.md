---
type: concept
tags: [golden, battery, charging]
---

# Golden Battery Charging

General battery care/charging guidance plus operation of Golden's two
documented off-board chargers. Cross-model — not tied to one specific unit.

Sources: [[Battery Charging Insert]], [[Connecting the Batteries]],
[[HP8204B Charger Operation]], [[MRC24-4LX Charger Operation]].

## General charging guidance (from "Battery Charging" and "Connecting the
Batteries" inserts)

- New batteries must be charged 12 hours before first use, even if the
  gauge already shows full — conditions the battery for max performance.
- Daily use: plug in the off-board charger after every use, 6-8 hours
  (overnight recommended).
- Storage over a week: fully charge, then disconnect batteries from the
  unit; check stored batteries monthly and recharge as needed.
- Never use an automotive or "wet type" charger — off-board charger only.
- Never let batteries sit in a low state of charge.
- Connecting batteries for the first time varies by model: plug-in,
  hardware assembly, or removing shipping spacer blocks — always defer to
  the specific unit's owner's manual.

## Model-specific charging notes (from service guides and manuals)

- **Buzzaround XL (GB117/147):** charge at the battery pack or the tiller
  port. Batteries read about **27 V** at rest and rise to about **29.5 V**
  with the charger plugged in. Fuses: 5 A charger fuse, 40 A battery fuse
  ([[GB1xx-Buzzaround-XL]]).
- **Buzzaround EX (GB118/148):** 10 A charger fuse; dual packs charge on
  the charging dock ([[GB118-148-Buzzaround-EX]]).
- **GB120 Carry On:** 24 V lithium pack, about 29 V when full
  ([[GB120-Buzzaround-CarryOn]]).
- **GB106 Buzzaround Lite (S-Drive):** the charger won't work if the
  batteries are too low; boost-charge them first.
- **GR595 Eagle:** 8 A high-power charger, XLR port ([[GR595-Eagle]]).
- **GP302 Cricket:** 2 A lithium charger. The LED is **blue while
  charging and green when full**. Charge 5–8 h after use
  ([[GP302-Cricket]]).
- **GP620 Compass HD (Shark):** battery load test, driving with someone
  seated, should hold about **24 V** or more ([[Shark-Diagnostics]]).
- **PG VR2 chairs** (GP160, GP204/215, GP205): charge through the
  joystick's charger socket ([[TruCharge-Diagnostics]]).

## HP8204B charger

- AC input switch: 115VAC (USA/Canada) vs. 230VAC (overseas) — confirm
  before switching.
- XLR cable connects to the unit's off-board charging port.
- LED states: red (Power) + yellow (Charge) = charging normally;
  red + green = full charge; red with Charge LED off = battery not
  connected; no LEDs = check AC input switch, ON/OFF switch, and
  connections.
- Fuse: 10A 125V/250V, replace only when charger is off and unplugged.

## MRC24-4LX charger

- MRC Technology Inc., 29.5VDC / 4A output, 120VAC 1.5A input.
- Two LEDs only: red = charger powered on; red+green together = 100%
  charge (no yellow "charging" state, unlike the HP8204B).

## In the field

- **Per the human: when the call is "batteries not charging," check the
  charger.**
- **Charger green the whole time, even on drained batteries = it isn't
  charging**, even with a normal no-load voltage (28 V). Swap in a
  known-good charger to confirm. See [[2026-10-05 GP162 bad charger stays green]].

## See also

[[Golden]]
