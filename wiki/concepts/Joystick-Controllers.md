---
type: concept
tags: [controller, joystick, q-logic, pride]
---

# Joystick Controllers — Q-Logic / Q-Logic 3 (Pride)

Pride/Quantum Rehab's controller family, used across [[J6]] and
[[Q6-Edge-3-Stretto]] (and other Pride/Quantum chairs not yet on file).
Two generations documented here: legacy **Q-Logic** and current
**Q-Logic 3**.

## Q-Logic (legacy)

Source: [[Q-Logic Controller Basic Operation Instructions]].

Modular electronic controller system, factory pre-programmed, with several
input-device form factors sharing the same core mechanics:
- **Hand control** (standard, or "with Lights" variant adding horn/turn
  signal/hazard/headlight buttons for road use)
- **Attendant Control** — simplified rear-mounted control for an ambulatory
  attendant
- **Stand-alone Joystick**
- **Enhanced Display** — color LCD, optional built-in IR, can drive
  specialty input devices (head arrays, switches) and Bluetooth mouse

Core mechanics: On/Off and Mode Select Lever (push up = power on/cycle
through up to 5 drive profiles; push down = power off — **not an
emergency-stop control**, will stop the chair abruptly if misused),
joystick drive with electromagnetic brake engagement at neutral,
programmable lock/unlock (lock: hold lever in "on" position until
controller turns off; unlock: power on, then full-forward then
full-reverse joystick), speed adjustment knob, actuator adjustment via seat
screen (up to 5 power seat actuators — tilt/elevate/recline/ALR/ELR
combinations), Sleep Mode (0–240 min idle timeout), Thermal Rollback
(reduces output to 20% when overheated, resumes automatically once cool),
Battery Condition Meter (green=full, amber=partial, red=low).

### Q-Logic error codes

| Code | Diagnosis | Solution |
|---|---|---|
| 35, 37 | Joystick Fault/Connection | Check joystick cable connection |
| 36, 110 | Joystick Not Centered | Release joystick while turning chair on |
| 46 | High Battery Voltage | Disconnect charger |
| 47, 101, 105 | Low Battery Voltage | Charge battery |
| 49–53 | Motor Not Connected | Check motor brake connector |
| 74–75 | Motor Disconnected | Check motor brake connector |
| 81–90 | Motor/Brake Fault | Check motor brake connector |
| 107 | Charger Drive Inhibit | Disconnect charger |
| 111–112 | Center Detect Fault | Check joystick cable connection |
| 131–132 | Motor Fault | Check motor wiring |
| 141, 187 | Drive/Actuator Restriction | Clear restriction |
| 192–195 | Motor Disconnected/Shorted | Check motor brake connector |
| 200–201 | Motor Fault | Check motor wiring |

Any other code, or persistence after the listed fix: contact the Quantum
Rehab Provider. See also [[Q6 Edge Basic Troubleshooting]] for a broader
symptom-based checklist (dead system, reduced range, slow operation,
pulling, clicking) that's a natural companion to this error-code table.

## Q-Logic 3 (current)

Sources: [[Q-Logic 3 Basic Operation Instructions]] (end-user) and
[[Q-Logic 3 Programming Guide]] (provider/ATP-level).

Touchscreen-based successor to Q-Logic. End-user operation (Home screen,
Settings, drive-profile selection, actuator/seat screen, Standby Select) is
conceptually the same as legacy Q-Logic but presented on a touch interface
rather than a keypad+LCD.

### Programming (provider-level only)

Programmed via **Econ-W** (PC software, wired or Bluetooth-connected to the
controller — Bluetooth allows real-time adjustment while the client is
driving, without tethering by cable) or **HHP** (Hand-Held Programmer, a
standalone field device exposing the same parameter tree as an on-screen
menu). All programming changes carry an explicit safety warning: incorrect
settings can affect speed, acceleration, deceleration, dynamic stability,
and braking.

Startup behavior is configurable: which input device powers up by default
(default device / last device used / input-selection screen / power-on
device), and what screen the system opens to (Home, a numbered drive
profile, input selection, auxiliary, seat, or last-used).

**Supported input devices**, each with its own programming section:
- **Proportional hand control** — center deadband, tremor suppression,
  direction assignment, joystick throw
- **Proportional/mini-proportional alternative drive controls** (mo-Vis
  All-Round/Stealth Mushroom/Switch-It-A-Can and mo-Vis
  Micro/Multi/All-Round Lite) — plug into the 9-pin SCIM/Enhanced Display
  port, require joystick calibration (move in two circles) before first use
- **Head array** — 3-switch or i-Drive 4 (3-direction proportional) variants
- **Sip-N-Puff** — 2-pressure (double-puff/sip = forward/reverse) or
  4-pressure (hard vs. soft puff/sip) configuration, with latch-driving
  modes (Cruise / 3-Step / 1-Step) and configurable braking behavior on a
  >50% reverse command
- **Switches** — 5/4/3/2/1-switch scanning, including a "linked" 2-switch
  driving mode that's internally programmed as a 3-switch head profile
- **iAccess** — 4-button module, up to 19 mappable functions across up to
  5 pages

Up to **4 specialty controls** can be connected simultaneously (one 9-pin
on the Enhanced Display, one 9-pin on the SCIM module, Sip-N-Puff module,
1-switch scanning), switchable via the **Change Input Device** menu — handy
for evaluations. **Clinic Mode** offers a no-programmer quick-setup path
for a clinician/ATP to demo alternative drive devices.

**Seat/actuator programming**: drive-inclination thresholds (limits driving
while tilted/reclined), latched actuators (single command runs the actuator
for a programmed timeout instead of requiring the command held), input
command inversion (for users who find forward-to-exit-tilt counter-
intuitive), pretilt angle presets (max 25° while still drivable), and
**Combined Functions** — grouping multiple actuators (e.g. recline + back +
legs) under one mapped switch/timeout to approximate "memory seating"
behavior (explicitly *not* true memory seating, just a naming convention to
avoid).

**Bluetooth**: mouse-emulation pairing to phones/tablets/computers, with a
dwell-click option for users who can't physically click.

This is the wiki's first fully-ingested controller/joystick-system
documentation — a natural hub for any future controller manuals (Pride,
Golden's PG/LiNX/Dynamics/Shark controllers, etc.) that need cross-model
comparison.

## See also

- [[J6]], [[Q6-Edge-3-Stretto]]
- [[Tru-Balance-3-Power-Positioning]] (Q-Logic 3 inhibit-matrix integration
  with iLevel/tilt)
- Golden's controller-adjacent pages, for cross-manufacturer contrast:
  [[LiNX-Diagnostics]], [[Flash-Beep-Diagnostics]],
  [[Golden-Joystick-Side-Conversion]]
