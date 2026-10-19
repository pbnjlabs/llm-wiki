---
type: source
manufacturer: Pride
doc_type: Service Bulletin
source: "MANUALS/Pride/TechnoBulletins/jazweb151.pdf; MANUALS/Pride/TechnoBulletins/jazweb164.pdf; MANUALS/Pride/TechnoBulletins/jazweb165.pdf; MANUALS/Pride/TechnoBulletins/jazweb168.pdf; MANUALS/Pride/TechnoBulletins/jazweb169.pdf; MANUALS/Pride/TechnoBulletins/jazweb170.pdf; MANUALS/Pride/TechnoBulletins/jazweb171.pdf; MANUALS/Pride/TechnoBulletins/jazweb174.pdf; MANUALS/Pride/TechnoBulletins/jazweb175.pdf; MANUALS/Pride/TechnoBulletins/jazweb176.pdf; MANUALS/Pride/TechnoBulletins/GENERAL009CA.pdf; MANUALS/Pride/TechnoBulletins/GENERAL011-NFC-Key-Tag-Techno-Bulletin.pdf"
date: 2024-04-04
tags: [pride, technobulletin, service-bulletin, jazzy, q6-edge, scooter, gc3, dynamic, voltmeter, nfc]
---

# Pride TechnoBulletins (12 bulletins, 2006–2024)

The newer bulletins from the PQ-365 TechnoBulletins list (the library
also holds Jazzy 001–166, mostly 1990s–2000s product releases, not
pulled). One page each; the [[S19 Analog Console Part Runout (GENERAL-010)|GENERAL-010]]
bulletin has its own page.

| Bulletin | Date | Content |
|---|---|---|
| JAZZY-151 | 2006-11-10 | **VR2 controller release**: 5 profiles, sleep, thermal rollback, replaceable cable, 60 A (70 A option) |
| JAZZY-164 | 2008-05-02 | **Jazzy 614HD release**: 450 lb, Dynamic 50 A, seats to 24 × 24 in, rear battery access, 5 A charger |
| JAZZY-165 | 2008-05-02 | **Dynamic 50 A controller** release (Jazzy 614 series): service indicator, system status light, sleep, OONAPU |
| JAZZY-168 | 2010-08-18 | **Q6 Edge seat height and seat angle (dump)**: move the L-brackets up/down (one set only for dump), blue thread lock, **35 N·m (25.8 ft·lb)**, new nylon nuts |
| JAZZY-169 | 2011-01-13 | **GC charge reminder**: after 8 h of driving without a charge, left red LED flashes 4× at 0.5 s at every power-off; reset by a full charge with the controller **on** |
| JAZZY-170 | 2011-05-05 | Update to 169 (GC2/GC3): controller on → charger to controller → charger to wall → full charge (8–14 h) → unplug wall, then controller → power-cycle. Batteries already full? Drive a while first: the charger must actually charge to reset it |
| JAZZY-171 | 2011-06-20 | Q6 Edge: improved battery harness routing (quick-disconnect locations; figure only) |
| JAZZY-174 | 2013-02-11 | Q6 Edge HD: correct battery harness routing (figure only) |
| JAZZY-175 | 2013-10-22 | Jazzy 600 ES: battery harness routing (figure only) |
| JAZZY-176 | 2013-10-22 | Jazzy 600 ES **motor harness**: M1 port → **left** motor, M2 → **right**. Error table: **3 = right motor, 4 = left motor, 5 = right brake, 6 = left brake** (opposite of the Jazzy 614 TTG; see [[Jazzy-600-ES]]) |
| GENERAL-009CA | 2022-02-23 | **Scooter voltmeter options** (below) |
| GENERAL-011 | 2024-04-04 | **NFC key tag programming** (below) |

**GENERAL-009CA, voltmeters (Canada bulletin):**
- **DGN142447**, black PCB, 2 red / 3 yellow / 5 green: SLA with a
  **TruCharge** program (PG S-Drive Status Output Type = 0; Dynamic
  R-Series PIN 10 = Other). Start-up: ten bars then one, then voltage;
  controller fault = all ten lit while the blue LED flashes the beep
  code. Program wrong = one red LED and blue only. Wrong voltage shown
  → charge above **26 V** (the program's reset voltage; S66/S67
  programs lowered to 25 V on 2/14/22).
- **ELE1906793**, green PCB, same LED layout: SLA, **non-TruCharge**
  (S-Drive Status Output Type = 1; R-Series PIN 10 = Status Low). Sweeps
  left to right at start-up. Wrong program = blue LED blinks randomly.
- **ELE2008025**, green PCB, 3 red / 4 yellow / 3 green: **lithium
  (LiFePO4)**, non-TruCharge, Dynamic R-Series only. 3 green = 90–100%,
  2 = 80–90, 1 = 60–80; 4 yellow = 50–60, 3 = 40–50, 2 = under 30,
  1 = under 20; all red = dead. Charge with **no fewer than 4 yellow
  left**. Calibrates for up to 2 min while driving.

**GENERAL-011, NFC key fobs (scooters with NFC tiller):** remove the 2
screws in the tiller console bottom plate and the tiller knob, slide the
plate down. Hold the PCB button and press power until a **4-note tone
twice** (≈10 s) = all keys unpaired. Power off; power on and hold fob 1
over the NFC label until it sounds. Second fob: power off, hold the PCB
button, press power, release the button, present fob 2. **PCB
ELE1908966 Rev C** pairs with a 4-note tone and is silent at start-up;
**Rev D** beeps rapidly on pairing and gives a 2-note tone at start-up
(rev letter also on the harness label in the tiller). Won't pair →
new fob, then reset all and re-pair.

Feeds into: [[Q6-Edge]], [[Q6-Edge-HD]], [[Jazzy-600-ES]],
[[Jazzy-614]], [[Pride-Controller-Flash-Codes]], [[TruCharge-Diagnostics]],
[[Pride]].
