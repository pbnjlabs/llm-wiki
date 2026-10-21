---
type: source
manufacturer: Bruno
doc_type: Instruction Sheet
source: "MANUALS/Bruno/Drawings/VPL/ILS-01036.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01108.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01119.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01130.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01131.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01132.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01133.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01138.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01139.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01140.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01166.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01198.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01248.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01269.pdf; MANUALS/Bruno/Drawings/VPL/ILS-01309.pdf"
url: https://www.brunopartner.com/er26ya59sp/drawings.aspx
date: 2023-05-02
tags: [bruno, vpl, ils, timer, esi, door-operator, gate-operator, open-sesame, duraswing]
---

# ILS - VPL Interlock Timers and Door Operators

**Interlock shut-off timers:**
- **ILS-01036** tall VPL **VPL-K-3222/3223** (+ **VPL-K-3225** add-on) (Rev 2, 9/3/13); **ILS-01108** low-rise **VPL-K-3140** retrofit (10/31/12).
- Each timer powers an electric strike when the landing limit trips, then cuts it after the set time (range 0.1 s–1000 h). **Set it to about 6 s.** Top dial = range, bottom dial = fine.
- Yellow monitor wire to the landing's call buttons:
  - tall: TB8-**65 upper**, **66 lower**, **64 mid**
  - low rise: TB7-**23 upper**, **22 lower**
- Low rise needs an interlock wiring kit fitted first.
- Test: unlocks at its landing, relocks after the time, and a **call button re-energizes it**.

**Landing door operator wiring kits:** these add a **landing detection switch** stacked on the landing limit switch, a delay-off timer and an operator harness. The timer's contact starts the operator cycle: unlock the strike, open, hold, close. **Re-trigger with the landing's DOWN (lower) or UP (upper) button.**
- Low-rise lower **VPL-K-3141 (ILS-01130)** and upper **VPL-K-3142 (ILS-01131)** (Rev 6, 7/22/15): short black #20, yellow #22 (lower) / #23 (upper), switch black #33, red to timer A1; DIN rail riveted in the enclosure; lower interlock harness red 27, white 26, black 25.
- Low-rise upper retrofit **SPO-04607 (ILS-01248**, 11/13/14): black to the chassis ground stud, yellow TB2-8, ULDS black TB2-3, red A1; operator enable black 15, red 18.
- Tall lower **VPL-K-3234 (ILS-01132)** yellow **#66**, upper **VPL-K-3235 (ILS-01133)** **#65** (3/6/15).
- **Mid landing VPL-K-3238 (ILS-01198**, Rev 5, 11/6/15): needs the **3-stop kit VPL-K-3233 first**. Timer top switch 1–10 s, **blue knob 2 s** (delay), bottom knob **"Ac"** mode, yellow **#64**. **Hold the mid-landing button until the door starts to open.** If it opens while passing the mid landing, raise the blue knob slightly.

**Platform gate operators:**
- **VPL-K-3144LCP/RCP (ILS-01140**, 05/02/23) is an Open Sesame operator on the platform gate (QR install video):
  - mounting plate VPL-31172; fixed-arm bracket **VPL-31194CP**, drilled and tapped ¼-20
  - new handle with one shim and two RBW-38001 washers
  - **home switch**: with the door about **2 in open**, line the red dots so the home LED lights; it stays lit when closed
  - rain cover **VPL-31323CP**, with RTV outdoors
- Wiring kits:
  - low rise **VPL-K-3143 (ILS-01138**, 05/02/23): timer; cable in split loom on the travelling cable, **not where the cable weight slides**; the timer should shut off before the gate closes
  - tall **VPL-K-3237 (ILS-01139**, 9/30/13): timer enclosure, TB8-58/66
  - tall **VPL-K-3239 (ILS-01269**, 05/02/23): red TB10-58, black TB10-67, 2-wire plug on **JP9**; delay set on **PCB-00164's BOT TIMER pot**
  - low-rise commercial **VPL-K-3361 (ILS-01309**, 05/02/23): red TB10-33, black TB10-20, JP9
- Tape the cables where the cable weight rolls over them. Re-trigger with DOWN held about 1 s.
- **The lift must stop at the lower landing on the lower landing switch, not the safety pan switches**, or the operator won't open the gate (ILS-01269).

**Commercial landing door operators (DuraSwing DS-4H):** **ILS-01119** (Rev 2, 7/15/19, kit **VPL-K-3302**, includes the 19-page DS-4H manual) and **ILS-01166** (12-22-2015, 3-gate lower landing, **VPL-K-3317L/R**, bracket VPL-33204).
- **Hardwire it for commercial use**: open the bottom holes to 7/8 in for ½ in fittings, and run **signal and AC in separate conduits** (the operator acts erratically otherwise).
- Bruno cable **VPL-33046** to the landing control enclosure on the tower.
- Weatherproof kit DS-WP; threadlock the fasteners.
- **DS-4H setup and LED codes:**
  - The home switch isn't a limit: set it with the collar, door closed. R30 = open angle, R31 = hold time, R12 = master force.
  - **2 blinks at power-up = ready.**
  - **Steady on = closing relay**; on for 7 s, then 3 blinks with no movement = no motor power (F1 10 A, F3 4 A).
  - **Blink-blink-pause loop = home switch not made.**
  - **3 blinks after a failed open = encoder or motor**: the door jumps a few inches and closes = encoder.
  - A stiff motor should move with 2–4 lb at the end of a 2 ft arm.
  - Door opens by itself = home switch, or trigger wires run beside AC.
  - Isolate it by jumpering terminals 1–2.

Feeds: [[Automatic-Door-Operators]], [[Gate-and-Door-Interlocks]], [[VPL-3100B]], [[VPL-3200B]], [[VPL-3300B]]
