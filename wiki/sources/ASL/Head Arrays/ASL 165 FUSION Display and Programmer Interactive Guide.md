---
type: source
manufacturer: Adaptive Switch Laboratories
model: ASL 165 FUSION Display, Programmer and Attendant Control (with ASL 110 FUSION)
doc_type: Web Article
source: "MANUALS/ASL/165 Interactive Guide/img-all-elements3.jpg"
url: https://www.asl-inc.com/165-fusion-display-and-programmer-interactive-guide.php
date: 2026-10-27
tags: [asl, head-array, fusion, programming, display, attendant-control]
---

# ASL 165 FUSION Display and Programmer Interactive Guide

ASL's web **interactive guide** to the **ASL 165 FUSION Display,
Programmer and Attendant Control** menus for the
[[ASL 110 FUSION Head Array Instruction Manual (Rev 3-2022)]]. The page is
an image-only flowchart (its "interactive" steps just zoom into it). It
was viewed in Chrome (the site blocks scripted fetches) and its 36 images
were saved to `MANUALS/ASL/165 Interactive Guide/`;
`img-all-elements3.jpg` is the whole diagram. **No dated revision**; the
diagram's More Programming screen shows firmware **ASL110 1.8.0, ASL165
1.8.2**. It's ASL's own material, but the screens are
illustrations with no explanatory text, so where this page says what a
screen does, that's read from the diagram. The 165's own manual isn't on
file. Feeds [[Alternative-Drive-Controls]].

## Getting into programming

**Press both buttons on the display at the same time** to open the
**FUSION Programming** screen: **Pad Settings**, **Settings**, **More**
(OK to exit).

## Drive-side screens (what the user sees)

- **Start screen:** FUSION logo.
- **Out of neutral:** "**Release pad**": a pad was touched at power-up;
  let go.
- **Fault screens:** "**Fault – cycle power**", with the faulty pad shown
  red: **left pad**, **back pad** or **right pad**. Turn the chair off and
  on; if it comes back, check that pad and its cable.
- **Main user menu:**
  - **Standard** (non-R-net): Power on/off, Bluetooth, Next Function,
    Next Profile.
  - **R-net:** Power on/off, Bluetooth, Toggle F/R, User Menu, Seating,
    Sleep.
  - The user steps through these with the user switch (see the
    [[ASL 110 FUSION Head Array Instruction Manual (Rev 3-2022)|FUSION manual]]:
    tap = select, hold = next item).
  - Selecting Power on/off shows "**Fusion off – press switch**" (press
    the user switch to turn it back on).
- **Attendant Control** (from the attendant icon on the main menu):
  on-screen arrows to drive, an OK button, and an icon in the corner that
  steps through **head array**, **head array crossed out** and **red
  power**. That reads as **shared**, **head array locked out / attendant
  only** and **power off**, but the guide doesn't label them.

## Pad Settings

- **Set Pad Type:** touch a pad to change it between **PROP**
  (proportional) and **DIGITAL**; **hold a pad to calibrate it**.
  Proportional calibration: **Prop Calibration Min** (use the arrows to
  set the minimum, shown 0) then **Prop Calibration Max** (shown 85).
- **Set Pad Direction:** touch a pad to change the direction it drives
  (left, right, forward arrows).
- **Set Minimum Speed:** minimum drive speed **for each pad**
  (shown 20 % / 20 % / 20 %).

## Settings

- **User Settings:**
  - **Clicks (audio)** on/off.
  - **Power up idle** on/off.
  - **RNet enable** on/off.
  - **Mode (Reverse)** on/off.
  - **Timeout** (shown 2.0).
- **Feature List**, i.e. which items appear on the user menu:
  - **If R-net is not enabled:** Power on/off, Bluetooth, Next Function,
    Next Profile.
  - **If R-net is enabled** (two screens): Power on/off, Bluetooth,
    Toggle F/R, User Menu, Seating, Sleep.
- **Performance:**
  - **Set Veer Adjust:** "slide the anchor point to eliminate veering"
    (a slider and a value, shown −2).
  - **Attendant Setting:** **Active** and **Proportional** on/off.

## More Programming

- **Diagnostics:** "**Activate pad**" screen. Each pad lights when
  pressed and shows its reading, with **user port** and **mode port**
  indicators: a quick way to check the pads and switches.
- **Reset Settings:** "This resets all settings to factory default. Are
  you sure?" Yes / No, then "**All settings have been reset**".
- Shows the firmware versions (ASL110, ASL165).

## Service use

- A **fault screen pointing at one pad** narrows a FUSION problem to that
  pad or its cable before you blame the interface.
- Use **Diagnostics → Activate pad** to check each pad, the user port and
  the mode port after any repair or cable reroute.
- After **Reset Settings**, the pad types, directions, minimum speeds,
  feature list and veer must be set up again for the user. Note the
  settings first.
- Whatever is set here, the **reset switch rule** and the chair-side
  programming still apply
  ([[ASL 110 FUSION User Installation Guides (LiNX, Q-Logic, R-net, Permobil)]]).

## Feeds into

[[Alternative-Drive-Controls]], [[Adaptive-Switch-Laboratories]],
[[ASL 110 FUSION Head Array Instruction Manual (Rev 3-2022)]]
