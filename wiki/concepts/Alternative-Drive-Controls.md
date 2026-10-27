---
type: concept
tags: [alternative-drive, head-array, specialty-joystick, scanner, sip-n-puff, r-net, q-logic, linx, asl, permobil]
---

# Alternative Drive Controls

Inputs that replace the standard joystick: **head arrays**, **mini and
micro joysticks** (hand, chin), **switch scanners**, sip-and-puff. On file:
[[Adaptive-Switch-Laboratories]] (ASL) controls and Permobil's
[[Total Control Head Array User Manual (338998)]]; Q-Logic's own
input-device programming is on [[Joystick-Controllers]].

**Set-up is an ATP / specialist job.** Every ASL sheet puts testing of the
finished chair (ISO/RESNA, RFI) on the wheelchair manufacturer and the
programming on someone trained on both the device and the chair's
electronics. A tech's part is mounting, cabling, checks and repairs.

## Rules that apply to all of them

- **Always fit a reset (emergency stop) switch** in a port programmed to
  stop the chair (ASL: the mode/reset port).
- **Moisture makes head arrays and joysticks move the chair on their
  own:** no rain or snow, no wet hair, no porous covers; dry covers fully
  after cleaning. Liquid or debris in a mini joystick = error codes or
  unwanted movement. The MEC's **dust cover stays on**.
- **A head array is not a headrest:** in a vehicle, swap in a headrest approved by
  the wheelchair manufacturer (Permobil) or don't use it as head support (ASL).
- **Cables:** route so tilt, recline and lift can't pull or pinch them,
  and **run every seat function to its end range before delivery**.
- Check that the system works **before the user sits in the chair**, and
  tighten adjustment points periodically.

## Where it plugs in (by electronics)

| Electronics | Port | Notes |
|---|---|---|
| **R-net** (Permobil and others) | **Omni / Omni2 Port 1 (SID)** | OBP → Omni → Port 1: SID type (FUSION: **3 Prp**), Switch Detect, Switch Long/Medium, Double Click Time; profiles 3–4 usually Omni. See [[R-net-Diagnostics]] (SID / Switch Detached trips) |
| **Q-Logic 3** (Pride/Quantum) | **Enhanced Display 9-pin** or **SCIM** | Input Configuration: 3-Directional Proportional Head; center dead band; mode switch short/long/double. See [[Joystick-Controllers]] |
| **LiNX** (Golden and others) | **Input Module (IN500) 9-pin** | User Configuration = Proportional Head Array; Stop While Driving and Seating ON. See [[LiNX-Diagnostics]] |
| **MK6i** | MK6i connector / digital interface | FUSION needs an **ASL 171** |

ASL's settings per electronics for the FUSION:
[[ASL 110 FUSION User Installation Guides (LiNX, Q-Logic, R-net, Permobil)]].

## Device quick reference

| Device | Type | Key facts |
|---|---|---|
| ASL 110 FUSION | Proportional and digital head array | Power light green = drive, amber = BT; ASL 165 display/programmer/attendant; beeps 1 on/off, 2 BT, 3 next function, 4 next profile |
| ASL 104 ATOM | Digital (switch) head array | DIP 1 SEL = reset vs reverse, 2 BT pair, 3 power with chair, 6 beeps; switch timer sets long-hold |
| Permobil Total Control Head Array | Proximity / egg-switch head array (R-net) | LEDs green ready, amber active, flashing amber standby |
| ASL 125 Orbit / 128 Molecule / 130 MEC | Mini / micro joysticks | 50 g / 4 mm, 8 g / 3 mm, 18 g / 9 mm; DIP 1 up = 3-direction proportional; L/R click plug in before power-up |
| ASL 133 / 134 Compact | Compact joystick + 1 or 2 mono switches | 240 g / 23 mm |
| ASL 102 UNO | Single-switch scanner | 0.2–4.0 s per step; returns to forward on release; attendant control included |
| ASL 558 | Bluetooth mouse emulator | Pairs with ATOM / ASL BT joysticks; 12 DIP + 6 dials |

Sources: [[ASL 110 FUSION Head Array Instruction Manual (Rev 3-2022)]],
[[ASL 104 ATOM Bluetooth Head Array Instruction Manual (Rev 5-2020)]],
[[ASL Bluetooth Joystick Instruction Manuals (125, 128, 130, 133, 134)]],
[[ASL 102 UNO Single Switch Scanner Instruction Manual (Rev 5-2020)]],
[[ASL 558 ATOM Bluetooth Mouse Emulator (Manual and Common Setups)]],
[[Total Control Head Array User Manual (338998)]].
