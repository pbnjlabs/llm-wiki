---
type: source
manufacturer: Pride
doc_type: Technical Manual
source: "MANUALS/Pride/Controllers/Q-Logic/q_logic_technical_manual.pdf"
date: 2008-06
tags: [pride, quantum, q-logic, controller, programming, diagnostics, firmware, technical-manual]
---

# Q-Logic Technical Manual (INFMANU3580)

138-page **dealer/technician** manual for the legacy (first-generation)
**Q-Logic** drive control system, Pride Mobility, INFMANU3580/Rev B/June
2008. Curtis Instruments built the programming tools (the 1314 PC
Programming Station, CAN-USB interface). Much deeper than the end-user
[[Q-Logic Controller Basic Operation Instructions]].

Sections:
- **I. Overview (pp. 6–8):** the modules and their part numbers (power
  module CTLDC1466, AAM CTLDC1472, ECU CTLDC1486, hand control
  CTLDC1467, SAJ/attendant CTLDC1469, Enhanced Display CTLDC1471, Sip &
  Puff CTLDC1487, handheld programmer ELEASMB5215, PCPS ELEASMB5216),
  daisy-chained on a proprietary **CAN bus**; any charger/programmer
  port works.
- **II. Operation (pp. 9–10):** "who's in charge" (the input device that
  powered the chair up has control), the three shut-off methods (switch,
  auto shutoff, System Lock), the fast/emergency/park-brake stops,
  5 profiles per input device, switched vs proportional vs latched
  input, Simple vs Advanced Mode Key Navigation, Standby Select.
- **III. Input devices (pp. 11–22):** hand control, SAJ/attendant
  joystick (LED fault display), Enhanced Display (9-pin D-sub pinout
  per input type), 5/4/3/2/1-switch and head-array command sets,
  proportional 3-axis and 4-axis input.
- **IV. Programming parameters (pp. 23–99):** every parameter for hand
  control, Enhanced Display specialty input, SAJ, attendant, Sip &
  Puff, Enhanced Display Bluetooth/IR/mouse, system settings (tracking,
  reverse beep, reminders, auto shutoff, motor polarity/swap, wheel
  position, **battery type**, System Lock, charger inhibit polarity) and
  seat (AAM actuators A1–A5, **tilt thresholds with factory defaults**,
  configuration numbers 1–39, latch operation).
- **V. Diagnostics and troubleshooting (pp. 100–109):** warnings vs
  recoverable faults vs serious errors, and the **full numbered error
  table**.
- **Appendices:** A programmers (HHP and PCPS), B **system specs**
  (24 V nominal, 16–33 V operating, 35 V max; bus up to 10 m, 10
  modules, 13 A continuous; -25 to 50 °C), C input device installation
  and wiring (the off-board port is a standard **3-pin XLR, 13 A** on
  fused B+/B-, plus two programmer pins), D IR remote control and mouse,
  E **firmware update** with the PCPS.

Feeds into: [[Joystick-Controllers]], [[Q-Logic-Fault-Codes]],
[[Q-Logic-Seat-Configuration]], [[Q-Logic-Firmware-Updates]],
[[Power-Chair-Troubleshooting]].
