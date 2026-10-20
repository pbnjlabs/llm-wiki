---
type: source
manufacturer: Pride
doc_type: Tech Support Guide
source: "MANUALS/Pride/Seating/1666615580540_US_CA_AU_UK_TB4 Technical Troubleshooting Guide_om_RevA_Sept22_5254.pdf"
date: 2022-09
tags: [pride, quantum, tru-balance-4, seating, troubleshooting, q-logic-3, aam, fault-codes]
---

# TRU-Balance 4 Technical Troubleshooting Guide (INFMANU5254)

28-page dealer troubleshooting guide for the **TRU-Balance 4** seat
(Rev A, Sep 2022). Fills the "TB4 technical troubleshooting guide" gap
on the Missing manuals list. Pulled from the PQ-365 owner's manuals / basic operations library on 2026-10-20.

Organized by Q-Logic 3 seat code: tilt **#150–154**, anterior tilt
switch **#155**, recline **#156–158**, elevate **#159–161**, dual
actuator AFP elevate **#169–171** and articulate **#166–168**, memory
**#174**. Tools: a Q-Logic 3 programmer (Econ-W or handheld: Monitor →
Advanced Actuator Module → Actuator Feedback / End Switches) and a
multimeter.

Key points (procedures on [[Tru-Balance-4-Power-Positioning]]):
- **Any error puts the seat in Fall Back Mode** (no memory positions or
  anterior tilt; it works like a TB3). Accept it with a forward command
  so you can still run the actuator and watch the wiper voltage.
- **Actuator calibration fixes most feedback codes.** If the wiper
  voltage moves when the actuator runs, calibrate; if it stays near 0 V
  or pegged near 4 V+, the actuator (often the **seating frame**, which
  carries the tilt and lift actuators) is bad.
- **Switching motor** (under the seat pan) flips tilt polarity for
  anterior tilt: LED1 = power in, LED2 = power out. LED1 lit but LED2
  dark = replace the switching motor (first try nudging it with an 8 mm
  wrench to reseat the slide pins).
- Multimeter checks at the AAM: actuator motor lead **1–3 Ω = actuator
  OK, replace the AAM; open = replace the actuator**; feedback pins
  **0–10 kΩ = replace the AAM; open = actuator**.
- Normal home readings and wiper ranges are tabled.

Feeds: [[Tru-Balance-4-Power-Positioning]], [[Q-Logic-Fault-Codes]],
[[Power-Chair-Troubleshooting]].
