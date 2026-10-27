---
type: source
manufacturer: Adaptive Switch Laboratories
model: ASL 558 ATOM Bluetooth Wireless Mouse Emulator
doc_type: Operator Manual
source: "MANUALS/ASL/Instruction-Manual-ASL-558-Bluetooth-2020-new.pdf; MANUALS/ASL/ASL-558-Atom-Mouse-Emulator-Set-Up.pdf"
date: 2021
tags: [asl, mouse-emulator, bluetooth, computer-access, atom]
---

# ASL 558 ATOM Bluetooth Mouse Emulator (Manual and Common Setups)

Two ASL documents for the **ASL 558 ATOM Bluetooth Wireless Mouse
Emulator**, a USB box (3.64 × 2.63 × 1.09 in, 40 in USB lead) that turns
an ATOM head array or ASL Bluetooth joystick into a computer mouse: the
2-page instruction manual (Rev 2-2020) and the 1-page **Common Setups**
technical guide (Rev 2021). Feeds [[Alternative-Drive-Controls]].

## Pairing

- **ASL Bluetooth joysticks:** plug a switch into the joystick box's user
  port and hold about 2 s (long beep); press the 558's BT pairing button
  (blue light: two quick flashes, pause); if the joystick's status light
  still flashes, press its pairing switch. **First pairing can take 8–10
  s**; afterwards it pairs automatically.
- **104 ATOM head array:** **DIP switch 2 up**, hold the user or attendant
  switch for the long beep (wireless/ECU mode), press the 558 pairing
  button, then the ATOM's. Solid blue light = connected.
- Blue lights on the 558 flash as it receives directions.

## Settings

12 DIP switches (pairs): **A** initial mouse speed (SW1–2), **B** maximum
cursor speed (SW3–4: off, 2×, 4×, 8× the computer's base speed), **C**
cursor delay before speeding up (SW5–6: off, 1, 2, 4 s), **D** switch
delay against accidental hits (SW7–8: off, 0.5, 1, 2 s), **E** latch
delay for click-and-drag (SW9–10: off, 1, 2, 4 s; repeat to unlatch),
**F** cursor movement options (SW11–12: 3, 4 or 5 switch; **both down for
3-switch ATOM head array**). **ON switch:** up = +1/3 mouse speed (better
for Mac), down = base speed (better for PC). Six **dials A–F** (Reverse,
Left, Right, Forward, Left Click, Right Click inputs) each set 0 no
change, 1 down, 2 left, 3 right, 4 up, 5 right click, 6 left click; **no
two inputs may share a value except 0**.

## Common setups (2021 guide)

| Setup | Forward | Reverse | Right | Left |
|---|---|---|---|---|
| 1: 3-switch head array | up/down | – | **left click** | left/right |
| 2: 3-switch joystick | up/down | right click | right/left | left click |
| 3: 4-switch | up/down | left click | right | left |
| 4: 5-switch | forward | reverse | right | left (clicks through switches) |

**Conflict:** the 2020 manual's "current view" for 3-switch use maps
**forward = left click, right = up/down**, while the 2021 guide's Setup 1
has **forward = up/down, right = left click**. Go by the newer guide, and
check against the user.

Warranty **one year** (the drive controls are two).

## Feeds into

[[Alternative-Drive-Controls]], [[Adaptive-Switch-Laboratories]]
