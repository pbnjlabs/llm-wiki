---
type: concept
tags: [pride, quantum, q-logic, q-logic-3, qlnes, fault-codes, error-codes, diagnostics, controller]
---

# Q-Logic Fault Codes (full lists)

The complete numbered fault lists for Pride/Quantum's **Q-Logic family**,
for when the short tables on [[Joystick-Controllers]] and
[[Power-Chair-Troubleshooting]] don't have the number. Three systems,
**three different numbering schemes**:

| System | Where the number shows | Source |
|---|---|---|
| **Legacy Q-Logic** (2008-era, colour LCD hand control or Enhanced Display) | Pop-up on the LCD; SAJ-only chairs show LED patterns and need a programmer for the number | [[Q-Logic Technical Manual (INFMANU3580)]] (2008), [[Q-Logic Fault Codes (2011)]] |
| **Q-Logic 3 / 3e** (touchscreen-style display) | Number and text on the display | [[Q-Logic 3 Fault List (2025)]], [[Q-Logic 3 Basic Operation Instructions]] |
| **QLNES** (2024, LED hand control, no screen) | Three LEDs blink the digits (below) | [[QLNES Basic Operation Instructions (INFMANU5366)]] |

**The same number means different things on legacy Q-Logic and Q-Logic
3.** Examples: #35 (legacy joystick center fault / QL3 joystick out of
center), #47 (legacy low battery / QL3 suspension lock), #75 (legacy
right motor disconnected / QL3 not charging), #20–26 (legacy software
and bus faults / QL3 voltage, motor and brake). **Identify the
controller first.** QLNES uses the Q-Logic 3 numbers (see the 32–36
conflict below).

First step for any code: **power off and on**. It clears transient
faults and tells you whether it's real. Persisting → Quantum Rehab
Technical Support **866-800-2002**.

## How each system reports

**Legacy Q-Logic** (tech manual p. 100): three levels.
- **Warning:** 2 s pop-up, repeats once a minute; horn double-beeps once
  a minute. E.g. #105 Low Battery Voltage, #110 High Pedal Warning.
- **Recoverable fault:** pop-up stays until fixed; horn beeps twice a
  second. If #110 isn't cleared within 5 s it becomes **#36 Joystick
  Not Centered**, which needs a power cycle.
- **Serious error:** dealer needed; horn twice a second.
- **SAJ without an Enhanced Display:** slow LED blinks (2/s) =
  warning, fast (4/s) = fault, **red Battery and Mode LEDs both fast** =
  unrecoverable, call service. A programmer gives the number.

**Q-Logic 3:** Information, Warning or Error, shown by number and text.
Providers read the **error history** with Econ-W, the HHP or remotely
with Interactive Assist ([[Q-Logic-3-Bluetooth-and-Remote-Programming]]).

**QLNES:** no screen. **Red LED blinks the hundreds digit, yellow the
tens, green the ones**, each blink 0.5 s on/off; a zero digit doesn't
blink. Example: #208 = red ×2, (no yellow), green ×8. Only one fault
shows at a time; fix it and **power-cycle** to see the next. Warnings
that aren't on the display list give an error beep and flash the two
yellow LEDs for 4 s (repeats each minute while active).

## Legacy Q-Logic (1–245)

From the 2008 tech manual and the 2011 list; codes not listed are
unused. "OEM parameter" = only Pride can change it.

