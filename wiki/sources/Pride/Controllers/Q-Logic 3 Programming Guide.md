---
type: source
manufacturer: Pride
doc_type: Programming Guide
source: "MANUALS/Pride/us_ca_q-logic3 programming guide_om.pdf"
date: 2020-09
tags: [pride, q-logic-3, controller, joystick, programming]
---

# Q-Logic 3 Programming Guide (INFMANU5071)

44-page **provider/ATP-level** programming reference for the Q-Logic 3
Drive Control System, US/Canada, Rev B/September 2020. Programmed via the
**Econ-W** PC software (wired or Bluetooth to the controller) or the
**HHP** (Hand-Held Programmer) field device — both expose the same
parameter tree, HHP through an on-screen menu, Econ-W through a desktop
GUI.

Major sections (see [[Joystick-Controllers]] for the synthesized
cross-cutting summary):
- **Setup**: startup configuration (default/last-used/selection-screen/
  power-on input device; user entry point), Clinic Mode (quick
  no-programmer demo setup), provider contact info storage.
- **Hand Control**: input configuration (proportional / switch operation /
  3-direction variants), joystick setup (center deadband, tremor
  suppression, assign direction, throw), button operation (toggle, horn,
  Key I/II, Home button, Custom MIO mapping), device double-command
  mode-switching, switch jack config/E-stop options, proportional and mini-
  proportional alternative drive control (mo-Vis, Stealth, Switch-It)
  programming and joystick calibration.
- **Head Array**: 3-switch and i-Drive 4 head array programming, toggle
  command, mode jack config, sleep mode, switched-turn shaping.
- **Sip-N-Puff**: 2-pressure or 4-pressure input config, pressure direction
  assignment, latch driving (Cruise/3-Step/1-Step) with decel/quick-stop/
  speed-step braking options, sampling delay, profile-change-by-double-
  command.
- **Switches**: 5/4/3/2/1-switch scanning configurations, linked 2-switch
  driving, latch driving, scan order/rate, list navigation modes (manual/
  auto-repeat/auto-change).
- **Multiple Input Devices**: up to 4 specialty controls at once, Change
  Input Device menu, evaluation-mode quick switching.
- **Seat**: drive inclination/tilt thresholds (Econ-W and HHP paths),
  latched actuators with timeout, input-command inversion, **Combined
  Functions** (groups multiple actuators, e.g. recline+back+legs, under one
  mapped switch to mimic "memory seating" without being true memory
  seating), pretilt angle presets (25° max drivable).
- **iAccess**: up to 19 functions across up to 5 pages on the 4-button
  iAccess module, single- or multi-page mode.
- **Bluetooth**: mouse-emulation pairing for phone/tablet/computer, dwell
  click option.
- **Infrared, Reminders, HHP**: IR remote teaching, on-display reminder
  scheduling, and HHP-specific navigation (mirrors Econ-W's parameter tree
  as an on-screen menu: Program Adjustments → System/Display/Audio/
  Battery/Error History/Seat Configuration/Seat Presets, etc.).

Warns throughout that incorrect programming can affect speed, acceleration,
braking, and dynamic stability — provider/trained-technician use only.

Feeds into: [[Joystick-Controllers]].
