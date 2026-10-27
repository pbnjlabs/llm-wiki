---
type: model
manufacturer: Pride
model: Jazzy-Select-Elite
tags: [pride, jazzy, jazzy-select-elite, power-chair, gc2, gc3, pg-drives]
---

# Jazzy Select Elite (GC2 / GC3)

Pride Jazzy power chair (about 2008–2011) with **PG GC2 or GC3**
electronics. The current Jazzy Elite ES and Jazzy Select also run 40 A
GC3 ([[Pride-Power-Chair-Lineup]]), so the GC3 tests and codes below
carry over to them.

## Documents

- Retailer part numbers (Mobility Scooters Direct, 2026-10-27; confirm by serial with the manufacturer): [[Parts Catalog - Mobility Scooters Direct (Pride)#Jazzy Select Elite Parts|Jazzy Select Elite Parts]] (11), [[Parts Catalog - Mobility Scooters Direct (Pride)#Jazzy Select Elite Parts|Jazzy Select Elite Parts]] (8)
- [[Jazzy Select Elite Technical Troubleshooting Guide (INFMANU4104)]]
  (Rev A, 2011): dealer guide with wiring diagrams.
- Warranty: 5-year frame, 13-month electronics and drive
  ([[Pride Warranty Update Inserts (2010)]]).
- Armor and refurb kits for the Select Elite are in the PQ-365 library
  but weren't pulled (accessory kits).

## Codes and checks (GC2/GC3)

All battery LEDs flash the count:

| Flashes | Fault | Check |
|---|---|---|
| 1 | Under **22 V** at the power module | Charge 8–14 h, charger, outlet |
| 2 / 4 | Left / right motor disconnected | 0.5–1.5 Ω at motor pins 3–4 |
| 3 / 5 | Left / right motor-to-brake wiring | Pins 2–4 should be open |
| 6 | Charge inhibit | Charger in, or socket pins 2–3 shorted |
| 7 | Joystick | Center, power-cycle |
| 8 | Controller | Cross-motor short test |
| 9 | Park brake | Levers in drive; **about 60 Ω** each |
| 10 | Over **32 V** | Charger output over 30 V → charger |

Meter scrolling left to right = inhibit (charger in or a shorted
socket). Locked: battery LEDs scroll left to right; unlock forward to
a beep, back to a beep ([[Controller Locking Instructions (INFINFB2311)]]).
**GC charge reminder** (left red LED flashes 4× at power-off after 8 h
of driving): reset by a full charge with the controller **on** the
whole time ([[Pride TechnoBulletins (2006-2024)]], JAZZY-169/170).

Freewheel on the Select family: pull the levers **up** for drive, push
**down** for freewheel ([[Freewheel-Mode]]).

## See also

[[Pride-Controller-Flash-Codes]], [[Power-Chair-Troubleshooting]],
[[Pride-Power-Chair-Lineup]], [[Pride]]
