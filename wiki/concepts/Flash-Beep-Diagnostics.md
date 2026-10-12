---
type: concept
tags: [diagnostics, golden, electrical, companion, literider, buzzaround]
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
- [[GB1xx-Buzzaround-XL]]: **GB116/GB146** ([[Buzzaround XL Service Guide (GB116, GB146)]])
  and **GB117/GB147** ([[Buzzaround XL Service Guide (GB117, GB147)]],
  [[Buzzaround XL Owners Manual (GB117, GB147)]]). **Not the GB106**,
  which uses an S-Drive ([[S-Drive-Beep-Codes]]).
- [[GB118-148-Buzzaround-EX]]: [[Buzzaround Extreme Service Guide (GB118, GB148)]]
- [[GB120-Buzzaround-CarryOn]]: [[Buzzaround Carry On Service Guide (GB120)]]
- [[GL109-LiteRider-Mini]]: [[LiteRider Mini Service Guide (GL109)]]

Distinct from the [[TruCharge-Diagnostics]] 10-bar display confirmed on
the GA541 Avenger and the GP162 PTC/VR2 wheelchair variant (PG
"S-Drive"/VR2 controllers), from [[LiNX-Diagnostics]] (7-code, GP162's
LiNX-controller variant), from [[S-Drive-Beep-Codes]] (GB106, Patriot,
Eagle) and from [[Shark-Diagnostics]] (11-code). Golden uses at least five diagnostic schemes
across its scooter and power-wheelchair lines — the controller family is
what determines which scheme applies, not the model name or product
category, so check for a Dynamics R-Series controller before assuming
this table applies to an un-ingested model.

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
mat (under the battery box on the Buzzaround XL) for field reference.

**Test values from the scooter service guides** (useful with codes 5 and
8): GB117/147, GB118/148 and GB120 motors read **0.8–1.5 Ω** and brakes
**45–52 Ω**. The 2011 GB116/146 guide gives looser limits: motor under
50 Ω (can be as low as 0.2 Ω), brake under 80 Ω.

## See also

[[GC240-340-440-540-Companion]], [[GL110-140-LiteRider]],
[[GL111-141-LiteRider]], [[GB1xx-Buzzaround-XL]], [[GB118-148-Buzzaround-EX]],
[[GB120-Buzzaround-CarryOn]], [[GL109-LiteRider-Mini]], [[TruCharge-Diagnostics]],
[[S-Drive-Beep-Codes]], [[Golden]]
