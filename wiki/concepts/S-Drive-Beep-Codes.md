---
type: concept
tags: [diagnostics, golden, pg-drives, s-drive, scooter]
---

# S-Drive Beep Codes (Golden scooters)

The **beep/flash code** set used on Golden scooters with a **PG S-Drive**
controller. It is a 7-code subset: there are **no codes 1 or 4**.

Confirmed on:
- [[GB1xx-Buzzaround-XL]]: **GB106** Buzzaround Lite only
  ([[Buzzaround Lite Service Guide (GB106)]]). The other Buzzarounds use
  the Dynamics R-Series ([[Flash-Beep-Diagnostics]]).
- [[GR575-Patriot]] ([[GR575 Patriot Service Guide]]).
- [[GR595-Eagle]] ([[GR595 Eagle Owners Manual]]). The Eagle also shows
  the code as an **E-code** on its LCD.

The [[GA541-Avenger]] also uses an S-Drive, but its owner's manual gives
the code as a 10-bar [[TruCharge-Diagnostics]] reading. For any S-Drive,
a PG programmer gives the 4-digit codes on [[PG-Drives-Trip-Codes]].

The controller beeps (or flashes) the count, pauses about 2 seconds, and
repeats.

| Code | Meaning | Check |
|---|---|---|
| 2 | Low battery voltage | Charge. Check for loose or corroded terminals. Measure across the breaker-side terminals, then check breaker continuity. |
| 3 | High battery voltage | Usually a poor battery connection. May appear only **going downhill**, when regeneration pushes power back into the batteries. |
| 5 | Solenoid brake trip | Bad brake connection. Check the brake and motor connections. |
| 6 | Throttle trip (out of neutral) | Throttle not at neutral at switch-on. Release it and power-cycle. |
| 7 | Throttle trip / speed control fault (voltage error) | Throttle pot or speed pot. |
| 8 | Motor disconnected | Motor leads and connections. **Check the freewheel lever position.** |
| 9 | Possible controller trip | Make sure all connections are secure. Eagle: also check tire inflation (35 psi). |

Motor resistance on these service guides: **under 50 Ω, not shorted
(can be as low as 0.2 Ω)**.

## See also

[[Flash-Beep-Diagnostics]], [[TruCharge-Diagnostics]], [[PG-Drives-Trip-Codes]], [[Freewheel-Mode]], [[Golden]]
