---
type: source
manufacturer: Golden
model: GP162
doc_type: Supplemental Insert
source: "MANUALS/Golden/GP162 LiteRider Envy LiNX Insert Golden 06.29.2018.pdf"
date: 2018-06-29
tags: [golden, gp162, literider-envy, linx, diagnostics]
---

# LiteRider Envy LiNX Supplemental Insert (GP162)

2-page mandatory supplement for GP162 units built with the **LiNX
controller** (distinct from the PTC/VR2-controller variant — see
[[LiteRider PTC Service Guide (GP162, PG VR2 Controller)]]). Covers:

- Controls: joystick, speed dial, power button/status indicator, horn
  button, battery gauge (5 LEDs: 1 red, 2 amber, 2 green), XLR charger
  connector, communications bus connector.
- OONAPU ("Out Of Neutral At Power Up") safety interlock: if the joystick
  isn't centered at power-on (or when exiting an inhibit state), the chair
  won't drive; battery gauge flashes continually; clears if joystick
  returns to center within 5 seconds, otherwise the status indicator
  flashes red and requires a power cycle with the joystick at rest.
- Drive inhibit indication: right-to-left chasing light sequence on the
  battery gauge, repeating until the fault clears.
- Battery gauge readout (charge level, separate from fault flashing):
  5/4/3/2/1 LEDs lit = fully charged down to needs charging. High-voltage
  warning = all LEDs on with green flashing. Low-voltage warning =
  left-most LED flashing. Cut-off voltage = red LED flashes, status
  indicator shows flash code 2, horn beeps every 10s.
- **LiNX status indicator flash codes (1-7)**:

| Code | Meaning | Remedy |
|---|---|---|
| 1 | Remote/joystick error | Check LiNX connections/wiring; replace LiNX Control Unit |
| 2 | Network or configuration error | Check LiNX connections/wiring; replace LiNX Control Unit |
| 3 | Left motor error | Check left motor, connections, cabling |
| 4 | Right motor error | Check right motor, connections, cabling |
| 5 | Left park brake error | Check left park brake, connections, cabling |
| 6 | Right park brake error | Check right park brake, connections, cabling |
| 7 | Module error (other than Remote) | Check LiNX connections/wiring; replace Power Module |

This 7-code LiNX scheme is a different fault architecture from the
[[TruCharge-Diagnostics]] 10-bar scheme used on the PG VR2-controller
variant of the same GP162 model — confirms controller choice, not model
number, determines which diagnostic table applies (same lesson already
seen with [[Flash-Beep-Diagnostics]]).

Feeds: [[GP162-LiteRider-Envy]]
