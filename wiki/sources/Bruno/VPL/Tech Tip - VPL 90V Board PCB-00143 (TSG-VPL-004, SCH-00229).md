---
type: source
manufacturer: Bruno
model: VPL-3153-3175
doc_type: Tech Tip
source: "MANUALS/Bruno/Tech Tips/VPL/TSG-VPL-004 PCB-00143(90V)  LED Diagnostics.pdf; MANUALS/Bruno/Tech Tips/VPL/SCH-00229.pdf"
url: https://www.brunopartner.com/er26ya59sp/tech-tips.aspx
date: 2018-03-19
tags: [bruno, vpl, tech-tip, ac, circuit-board, diagnostics, schematics, vpl-3153, vpl-3175]
---

# Tech Tip - VPL 90V Board PCB-00143 (TSG-VPL-004, SCH-00229)

Two documents for the **PCB-00143 "90V VPL" board** used in the AC low-rise **VPL-3153/3175**: TSG-VPL-004 Rev 0 (03/19/18, LED diagnostics; portal tech-tips 196, and 195 which links the same file) and schematic **SCH-00229** Rev 0 (5/24/17, 3 pages; portal tech-tip 212).

**Board:** 115 VAC in through a 15 A internal breaker and line filter, upper final limit, **F1 20 A**; a 24 VDC supply (accessories through **F2 2.5 A slo-blo**); a motor controller driving a **½ hp 90 VDC motor** (red + = clockwise shaft). **Remove AC power and wait 3 minutes before touching the board** (high voltage).

| LED | Meaning (on = OK unless noted) | Off / problem |
|---|---|---|
| E1 | HV bus on | AC in? F1 blown? Upper final limit open |
| E2 | 3.3 VDC logic | 24 V regulator bad: replace board |
| E3 | 24 VDC fused (F2) | F2 blown |
| E4 / E5 | Top cover OK / E-stop OK | Top cover switch; E-stop or nut safety tripped |
| E6 / E7 | Upper gate closed / locked | That switch open |
| E8 / E9 | Platform gate closed / locked | That switch open |
| E10 | Switch enable (ready for a command) | Lit on up or down |
| E11 / E12 | Up / down enable (valid command) | Invalid input, or up and down pressed together |
| E13 / E15 | Up / down call switch | Same |
| E14 / E16 | Up / down limit | Limit tripped |
| E17 | Safety pan OK | Pan switch tripped |
| **E18** | **Fault (red): off is normal** | Flash code below |

**E18 flash codes** (short flashes, then one long one; count both: 5 short + 1 long = 6):

| Code | Name | Likely cause |
|---|---|---|
| 1 | STALL | Overloaded platform |
| 2 | STALL2 | Overloaded and over-temperature |
| 3 | OVERTEMP | Over-temperature |
| 4 | EXT_24V | 24 V overload |
| 5 | OVERVOLTAGE | High AC line |
| 6 | OVERCURRENT | Overloaded platform |
| 7 | MAX_CURRENT | Motor failing |
| 8 | LOW_VOLTAGE | AC line too low |
| 9 | LOW_24VDC | AC line too low |

**Most codes reset with the E-stop**; otherwise remove AC power and wait 1 minute.

**Terminal strip TB7 (20–33):** no gates or interlocks = jumper **25–33**; upper landing gate or interlock = jumper **25–29**; platform gate or lower interlock = jumper **27–29**. Connectors: JP2 expansion, JP3 platform controls, JP4 gate/call-send, JP5 lower limits, JP6 upper limits/cover switch. Page 2 shows the optional interlock wiring at each landing: **HES 5200** and **Von Duprin 6211** electric strikes, Waupaca EMI and Euchner interlocks (the EMI's own wire colours don't match the harness).

Feeds: [[VPL-3153-3175]], [[VPL-Troubleshooting]], [[Gate-and-Door-Interlocks]]
