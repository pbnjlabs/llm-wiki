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
- [[GR575-Patriot]] ([[GR575 Patriot Service Guide]] and the 2020
  [[GR575 Patriot Owners Manual]]: fast beeps for 2 s, then the code
  once; 8 says check the freewheel switch, 9 says check tire inflation).
- [[GR595-Eagle]] ([[GR595 Eagle Owners Manual]]). The Eagle also shows
  the code as an **E-code** on its LCD.
- [[GR596-Eagle-All-Terrain]] ([[GR596 Eagle All Terrain Owners Manual]],
  2025): **E2–E9 on the display, with beeps**, same meanings. Its 200 A
  controller's maker isn't named, so it may not be an S-Drive. It adds
  **E1 = sleep mode** (15 min idle with the key on; key off and on).
  E9 can also come from low batteries.

**Pride scooters on S-Drive:** the Go-Go **Elite Traveller** (45 A)
and the **Victory 9/10** use it too; their dealer guides give the same
codes 3, 5, 6, 7, 8, 9 with meter values (brake **30–65 Ω**, motor
0.5–1.5 Ω, beep 3 above 32 V). The Elite Traveller plays ten fast
beeps first, then the count, once
([[Elite Traveller Technical Troubleshooting Guide (INFMANU3206)]],
[[Victory 9-10 Technical Troubleshooting Guide (INFMANU3986)]]).

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

## Pride scooter owner's manuals: the full 1–9 list

Pride's 2025–2026 scooter owner's manuals
([[Mid-Size Scooter Series Owners Manual (INFMANU4468)]],
[[Travel Scooter Series Owners Manual (INFMANU4392)]],
[[Pride Travel Scooter Series Owners Manual (INFMANU4916)]]) give nine
codes, filling in the 1 and 4 that Golden's guides leave out:

| Beeps | Pride owner's manual |
|---|---|
| 1 | Battery too low to run the scooter: charge now |
| 2 | Battery charge low: charge |
| 3 | Voltage too high, or the charger is still plugged in: unplug, key off and on; slow down on hills |
| 4 | **Current limit time-out** |
| 5 | **Manual freewheel lever in freewheel**: key out, lever back to drive, restart |
| 6 | Throttle not centered at start-up: charge check, center it, key off and on |
| 7 | Speed pot error: provider |
| 8 | Motor volts error: provider |
| 9 | Other internal error: off a few minutes, then provider |

Codes either play once (fast beeps then the count; reinsert the key to
hear it again) or repeat until the key is off, depending on the model.
The scooter won't run until the condition is cleared and the key
cycled. Note Pride's 5 is the freewheel lever while the Golden service
guides call 5 a brake trip; on Pride a brake/motor fault shows as 8.

## See also

[[Flash-Beep-Diagnostics]], [[TruCharge-Diagnostics]], [[PG-Drives-Trip-Codes]], [[Freewheel-Mode]], [[Golden]]