| Code(s) | Fault | Cause → action |
|---|---|---|
| 1–17, 26–34, 41–43 | SW fault | Software error → update software |
| 19, 24, 40, 121, 125–127 | Communication / output-definition faults | Bus comms failed or another module failed → check bus cables, check for a fatal error on another module, replace module or update software |
| 20, 136, 157, 234 | Incompatible module / wrong protocol | Remove the module or update software |
| 21 | CMM pool empty | Module out of resources → remove modules |
| 22 | A/D conversion timeout | Replace module (check error history) |
| 23, 109, 117, 129, 139 | Bus faults (more than one power flip-flop, CAN timeout, CAN bus off) | Bus cable unplugged while driving or defective → check bus cables; unplug modules one at a time until it clears |
| 35, 37, 39 | Joystick center / connection / signal fault | Joystick disconnected or bad → check connection, replace joystick, replace module |
| 36 | Joystick not centered | Out of center >5 s after power-up → release, power-cycle |
| 38 | Joystick out of range | Limiter plate changed/bad or badly calibrated → **calibrate joystick**, replace |
| 44 / 45 | Limit sense pots open / shorted | Seat position feedback wiring → check connector, wiring, feedback devices |
| 46 | High battery voltage | Disconnect charger |
| 47 | Low battery voltage | Charge |
| 48 | Temperature out of range | Let it cool 15 min |
| 49–53, 177 | Motor 1–6 not connected (resistance too high) | Check motor/brake connector, wiring, motor resistance; replace motor |
| 54 | Motor overcurrent | Stalled or shorted actuator/motor → check wiring, resistance |
| 55 | Motor timeout | Ran one way past the limit (OEM parameter) |
| 56 | Sensor reference fault | Pressure sensor (Sip & Puff) → replace |
| 57 | Buffer empty/overflow | Update software |
| 58–59 | EEPROM CRC (profile, calibration) | Replace module |
| 60–64 | EEPROM CRC / parameter disturbed | **Re-download the parameter file with the PCPS, Advanced Cloning on** |
| 65 | Inactive input device not centered | Release it; check bus cables |
| 69 | Bus overload (B+ fuse tripped) | Check bus cables; unplug modules one at a time |
| 70 | ROM CRC | Update software (Inhibit Application Start) or replace module |
| 73 | Precharge fault | Replace power base |
| 74 / 75 | Left / right motor disconnected | Check motor/brake connector, wiring, resistance; replace motor |
| 80 / 138 | Main relay not open (welded; or charger connected / low battery at start-up) | Disconnect charger, charge, else replace power base |
| 81 / 82 | Left / right motor shorted | Check connector, wiring, resistance |
| 83 / 84 | Left / right brake disconnected | Connector, brake wiring, brake resistance; brake voltage (OEM) too low |
| 85 / 86 | Left / right brake overload | Brake wiring shorted or brake bad → replace |
| 87 / 88 | Left / right brake not released | Brake open/bad, **battery low**, or brake voltage too low → charge, check, replace brake |
| 89 / 90 | Left / right brake voltage too high | Connector, wiring; replace brake |
| 94, 96, 97, 140, 142, 143, 196–199, 219, 230 | Power module internal faults (relay, current sense, offsets, power-down, reference voltage, charge pump) | Replace power module/power base (142/143: if it repeats) |
| 98 / 102 | Heatsink too hot | High load → cool 15 min, check output currents |
| 99 | High motor temperature | Cool 15 min |
| 100 / 104 | Battery overvoltage | **Downhill on full batteries** → slow down |
| 101 / 105 | Battery undervoltage | Charge |
| 107 | Charger/drive inhibit (low DMS line) | **Charger plugged in**, or an inhibiting module/bus cable → disconnect charger, check modules |
| 110, 134 | High pedal (input not zero at power-up) | Release, power-cycle |
| 111 / 112 | Center detect fault | Joystick cable/joystick |
| 122 | Overtake abort | Replace the module named in error history |
| 123 / 124 | Duplicate output / input definition | Remove duplicate modules |
| 128 | Motor control loop unstable | Wrong motor parameters → re-clone with Advanced Cloning; motor impedance (OEM); replace motor |
| 130 | SDO client error | Remove modules; call Quantum |
| 131 / 132, 200 / 201 | Motor output fault (wrong output voltage) | Motor wiring, motor, power module |
| 133 | EEPROM BDI CRC | BDI resets to 100%; update software |
| 135 | Direction assignment error | Two commands on one direction → reassign |
| 137 | Invalid device type/serial | Incompatible or failed module |
| 141 | Drive restricted | Clear the restriction (seat position etc.) |
| 144 / 145 | Puff / sip parameters overlap | 4-pressure setup → adjust |
| 149–151 | Open wire: left/right indicator, lights | Bulb or wiring |
| 155, 164 | Config section CRC / invalid configuration | Set config with the PCPS (OEM) |
| 156, 163, 166 | Unexpected interrupt / initial tests / distance CRC | Replace power base if it repeats (166 resets trip counters) |
| 160 / 161 | Set recline vertical / standup down first | Move it there |
| 167 | Brake switch opened during idle | Close brake switch, check wiring |
| 174–176 | IR memory full / learning failed | Delete unused data; reposition remote |
| 178, 180, 220 | EEPROM CRC (encoder, motion, generic) | Power-cycle |
| 179, 186 | Encoder counts / signals missing | Servo blocked; check feedback, **re-home** the seat |
| 181 | Speed pot out of range | Replace hand control |
| 192–195, 203, 204, 208, 209, 235, 236 | Motor/brake 1–2 disconnected, shorted, overload | As 74–90 |
| 205 / 206 | Brake driver / oscillator | Replace power base / AAM |
| 207 | On/off switch disconnected | Reconnect |
| 210 / 211 | Poti CRC / out of range | Recalibrate |
| 217 / 218 / 238 | Actuator overcurrent / timeout / driver overtemp | Wiring, release command, cool 15 min |
| 221 | Mode switch disconnected | Reconnect, or turn off Mode Jack Supervision |
| 222–229 | Hand control / SAJ / attendant / AAM / Enhanced Display / Sip & Puff / ECU / module missing | Reconnect or replace; **run Save System Configuration** if a module was removed on purpose |
| 231 | Input device not active | Off center → release; check cable |
| 237 | Incompatible start manager | Update the start manager |
| 239 | D-Sub-9 switch disconnected | Reconnect or turn off D-Sub-9 Supervision |
| 240 | MIO definition overflow | Reduce Mapped IO definitions |
| 241 | New firmware uploaded | Power-cycle |
| 242 / 243 | Motor stall / power reduction | Clear obstruction, let motors cool |
| 244 | Same device number | Renumber modules of the same type |
| 245 | All profiles disabled | Enable at least one profile |

