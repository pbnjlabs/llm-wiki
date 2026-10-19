---
type: source
manufacturer: Pride
model: Jazzy-614
doc_type: Troubleshooting Guide
source: "MANUALS/Pride/Jazzy Power Chairs/ttg_jazzy_614.pdf"
date: 2011-01
tags: [pride, jazzy, jazzy-614, troubleshooting, dynamic, flash-codes, wiring]
---

# Jazzy 614 Technical Troubleshooting Guide (INFMANU3834)

22-page dealer **Technical Troubleshooting Guide** for the **Jazzy 614
with Dynamic electronics**, Rev B, January 2011. Numbered steps keyed to
3D and 2D wiring diagrams (13 components: Dynamic joystick, power
module, bus cable extension, bus cable, power interface harness, front
and rear battery harnesses, motors, run plug, charger, cord, breaker).

Sections:

- **No power** (battery meter dark) — charger/programming socket on the
  joystick (over 18 V → joystick; under 18 V → charge), bus cable, bus
  extension, power module, battery harnesses (0 V at both ends → replace
  **both** batteries), circuit breaker.
- **Battery meter diagnostics:**
  - **Ripple left to right, alternating with steady; speed light flashes
    when the joystick moves** = **inhibit / charging mode**: pins 2–3 of
    the charger socket are shorted. Nothing plugged in? Check the **run
    plug**: pin 1–4 and pin 3–4 under 1 Ω, else replace the run plug;
    both good → joystick.
  - **Left red LED flashing** = low battery: charger lights, 120 VAC at
    outlet and cord, harnesses, breaker, power module and bus continuity.
  - **Ripple right to left** = **locked**. Unlock: power on, press the
    **horn twice within 10 s** while it ripples (it powers down after
    about 15 s).
- **Flash codes** (amber wrench service indicator):
  - Steady flashing speed LEDs = joystick off center at power-up.
  - 1 stall timeout (motors working too hard; check for obstruction,
    else power module), 2 battery fault (about **20 V** at the module),
    3 / 4 left / right motor (**0.5–1.5 Ω**, else motor), 5 / 6 left /
    right park brake (**about 35 Ω** across pins 3–4, else brake;
    freewheel levers in drive first), 7–11 joystick, power module,
    communications, unknown, incompatible controller (bus cable and
    extension continuity, corrosion, then power module, then joystick).

The breaker test is printed two ways (under 1 Ω in one step, "about
1 Ω" in another); either way an open = replace the breaker.

Feeds into: [[Jazzy-614]], [[Pride-Controller-Flash-Codes]],
[[Power-Chair-Troubleshooting]].
