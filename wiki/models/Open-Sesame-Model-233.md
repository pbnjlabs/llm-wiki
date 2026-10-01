---
type: model
manufacturer: Open Sesame
model: Model 233
tags: [open-sesame, automatic-door, swing-door, public-access, storm-door]
---

# Open Sesame Model 233

[[Open Sesame]]'s **public-access** swing-door operator. It has a
**constant-torque slipping-disc clutch (15 in-lb) that is always
engaged**, so when the door is pushed open by hand, the operator closes
it like a door closer with ADA-compatible force. It's used in the Public
bundles and for **storm and screen doors**, and can run a gate if a rain
shield is fitted.

## Spec summary

- Power: plug-in transformer, 115 V AC in, **24 V AC 20 VA** out. The
  operator takes 16–24 V AC/DC with no polarity, so an existing doorbell
  transformer with 16–28 V output can be used.
- Backup battery: **12 V 1.2 Ah sealed lead-acid** (MK ES1.2-12 or
  equivalent). It's trickle-charged, runs about 2 days without power and
  lasts 3–5 years.
- Motor 12 V DC 1.5 A. Strike output **12 V DC, 1 A** (green −, yellow +).
- Opens up to **120°**. Hold-open is 5–50 s per the 2025 spec sheet, or
  5–35 s per the manuals and board sheet. Factory setting 15 s.
- 2⅝ × 4 × 14⅛ in, 10 lb, powder-coated steel. Colors: antique white,
  dark bronze, silver.
- Activation: RF remotes (green antenna = 433 MHz on current units), wired
  dry contacts (push plates, mats, motion sensors), keypad, Voice
  Interface, proximity tags.
- Clutch: constant-torque slipping disc, 15 in-lb, adjustable.

## Install

- **Operator 4 in from the hinges** (the 133 is 3 in). Arm shoe 13 in
  from the hinges. The rest is the same as [[Open-Sesame-Model-133]].
- An extra bumper accessory can be added if needed.
- Storm/screen doors take the long screw spacer and drop plate A or B.

## Clutch adjustment (233 only)

Turn the **red ring** on the clutch using the 3 mm tool in one of its 6
holes. Clockwise, seen from above, gives more force, for example against
wind on an outward door. Counterclockwise makes manual opening easier. It
shouldn't need to be fully tight.

## M210 circuit board (2022)

The newer board, see [[Open Sesame M210 Circuit Board Sheet (2022)]]:

- Blue pot: opening angle. Yellow pot: close delay, 5–35 s.
- **Speed jumper (blue):** off / top / middle / bottom = slowest to normal.
- **Park jumper (red):** both pins = park; one pin = no park. With no
  park, a cycle can't be stopped once it starts.
- **Black jumper:** one pin = single operation (press to open, press again
  to close).

The 233 has no obstruction knob and no auto-close jumper.

## Troubleshooting (from the install guide and owner's manual)

| Symptom | Check |
|---|---|
| No green light on the board | No power from the transformer: check the outlet, transformer wiring, or the transformer |
| No red light | Switch off; **"H" sensor not lined up with the red dot** (push it to 1/8 in from the disc); blown fuse (tube holder on the orange battery wire, pre-2021 units); bad top board |
| Door won't open | Red light off; loose connections; **battery** (test 13–14 V DC, replace if 3–5 years old); obstruction or thick weather stripping; bad radio receiver board (if the Test button also fails) |
| Doesn't open wide enough | Blue knob; battery |
| No hold-open delay | Yellow knob; bad top board |
| Only works in one direction | Bad bottom board (pre-2021): flip the direction switch and press Test |
| Slow | Door dragging or weather stripping; battery |
| Strike won't release | Battery; wiring; door cord or RJ-11 jack; red dot out of line |
| Opens the wrong way | Direction switch: toward the hinges, or **away from them on a parallel mount** |
| Won't close | M233: tighten the clutch ring. Both models: move the arm shoe one hole toward the hinges. Battery |
| Clutch slips or grinds | Bad clutch: call for an RA number and send it in |
| Remote does nothing | Wrong frequency (antenna color), remote not programmed, remote battery dead, loose receiver board connection, bad receiver board |

## Documents

[[Open Sesame Installation Guide]], [[Open Sesame Owner's Manual (2025)]],
[[Open Sesame Model 133 and 233 Specifications (2025)]],
[[Open Sesame M210 Circuit Board Sheet (2022)]],
[[Open Sesame Mounting Instruction Sheets]],
[[Open Sesame Remote Control Programming (2025)]]

## See also

[[Open-Sesame-Model-133]], [[Automatic-Door-Operators]], [[AutoSwing]]
