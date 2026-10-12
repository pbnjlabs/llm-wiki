---
type: model
manufacturer: Golden
model: GP6xx
tags: [golden, gp600, gp605, gp615, gp620, compass, power-wheelchair]
---

# GP6xx (Compass / Compass Sport)

Power wheelchair family: GP600, GP605 "Compass Sport", GP615, GP620
"Compass HD". Direct textual evidence confirms GP600/605/615/620 share
caster wheel hardware (one procedure covers all four by number), and the
Compass "H-frame" ELR/Swing-Away bracket/hanger system spans the plain,
CTOR, and power-seat frame variants. Controllers differ by model and
year (see below), so don't assume every subsystem is shared across all
four. Link to [[Golden]].

## Controllers: check which one is fitted

| Model | Controller | Codes |
|---|---|---|
| GP605 Compass Sport, **2010–11 supplements** | Dynamic **SHARK** | [[Shark-Diagnostics]] |
| GP605 Compass Sport, **2017 service guide** | Dynamic **LiNX** | [[LiNX-Diagnostics]] (7 codes) |
| GP620 Compass HD (2017) | Dynamic **Shark** (REMA/REMD remotes) or **A-Series** | [[Shark-Diagnostics]] (11 codes) |

All of these are Dynamic Controls products. Look at the joystick: a
LiNX remote has a status light under the power button, and a Shark
remote has an amber wrench LED.

- **GP605 (LiNX):** 18–32 VDC, **two U1 35 Ah**. The power module is
  on the battery box. See [[Compass Sport Service Guide (GP605, LiNX)]].
- **GP620:** **two U1 35 Ah or two NF-22 55 Ah**. The power harness
  has the main circuit breaker. Motor 0.3–50 Ω cold, park brake 40–80 Ω,
  controller motor outputs about 22 kΩ. The battery load test should
  hold about 24 V or more under load. To unlock a locked Shark, press
  the horn twice within 10 s. See [[Compass HD Service Guide (GP620)]].

## GP605 Compass Sport sell sheet (Mar 2023)

From [[Golden Sell Sheets (2018-2026)]]: 300 lb, mid-wheel drive, 4 mph, 24 mi (up to 34 on 50 Ah),
6° max incline, 40 A controller, **179 lb assembled** (base 97, seat 40,
batteries 22 or 30 lb each), 39.5 × 24 in, 24 in turning radius, seats
16–22 in wide. See [[Mobility-Device-Weights]].

## Documents on file

- [[Compass Sport Service Guide (GP605, LiNX)]] (2017)
- [[Compass HD Service Guide (GP620)]] (2017)
- [[Compass Battery Replacement, Power Elevating Seat (GP600)]]
- [[Compass Caster Wheel Mounting (GP600, GP605, GP615, GP620)]]
- [[Compass ELR Swing-Away Installation and Adjustment]]
- [[Compass Footrest Extension (GP600)]]
- [[Compass Sport Battery Connections (GP605)]]
- [[Compass Sport Brake Replacement (GP605)]]
- [[Compass Sport Circuit Breaker Wire Routing Upgrade (GP605)]]
- [[Compass Sport ELR Installation (GP605)]]

GP605 and GP620 have full service guides. There is no owner's manual,
and GP600/GP615 have only single-procedure supplements.

## Key procedures

- **Caster wheels**: GP600M/605M/615M/620M share the same upgrade to a
  spoke-style wheel — old style used 3 washers, new style replaces 2 of
  them with supplied spacers.
- **ELR/Swing-Away**: same H-frame hanger pins for both accessories and
  across plain/CTOR/power-seat frame variants; height-adjustment bolt
  position differs by attachment type (ELRs at front of tube, Swing-aways
  at rear). GP605's ELR hardware is shared with [[GP204-Alante-DX]] and
  Alante GP201.
- **GP600 power elevating seat battery swap**: 2-person job — the power
  seat's 4-post detent-pin lift must be raised and decoupled before the
  batteries underneath are reachable; seat-post realignment on
  reassembly is the most likely sticking point.
- **GP605 batteries ship disconnected** (shelf-life preservation) — won't
  power on until both battery cables and the controller power cable are
  connected.
- **GP605 brake replacement**: 28-step, ~30 min, per-side procedure —
  by far the most involved of Golden's three documented brake procedures,
  see [[Brake-Replacement]]. Confirms GP605's controller is branded
  **"SHARK"**. Shark is a Dynamic Controls product; its code table is on
  [[Shark-Diagnostics]] (from the GP620 guide). The 2017 GP605 guide
  shows a **LiNX** controller instead, so later GP605s changed
  controllers.
- **GP605 circuit breaker routing upgrade**: field retrofit repositioning
  breaker wire routing — implies an early-production wire-chafe issue
  Golden corrected via retrofit.
- **Joystick side conversion**: a cross-model doc names the "Shark"
  controller by brand for a right-to-left desk-arm joystick conversion —
  see [[Golden-Joystick-Side-Conversion]], likely applicable to GP605's
  SHARK-controller joystick.
- **Power elevating seat operation**: GP600's power-elevating seat (see
  battery-replacement doc above) is documented generically in
  [[Golden-Power-Seat-Operation]] — speed interlocks to seat height, and a
  "won't move" complaint after seat use may just need the seat lowered.

## Warranty

GP605 "Compass Sport" and GP620 "Compass HD" are explicitly named in
[[Golden-Wheelchair-Warranty]] — note GP605's frame is warranted for
**LIMITED LIFETIME**, not the standard 5 years. GP600/GP615 are not named
in that warranty text; not confirmed whether they're covered under a
different/older document.

## See also

[[Golden]], [[GP204-Alante-DX]], [[GP162-LiteRider-Envy]],
[[GP303-Ally]], [[Golden-Wheelchair-Warranty]],
[[Golden-Joystick-Side-Conversion]], [[Golden-Power-Seat-Operation]],
[[Brake-Replacement]], [[Shark-Diagnostics]], [[LiNX-Diagnostics]]
