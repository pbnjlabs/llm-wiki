---
type: concept
tags: [controller, joystick, q-logic, q-logic-3, qlnes, ne-plus, pride, quantum]
---

# Joystick Controllers — Q-Logic family (Pride/Quantum)

Pride/Quantum Rehab's own controller family: legacy **Q-Logic**, the
**NE/NE+** electronics, **Q-Logic 3 / 3e**, and the 2024 **QLNES**.
Pride's **Jazzy** and retail chairs mostly use PG Drives (VR2, GC3,
newVSI) or Dynamic controllers instead; those are on
[[Pride-Controller-Flash-Codes]].

## Which controller is on the chair?

| You see | It is | Codes |
|---|---|---|
| Colour LCD hand control with on/off–mode lever and speed knob (2008-era) | Legacy **Q-Logic** | [[Q-Logic-Fault-Codes]] |
| Hand control J/AJ/LJ on a Power Base 75; LCD with **icons** and text messages | **Q-Logic NE / NE+** | Message table on [[Power-Chair-Troubleshooting]] §7 (from the Q6 Edge and J6 TTGs) |
| Display hand control or Enhanced Display, Home/Aux/Settings screens, Key I/II | **Q-Logic 3** (3e: Bluetooth under Settings) | [[Q-Logic-Fault-Codes]] |
| **LED-only** joystick, Key I/II, USB-C port, magnetic charger port | **QLNES** | [[Q-Logic-Fault-Codes]] (3-LED digit blink) |
| Speed dial; or 10-LED arc with speed/profile buttons; or service indicator | GC3; VR2; Dynamic | [[Pride-Controller-Flash-Codes]] |

Model-by-model electronics (2025–2026 charts): [[Pride-Power-Chair-Lineup]].
Chairs on file: [[Q6-Edge]] (original, NE/NE+/Q-Logic), [[J6]], [[J4]], [[Q6-Edge-3-Stretto]], [[Q6-Edge-3]],
[[Q6-Edge-4]], [[Q6-Edge-2.0]], [[Q6-Edge-HD]], [[4Front-2]],
[[R-Trak]], [[Jazzy-1450]].

## Q-Logic (legacy)

Sources: [[Q-Logic Controller Basic Operation Instructions]] (end
user) and the 138-page dealer [[Q-Logic Technical Manual (INFMANU3580)]]
(2008).

**System (tech manual):** plug-and-play modules daisy-chained on a
proprietary **CAN bus**: power module (the master; holds most settings),
hand control, Stand-alone Joystick (SAJ), attendant joystick (same
hardware as the SAJ, programmed differently, takes over when switched
on), Enhanced Display (colour LCD, IR, Bluetooth; required for Sip &
Puff and switch/specialty inputs), AAM (5 seat actuators), ECU (8
relays for environmental devices), Sip & Puff. Programming by
hand-held programmer or the Curtis **1314 PC Programming Station**
through **any** charger/programming port. Specs: 24 V nominal, 16–33 V
operating, 35 V max; bus up to 10 m and 10 modules, 13 A continuous.
The charger/programming port is a standard 3-pin XLR rated 13 A, plus
two programmer pins.

Behaviour worth knowing:
- **The input device that powered the chair on is in control.** To
  switch devices, power off and back on from the other one.
- Each input device has **5 profiles**; P1 is always drive, P2–P5 can
  be drive, seat or aux. Quick Setup Speed and Response (1–5 each) set a
  whole drive profile at once.
- **Stops:** release to center or pull back past 50% = **fast stop**
  (about twice the normal deceleration); power off while driving =
  **emergency stop**; park-brake stop is system-only.
- **System Lock** (if enabled): holding mode >5 s turns the chair off
  locked; to start it, on, then forward ≥3 s until beep, then reverse ≥3
  s until beep.
- **Mode Key Navigation** Simple (each press = next profile) or Advanced
  (short = next drive profile, long = drive ↔ seat/aux). Must be Simple
  if a Smart Switch (short = mode, long = off) is used.
