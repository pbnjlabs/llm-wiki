---
type: source
manufacturer: Bruno
doc_type: Instruction Sheet
source: "MANUALS/Bruno/Drawings/VPL/ILS-00895.pdf; MANUALS/Bruno/Drawings/VPL/ILS-00897.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01012.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01018.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01092.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01093.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01117.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01321.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01408.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01481.pdf"
url: https://www.brunopartner.com/er26ya59sp/drawings.aspx
date: 2020-02-24
tags: [bruno, vpl, ils, electrical, circuit-breaker, pcb, emergency-lowering, keyswitch, 240v, disconnect, phone]
---

# ILS - VPL Electrical Retrofit Kits

- **External circuit breaker kits (ILS-00895/00897, 8/3/09):** **SRV-3100-023 DC** and **SRV-3100-022 AC**.
- **Emergency lowering kit VPL-K-3212 (ILS-01012**, 6/14/11): **red contact block N.C.** (white and green), **green N.O.** (black and red), 4-pin in-line connector on the centre tube. **It lowers at half speed** and stops at the bottom.
- **Keyswitch bypass VPL-K-3134 (ILS-01018**, Rev 2, 3/21/16): for any call/send, gate or platform control, rocker or paddle.
  - Rocker stations: remove the red jumper; the cable's red wire goes to the **centre rocker terminal**.
  - Paddles: a metal jumper across the keyswitch terminals with heat-shrink.
  - Optional hole plug and decal.
- **AC board daughter-boards:** **SRV-3100-030 (ILS-01092**, 9/7/12) **PCB-00131** for **PCB-00107**, and **SRV-3100-031 (ILS-01093**, 8/22/12) **PCB-00132** for **PCB-00129**. They **lock out both directions if UP and DOWN are pressed together**. Test it: press both, and the lift must not move.
- **DC logic board retrofit (ILS-01408**, 12/11/2019): **PCB-00141 or PCB-00159 → PCB-00164**.
  - **ESD strap.**
  - Move the connectors; set jumpers **S3/S4** as on the old board.
  - Set the delay pots **VR2 = top, VR3 = bottom** for interlocks or door operators.
  - Doors and operators must **not** be energized at power-up.
- **120 V → 240 V conversion VPL-K-3158 (ILS-01321**, 9/23/16): a transformer on foam tape at the top of the tower feeds the charger; adapter from SRE-K-2174; labels DEC-00585/00586.
- **Auxiliary contact disconnect VPL-K-3368 (ILS-01481**, 02/24/2020): for **VPL-3300B and VPL-3310B commercial lifts**, to meet **NEC 620.91(C)** (one disconnect drops all normal power).
  - A contactor is spliced into the big red battery wire.
  - **The fused red wire must be on the battery side** (35 A breaker on low rise, 60 A on tall), or the contactor won't pull in.
  - Coil ground to **TB10-20 (low rise) / TB10-68 (tall)**; 2 A fuse inside.
  - Test: cut the black loop and the board stays dark. The black loop then goes to the building disconnect's auxiliary contact.
- **Telephone kit VPL-K-3301 (ILS-01117**, 02-19-13, commercial): Rath SmartPhone, wired to the tower's lower landing box (red and green); plug in the phone's internal battery.
  - Troubleshooting: **about 48 V** on the line; low audio → VR1 (speaker) / VR2 (mic); won't hang up → the phone system needs CPC, or press * then #; hum then hang-up → bad microphone.
  - Rath support 800-451-1460.

Feeds: [[VPL-Troubleshooting]], [[VPL-3100B]], [[VPL-3153-3175]], [[VPL-3200B]], [[VPL-3300B]]
