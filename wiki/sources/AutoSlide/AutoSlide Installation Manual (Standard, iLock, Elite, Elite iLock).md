---
type: source
manufacturer: AutoSlide
model: AutoSlide
doc_type: Installation Manual
source: "MANUALS/AutoSlide/AutoSlide-Installation-Manual-102122.pdf"
date: 2022-10-21
tags: [autoslide, automatic-door, installation]
---

# AutoSlide Installation Manual (Standard / Standard iLock / Elite / Elite iLock)

36-page DIY installation and setup manual (P/N dated 10/21/22) for the
AutoSlide automatic sliding-door retrofit kit, covering all four hardware
variants on a single sliding-panel door: **Standard**, **Standard iLock**,
**Elite**, and **Elite iLock**. Not a mobility-equipment manual — this is a
motorized drive that automates an *existing* sliding door panel (patio door,
screen door, barn door, or pocket door), unlike every other manufacturer in
this wiki.

## Covers

- **In the box**: drive system (motor + electronic controller under a metal
  cover), L-mounting adapter bracket, friction tester (Standard units only),
  power pack (24VDC), screws/tools, two 20" rack sections, rack screws, two
  wireless wall push buttons.
- **Prepare**: power-point placement, door drag-force friction test (decides
  Standard vs. Elite motor — silver barrel vs. black barrel), drive mounting
  options (top mount over active/fixed panel, inside vs. outside; bottom/floor
  mount as a last resort, which normally requires re-handing on a
  right-handed door), adapter bracket use, vertical-gap shimming.
- **Install**: drive mounting (3" overlap target between unit and sliding
  panel when closed, 21–25mm endcap inset), track cutting/joining (cut to the
  exposed panel width with a hacksaw), track mounting (flange up/down,
  aligned to the panel's back edge, screwed in incrementally while holding
  tension against the motor wheel).
- **Operate — locking, mode, and sensor port guide**: iLock units (Standard
  iLock, Elite iLock) have a dynamic braking lock built into the motor,
  identifiable by a chrome cylindrical segment on the motor barrel. Four
  modes selected via a front-panel Mode button: **Green/Auto** (human use,
  pet sensors disabled, no lock), **Blue/Stacker** (keeps door open by
  default; a Stacker-port sensor can partially open it like a garage door),
  **Red/Secure** (iLock security mode — outside sensors and open-assist
  disabled, door locked), **Orange/Pet** (pet + inside sensors enabled,
  outside sensors optional, door locked). Four sensor ports: Inside (top,
  master channel), Outside (2nd, secondary), Pet (3rd, Pet Mode only),
  Stacker (bottom, Blue Mode only). Open Time dial (0–24s, or max = Toggle
  Mode/push-to-open-push-to-close).
- **DIP switch settings guide**: 8 switches — #1 Direction/Learn (also used
  to trigger width-programming), #2 Slam Shut (extra power at open/close
  extremes, incompatible with #7), #3 Pet Learn, #4 Secure Pet (disables
  Outside Sensor in Pet Mode), #5 75% Power (light doors), #6 App Control
  (enables Bluetooth module), #7 Extra Power (heavy doors, incompatible with
  #2), #8 Beep.
- **Powering on / programming opening widths**: initial power-on direction
  check (flips DIP #1 if the door tries to open instead of close), then
  three separate width-programming routines (flip DIP #1 back-and-forth for
  normal/human width, Blue Mode + DIP #1 flip for Stacker width, DIP #3
  flip for Pet width) — each relies on a physical doorstop/jamb to define the
  learned endpoint.
- **Pairing wireless wall buttons and sensors**: universal "Sensor Learn"
  button pairing sequence (press Sensor Learn once, trigger the
  device twice) used for wall push buttons, the RFID pet sensor (see
  [[RFID Pet Sensor Operation Instructions]]), and any other wireless
  accessory.
- **Finalize**: cover installation/removal, cable concealment (valence,
  cable covers).
- **Rehanding** (Section 07): full procedure to physically swap the motor
  and control-panel sides of the unit — required before installing a
  floor-mounted unit on a right-handed door.
- **Troubleshooting**: FAQ (DIY-installable, outdoor use OK if covered and
  kept out of rain/snow above 32°F, power-failure behavior — motor/lock
  fully disengages for manual egress, auto-reverse safety on obstruction,
  home-automation via a momentary-relay key-switch cable, phone control via
  a Bluetooth module + AutoPlus Hub — not documented elsewhere in this
  wiki), and a Common Issues table (partial-open after incomplete learn
  cycle, grinding noise from loose track/wheel pressure, slow operation from
  under-powered DIP settings, random opening from RFID interference).
- **Policy**: 2-year limited manufacturer's warranty (Autoslide Pty Ltd,
  service centers in California and Florida; excludes normal wear, misuse,
  non-AutoSlide accessories, batteries, commercial/institutional use) and a
  standard return policy (30-day RMA window, 20% restocking fee if not
  returned in original condition, no shipping reimbursement).

## Not yet documented anywhere in this wiki

The FAQ mentions two accessories with no manual on file: a **Bluetooth
module** (phone-app control, paired with an "AutoPlus Hub") and a
**key-switch/home-automation relay cable**.

## Feeds into
[[AutoSlide-Drive-System]]