## Q-Logic 3 (1–221)

From the 2025 list. Most actions start "turn power off" and end "turn
power on". QLNES uses the same numbers for 1–4, 20–26, 46 and 47.

> **Conflict, codes 32–36.** The 2025 list has 32 = overtemperature
> (chair stopped), 33 = speed reduction (overtemperature), 34 = bus
> voltage dropped, 35 = joystick not centered, 36 = joystick out of
> center. The [[Q-Logic 3 Basic Operation Instructions]] and the 2024
> [[QLNES Basic Operation Instructions (INFMANU5366)|QLNES BOI]] both
> put **speed reduction at 32** and the **joystick at 34/35**. It may
> differ by firmware. **Go by the text on the display** (or the error
> history), not the number alone.

| Code(s) | Fault | Action |
|---|---|---|
| 1 / 2 | Motor 1 / 2 not connected | Inspect motor connections |
| 3 / 4, 25 / 26 | Brake 1 / 2 not connected / error | **Disengage and re-engage the brake lever**, inspect motor connections |
| 5–8 | On/off jack disconnected (attendant, Enhanced Display, hand control, secondary adaptive joystick) | Unplug and replug the on/off jack switch |
| 9–12 | Mode jack disconnected (same four devices) | Unplug and replug the mode jack switches |
| 13 | D-Sub (9-pin) disconnected | Reseat the D-sub |
| 14 | Proportional input device not connected | Select the right input device in programming, or reseat the D-sub |
| 15 / 19 | Drive motor encoder not connected / shorted | Disconnect both encoder cables, inspect, reconnect |
| 16 / 17 | Brake 1 / 2 shorted **or programmed incorrectly** | Check the **brake voltage setting** with a programmer, then as 3/4 |
| 18, 56, 58 | Actuator shorted / overcurrent / H-bridge | Disconnect and reconnect seat module cables one at a time; 58: change actuator module if it persists |
| 20 | Undervoltage | Charge |
| 21 / 22 | Overvoltage / speed reduction (overvoltage) | Batteries may be overcharged; avoid fast downhill driving on full batteries |
| 23 / 24 / 27 | Motor 1 / 2 output defect; motor output defect | Inspect motor connections/wiring |
| 28–30 | Main contactor error | Power off, wait 5 s, on |
| 31 | Motor stall | Back up and retry with more speed, or go around/find a lower spot |
| 32 / 33 | Overtemperature (stopped) / speed reduction | Let it cool. Normal behavior |
| 34 | Bus voltage dropped | Inspect and reseat the hand control / Enhanced Display cable |
| 35 / 36 | Joystick not centered / out of center | Release to neutral, power-cycle |
| 37 / 38 | Switched input pressed / not released at power-up | Release it |
| 39 | Incompatible device | Remove it |
| 40 | Encoder connected but not configured | Enable encoders, or disable and unplug both encoder cables |
| 41 | Input device not configured | Power off 5 s |
| 42 | Module with incompatible firmware | **Update to the latest firmware pack** with a programmer |
| 43 / 44 | Motor 1 / 2 current measurement out of range | Inspect motor connections |
| 45 | Selected input device not present | Pick a connected device in Startup Configuration |
| 46 | Bluetooth not working | Off, wait 5 s, on |
| 47 | Suspension lock not engaged | Level ground; check the suspension lock |
| 48 | Invalid 1-switch scanner sequence | Fix the scanner sequence |
| 49 | DMS fault (DMS line interruption) | Off 5 s, on |
| 50–52 | Device exchanged / added / removed | Reboot (off 5 s) |
| 53 / 54 | Sip N Puff not in neutral at power-up | Release it |
| 55 | Test/demo firmware installed | Informational |
| 57 | Severe overtemperature (seat) | Cool; change actuator module if it persists |
| 59–71 | ADC overrun, pressure sensor, non-active input, actuator relay, sip/puff parameter, actuator undervoltage, current-limit speed reduction, actuator timeout, IR not enabled, corrupt IR data | No action text in the list |
| 72 | Speed reduction (traction control) | Stop the chair to clear |
| 73 / 74 | Speed feedback timeout / intervention ramp | — |
| 75 | **Chair is not charging. Please check charger.** | (BOI: charger in the controller but not the wall → unplug from controller, power-cycle) |
| 78 | Safeguard brake not engaged | — |
| 80 | System in configuration mode | **Don't power off until it finishes** |
| 81 / 82 | Motor overcurrent M1 / M2 | — |
| 84 | Chair type / traction control combination not supported | Set them to a valid combination |
| 85 | Smart traction control offset (turn rate or temperature) | — |
| 86 | Power cycle required | Power-cycle |
| 141 | Advanced seat navigation not allowed with 1-switch scanner | — |
| 150–155 | **TRU-Balance 4 tilt**: feedback defect, out of tolerance, actuator / anterior tilt / cam lock defect, function error, home switch, anterior tilt switch | Recalibrate feedback; else change tilt actuator, cam lock or switch assembly (150: see the TRU-Balance 4 technical troubleshooting guide, not on file; actuator calibration and parts: [[Tru-Balance-4-Power-Positioning]]) |
| 156–158 | TRU-Balance 4 recline feedback / tolerance / switch | Recalibrate; change recline actuator |
| 159–162 | Elevate feedback / tolerance / switch / not moving | Check cable; recalibrate; change elevate actuator |
| 163–171 | AFP (articulating foot platform), AFP articulation and AFP elevation actuators: feedback, tolerance, switch defects | Check feedback cable; recalibrate; change that actuator assembly |
| 172 | Actuator feedback supply shorted | Check feedback wiring; change the damaged actuator |
| 174 | Memory position invalid | Bring out of anterior tilt and retry; reset the memory position |
| 177 | Actuator calibration data invalid | Recalibrate the system |
| 202–206, 208–211 | Emergency power down, pre-drive test, communication, memory, data, supervision, software errors | **Off, wait 5 s, on** |
| 207 | SD card access failed | Remove, inspect and reseat the SD card; format if it persists |
| 212 / 213 | Reset to defaults / parameter database restored | Reboot (and check the programming) |
| 214 / 215 | Database load error / not saved | Reboot |
| 220 | Firmware update hardware version check failed | — |
| 221 | Gyro/accelerometer (IMU) fault | — |

Not on file: the **TRU-Balance 4 technical troubleshooting guide**
(see the index's Missing manuals).

**Field note:** repeated "joystick out of center" that only shows up
over bumps, and survives a firmware update, can be a **bus cable routing
problem**, not the joystick ([[2026-10-16 Q6-Edge-HD cuts out then powers down on bumps]]). **Check the cable connections
first**, before a firmware update (10 min vs 1 h+, per the human).

## See also

[[Joystick-Controllers]], [[Power-Chair-Troubleshooting]],
[[Pride-Controller-Flash-Codes]] (VR2, GC3, newVSI, Dynamic),
[[Q-Logic-Firmware-Updates]], [[Q-Logic-Seat-Configuration]],
[[Tru-Balance-3-Power-Positioning]], [[Pride-Power-Chair-Lineup]],
[[Freewheel-Mode]] (brake codes 3/4, 25/26), [[iLevel]] (#47 suspension lock),
[[Q-Logic Error Code Reference Guide (INFINFB2653)]] (2011 booklet of the legacy codes)
