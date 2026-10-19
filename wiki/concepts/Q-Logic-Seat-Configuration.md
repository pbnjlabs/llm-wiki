---
type: concept
tags: [pride, quantum, q-logic, ne-plus, aam, am1, am2, lam2, seating, actuator, tilt, drive-inhibit, programming]
---

# Q-Logic Seat Configuration (actuator modules and tilt thresholds)

How legacy **Q-Logic** and **NE+** chairs know which power-seat
functions are fitted, and the **tilt thresholds** that stop driving or
seat movement. You need this after adding or removing an actuator, or
when a tilted chair won't drive.

Sources: [[Q-Logic Seat Configuration Settings (AAM)]],
[[Q-Logic Seat Configuration Settings (AM1, AM2, LAM2)]],
[[Tilt Threshold Definitions for Seating Modules]] and the seat
parameters in the [[Q-Logic Technical Manual (INFMANU3580)]] (pp.
95–99). For Q-Logic 3 seat programming (Combined Functions, latched
actuators, pretilt) see [[Q-Logic 3 Programming Guide]] and
[[Tru-Balance-3-Power-Positioning]].

## Actuator modules and channels

| Module | Actuators | Used with |
|---|---|---|
| **AAM** (Advanced Actuator Module, CTLDC1472) | 5 (A1–A5) | Q-Logic |
| **AM1** | 1 (A1) | Q-Logic power base 2.19+ and NE+ |
| **AM2** / **LAM2** (light actuator module) | 2 (A1–A2) | Q-Logic power base 2.19+ and NE+ |

AAM channel map: **A1 tilt, A2 recline, A3 elevate (or lift), A4 left
leg / both legs / foot platform, A5 right leg / back.**

## Configuration numbers

Set the **Configuration Number** parameter (Seat > Misc.) to match what's
fitted. **If you add or remove an actuator, change this number**, or
the seat functions won't match the hardware. The numbers are the same
across modules for the same function.

| No. | Functions | AAM | AM1 | AM2/LAM2 |
|---|---|---|---|---|
| 1 | Independent legs | ✓ | | ✓ |
| 2 | Combined legs | ✓ | | ✓ |
| 3 | Articulating foot platform | ✓ | ✓ | ✓ |
| 4 | Elevating seat | ✓ | ✓ | ✓ |
| 5 / 6 | Elevating seat + independent / combined legs | ✓ | | |
| 7 | Elevating seat + foot platform | ✓ | | ✓ |
| 8 | Recline | ✓ | ✓ | ✓ |
| 9–13 | Recline + legs / foot platform / back, synchronized | ✓ | | 11 only |
| 14 | Recline + elevating seat | ✓ | | ✓ |
| 15–19 | Recline + elevate + legs / foot platform / back, synchronized | ✓ | | |
| 20 | Tilt | ✓ | ✓ | ✓ |
| 21 / 22 | Tilt + independent / combined legs | ✓ | | |
| 23 | Tilt + foot platform | ✓ | | ✓ |
| 24 | Tilt + elevating seat | ✓ | | ✓ |
| 25–27 | Tilt + elevate + legs / foot platform | ✓ | | |
| 28 | Tilt + recline | ✓ | | ✓ |
| 29–33 | Tilt + recline + legs / foot platform / back, synchronized | ✓ | | |
| 34 | Tilt + recline + elevating seat | ✓ | | |
| 35–39 | Tilt + recline + elevate + legs / foot platform / back | ✓ | | |
| 40–47 | **Lift & tilt** (alone, + legs, + foot platform, + recline, + recline and legs/foot platform) | ✓ (newer chart only) | | |

The 2008 tech manual lists 1–39; the undated AAM chart adds 40–47.
Recline and legs/foot platform settings work together or independently.

## Tilt thresholds

Angles are combined tilt + recline where both are fitted. Range
**10°–78°**.

| AAM parameter | AM1/AM2/LAM2 name | What it does | Factory (2008 manual) |
|---|---|---|---|
| Tilt Threshold 1 | Driving 4 | Tilt/recline **won't go back further while the seat or lift is elevated** (only with elevate or lift & tilt) | 25° |
| Tilt Threshold 2 | Driving 3 | Tilt/recline **won't go back further** at all (e.g. to stop short of the full 55°) | 78° |
| Tilt Threshold Driving 1 | Driving 1 | **Full drive lockout** when tilted/reclined past this | 25° |
| Tilt Threshold Driving 2 | Driving 2 | Seat/lift **won't elevate** when tilted/reclined past this (only with elevate) | 25° |
| Tilt Threshold Driving 3 | — | Not used | |
| Tilt Threshold Head Control | same | With a 3/4/5-switch **head array**: between this angle and the drive lockout, it drives as a **2-switch** (right pad forward/reverse, left pad left/right, back pad inactive; two arrows on the drive screen) | |

**R4000 units with an AAM but no lift & tilt:** Threshold 1 is simply
"tilt won't go back further", and Driving 2 is unused.

Other seat parameters: tilt angle definition (-90°, 0°, +90°, 180°) and
direction (clockwise/counterclockwise, seen from the back of the AAM)
tell the AAM how it's mounted; per-actuator max speed (20–100%),
acceleration/deceleration (low/medium/high), **timeout** (0 disables;
defaults 120 s) and polarity (A2 recline is inverted by default); 12 V
output on/off; **latch operation** (seat functions keep running after
the command is released; only for users who can reliably stop them).

**A chair that won't drive while tilted is usually working as designed.**
Bring the seat back below the Driving 1 angle. On the hand control the
"traffic light" goes red at drive lockout and amber when drive is
limited (quarter speed). Pride: don't bypass or reprogram factory
inhibits.

## See also

[[Joystick-Controllers]], [[Q-Logic-Fault-Codes]] (seat codes 44/45,
141, 160/161, 186, 217/218),
[[Tru-Balance-3-Power-Positioning]], [[iLevel]], [[Q-Logic-Firmware-Updates]],
[[Power-Chair-Troubleshooting]]
