---
type: model
manufacturer: Pride
model: Quantum-614
tags: [pride, quantum, quantum-614, power-chair, ne-plus, legacy]
---

# Quantum 614 (NE+, legacy)

Quantum mid-wheel chair with **NE+** electronics. The guide's layout
and brake value (35 Ω) match the [[Jazzy-614]] (Dynamic), so it looks
like the same base; the documents don't say so. No owner's manual on
file.

## Documents

- [[Quantum 614 NE+ Technical Troubleshooting Guide (INFMANU3988)]]
  (Jan 2010)

## Troubleshooting values

| Test | Good |
|---|---|
| Charger socket pins 1–2, chair on | about 25 V (under 18 V: charge) |
| Breaker | under 1 Ω |
| Motor (pins 1–2 at 7a / 8a) | 0.5–1.5 Ω |
| Brake (pins 3–4) | **about 35 Ω** (same as the Jazzy 614) |
| Inhibit jumper, power module | pin 1–9; PTO 4-pin pin 3–4 |

- Inhibit programming: **High Inhibit**.
- **System Lock on this chair: press the Mode switch until it powers
  off**; unlock forward to a beep, back to a beep.
  The NE+ BOI ([[NE+ Controller Basic Operation Instructions (INFMANU3765)]])
  says hold **both profile keys** instead; if Mode doesn't lock it, try that.
- Extra NE+ messages here: left/right indicator, hazard and running
  light errors (press that key; persists → Quantum).

## See also

[[Jazzy-614]], [[Joystick-Controllers]], [[Power-Chair-Troubleshooting]], [[Pride]]
