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

## GP162 PTC (PG VR2, dual-motor wheelchair)

Same 10-bar architecture, but codes 2-5 and 9 split into left/right motor
pairs to match the wheelchair's independent drive motors:

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

## See also

[[GA541-Avenger]], [[GP162-LiteRider-Envy]], [[LiNX-Diagnostics]],
[[Flash-Beep-Diagnostics]], [[Golden]]
