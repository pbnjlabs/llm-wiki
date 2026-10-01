---
type: model
manufacturer: Open Sesame
model: Model 133
tags: [open-sesame, automatic-door, swing-door, residential]
---

# Open Sesame Model 133

[[Open Sesame]]'s **residential** swing-door operator. The clutch
**disengages whenever the operator isn't running**, so the door swings by
hand as if there were no operator. It's the operator in every Residential
bundle (see [[Open Sesame Field Survey Forms]]).

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
- Clutch 12 V DC 0.5 A, auto-disengaging.

## Install

- **Operator 3 in from the hinges.** Arm shoe **13 in from the hinges**
  (except on commercial installs). Arm at 90° with the door closed, then
  tighten it with the 4 mm Allen wrench.
- Door mount for inward doors, lintel mount for outward doors (shoe 1⅜ in
  below the top of the door), parallel mount for storm/screen doors or a
  wider opening. See [[Open Sesame Mounting Instruction Sheets]].
- Units ship for **right-side hinges**. For left hinges, reroute the
  wires through the gray tube and slide the direction switch toward the
  hinges.

## Adjustments (cover off)

- **Yellow knob:** close delay. **Blue knob:** opening angle.
- **White knob:** obstruction sensitivity. Turn it clockwise for a heavy
  door or a dragging sweep. **133 only.**
- **Auto-close jumper (133 only):** bottom two pins = park enabled,
  middle two = park disabled with auto-close on. With auto-close on, a door
  opened by hand closes itself after the delay.
- Diagnostic lights: red = door closed, green = power from the
  transformer, plus lights for clutch, strike, opening, open and closing.

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
[[Open Sesame Mounting Instruction Sheets]],
[[Open Sesame Remote Control Programming (2025)]],
[[Open Sesame Electric Strike Dimension Sheets]]

## See also

[[Open-Sesame-Model-233]], [[Automatic-Door-Operators]], [[AutoSwing]]
