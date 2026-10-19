---
type: source
manufacturer: Pride
doc_type: Training Guide
source: "MANUALS/Pride/General/power_chair_diagnostics.pdf"
date: 2004-01
tags: [pride, jazzy, power-chair, diagnostics, legacy, vsi, pilot, remote-plus, dynamic, dl50, training]
---

# Pride Technical Troubleshooting Guide — Power Chair Diagnostics (2004)

56-page chapter of Pride's general Technical Troubleshooting Guide (Rev
B, Jan 2004), the same guide as the
[[Technical Troubleshooting Guide - Battery Guide (2004)|Battery Guide]]. For
**older Jazzy chairs**: integrated controllers on the **9-pin power
interface harness** (PG **Pilot**, **VSI**, Dynamic **DL50**), PG
**Remote Plus** with a separate power module (M1/M2 harnesses), and
**Dynamic DX** (Europa) with module status LEDs. Model-specific guides
for newer chairs supersede it.

Values that still apply widely:
- **Joystick XLR/charger port pins 1–2:** about 24 V → joystick bad.
- **Circuit breaker:** under 1 Ω good; open or **over 3 Ω** = replace.
  It makes the **series link** between the batteries (+ of one to − of
  the other), so 0 V across one pair of posts is normal; try the other.
- **Charger output:** unplug the charger's white 3-pin, read the two
  outside pins: **25–30 V DC**; the harness side should read battery
  voltage, else the **charger fuse** (meter it; looks can lie).
- **Won't drive, no code ("Low Enable, No Drive Away"):** the chair
  only drives while the charger harness **center pin** reaches the most
  negative battery post. Check that line under 1 Ω and the fuse; jumper
  center to outside negative on the harness: drives → charger fault.
- **Motor:** 0.5–1.5 Ω. Brushes: at least **½ in** long, no chips, no
  discolored (overheated) braid. *(The newer model guides say replace
  under 0.25 in.)*
- **Brakes:** about **60 Ω** each; on the 9-pin they're in parallel, so
  about **30 Ω** pin 9 to 7 and 9 to 8.
- **High battery voltage:** charger over 32 V (each battery over 16 V).
  Charger reading 30 V or more → replace it.
- **Flash codes** (Pilot, Remote, VSI, Remote Plus): 1 low battery,
  2 left motor, 3 left motor wiring, 4 right motor, 5 right wiring,
  6 inhibit, 7 joystick, 8 controller, 9 brake, 10 high voltage.
  **DL50 numbers them differently:** 1 low battery, 2 high voltage,
  3 left motor, 4 right motor, 5 brake, 6 controller, 7 joystick.
  **Dynamic DX** status LED: 1 module, 2 accessory, 3/4 left/right
  motor, 5/6 brakes.
- Programmers: **PP1** (Pilot, Remote Plus; fault log of last 8 faults,
  "preset unit" = factory reset), Dynamic **HHP** for DL50/DX.

Feeds into: [[Power-Chair-Troubleshooting]], [[Pride-Controller-Flash-Codes]].
