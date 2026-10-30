---
type: source
manufacturer: Bruno
model: SRE-3050
doc_type: Training Doc
source: "MANUALS/Bruno/Training/Installation & Troubleshooting/Troubleshooting Guide SRE-3050 Elan.pdf"
date: 2019-10-17
tags: [bruno, stairlift, sre-3050, sre-3000, elan, training, troubleshooting]
---

# Training - SRE-3050 Elan Troubleshooting Guide

3-page "unit does not operate" checklist from Bruno's dealer **training** library (Installation & Troubleshooting docs), dated **10/17/19**, for the **SRE-3050 Elan**. It's a later version of [[Tech Tip - SRE-3000 Elan Troubleshooting Guide]], with a **motor brake test** and a **phone-camera remote test** added. Manufacturer-authored, ranked like a tech tip: the [[SRE-3050 Tech Support Guide]] wins any conflict.

1. **Battery:** load test; **at least 23 V to run up, 21 V down**; the controller cuts out under load at **about 16 V**.
2. **Charger LED** red, yellow or green? None → charger fuse or incoming power. Unit **on 3 s** before the board charges; the charger needs **at least 4 V** to turn on, and turns on below **26.5 VDC**. Battery voltage with the charger on vs off the rail should differ by **at least 1 VDC**; none with the red light on → check each lead back to the board, clean the contacts, then replace the charger.
3. Carriage and rail contacts: clean; battery voltage should be on them if the board's charge circuit is good.
4. **Board B+/B−** (red/black) **18 VDC or more**? No → breaker, final limit or overspeed governor.
5. **Limits:** jump the 3 pins on the limit connector at the board corner, both armrests down (barrier-arm switches), try the rocker. Bypasses every limit: keep off the end stops.
6. **Seat safety:** unplug the 5-wire seat switch/rocker harness, jump the 2 pins nearest the board corner; run with a remote, or centre pin to either outer pin. **Never jump all the pins together** (board damage).
7. **Rocker:** jump red–black or green–black on the 5-pin connector, or unplug it, 2-pin jumper on the seat switch pins, then centre pin to either outer pin.
8. **Motor voltage:** resting **25–27.5 VDC**; on the blue and orange motor leads, with **26 V+** resting expect **20 VDC or more**. Right voltage, motor doesn't run → power it direct; relays click but no motor → step 9. Low or none → board.
9. **Motor brake:** take the 3 brake screws out and lift the brake off. Motor runs now → test the brake circuit: brake leads off the board, meter on the brake terminals, rocker → **battery voltage** (none → board). Refit the brake. One brake lead goes straight to the board, the other **through the circuit breaker**: move that one to the board too. Runs → **replace the breaker**; still no brake → replace the brake.
10. **IR inputs:** red wire of the IR harness to battery ground **5 VDC**; none → board. Intermittent remotes: check the remote batteries; jump the limits and seat switch (runs fine → a safety is set too close to its switch); look at the remote's end through a **phone camera in selfie mode** while pressing a button: no IR light → replace the remote.

**Changed from the 2016 tech tip:** one motor-voltage figure (20 V+ at 26 V resting) instead of 23–24 V up / 12–13 V down; brake and phone-camera tests added; the key switch step is gone. **Flag:** this guide calls the motor leads **blue and orange**; the 3050 tech support guide's brake section says **blue or brown**. Go by the colours on the board.

Feeds: [[SRE-3050]], [[SRE-3000]], [[Stairlift-Troubleshooting]]
