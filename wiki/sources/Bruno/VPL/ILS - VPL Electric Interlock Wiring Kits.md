---
type: source
manufacturer: Bruno
doc_type: Instruction Sheet
source: "MANUALS/Bruno/Drawings/VPL/ILS-00718.pdf; MANUALS/Bruno/Drawings/VPL/ILS-00976.pdf; MANUALS/Bruno/Drawings/VPL/ILS-00977.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01034.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01035.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01048.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01049.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01052.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01053.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01170.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01251.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01261.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01440.pdf"
url: https://www.brunopartner.com/er26ya59sp/drawings.aspx
date: 2019-02-04
tags: [bruno, vpl, ils, interlock, electric-strike, emi, esi, wiring]
---

# ILS - VPL Electric Interlock Wiring Kits

Wiring kits for **door interlocks**: **EMI** (electro-mechanical, e.g. Waupaca) and **ESI** (electric strike, e.g. Von Duprin).

**Low-rise VPL-3100 / 3100B:**
- **ILS-00718** (2/12/07): dealer-supplied Access Industries ES1 strike, harness **VPL-31197**.
- **ILS-01048** **VPL-K-3138** upper and **ILS-01049** **VPL-K-3139** lower (both 3/31/15).
- **Voltage warning: VPL-3100 (AC) needs a 24 VAC interlock; VPL-3100B (DC) needs a 24 VDC interlock.** The wrong one can damage the interlock or the board.
- Both kits add a **second limit switch** beside the landing switch, using the longer screws.
- Upper: green to TB7-20, violet to TB7-33, then remove the shorting connector (blue wire).
- Lower: move the yellow jumper to **27–29**; harness VPL-31912 red TB7-27, black TB7-20, green TB7-25, white TB7-26.

**Tall VPL-3200B:**
- **ILS-00976 VPL-K-3219 upper** (11/1/10): green into **TB3-7**; the green wire on the "Upper Gate Enable" switch is taped off and yellow goes to the bottom limit switch.
- **ILS-00977 VPL-K-3220 lower** (12/2/10): BLK9–11 off **TB4-4/5/6** and taped; the white from TB5-2 is reused; **cut jumper J1** on the board; drawing SCH-00176.
- **ILS-01034/01035** (10/19/11) are the later versions of K-3219/K-3220, and **ILS-01052/01053 VPL-K-3228/K-3229** (4/19/12) are the next kits. All of them add a stacked limit switch (**red COM, back terminal; black N.O., middle**) and plug the "Upper/Lower Interlock" 6-pin harness after **removing the shorting jumper**.
- Test: **door open = lift won't run; door closed = it runs.**
- **ILS-01251 SPO-04690** (12/2/14), a **lower door EMI plus a platform gate**: on TB8, pull the yellow 59–61 jumper (keep it for troubleshooting), move red 61→59, white 62→61, green 63→61. EMI terminals: red 4, black 3, green and brown 2, white 1. It must not run with **either** the door or the gate open.

**Bruno ESI kit (ILS-01261, 02/19/15)** on an existing door: strike just below the handle. **E1/E2 = solenoid** (VPL-31918 red/black), **11–12 door closed** (brown jumper/white), **21–22 door locked** (green/brown). The door must open within the landing timer's window. **ILS-01440 VPL-K-3366** (2/4/19): **key removal** from the ESI. Fit the ½ in screws, put the Bruno label over the gray circle, and fix the cover plate with security screws (bit supplied).

**Flush-mount door wiring (ILS-01170 Rev 2, 4/10/16):** commercial uses harness **VPL-33287 (12-conductor)**, residential **VPL-31918 (5-conductor)**. **Pull the tower breaker before plugging in the connectors, or the 24 V fuse blows.** Leave 6–12 in past the interlock; green and black/white usually unused. **The timer option must be installed** for proper door operation.

Feeds: [[Gate-and-Door-Interlocks]], [[VPL-3100B]], [[VPL-3200B]], [[VPL-Troubleshooting]]
