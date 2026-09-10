---
type: concept
tags: [diagnostics, golden, electrical, companion, literider]
---

# Flash/Beep Code Diagnostics (Dynamics R-Series Controller)

A 9-code flash/beep diagnostic scheme tied to Golden's **Dynamics
R-Series controller**, not to any single model line. Confirmed identical
(same 9 codes, same order, same meanings) across every model documented
with that controller so far:

- [[GC240-340-440-540-Companion]] — [[Companion Owners Manual (VA Contract Variant)]],
  [[Companion Service Guide (GC240, GC340, GC440)]]
- [[GL110-140-LiteRider]] — [[LiteRider Service Guide (GL110, GL140)]]
  (calls out the same controller by name and gives the fullest
  troubleshooting detail behind each code, including voltmeter/ohmmeter
  test points)
- [[GL111-141-LiteRider]] — [[LiteRider Owners Manual (GL111, GL141)]] and
  [[LiteRider Illustrated Parts Breakdown (GL111, GL141)]] (the IPB
  explicitly names the controller part, 3051600170, as shared between
  Companion GC240/340/440 and LiteRider GL111/141 — direct textual
  evidence, not inferred)

Distinct from the [[TruCharge-Diagnostics]] 10-bar display confirmed on
the GA541 Avenger, which uses a different controller (PG "S-Drive").
Golden uses more than one diagnostic scheme across its scooter line — the
controller family is what determines which scheme applies, not the model
name, so check for a Dynamics R-Series controller before assuming this
table applies to an un-ingested model.

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

[[GC240-340-440-540-Companion]], [[GL110-140-LiteRider]],
[[GL111-141-LiteRider]], [[TruCharge-Diagnostics]], [[Golden]]
