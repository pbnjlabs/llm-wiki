---
type: source
manufacturer: Pride
doc_type: Basic Operation Instructions
source: "MANUALS/Pride/Controllers/Q-Logic NES/1729690570758_US_QLNES_om_RevA_Aug24_5366.pdf"
date: 2024-08
tags: [pride, quantum, qlnes, controller, error-codes, bluetooth, attendant-control]
---

# QLNES Basic Operation Instructions (INFMANU5366)

24-page US Quantum basic operation instructions for the **QLNES**
controller, INFMANU5366/Rev A/August 2024. In 2025 it's the standard 75 A
or 90 A electronics on most Quantum mid-wheel chairs
([[Quantum End-to-End Chart (INFINFB4546, 2025)]]).

- **Hand control:** 6-key or 10-key joystick (on/off, horn, plus/minus
  profile keys, Key I/II, and on the 10-key lights, hazard and turn
  signals), LED strip instead of a screen, **USB-C port** (up to 5 V 3 A)
  for small devices, mode and on/off jacks.
- **Charging:** a standard XLR port **and a magnetic charger port**.
  **Never use two chargers at once.** Keep the magnetic connector at
  least **6 in from any implanted device**. Off-board charger max
  **8 A** (the text says a 5-pin socket).
- **Battery gauge:** 6 segments (green 3 ≥91%, green 2 ≥71%, green 1
  ≥51%, yellow 2 ≥31%, yellow 1 ≥16%, red ≥8%, red blinking below).
  Charge when it reaches yellow.
- **Drive modes 1–4** shown by LED colour: yellow number = drive
  restriction, red = drive lockout, green blinking = iLevel active,
  orange blinking = suspension lock not engaged while elevated, all
  four orange 2 Hz = rescue drive.
- **Actuators:** up to two, via Key I/II, the profile keys, a switch in
  the mono jack (two need a splitter) or the attendant control; can
  drive and move actuators together until the drive lockout point.
- **Lock** isn't factory-programmed; once enabled, hold the mode keys
  to lock, unlock with full forward then full reverse.
- **Bluetooth** for programming (hold on/off 3 s to pair; accept with a
  forward input) and for **Interactive Assist** diagnostics.
- **Thermal rollback to 20%.** Keep the chair between 18 °F and 122 °F.
- **Error display:** three LEDs blink the three digits of the code (red
  = hundreds, yellow = tens, green = ones; e.g. #208 = red 2, green 8).
  One fault at a time; power-cycle to see the next. Warnings flash the
  two yellow LEDs for 4 s with an error beep.
- **Error codes listed:** 1–4, 20, 21, 23–26, 32, 34, 35, 46, 47, with
  the same meanings as Q-Logic 3.

Feeds into: [[Joystick-Controllers]], [[Q-Logic-Fault-Codes]],
[[Power-Chair-Troubleshooting]].
