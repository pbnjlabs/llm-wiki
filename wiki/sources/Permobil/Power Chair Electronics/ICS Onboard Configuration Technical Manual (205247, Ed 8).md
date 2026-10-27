---
type: source
manufacturer: Permobil
model: ICS (Intelligent Control System) seating
doc_type: Service Guide
source: "MANUALS/Permobil/Power Chair Electronics/ics_v8_us-web.pdf"
date: 2015-09
tags: [permobil, ics, corpus, vs, k450, seating, actuator, calibration, programming]
---

# ICS Onboard Configuration Technical Manual (205247, Ed 8)

Permobil's **ICS Onboard Configuration** technical manual (Ed 8, 2015-09,
order no. 205247-US-0, 86 pp.): the full manual that
[[Permobil ICS Error Codes and Quick Reference]] points to. ICS is the
seat-actuator bus on Corpus II, Corpus 3G, Corpus APE/VS, VS and K450 MX
seating. Chapters: **operation** (switchbox, memory, standing),
**programming** (switchbox button combos, R-net OBP, PC), **diagnostics**
and **servicing**. Feeds [[R-net-Diagnostics]] and the Permobil model
pages.

## Switchbox LEDs

| LED | Meaning |
|---|---|
| Solid green / yellow / red | Function available: full speed / drive speed limited / drive inhibited by this function |
| Flashing green / yellow | Memory mode |
| Flashing red | End of travel or current limit reached |
| **Brief red flash (5 s), not at end of travel** | Binding, worn actuator, or a sensor problem (worn **SoftPot** or its cable) |
| **Constant red flash** | Actuator expected but not talking: bus wire damage, or it's programmed but not connected |
| LEDs toggling red | Restart needed (after plug-and-play or programming) |
| All LEDs flashing red together | Switchbox layout setting error: pick another layout in Wheelchair Builder |
| Seat elevator icon **yellow/red** (and **M8** flashing on the R-net JSM) | **SoftPot error mode** (VS seat elevator) |

**SoftPot error mode:** no stand up, no elevator up, elevator slow, drive
at **half speed** max. Run the elevator fully down to try to clear it;
if it keeps flashing, the SoftPot needs service.

## Servicing

- **ICS bus:** any device can go in any open ICS port (master module
  near the power module, or connector blocks in the backrest hinge or
  seat pan). Press the latch tabs to unplug; pull on the housing, not
  the cable.
- **Linak LA28 (item 324195) on Corpus APE / VS:** when replaced or after
  a position fault, it enters **recalibration mode** (LED 1 flashes
  red/yellow): any button drives it down to its mechanical end, then it
  asks for a restart.
- **Smart actuator calibration:** off, hold **5 + 6 + 3** and power on;
  release when all LEDs go green; LEDs 7–8 flash red. **Button 4** =
  automatic (actuator stays in the seat, must reach its hard stops; not
  on ICS programs older than v30, December 2010, or SoftPot actuators).
  Corpus II/3G: 2 = tilt, 3 = tilt + backrest, 4 = tilt + backrest +
  legrest. Corpus APE/VS: 1 anterior tilt, 2 tilt/elevator, 3 backrest,
  4 all, 5 support wheels (VS), 6 articulating legs, 7 legrest. Success:
  all LEDs flash green (and a beep).
- **Manual calibration** (not Corpus 3G/APE/VS): remove the actuator and
  set its centre-to-centre length, front hole aligned with the fixed
  hole: **VS** standing 520, recline 250, legrest 300, tilt 300 mm;
  **RS** recline 300, legrest 300; **Corpus on C300/C350** legrest 300;
  **Corpus on C400/C500** backrest 250, legrest 300 (20° tilt: automatic
  only). Tape the screw of a new Smart actuator until it's bolted in, or
  it loses calibration.
- **SoftPot actuators:** move to the calibration position (hold 5 until
  LEDs 7–8 go green), off, remove, measure; if short, move the SoftPot
  housing away from the moving end, if long, toward it. Lengths: C300/C350
  30°/45° tilt 400 mm; C400/C500 30° tilt 300 mm (45°: automatic).
- **Emergency manual operation ("Take Me Down"):** off, hold **6 + 8**,
  power on, keep holding until all LEDs turn **red** (about **30 s**);
  LEDs oscillate green. Actuators run at **50 %** with no collision
  protection. Buttons: elevator 2 up / 6 down, legrest 4 / 8, recline 3
  forward / 7 back, stand 1 up / 5 down; no standing sequence. Exit by
  switching off. (The manual labels the elevator buttons "will raise/lower
  the Legrest", a misprint.)
- Switchbox, actuator and general module replacement: see the seating
  system service manual (not on file).

## Programming highlights

User weight range, LED indication level, switchbox layout and label
sheet, leg rest angle for speed reduction, 45° tilt calibration
(C400/C500), Corpus 3G IRM and seat depth, VS/APE standing sequence and
ground clearance, **K450** transport (WC19) mode, seat width and armrest
type, and enabling the ICS menu in R-net OBP to limit movements or change
the speed-reduction position.

## Feeds into

[[R-net-Diagnostics]], [[Permobil ICS Error Codes and Quick Reference]],
[[Permobil-M-Corpus]], [[Permobil-F-Corpus]], [[Permobil-K450]], [[Permobil]]
