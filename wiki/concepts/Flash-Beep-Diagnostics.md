---
type: concept
tags: [diagnostics, golden, electrical, companion]
---

# Flash/Beep Code Diagnostics (Companion)

A 9-code flash/beep diagnostic scheme, confirmed identical between the
[[Companion Owners Manual (VA Contract Variant)]] and the
[[Companion Service Guide (GC240, GC340, GC440)]]. Distinct from the
[[TruCharge-Diagnostics]] 10-bar display confirmed on the GA541 Avenger —
Golden uses more than one diagnostic scheme across its scooter line;
don't assume either applies outside the models it's confirmed on.

The Dynamics R-Series controller's power indicator LED flashes and the
horn beeps together, in a series separated by a 2-second pause. The count
of flashes/beeps is the code.

| Code | Meaning | Remedy |
|---|---|---|
| 1 | Battery voltage below 19V (throttle neutral) | Charge batteries; scooter still runs at reduced speed until 17.5V |
| 2 | Battery voltage at/below 17.5V | Scooter stops; charge, or load-test if charging doesn't clear it |
| 3 | High battery voltage (above 26VDC) | Let battery level drop, don't let charger overcharge; check charger is an approved type |
| 4 | Current limit timeout — motor control board overloaded/overheated | Power off, wait 10 min; check tire pressure; load-test battery |
| 5 | Brake fault | Check freewheel lever is engaged; check brake/wiring |
| 6 | Paddle fault — throttle not in neutral at power-on, or out of adjustment | Power cycle with throttle at rest; readjust if needed |
| 7 | Paddle/speed control fault (throttle pot or speed pot voltage error) | Check connectors firmly joined; else contact provider |
| 8 | Motor voltage fault (open circuit) | Contact provider |
| 9 | Controller fault (other internal error) | Contact provider |

The Service Guide provides a full voltmeter-based diagnostic tree behind
several of these codes (component-by-component test points, expected
readings) — see that source page for the detailed procedure.

Serial number and this code table are printed under the Companion's floor
mat for field reference.

## See also

[[GC240-340-440-540-Companion]], [[TruCharge-Diagnostics]], [[Golden]]