- Battery type parameter (U1, NF-22, Group 24, Group 34) sets the
  battery gauge; set it right after a battery change.
- Hand control "traffic light": green = drive OK, amber = limited
  (quarter speed), red = drive inhibited (usually seat tilted past the
  threshold, [[Q-Logic-Seat-Configuration]]).
- Firmware updates and module compatibility: [[Q-Logic-Firmware-Updates]].

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
Rehab Provider. **Full 1–245 list:** [[Q-Logic-Fault-Codes]]. See also [[Q6 Edge Basic Troubleshooting]] for a broader
symptom-based checklist (dead system, reduced range, slow operation,
pulling, clicking) that's a natural companion to this error-code table.

## Q-Logic 3 (current)

Sources: [[Q-Logic 3 Basic Operation Instructions]] (end-user) and
[[Q-Logic 3 Programming Guide]] (provider/ATP-level).

Touchscreen-based successor to Q-Logic. End-user operation (Home screen,
Settings, drive-profile selection, actuator/seat screen, Standby Select) is
conceptually the same as legacy Q-Logic but presented on a touch interface
rather than a keypad+LCD.

### Q-Logic 3 error codes

From [[Q-Logic 3 Basic Operation Instructions]] (pp. 24–25). Messages are
Information, Warning or Error, shown by number.

| # | Meaning | Fix |
|---|---|---|
| 1 / 2 | Motor 1 / 2 not connected | Power off, inspect motor connections, power on |
| 3 / 4 | Brake 1 / 2 not connected | Power off, disengage then re-engage the brake lever, inspect motor connections |
| 20 | Undervoltage | Charge |
| 21 | Overvoltage | Check battery voltage; avoid fast downhill driving on full batteries |
| 23 / 24 | Motor 1 / 2 output defect | Power off, inspect motor connections |
| 25 / 26 | Brake 1 / 2 error | As 3 / 4 |
| 32 | Speed reduction (overtemperature) | Let it cool (normal behavior) |
| 34 / 35 | Joystick not centered / out of center | Release joystick, power-cycle |
| 46 | Bluetooth not working | Power off, wait 5 s, power on |
| 47 | Suspension lock not engaged | Level ground; check the lock |
| 75 | Chair is not charging (charger in the controller but not the wall) | Unplug the charger from the controller, power-cycle |
| 174 | Invalid memory position | Bring out of anterior tilt and retry; reset the memory position |

Full list (about 1–221, including TRU-Balance 4 actuator codes 150–177;
note the 32–36 numbering conflict): [[Q-Logic-Fault-Codes]].

**Don't mix the two tables:** legacy Q-Logic #75 is "motor disconnected"
and #35 a joystick connection fault; on Q-Logic 3 they mean "not
charging" and "joystick out of center". Symptom-first steps:
[[Power-Chair-Troubleshooting]].

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

Bluetooth programming apps (Econ-W, Econ-I), **Interactive Assist**
remote diagnostics, phone/tablet mouse and Switch Control pairing, and
the GyroSet Vigo head control:
[[Q-Logic-3-Bluetooth-and-Remote-Programming]]. **Q-Logic 3e** (on the
J4E/J4EHD) turns Bluetooth on from the Settings screen instead of Aux.

## QLNES (2024)

Source: [[QLNES Basic Operation Instructions (INFMANU5366)]]. The 75 A
or 90 A electronics on most 2025 Quantum mid-wheel chairs. **No
screen**: a 6-key or 10-key LED joystick with Key I/II, plus/minus
profile keys, mode and on/off jacks, a **USB-C** device-charging port
(5 V 3 A) and both an **XLR and a magnetic charger port** (never two
chargers at once; keep the magnetic connector 6 in from implanted
devices).

- 6-segment battery gauge (green ≥51%, yellow 16–50%, red below);
  charge at yellow.
