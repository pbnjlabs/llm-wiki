---
type: source
manufacturer: Bruno
model: VSL-4000HW
doc_type: Install Manual
source: "MANUALS/Bruno/Vehicle Lifts/VSL-4000HW INSTALLATION _01-10-2017.pdf"
date: 2017-01-10
tags: [vehicle-lift, bruno, vsl-4000hw, joey, install, legacy]
---

# VSL-4000HW Hardwire Joey Installation Manual (01-10-2017)

Install manual for the legacy **VSL-4000HW "Hardwire" Joey** in-vehicle
platform lift (24 pages; © 2007–2017). It came before the [[VSL-4400]].

- **350 lb (159 kg)** (Joey assembly VSL-40246). Ships in 3 cartons:
  lift, platform with belts and chocks, mounting kit. **Grade 8**
  replacement hardware.
- **Power:** run from the battery through the interior with an in-line
  fuse at the battery.
- **Door safety switch** (normally closed):
  - Gap between the switch and magnet **¼–⅜ in max**.
  - Wired white to white.
  - Test it with the pendant on: the lift must not run with the door
    closed.
- **Mounting:**
  - Drive the carriage about 12 in onto the rail.
  - The rail-to-kit channel screw goes through the mounting kit "leg".
  - Platform about 2–3 in above the ground.
- **Chocks (wheel wedges)** adjust per the hardware stack in the manual.
  The barrier installs per ILS-00943.
- **Emergency electrical backup:**
  1. Check the **fuse**.
  2. Slide the shroud off (2 screws) and unplug the **red 8-pin pendant
     connector**.
  3. Use board buttons **A (OUT), B (IN) and C (UP or DOWN)**. Button
     C's direction is set by the **J8 XTRA jumper**: OFF = up, ON = down.
  4. **The buttons bypass every limit switch**: tap them near the end
     positions.
  5. Reconnect, then cycle power at the pendant.
- **Board LEDs:**
  - 1 = IN limit, 2 = OUT limit, 3 = MAST limit.
  - **INVALID OPERATION**: return it home (all the way up and in), or
    cycle power.
  - At least one LED is lit whenever the board has power.
- **Emergency manual backup:**
  - The tools are under the shroud, on the carriage.
  - **If the actuator failed as it started to extend, take the mobility
    device off first.**
- **Troubleshooting:** the fuse at the battery, the pendant ON/OFF
  switch, the door safety switch connection.

Feeds: [[VSL-4400]]
