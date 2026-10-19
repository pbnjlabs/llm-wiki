---
type: source
manufacturer: Pride
model: Q6-Edge
doc_type: Troubleshooting Guide
source: "MANUALS/Pride/Quantum Power Chairs/infmanu4109_ttg.pdf"
date: 2012-03
tags: [pride, quantum, q6-edge, troubleshooting, ne, ne-plus, q-logic, wiring]
---

# Q6 Edge Technical Troubleshooting Guide (INFMANU4109, Rev B 2012)

32-page dealer **Technical Troubleshooting Guide** for the original
**Q6 Edge with NE, NE+ or Q-Logic electronics**, Rev B, March 2012.
Supersedes [[Q6 Edge Technical Troubleshooting Guide (INFMANU4109 Rev A, 2011)]];
same procedures, redrawn as flowcharts, plus the **2012-and-later
programmer menus** for System Lock, Inhibit and Save System
Configuration. Not for the Edge 2.0 and later on QLNES or Q-Logic 3.

Contents (all multimeter flowcharts, with a connector reference guide and
shroud/power-module removal appendix):

- **No power** — voltage walk: joystick charger port (≈25 V → replace
  joystick; under 18 V → charge; 0 V → keep going), front and rear
  battery harnesses, battery cable, **circuit breaker (under 1 Ω good)**,
  power module bus port, bus cable extension, bus cable, joystick.
- **System Lock** — NE/NE+ show a key icon, Q-Logic shows "System
  Lock". Unlock: power on, joystick full forward to a beep, full back to
  a beep. Lock: NE hold power; NE+ hold both profile keys; Q-Logic hold
  the mode lever forward (or AUX menu).
- **Battery Charging or Drive Inhibit** (Q-Logic #107) — open inhibit
  circuit. Jumper tests: PTO/inhibit 4-pin barrel **pin 3–4** (never
  1–2: sparks, blows the harness fuse); power-module 14-pin connector
  **NE: pin 4–6**, **NE+/Q-Logic: pin 1–9**. Then check the inhibit
  program (NE `chrgInb` ON; NE+/Q-Logic Inhibit "High"), else replace
  the power module.
- **Open motor** — motor harness **0.5–1.5 Ω**; brushes worn below
  **0.25 in** or damaged → brushes, else motor; both good → power module.
- **Motor/brake error** — freewheel levers in drive; brake about **80 Ω**
  across the motor harness.
- **Missing/defective module**, **joystick error**, **power module /
  communications / software error** — bus cable and multiplier
  continuity (under 1 Ω per pin), Save System Configuration when a
  module was removed on purpose.
- **Low battery voltage** — charger port over 16 V, charger status
  lights, 120 VAC at outlet and cord, battery harness comparisons,
  breaker, bus port. Batteries too low for the off-board charger → shop
  load test and charge.
- **Error tables:** NE (LCD text), NE+ (LCD text), Q-Logic (#19, 23, 36,
  37, 38, 105, 192/193, 203/204, 229; refer to the Q-Logic code guide for
  the rest).

Fault details are read with a **Curtis handheld programmer**
(Diagnostics → Actual Faults / Fault History) on NE/NE+.

Feeds into: [[Q6-Edge]], [[Power-Chair-Troubleshooting]],
[[Joystick-Controllers]], [[Q-Logic-Fault-Codes]].
