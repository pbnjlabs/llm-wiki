---
type: source
manufacturer: Bruno
model: VPL-3100B
doc_type: Training Doc
source: "MANUALS/Bruno/Training/Installation & Troubleshooting/DC_color_schematic.pdf"
date: 2012-05-31
tags: [bruno, vpl, dc, training, schematics, vpl-3100b]
---

# Training - Low-Rise DC VPL Ladder Logic (SCHL-00189)

One-page **colour ladder-logic** drawing **SCHL-00189** rev 0 (5/31/12), *Low Rise DC VPL - Ladder Logic*, from Bruno's dealer **training** library (Installation & Troubleshooting docs; file 2020). It's the logic view of the relay-controlled **low-rise DC VPL** ([[VPL-3100B]] generation from 2012); the 3100B install manual has the plain wiring sheets (SCH-00189).

- **Power:** 2 × 12 VDC battery (top and bottom), **35 A circuit breaker**, **final limit** (N.C.) in the red battery feed, **3 A fuse** to the control connector J1. A red **24 V LED** shows battery voltage is there.
- **Motor:** **24 VDC ½ hp**, switched by two relays **RLY1/RLY2** (orange and blue motor leads). J1 pins: 1 red (Vbat), 2 black, 3 orange (up), 4 white, 5 blue (down), 6 brown.
- **Safety chain** (from JP6-1): top cover switch → E-stop → nut safety switch → upper gate/door closed → upper landing enable switch → upper gate/door locked → terminal 29 → jumper **29 to 25 with no platform gate** (29 to 27 with one) → key switches and up/down on the platform controls, gate controls and call/send.
- **Delay and interlock circuit:** relays **K1 (up)** and **K2 (down)**, each with a yellow LED (**UP LED**, **DOWN LED**). Down runs through the **safety pan switches** and the **lower limit switch**; up through the **upper limit switch**.
- **Notes on the sheet:** no gates or interlocks = jumper terminal **25 to 33**; upper landing gate or interlock = jumper **25 to 29**. Connectors: JP2 expansion, JP3 platform controls, JP4 gate/call/send, JP5 lower limits, JP6 upper limits/cover switch, TB7 terminal block 20–33.

Feeds: [[VPL-3100B]], [[VPL-Troubleshooting]]
