---
type: concept
tags: [diagnostics, golden, electrical]
---

# TruCharge Battery Display Diagnostics

Golden's "TruCharge" volt-meter/diagnostics gauge reports a 1-10 bar fault
code. Confirmed on the [[GA541-Avenger]] operator manual — not yet
verified whether other Golden models use the same TruCharge display or
fault-code table; check as more Golden models are ingested.

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

## See also

[[GA541-Avenger]], [[Golden]]
