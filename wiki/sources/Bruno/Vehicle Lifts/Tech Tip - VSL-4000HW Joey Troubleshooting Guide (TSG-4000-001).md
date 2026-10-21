---
type: source
manufacturer: Bruno
model: VSL-4400
doc_type: Tech Tip
source: "MANUALS/Bruno/Tech Tips/Vehicle Lifts/TSG-4000-001 VSL-4000HW Troubleshooting Guide.pdf"
url: https://www.brunopartner.com/er26ya59sp/tech-tips.aspx
date: 2016-01-13
tags: [bruno, vehicle-lift, vsl-4000hw, joey, tech-tip, troubleshooting, legacy]
---

# Tech Tip - VSL-4000HW Joey Troubleshooting Guide (TSG-4000-001)

TSG-4000-001, 9 pages (portal tech-tip 29), for the **VSL-4000HW Joey**, **serial 10100100777 to current** (as written): the Joey before the [[VSL-4400]]. Start with its install manual and Bruno's Brainshark Joey install video; you need a multimeter.

- **Won't turn on** (stowed, pendant on, no green light): pull the **PCB access plug** on the right of the carriage cover. **No red LEDs** → vehicle battery, the **fuse at the battery (+)** (blown → find the short: pinched twin-lead harness), then voltage at every connection to the board, both ends of the travelling cable. **Board powered but dark** → door safety switch or pendant harness: jump the **two white wires on top of the board** (bypasses the door switch **and** the pendant on/off, so the Joey stays live: troubleshooting only).
- **Mast limit switch** lost contact in transit → "**Invalid Operation**" (rightmost LED): the board stops everything. Engage or adjust the switch, then turn the Joey off and on.
- **Goes to the end of the rail but won't deploy:** actuator clutching → mast limit out of adjustment (move it toward the actuator; check the 1.5 in bumper below it). Not clutching → **inner carriage limit** tripped Invalid Operation: power-cycle; if it works, move that switch **away from the switch plate** (shorter than the bumper), check its bumper. **Don't pull on the platform** (damages the actuator tube and seal). Removing the switch plate fixes repeat errors but then obstructions won't stop the carriage.
- **Raises but won't go in:** the same inner limit "slap" at the transition, or **low voltage** (run the vehicle; check the In/Out motor on a fused known-good 12 V supply).
- **Stops and restarts while raising a load:** **low voltage**. The board cuts out below **8.5–9 VDC**. A battery reading 12 V at rest can sag under load; run the vehicle and load-test the battery.
- **Tries to go in with the platform on the ground:** broken mast limit switch or wire.
- **Loud actuator** and **popping** from the links are normal; Bruno charges a restocking fee on actuators returned for noise that are within range.
- **Electrical backup** on the board: button A drives the carriage **in**, C **out**, B runs the actuator in the direction set by the **actuator direction jumper** (top = up). It **bypasses all limit switches**. LEDs 1 inner limit, 2 outer limit, 3 actuator limit, 4 invalid operation.

Feeds: [[VSL-4400]], [[Bruno]]
