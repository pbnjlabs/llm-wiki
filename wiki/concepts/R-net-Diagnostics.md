---
type: concept
tags: [diagnostics, r-net, pg-drives, permobil, trip-codes, led-codes, power-chair, controller]
---

# R-net Diagnostics

How to read and clear faults on **PG Drives Technology R-net** control
systems, used on every Permobil power chair on file (M and F Corpus, M400,
M300 R-net, K/C300 R-net, K450, Koala). Main source:
[[R-net Technical Manual (SK77981-6)]] (PGDT, 2009); the Permobil chair
manuals agree with it. Other PGDT systems (VR2, S-Drive, VSI) are on
[[PG-Drives-Trip-Codes]].

**Rules:** R-net modules have **no serviceable parts**; a bad PM, JSM or
ISM goes back to Permobil or a PGDT-approved centre. Most "bad
controllers" sent back turn out fine, so check **connectors, batteries,
motors, brakes and wiring first**. Left/right motor references swap if
**Motor Swap** is programmed.

## 1. Read the fault

**LCD joystick (or a DTT):** the diagnostic screen shows the **module**
(PM power module, JSM joystick module, ISM seating/lighting module), the
**trip text** and a **4-digit trip code**. Write all three down. A fault
in a module that isn't in use lets the chair drive but the screen keeps
popping up.

**LED joystick (JSM-LED):** count the rapidly flashing battery-gauge LEDs:

| LEDs | Meaning | Check |
|---|---|---|
| 1 | Low battery or bad battery connection | Battery connections, charge |
| 2 | Left motor bad connection | Left motor plug |
| 3 | Left motor short to a battery connection | Service |
| 4 | Right motor bad connection | Right motor plug |
| 5 | Right motor short to a battery connection | Service |
| 6 | Drive inhibited by an external signal (on Permobil manuals: **charger connected**) | Unplug the charger; check inhibits |
| 7 | Joystick fault | Center the joystick before power-up |
| 8 | Possible control system fault | All connections |
| 9 | Parking brake bad connection | Brake and motor connections |
| 10 | Excessive voltage | Usually a poor battery connection |
| 7 + speed LEDs (Permobil: 7 + 5) | Communication fault | Joystick cable |
| Actuator LED | Actuator trip | Find which actuator; check its wiring |

Other LED states: gauge **steady** = OK; **slow flash** = charge soon;
**steps up** = charging (no drive until the charger is out and power is
cycled); **speed LEDs ripple outward** = new module found, reconfiguring;
**LEDs 2 and 4 flash** = reboot needed; **speed LEDs ripple left to
right** = chair is **locked**.

## 2. Trip texts and codes

| Trip text | Code(s) | Meaning / action |
|---|---|---|
| Center Joystick / Joystick Error | – | Joystick off center at power-up (5 s grace). Re-center; if it persists, joystick or JSM |
| Low Battery | 2C00 | Below **16 V**: batteries and connections |
| High Battery | – | Above **35 V**: overcharging or bad battery connection |
| M1 / M2 Brake Error | 1505 / 1506 | Solenoid brake, cable, connection |
| M1 / M2 Motor Error | 3B00 / 3C00 | Motor disconnected: motor, cable, connection |
| Inhibit Active | 1E01 (inhibit 1 = **off-board charger**), 1E20–1E23 (inhibits 2–5) | Cycle power (clears latched mode); check inhibit wiring and switches |
| Jstick Cal Error | – | Recalibrate in OBP |
| Brake Lamp / Lamp Short | 7205 left, 7209 right | Lamps, cables (ISM) |
| Indicator Lamp Short | 7206 left, 720A right | Indicators, cables |
| Indicator Lamp Failed | 7207 left, 7208 right | Usually a bulb |
| Over-current | – | Actuator channel: obstruction, end-stop switch, motor |
| Overtemp (acts / lamps) | – | SM/ISM too hot: let it cool, check actuators or bulbs |
| DIME Error | – | Two modules with conflicting IDs: unplug the new module, or one at a time |
| Memory Error | – | Check cables; unplug third-party modules one at a time |
| PM Memory Error | – | Re-program the PM with the chair's program file |
| Bad Cable | – | Communication cable: continuity, unplug one at a time |
| Bad Settings | – | Re-program; reset to defaults and re-add settings in groups |
| Module Error / System Error | – | Cables, power cycle; then the named module |
| SID Detached / Switch Detached | – | Omni input device or user switch unplugged (check 9-Way Detect / Switch Detect) |
| Gone to Sleep / Charging | – | Log entries only (sleep timer; charger on inhibit 1 or 3) |
| M1 / M2 Sensor Error, EM disconnected | 2001 / (3C00) / 7B01 | Encoder module |

The manual prints **3C00 for both M2 Motor Error and M2 Sensor Error**
(a misprint for one of them): treat 3C00 as the M2 motor first.

**System log:** OBP → System → Diagnostics (or DTT, PC Programmer) lists
every trip per module with counts, resolved or not.

## 3. Procedure

1. Note the module, trip text and code. 2. Power off. 3. Reseat every
connector on that module and the chair. 4. Check the batteries. 5. Act on
the trip text above. 6. Power on and try to drive; **if it trips again,
stop and don't use the chair.**

## 4. Lock, unlock and programming access

- **Keypad lock:** chair on, hold On/Off about 1 s to the beep, release;
  joystick **forward** to a beep, **back** to a beep, release (long
  beep). **Unlock:** press On/Off, then the same forward/back sequence.
- **Key lock:** insert and remove the PGDT key in the JSM charger socket.
- **OBP (on-board programming):** dongle in the bus then Mode to the OBP
  screen, or keycode: hold **Horn**, then **On/Off** to a short bleep,
  release Horn, keep On/Off for two more bleeps, release (long bleep).
  **Not possible on an LED JSM**; which method works is set at the factory.

## 5. After any repair: basic tests

General inspection (connectors, cables, joystick gaiter, mounting; don't
overtighten), **brake test** (each brake heard within **2 s** in four
directions), drive test at min and max speed, **gradient test** (stops on
the slope with the front wheels down; have a helper), lights (indicators
**1.5 Hz**, one bulb out = **3 Hz**), actuators (direction, end-stops stall
the motor), **inhibit test** (charger in = no drive).

## Seating (ICS) faults

Permobil seat faults show on the **ICS switchbox** (brief red flash =
binding or sensor; constant red flash = actuator not talking; all red =
layout error; yellow/red elevator icon + **M8** on the JSM = SoftPot error
mode, half speed). Error IDs: [[Permobil ICS Error Codes and Quick Reference]].
Calibration and the 6 + 8 "Take Me Down" emergency mode:
[[ICS Onboard Configuration Technical Manual (205247, Ed 8)]].

## Sources

[[R-net Technical Manual (SK77981-6)]], [[R-net LED Error Codes]],
[[Permobil M400 Corpus HD User Manual (337723)]],
[[Permobil M300 Owner's Manual (205255)]],
[[ICS Onboard Configuration Technical Manual (205247, Ed 8)]].
See also [[Troubleshooting]], [[Joystick-Controllers]].
