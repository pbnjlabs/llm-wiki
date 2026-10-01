---
type: model
manufacturer: AutoSlide
model: AutoSwing
tags: [autoslide, autoswing, automatic-door, swing-door]
---

# AutoSwing

[[AutoSlide]]'s **swing-door** operator (catalogue no. ASW8-1), the
counterpart to the sliding [[AutoSlide-Drive-System]]. It uses the same
AutoSlide app, sensors, K9 pet tags and AutoPlus Gateway. It mounts on
the transom header on the inside of the door. A **Pro** version adds a
backup battery and a 4-button remote.

## Spec summary

- 22.56 × 3.14 × 2.25 in (570 × 80 × 60 mm), 7 lb. 24 V motor.
- Doors up to **47 in wide (1200 mm)** and **198 lb (90 kg)**. The
  features list says 220 lb; the spec table says 198.
- Power adapter 100–240 V AC in, **25 V DC 2.6 A** out. Lithium backup
  21.6 V 3200 mAh (Pro version).
- Opening speed 30°/s (15°/s slow), closing 8°/s. Hold-open 0–23 s. **Any
  setting over 23 s switches to toggle mode.**
- Lock output: SPDT relay, max 2 A at 24 V DC, plus 24 V DC aux at
  220 mA. Works with maglocks, electric strikes, electric deadbolts, and
  Yale/August smart locks (through the AutoPlus Gateway).
- Auto-reverse and safety beams. RF, Bluetooth, RS485 and dry contacts.
  14–140 °F.

## Install

- **Pull (slide) arm for in-swing doors, push arm for out-swing.** The
  operator always goes on the inside. Each box comes with one arm.
- Close the door and fix the base to the frame with six countersunk wood
  screws (M6×15 hex countersunk for a steel frame). Use a level. Line the
  base edge up with the door edge, or over the hinges for a push arm.
  Remove or cut trim so it sits flush.
- **Slide arm:** the rail goes flush on the door, its edge 1 in from the
  ball with the door closed.
- **Push arm:** the bracket goes on the door just past the operator's
  edge. Set the arm to a 90° triangle and tighten the bolts.
- If the arm doesn't clear the frame, use the pinion extender.
- **Power-up:** DIP #1 off, DIP #6 on. Switch on with the door half open.
  It should close; if it opens instead, switch off, flip DIP #1 and try
  again.
- **Learn the width:** in Green mode, flip DIP #1 off and on again (or
  use the app). The door opens to the stop, then closes.
- **Electric lock:** power to Lock Port #5, ground to #4. For an electric
  strike, also turn on DIP #3.

## Modes

Mode button: **Auto** (inside and outside sensors), **Lock** (inside
sensor only), **Hold Open**, **Pet** (door locked, opens to the pet width
only for K9 tags). Secure Pet mode turns off the outside sensor.

## DIP switches

| # | On / off |
|---|---|
| 1 | Direction / learn |
| 2 | Slam shut |
| 3 | Lock type: on = electric strike (PTO), off = maglock (PTL) |
| 4 | Secure pet mode |
| 5 | 75% opening speed |
| 6 | Bluetooth app (on) / MODBUS (off) |
| 7 | Heavy door (on) / light door (off) |
| 8 | Fire alarm input: 12 V (on) / 0 V (off) |
| 9 | With fire alarm active: door opens (on) / closes (off) |
| 10 | End cap lights off |

## Safety

- **Safety sensors are required** with DIP 7 (heavy) on, DIP 2 (slam
  shut) on, DIP 5 (75% speed) off, or any app force setting over level 4.
  The manual cites AS5007-2007. Fit one on each side of the door.
- **Low-energy door signs**, 50 ± 12 in from the floor to the sign's
  center, on both sides: "AUTOMATIC CAUTION DOOR". Add "ACTIVATE SWITCH
  TO OPERATE" when a switch is used, or "PUSH / PULL TO OPERATE".
- **Power cord:** plug it into a socket nearest the **left side** of the
  operator. Don't run the cord through walls, doorways, ceilings or
  floors, fasten it to the building, or hide it behind walls. Use only the
  supplied adapter.
- Fit it only on a door that works properly and is balanced. Metal doors
  must be grounded.

## Documents

[[AutoSwing Installation Manual]]

## See also

[[AutoSlide-Drive-System]], [[Open-Sesame-Model-133]],
[[Open-Sesame-Model-233]], [[Automatic-Door-Operators]],
[[RFID Pet Sensor Operation Instructions]]
