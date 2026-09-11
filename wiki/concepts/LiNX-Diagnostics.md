---
type: concept
tags: [diagnostics, golden, electrical, linx]
---

# LiNX Controller Diagnostics

A 7-code flash-code scheme tied to Golden's **LiNX controller** — a third
distinct diagnostic vocabulary alongside [[TruCharge-Diagnostics]] (10-bar,
PG S-Drive/VR2 controllers) and [[Flash-Beep-Diagnostics]] (9-code,
Dynamics R-Series controller). Confirmed on the LiNX-controller variant of
[[GP162-LiteRider-Envy]] only so far — see
[[LiteRider Envy LiNX Supplemental Insert (GP162)]] and
[[LiteRider Envy LiNX Owners Manual (GP162)]] (identical table in both).
Reinforces that Golden's diagnostic scheme is determined by controller
choice, not model name or product category — check per-model before
assuming any of the three schemes applies.

The status indicator (under the power button) flashes red; the count of
flashes is the code.

| Code | Meaning | Remedy |
|---|---|---|
| 1 | Remote/joystick error | Check LiNX connections/wiring; replace LiNX Control Unit |
| 2 | Network or configuration error | Check LiNX connections/wiring; replace LiNX Control Unit |
| 3 | Left motor error | Check left motor, connections, cabling |
| 4 | Right motor error | Check right motor, connections, cabling |
| 5 | Left park brake error | Check left park brake, connections, cabling |
| 6 | Right park brake error | Check right park brake, connections, cabling |
| 7 | Module error (other than Remote) | Check LiNX connections/wiring; replace Power Module |

LiNX modules are explicitly **not user-serviceable** — the remedy for
codes 1, 2, and 7 is module replacement, not repair.

## Related but distinct: OONAPU and drive-inhibit

Two LiNX-specific behaviors that aren't fault codes but affect
troubleshooting a chair that "won't move":

- **OONAPU** ("Out Of Neutral At Power Up"): if the joystick isn't
  centered at power-on (or when clearing an inhibit), the battery gauge
  flashes and the chair won't drive. A 5-second grace period to center
  the joystick clears it as a warning; past 5 seconds it escalates to an
  error (status indicator flashes red) requiring a full power cycle with
  the joystick at rest.
- **Drive inhibit**: indicated by a right-to-left chasing light sequence
  across the 5-LED battery gauge (distinct from the gauge's normal
  charge-level display) — repeats until the inhibiting condition clears.

## See also

[[GP162-LiteRider-Envy]], [[TruCharge-Diagnostics]],
[[Flash-Beep-Diagnostics]], [[Golden]]
