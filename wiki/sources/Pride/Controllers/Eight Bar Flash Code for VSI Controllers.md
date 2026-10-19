---
type: source
manufacturer: Pride
doc_type: Training Guide
source: "MANUALS/Pride/Controllers/PG and Dynamic/eightbarflashvsicontroller.pdf"
tags: [pride, vsi, pg-drives, flash-codes, motor]
---

# Eight Bar Flash Code for VSI Controllers

1-page education sheet. On a PG **VSI**, eight flashing bars usually
means a bad controller, but rarely a **conductive path between the
drive motors** causes it.

Test: meter on 20 kΩ. Utility-tray chairs: Beau connector pin 1 or 2
to pin 3 or 4. VSI with flying leads: right motor red or black lead to
left motor red or black lead. **Any resistance at all = the motors.**
Open = VSI (or possibly batteries). Any resistance from a motor lead to
the **frame** also confirms a motor. One new motor fixes it, but Pride
recommends replacing **both**.

Feeds into: [[Pride-Controller-Flash-Codes]], [[Power-Chair-Troubleshooting]].
