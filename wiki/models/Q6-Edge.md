---
type: model
manufacturer: Pride
model: Q6-Edge
tags: [pride, quantum, q6-edge, power-chair, mid-wheel-drive, ne, ne-plus, q-logic]
---

# Q6 Edge (original, NE / NE+ / Q-Logic)

The first-generation Quantum **Q6 Edge** mid-wheel-drive chair (about
2010–2013), before the [[Q6-Edge-2.0]]. Built with **Q-Logic NE, NE+ or
legacy Q-Logic** electronics, not Q-Logic 3 or QLNES. No spec sheet or
owner's manual on file; the documents are service ones.

## Documents

- [[Q6 Edge Technical Troubleshooting Guide (INFMANU4109 Rev B, 2012)]]
  — the current dealer troubleshooting guide (flowcharts).
- [[Q6 Edge Technical Troubleshooting Guide (INFMANU4109 Rev A, 2011)]]
  — superseded first edition, numbered wiring diagrams.
- [[Q6 Edge Parts Replacement Guide (INFMANU4845)]] (2017) — titled
  "Q6 Edge"; its NE/NE+/Q-Logic joysticks, TRU-Balance/TB3 seats and
  articulating beam point to this generation. Check the IPB before using
  it on a 2.0.
- [[Q6 Edge Basic Troubleshooting]] (2011) — symptom checklist for the
  whole Q6 Edge family.

## Layout

Front battery door (squeeze the release levers; foot platform comes off
with it), rear electronics door (thumbscrews), center panel on reusable
fasteners, top shroud (4 screws). Power module behind the rear door with
**motor, power, bus and PTO/run-plug** harnesses. Battery wiring diagram
inside the front battery door. Drive wheels on 4- or 5-spoke hubs;
semi-independent articulating beam.

## Troubleshooting values (TTG)

| Test | Good |
|---|---|
| Joystick charger port, chair on | about 25 VDC (under 18 V: charge) |
| Circuit breaker | under 1 Ω |
| Motor across the harness | 0.5–1.5 Ω |
| Motor brushes | not below 0.25 in, undamaged |
| Brake across the harness | about **80 Ω** |
| Bus cable / extension / multiplier, each pin | under 1 Ω |
| Charger inhibit jumper, 14-pin power module plug | NE pin 4–6; NE+ / Q-Logic pin 1–9 |
| Charger inhibit jumper, PTO 4-pin barrel | pin 3–4 (**never 1–2**) |

Inhibit programming: NE `chrgInb` **ON**; NE+ and Q-Logic Inhibit
**High**. System Lock unlock: power on, full forward to a beep, full
back to a beep. Full procedures: [[Power-Chair-Troubleshooting]].

## Torque (PRG)

Lug nuts 25 N·m (18.4 ft·lb), hub nut 51 N·m, motor to bracket 7 N·m,
caster nut 27–34 N·m, articulating beam 40 N·m. **Re-seat the axle key**
when the hub comes off. All Pride/Quantum values side by side:
[[Pride-Parts-Replacement]].

## Bulletins and kits

- **Seat height and seat angle (dump)** (TechnoBulletin JAZZY-168,
  2010): power off, drive mode, controller unplugged; seat off the
  trapeze bar; move the **L-brackets** up or down (only one set, front
  or rear, to change the dump); blue thread lock, **35 N·m (25.8
  ft·lb)**; new nylon nuts. Synergy or TRU-Balance seats: see their
  manuals.
- **Battery harness:** improved routing from June 2011 (JAZZY-171) and
  the conversion kit ([[Q6 Edge Battery Harness Conversion (INFINFB2746)]]):
  never cut or shorten the harness; coil and tie any extra.
- Bulletins: [[Pride TechnoBulletins (2006-2024)]].

## See also

[[Q6-Edge-2.0]], [[Q6-Edge-3]], [[Q6-Edge-HD]], [[J6]] (same
electronics, same troubleshooting format), [[Joystick-Controllers]],
[[Q-Logic-Fault-Codes]], [[Pride-Power-Chair-Lineup]], [[Pride]]
