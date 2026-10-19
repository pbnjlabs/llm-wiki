---
type: source
manufacturer: Pride
model: J6
doc_type: Troubleshooting Guide
source: "MANUALS/Pride/Quantum Power Chairs/ttg_j6_ne_neplus_qlogic.pdf"
date: 2011-02
tags: [pride, quantum, j6, troubleshooting, ne, ne-plus, q-logic, wiring]
---

# J6 Technical Troubleshooting Guide (INFMANU4132)

28-page dealer **Technical Troubleshooting Guide** for the **J6 with NE,
NE+ or Q-Logic electronics**, Rev A, February 2011. Numbered steps keyed
to 3D and 2D wiring diagrams (components 1–14, connectors 1a, 2b…), the
same format as the Q6 Edge Rev A guide.

Sections and the J6-specific values:

- **No power** — joystick charger socket (≈25 V → joystick; under
  18 V → charge), battery cable, **battery/circuit-breaker harness**,
  breaker (under 1 Ω good), power interface harness, power module bus
  port, bus cable extension. **J6 gotcha:** the battery/circuit-breaker
  harness must go to the **positive of one battery and the negative of
  the other**; wired wrong, the chair won't power up and the breaker
  trips.
- **System Lock** (NE, NE+, Q-Logic): same unlock as the Q6 Edge (full
  forward, full back).
- **Battery charging or drive inhibit** (Q-Logic #107): same jumper
  tests as the Q6 Edge (PTO 4-pin pin 3–4; 14-pin NE 4–6, NE+/Q-Logic
  1–9) and inhibit programming (NE `chrgInb` ON, NE+/Q-Logic High
  Inhibit).
- **Joystick, power module, missing module, communication/software
  errors** — bus cable extension and multiplier continuity.
- **Open motor** — motor **0.5–1.5 Ω** at the motor plug and again at
  the motor interface harness; brushes under 0.25 in → brushes.
- **Motor/brake** — brake about **60 Ω** across the two white pins (the
  Q6 Edge guide says 80 Ω), checked at the motor and at the interface
  harness.
- **Error tables:** NE, NE+ (LCD text) and Q-Logic (#1–6, 19, 23, 36, 37,
  105, 192/193, 203/204, 229).

The seat must come off and the rear and center shrouds are removed to
reach the electronics.

Feeds into: [[J6]], [[Power-Chair-Troubleshooting]],
[[Joystick-Controllers]].
