---
type: concept
tags: [diagnostics, golden, electrical]
---

# TruCharge Battery Display Diagnostics

Golden's "TruCharge" volt-meter/diagnostics gauge reports a 1-10 bar fault
code, tied to the PG "S-Drive"/VR2 controller family. Confirmed on the
[[GA541-Avenger]] operator manual (single-motor scooter architecture) and
on the [[LiteRider PTC Service Guide (GP162, PG VR2 Controller)]]
(PG VR2-controller variant of [[GP162-LiteRider-Envy]] — a power
wheelchair, so the architecture is adapted for independent left/right
drive motors instead of one scooter drive motor). **Not** the scheme used
on the Companion/LiteRider scooter line (Dynamics R-Series controller —
see [[Flash-Beep-Diagnostics]]) or on GP162's LiNX-controller variant (see
[[LiNX-Diagnostics]]). Golden uses more than one diagnostic scheme across
both its scooter and power-wheelchair ranges; check the controller, not
the model name or product category, before assuming a table applies.

**Programmer codes:** the 4-digit trip codes a PG programmer reads
(e.g. 2C00 low battery, 1500 brake) are on [[PG-Drives-Trip-Codes]],
from PG's own [[PG Drives Mobility Diagnostic Guide]]. Use them when the
bar count isn't enough.

## GA541 Avenger (single-motor scooter)

| Bars | Fault | Self-help |
|---|---|---|
| 1 | Reaching low voltage | Charge battery; check controller/battery connections |
| 2 | Motor disconnected | Bad connection between motor and controller |
| 3 | Motor wiring fault | Short circuit to a battery connection — contact service agent |
| 4 | Parking brake off | Freewheel switch or manual brake disengagement is active |
| 5 | (not used) | — |
| 6 | Inhibit active | Battery charger still connected, or seat not in proper driving position |
| 7 | Throttle potentiometer fault | Make sure throttle is at rest before power-on |
| 8 | Possible controller fault | Contact service agent |
| 9 | Solenoid brake fault | Bad connection between parking brake and controller |
| 10 | High battery voltage | Excessive voltage, usually a poor battery connection |

General rule: when the display drops to 2 bars, batteries must be charged
before further driving.

## PG VR2 power chairs (dual motor)

Same 10-bar architecture, but codes 2-5 and 9 split into left/right motor
pairs to match the wheelchair's independent drive motors. The same table
appears in all four VR2 service guides on file:
[[LiteRider PTC Service Guide (GP162, PG VR2 Controller)]] ([[GP162-LiteRider-Envy]]),
[[LiteRider PTC Service Guide (GP160)]] ([[GP160-LiteRider-PTC]]),
[[Alante DX and LT Service Guide (GP204, GP215)]] ([[GP204-Alante-DX]]) and
[[Alante Sport Service Guide (GP205)]] ([[GP205-Alante-Sport]]).
The guides name them "VR2 flash codes" (e.g. 3 = left motor wiring trip,
6 = charger connected, 9 = solenoid brake trip). On these chairs the
motors read **under 5 Ω**.

Owner's manuals added 2026-10-20 print the same 10-LED table, with the
VR2 lock/unlock sequence, for the [[GP161-LiteRider-Envy-Lite]] (PG
**nVR2**, 50 A), the **GP205/206/207 Alanté** series
([[Alante Series Owners Manual (GP205, GP206, GP207)]], 50 A) and the
[[GP208-Alante-Sport]] (40 A). The [[GP130-CarryOn-Power-Chair]] is also a **PG VR2** chair (per its 2025
IPB), but its owner's manual prints a shorter 9-entry table (no 6,
brake at 9), on its own page.

| Bar | Fault |
|---|---|
| 1 | Low battery voltage (bad connection) |
| 2 | Left motor bad connection |
| 3 | Left motor short circuit |
| 4 | Right motor bad connection |
| 5 | Right motor short circuit |
| 6 | Charger connected, or other external signal preventing drive |
| 7 | Joystick fault (must be centered at power-on) |
| 8 | Control system fault |
| 9 | Parking brake bad connection |
| 10 | High battery voltage |

## Pride scooters: TruCharge voltmeters

Pride's scooter voltmeter **DGN142447** (black PCB) only reads correctly
with a **TruCharge** program (S-Drive Status Output Type = 0; Dynamic
R-Series PIN 10 = Other): it shows ten bars then one at start-up, and
all ten lit with the blue LED flashing the beep code on a fault. Wrong
program = one red LED and the blue LED only. Non-TruCharge programs use
ELE1906793 (SLA) or ELE2008025 (lithium) instead
([[Pride TechnoBulletins (2006-2024)]], GENERAL-009CA).

## See also

[[GA541-Avenger]], [[GP162-LiteRider-Envy]], [[GP161-LiteRider-Envy-Lite]], [[GP160-LiteRider-PTC]],
[[GP204-Alante-DX]], [[GP205-Alante-Sport]], [[GP208-Alante-Sport]], [[LiNX-Diagnostics]],
[[Flash-Beep-Diagnostics]], [[S-Drive-Beep-Codes]], [[Freewheel-Mode]], [[Golden]]
