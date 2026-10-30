---
type: source
manufacturer: Bruno
model: VPL-3153-3175
doc_type: Training Doc
source: "MANUALS/Bruno/Training/Installation & Troubleshooting/AC Board with LED Functions.pdf; MANUALS/Bruno/Training/Installation & Troubleshooting/PCB-00143 LEDs.xlsx; MANUALS/Bruno/Training/Installation & Troubleshooting/6. SCH-00229.pdf"
date: 2022-04-05
tags: [bruno, vpl, ac, training, circuit-board, diagnostics, schematics, vpl-3153, vpl-3175]
---

# Training - VPL 90V Board PCB-00143 LED Functions and Ladder Logic (SCH-00229)

Three files from Bruno's dealer **training** library (Installation & Troubleshooting docs) for the **PCB-00143 90 V board** in the AC low-rise **VPL-3153/3175**. They add to [[Tech Tip - VPL 90V Board PCB-00143 (TSG-VPL-004, SCH-00229)]].

- **AC Board with LED Functions.pdf** (2 pages, table dated 4/5/22, file edited 2025): p1 is a **board layout** showing where each LED E1–E18, fuse and connector sits (E1 by the 120 VAC input; E2/E3 on the left; E4–E12 in a column mid-board; E13–E17 below; E18 bottom left; F2 2.5 A slo-blo and F1 20 A along the bottom). p2 is the **LED table**: function, what it means, and what to check. **PCB-00143 LEDs.xlsx** is the same table as a spreadsheet.
- **6. SCH-00229.pdf:** a **colour ladder-logic** sheet of SCH-00229 (VPL-3153/3175 90 V controller assembly, rev 1, file 2019) with each LED's yellow callout drawn on the circuit it watches. The tech tip's SCH-00229 is the 3-page **wiring** drawing; this is the logic view of the same board.

**Run conditions** (training table, not in TSG-VPL-004):
- **To run down:** E2, E9, E16 and E17 lit, and E15 lights when a down button is pressed. Then **E10 and E12** light and it runs down.
- **To run up:** E2, E9 and E14 lit, and E13 lights when an up button is pressed. Then **E10 and E11** light and it runs up.

So a dead circuit shows as the first unlit LED along the chain. The ladder logic shows the order: 24 V (E3) → top cover switch (E4) → E-stop and nut safety switch (E5) → upper gate closed (E6) → upper landing enable switch → upper gate locked (E7) → terminal 29 → platform gate closed and locked (E8, E9) (jumper **29 to 27** with a platform gate, **29 to 25** without) → key switches and up/down buttons on the platform, gate and call/send controls (E13, E15) → upper limit (E14) or lower limit and safety pan switches (E16, E17).

**Table differences from the tech tip:** E10 is "switch enable: controller ready to receive an input command" (the tech tip has it lighting on up or down), and E18 says "software generated; check flash codes" (codes are on the tech tip page). Everything else matches.

Feeds: [[VPL-3153-3175]], [[VPL-Troubleshooting]]
