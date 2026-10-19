---
type: model
manufacturer: Pride
model: Jazzy-614
tags: [pride, jazzy, jazzy-614, power-chair, dynamic]
---

# Jazzy 614 / Jazzy 614 HD (Dynamic)

Pride Jazzy power chair with **Dynamic** electronics (2010–2011
documents). The 2026 Group 2 chart lists the **Jazzy EVO 614 / 614HD**
with a 60 A Dynamic controller and NF-22 batteries
([[Pride-Power-Chair-Lineup]]); whether the EVO is the same base as the
2010 Jazzy 614 isn't stated, so check the flash codes on the chair
against the table below.

## Documents

- [[Jazzy 614 Technical Troubleshooting Guide (INFMANU3834)]] (Rev B,
  2011) — dealer guide with wiring diagrams.
- [[Jazzy 614 Basic Troubleshooting (INFINFB2468)]] (Rev A, 2010) —
  symptom checklist and flash code table (covers the 614 HD too).
- No owner's manual or parts guide on file.

## Electronics

Dynamic joystick (on/off key, horn, speed LEDs, battery meter, amber
**wrench service indicator**), Dynamic power module, bus cable and bus
extension, power interface harness, front and rear battery harnesses,
**run plug**, circuit breaker. Off-board charger plugs into the
joystick's charger/programming socket.

## Codes and checks

Service indicator flashes 1–11 (Pride's Dynamic table,
[[Pride-Controller-Flash-Codes]]): 1 stall timeout, 2 battery (about
20 V at the module), 3/4 motors, 5/6 park brakes, 7 joystick, 8 power
module, 9 communications, 10 unknown/controller, 11 incompatible.

| Test | Good |
|---|---|
| Charger socket pins 1–2, chair on | over 18 VDC |
| Motor, pins 1–2 at the motor plug | 0.5–1.5 Ω |
| Park brake, pins 3–4 at the motor plug | about **35 Ω** |
| Run plug, pins 1–4 and 3–4 | under 1 Ω |
| Bus cable and extension, each pin | under 1 Ω |
| Circuit breaker | about 1 Ω or less (open = replace) |

Battery meter patterns: **ripple right to left = locked** (power on and
press the **horn twice** within about 10 s); **ripple left to right,
alternating with steady** = charging or **inhibit** (nothing plugged
in? check the run plug); left red LED flashing = low battery; speed
LEDs flashing = joystick off center at power-up.

## See also

[[Jazzy-600-ES]], [[Power-Chair-Troubleshooting]],
[[Pride-Controller-Flash-Codes]], [[Shark-Diagnostics]] (Golden's
11-code Dynamic table, same numbering), [[Pride-Power-Chair-Lineup]],
[[Pride]]
