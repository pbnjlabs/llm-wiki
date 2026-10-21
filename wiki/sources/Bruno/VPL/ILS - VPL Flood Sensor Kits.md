---
type: source
manufacturer: Bruno
doc_type: Instruction Sheet
source: "MANUALS/Bruno/Drawings/VPL/ILS-01211.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01453.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01472.pdf"
url: https://www.brunopartner.com/er26ya59sp/drawings.aspx
date: 2019-10-31
tags: [bruno, vpl, ils, flood-sensor, flood-zone, pit-switch]
---

# ILS - VPL Flood Sensor Kits

- **VPL-K-3149 (ILS-01211**, 10/21/19), **low rise** VPL-3100, 3100B, 3300B. Mount the sensor **below the lower limit switches**.
  - Residential: pull the yellow jumper; red TB7-33, black TB7-20, white TB7-25 (**TB7-27 with a lower interlock or platform gate**), green TB7-29.
  - VPL-3353B/3375B: white TB7-33, green TB7-32 (remove the "Pit Switch" junction-box jumper, or wire it in series with the pit switch).
- **VPL-K-3246 (ILS-01453)** and **VPL-K-3247 (ILS-01472)** (10/31/19), **tall** VPL-3200B(FZ) and VPL-3310B(FZ). The sensor goes in a bottom wire raceway.
  - No pit switch: green TB10-50 → 51, then sensor red and white TB10-50, black TB10-67, green TB10-51.
  - With a pit switch: butt-splice; the pit switch goes between 50 and 51.
  - 3310B: the red and white go to TB10-51; **don't take the green from the emergency lowering cable**.
- **Test:** a **damp cloth across the pins** stops the lift both ways and the **red LED flashes every 10 s**; dry = green flashes and it runs. On tall units, the **four green safety LEDs on the board go out** while wet.
- **Won't run:** check for about **24 VDC on red/black** and that green and white are on the right terminals.

Feeds: [[VPL-Troubleshooting]], [[VPL-Installation]], [[VPL-3100B]], [[VPL-3200B]], [[VPL-3300B]]
