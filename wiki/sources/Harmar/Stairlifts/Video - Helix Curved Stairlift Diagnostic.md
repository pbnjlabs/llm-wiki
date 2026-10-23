---
type: source
manufacturer: Harmar
doc_type: Training Video
source: "MANUALS/Harmar/Videos/Harmar-#10 Helix Curved Stairlift Diagnostic.mp4"
transcript: "MANUALS/Harmar/Videos/_work/10-helix-curved-stairlift-diagnostic/transcript.txt"
tags: [harmar, helix, stairlift, curved, diagnostics, software, troubleshooting, video]
---

# Video: Helix Curved Stairlift Diagnostic

Harmar training video #10, 2:16, by a Harmar Technical Services tech.
It shows Harmar's **Helix diagnostic software** on a laptop, connected by
a cable to the **diagnostic port on the side of the chassis**. The tech
presses each safety switch in turn and shows the screen. No date. The
screen shows **SW Ver 1.6, HW Ver F**.

## The screen

Window title **"HELIX LEFT"** (for this install), with a **Diag LED**, a
**System Status** line and tabs **BOARD / BATTERY / CHARGER / MOTOR /
SWITCHES**. A tab turns red when its group has a fault.

- **Motion switches:** RIGHT, LEFT, RF UP, RF DOWN, STOP RIGHT, STOP
  LEFT, BRAKE
- **Safety switches:** FOOTREST RIGHT, FOOTREST LEFT, OBSTR RIGHT, OBSTR
  LEFT, SEAT FAIL, "KEY SW ON and E-STOP OFF"
- **Readouts:** battery voltage (about **27.2–27.3 V** on charge, 26.9
  V off), charger voltage (about **26.9 V** at a charge point, 0.00 off
  it), motor current, PWM %, charge %, **track orientation** ("LEFT is
  UP"), charger state (CHARGING / NOT CHARGING), motion state

## What each test shows

| Time | Action | Screen |
|---|---|---|
| 0:09 | Plug the cable into the chassis side. | |
| 0:14 | Press a **footrest** obstruction switch (one each side of the footrest). | "Footrest Left Fault Detected", red, plus a beep code |
| 0:28 | Press the **chassis** obstruction switch. | "Obstruction Left Fault Detected" |
| 0:39 | Press the **top roller** obstruction. | Red on screen |
| 0:50 | **Swivel the seat.** | "Seat Fault Detected" and a beep code |
| 0:59 | Run down to the landing. | **STOP RIGHT on** (at the landing), charger voltage and battery voltage shown |
| 1:15 | Press the **E-stop**. | "Key Off Fault Detected" (key switch off or E-stop) |
| 1:26 | Pull the E-stop out. | System resets |
| 1:30 | Press **two obstructions at once** (here footrest right and obstruction left). | **"!!! MAJOR FAULT !!! Conf Switches: FR RIGHT & OBSTR LEFT — UAB MUST BE RESET or POWER CYCLED"** |
| 1:58 | Reset the chassis and restart the software. | |

## Use

- The software is the quickest way to see **which** switch is open on a
  Helix: a single obstruction is a minor fault that clears when
  released. **Two at once is a major fault** ("conflicting switches")
  that latches until the universal access board (UAB) is reset or power
  cycled. That matches the conflicting-switch major-fault codes in
  [[Harmar-Stairlift-Beep-Codes]].
- Charger voltage reads only at a charge point, so it's a quick check
  of the charge strip or contacts.
- The manuals only mark the **diagnostic port** on the chassis and
  describe the beep and LED faults. **The software and cable aren't on
  file**; get them from Harmar tech services (800-833-0478).

## Feeds into
[[Helix]], [[Harmar-Stairlift-Beep-Codes]], [[Stairlift-Troubleshooting]]
