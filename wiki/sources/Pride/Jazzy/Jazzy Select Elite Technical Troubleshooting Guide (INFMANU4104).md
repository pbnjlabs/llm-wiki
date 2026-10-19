---
type: source
manufacturer: Pride
model: Jazzy-Select-Elite
doc_type: Troubleshooting Guide
source: "MANUALS/Pride/Jazzy Power Chairs/ttg_jazzy_select_elite.pdf"
date: 2011-01
tags: [pride, jazzy, jazzy-select-elite, troubleshooting, gc2, gc3, pg-drives, flash-codes]
---

# Jazzy Select Elite Technical Troubleshooting Guide (INFMANU4104)

18-page dealer guide, Rev A, January 2011, for the **Jazzy Select
Elite with GC2 or GC3** electronics (PG). Numbered steps keyed to wiring
diagrams: joystick module, power module, battery harness, breaker,
left/right motors, off-board charger and cord.

- **No power:** charger socket pins 1(+)–2(−) over 18 V → joystick
  module; under 18 V → charge; 0 V → power module bus port (pins 1–4),
  power module battery plug, battery harness, breaker (under 1 Ω),
  battery pairs (under 18 V → replace both).
- **Meter scrolls left to right (inhibit):** charger in the socket, or
  pins 2–3 shorted at the socket (or connector 2e on GC2). Nothing
  plugged in → joystick module, then power module.
- **Flash codes** (all battery LEDs):

| Flashes | Fault | Test |
|---|---|---|
| 1 | Low battery: **under 22 V at the power module** | Charge 8–14 h; charger lights; 120 VAC; batteries too low → shop |
| 2 / 4 | Left / right motor disconnected | Motor pins 3–4: 0.5–1.5 Ω → power module; open → motor |
| 3 / 5 | Left / right motor wiring fault (motor-to-brake) | Pins 2–4 under 1 Ω → motor; open → power module |
| 6 | Charge inhibit active | See above |
| 7 | Joystick | Center, power-cycle; still there → joystick module |
| 8 | Controller | Cross-motor short test; else power module |
| 9 | Park brake | Freewheel levers in drive; brake pins 1–2 **about 60 Ω** each; open → that brake |
| 10 | High battery: **over 32 V** | Charger output over 30 V → charger; else power module |

- Joystick moved at power-up: meter ripples side to side; not released
  within 5 s, power-cycle needed.

Feeds into: [[Jazzy-Select-Elite]], [[Pride-Controller-Flash-Codes]],
[[Power-Chair-Troubleshooting]].
