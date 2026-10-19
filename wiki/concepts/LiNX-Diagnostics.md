---
type: concept
tags: [diagnostics, golden, electrical, linx]
---

# LiNX Controller Diagnostics

A 7-code flash-code scheme tied to the **LiNX controller** (Dynamic
Controls). It is one of six Golden diagnostic schemes, alongside
[[TruCharge-Diagnostics]] (PG S-Drive/VR2), [[Flash-Beep-Diagnostics]]
(Dynamics R-Series), [[S-Drive-Beep-Codes]], [[Shark-Diagnostics]] and the
Cricket's Micon table ([[GP302-Cricket]]). Confirmed on the LiNX-controller variant of
[[GP162-LiteRider-Envy]] — see
[[LiteRider Envy LiNX Supplemental Insert (GP162)]] and
[[LiteRider Envy LiNX Owners Manual (GP162)]] (identical table in both) —
and on the **GP605 Compass Sport** in the 2017
[[Compass Sport Service Guide (GP605, LiNX)]], which gives the full
test procedure behind each code ([[GP6xx-Compass]]). The **GP302B**
Cricket also has a LiNX controller ([[Cricket Illustrated Parts Breakdown (GP302)]]);
its own codes aren't documented, so this table is the best guide.
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

[[GP162-LiteRider-Envy]], [[GP6xx-Compass]], [[GP302-Cricket]], [[TruCharge-Diagnostics]],
[[Flash-Beep-Diagnostics]], [[Shark-Diagnostics]], [[Freewheel-Mode]], [[Golden]]
