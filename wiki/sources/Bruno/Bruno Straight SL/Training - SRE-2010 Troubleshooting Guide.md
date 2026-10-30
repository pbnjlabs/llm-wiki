---
type: source
manufacturer: Bruno
model: SRE-2010
doc_type: Training Doc
source: "MANUALS/Bruno/Training/Installation & Troubleshooting/Troubleshooting Guide for current SRE-2010.pdf"
date: 2014-09-26
tags: [bruno, stairlift, sre-2010, training, troubleshooting]
---

# Training - SRE-2010 Troubleshooting Guide

4-page "unit does not operate" checklist from Bruno's dealer **training** library (Installation & Troubleshooting docs), titled *Troubleshooting Guide (9/26/14), SRE-2010*; the file was published as "for current SRE-2010" (PDF dated 2026-01-30). It's the **fuller version** of [[Tech Tip - SRE-2010 Troubleshooting Guide (No Power Options)]]: twelve steps instead of eight, and several numbers changed (below). Manufacturer-authored, ranked like a tech tip: the [[SRE-2010 Tech Support Guide]] and install manual win any conflict.

1. **Code display** under the seat: look the code up ([[Diagnostic-Codes]]). Not lit → next step.
2. **Batteries:** voltage and load test. No load tester: take the batteries out, unplug the motor leads from the board, and on each battery in turn read the voltage, then connect the motor across it and read again. **More than 2 V drop = bad battery.** Cut off any connector that's turning brown and replace it.
3. **Charger:** red light on? No → charger fuse or incoming power. The carriage must sit on the contacts **3 s** before the board starts charging. Battery voltage on the contacts vs off them should **rise at least 0.5 VDC**. No rise with the red light on → tighten connections, then unplug the charge harness at the rail and at the board (red, black, purple) and read each wire end to end: **under 0.5 Ω**. Clean carriage and rail contacts and retest; all good → replace the charger.
4. **Charge connections:** orange connector (red, black, purple) off the board, each wire to its rail contact **0.5 Ω or less**.
5. **Board input** B+/B− (red/black): the board needs **16 V to turn on, 22–24 V to run up, 20–22 V to run down**. Low → breaker (on/off switch), final limit or overspeed.
6. **Seat safety:** in multi-user mode a bad or unmade swivel switch beeps every 3 s. Unplug the seat safety harness, jump the 2 pins, try the rocker.
7. **Limits** (single beep on rocker or call/send = limit circuit open): unplug the limit harness and jump the 3 pins (bypasses **every** limit, keep off the end stops). Runs → footrest, carriage limit switches and wiring. Facing the seat: **won't go to your right = green circuit, won't go left = red circuit.**
8. **Rocker:** no relay click and no movement → try call/send; works → rocker circuit. Unplug the rocker harness, centre pin to either outer pin.
9. **Motor voltage** (relays click, no movement): resting battery off the contacts **25–27 VDC**. Meter on the blue and orange motor leads (careful not to touch other parts of the board). Motor connected, battery 25 V+: about **21–22 VDC up, 23–24 VDC or more down**; motor disconnected: battery voltage. No voltage with everything jumped out → board. Right voltage → power the motor direct; doesn't run → motor.
10. **IR inputs:** red wire of the IR harness to battery ground **5 VDC**; none → board. Good → check the call/send battery. Intermittent → take the call/send off the wall and point it at the chair (may need mounting sideways); still intermittent → jump the swivel and limit switches: a safety may be set too close to its plate.
11. **Communication strip (folding rail):** sent down with the rail folded, it should stop on the mid-park strip. Parked on it with the harness connected: **about 17 V (manual fold) or about 6 V (power fold)**. None → unplug the red/black/purple harness; purple wire to the strip **under 0.5 Ω**.
12. **Key switch:** a single beep both ways = key off or faulty. Continuity across its 2 board pins; jumper them, runs → switch or its wire.

**Changed from the 2016 tech tip:** charge-contact rise **0.5 V** (was 1 V); board thresholds 16 / 22–24 / 20–22 V (was "18 V or more"); motor voltage down **23–24 V** (was "12 V or more"); new battery test without a load tester, charge-harness resistance, red/green circuit rule, comm strip voltages and key switch step.

Feeds: [[SRE-2010]], [[Stairlift-Troubleshooting]]
