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
| GP605 Compass Sport, **2017 service guide and 2022 owner's manual** | Dynamic **LiNX** (LiNX LE) | [[LiNX-Diagnostics]] (7 codes) |
| GP620 Compass HD, **2017** (service guide and owner's manual) | Dynamic **Shark** (REMA/REMD remotes) or **A-Series**; OM says **75 A** | [[Shark-Diagnostics]] (11 codes; the OM numbers 10) |
| GP620 Compass HD, **2019 owner's manual** | Dynamic **LiNX**, **60 A** | [[LiNX-Diagnostics]] |
| GP620 Compass HD, **2024 IPB** | Dynamic **Shark** REMD + 75 A module (no LiNX listed) | [[Shark-Diagnostics]] |
| GP605**A** (2022/2023 IPBs) | Dynamic **LiNX** DLX-REM050-A | [[LiNX-Diagnostics]] |

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

## Owner's manual specs

| | GP605 Compass Sport (2022) | GP620 Compass HD (2017 Shark / 2019 LiNX) |
|---|---|---|
| Capacity | 300 lb | **450 lb** |
| Speed / range | 4 mph / 24 mi (U1), 27.5 mi (40 Ah) | 4 mph / 12 mi (Shark); **4.5 mph / 21 mi (LiNX)** |
| Batteries | 2-U1 (22 lb) or 2-40 Ah (29 lb) | **2-NF22** (37 lb each) |
| Controller | 40 A LiNX | 75 A Shark / 60 A LiNX |
| Assembled | **185 lb CC / 179 lb SS** | **223 lb SS / 226 lb CC** |
| Base / seat | 97 / 40 (pan) or 46 (captain's) lb | 101 / 34 (pan) or 37 (captain's) + arms 14 lb |
| Size, turning radius | 39.5 × 24 in, 24 in | 40 × 25 in, 20 in |
| Seat heights | 3 (1 in) | 5 (0.5 in); seats to 24 × 20 in |
| Medicare | K0823 CC / K0822 SS | K0824 SS / K0825 CC |
| Frame warranty | **Lifetime** | 5 yr |

CC = captain's chair, SS = van/pan seat. The GP605's **battery
connection diagram** is inside the rear battery cover; the chair won't
power up until both battery harnesses and the power harness are plugged
in and locked. Freewheel: GP605 levers **forward** = freewheel; the
GP620 manuals only say "turn as shown" ([[Freewheel-Mode]]).

## GP605 Compass Sport sell sheet (Mar 2023)

From [[Golden Sell Sheets (2018-2026)]]: 300 lb, mid-wheel drive, 4 mph, 24 mi (up to 34 on 50 Ah),
6° max incline, 40 A controller, **179 lb assembled** (base 97, seat 40,
batteries 22 or 30 lb each), 39.5 × 24 in, 24 in turning radius, seats
16–22 in wide. See [[Mobility-Device-Weights]].

## Documents on file

- [[Compass Sport Owners Manual (GP605, LiNX)]] (Jan 2022)
- [[Compass Sport Illustrated Parts Breakdown (GP605A)]] (2022, 2023): LiNX DLX-REM050-A + power
  module, Bluetooth dongle, 50 A breaker harness, U1 or 12 V 40 Ah
  batteries, motors RA03E102/103
- [[Compass HD Illustrated Parts Breakdown (GP620)]] (Apr 2024): **Shark REMD + 75 A Shark module**,
  22NF batteries, 8 A charger. Lists only the Shark, though the 2019
  owner's manual is a LiNX edition: check the joystick
- [[Compass HD Owners Manual (GP620, LiNX)]] (May 2019)
- [[Compass HD Owners Manual (GP620, Shark)]] (Dec 2017)
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

GP605 and GP620 have full service guides and owner's manuals.
GP600/GP615 have only single-procedure supplements.

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