- Drive mode number colour: yellow = restricted, red = drive lockout,
  green blinking = iLevel active, orange blinking = suspension lock not
  engaged while elevated; all four orange = rescue drive.
- Error codes blink as three digits on three LEDs
  ([[Q-Logic-Fault-Codes]]). Thermal rollback to 20%.
- Bluetooth: hold on/off 3 s to pair a programmer, accept with a
  forward input; also supports Interactive Assist.
- Lock is off from the factory; once enabled, unlock with full forward
  then full reverse.

## NE / NE+

Older Pride electronics on the **Power Base 75** with J, AJ and LJ hand
controls, AM1/AM2/LAM2 actuator modules. Faults show as **icons**. Still
on the 2025 chart for the [[J6]] (70 A) and [[Q6-Edge-HD]] (75 A);
NE+ also on the [[R-Trak]]; originally on the [[Q6-Edge]].

No NE/NE+ operation manual is on file, but the dealer troubleshooting
guides for the original Q6 Edge
([[Q6 Edge Technical Troubleshooting Guide (INFMANU4109 Rev B, 2012)]])
and the J6 ([[J6 Technical Troubleshooting Guide (INFMANU4132)]]) cover
the parts a tech needs:

- **LCD** (NE and NE+): charging and lights indicators steady when
  active, **flashing to show where a problem is**; error/warning
  indicators; lockout key icon; actuator and controller error
  indicators; attendant control. Message list:
  [[Power-Chair-Troubleshooting]] §7.
- **Reading faults:** a **Curtis handheld programmer**, Diagnostics →
  Actual Faults (happening now) or Fault History (earlier).
- **System Lock** must be enabled in programming to lock out. Lock: NE
  hold the power button until it shuts off; NE+ hold **both profile
  keys**. Unlock: power on, full forward to a beep, full back to a beep.
- **Charger inhibit programming:** NE inhibit input i2 `chrgInb` = **ON**;
  NE+ (and Q-Logic) Inhibit = **High** (Program Adjustments → System
  Settings → Miscellaneous on 2012-and-later menus).
- **Save System Configuration** after removing a module on purpose, or
  the chair reports it missing.

**Lock on NE+ differs by guide:** the Q6 Edge and J6 guides and
Pride's locking sheet say hold **both profile keys**; the **Quantum
614** guide says press the **Mode switch** until it powers off
([[Quantum-614]]). Try both. The Quantum 614 NE+ also shows
indicator, hazard and running-light errors.

Firmware: [[NE+ Firmware Compatibility List (2009)]]. Symptom checklist:
[[Q6 Edge Basic Troubleshooting]].

## Hardware fixes

- **Q-Logic 3e keypad**: pry off, clean adhesive with isopropyl, peel
  and press the new one fully flush.
- **Q-Logic dial and toggle**: pry off; line up the flats; check the
  toggle's spring is in place.
  ([[Q-Logic 3e Keypad and Q-Logic Dial-Toggle Replacement]])
- Error code booklet for legacy Q-Logic (same codes as the 2011 list):
  [[Q-Logic Error Code Reference Guide (INFINFB2653)]].

## See also

- [[Pride-Power-Chair-Lineup]], [[Pride-Controller-Flash-Codes]],
  [[Q-Logic-Fault-Codes]], [[Q-Logic-Firmware-Updates]],
  [[Q-Logic-Seat-Configuration]],
  [[Q-Logic-3-Bluetooth-and-Remote-Programming]]
- [[Power-Chair-Troubleshooting]] (symptom-first, Pride + Golden)
- [[iLevel]] (Q-Logic 3 and QLNES iLevel indicators, #47), [[Freewheel-Mode]]
- [[Tru-Balance-3-Power-Positioning]] (Q-Logic 3 inhibit-matrix integration
  with iLevel/tilt)
- Golden's controller-adjacent pages, for cross-manufacturer contrast:
  [[LiNX-Diagnostics]], [[Flash-Beep-Diagnostics]],
  [[Golden-Joystick-Side-Conversion]]
