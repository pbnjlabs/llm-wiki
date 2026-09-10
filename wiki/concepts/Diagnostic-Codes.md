---
type: concept
tags: [troubleshooting, diagnostics, stairlift, bruno]
---

# Diagnostic Codes (Bruno Stairlift Circuit Board)

A shared diagnostic-code table and code-translation reference used across
confirmed models: [[SRE-2010]] (new PCB, PCB-00133136), [[SRE-3000]]
(PCB-00124140), and [[CRE-2110]] ("CRE & SRE" mode column). The identical
table appears in the SRE-2010 Tech Support Guide, the CRE-2110 Tech Support
Guide, and the CRE-2110 Install Manual.

**Not confirmed for [[SRE-3050]]** — the table's column headers name
SRE-2010, SRE-3000, and CRE-2110 specifically but no SRE-3050 column;
treat SRE-3050 codes as unverified against this table until checked
against its own manual.

## Code translations

**Normal codes** (not a failure — many display during normal operation):
- A1 — Power swivel switch enabled (CRE-2110 only)
- A3 — Seat fully rotated switch engaged (CRE-2110 only)
- A8 — Power swivel or power footrest actuator operating
- C1 — Unit is/was recently parked and charging
- C2 — Unit is/was recently running
- C3 — Unit parked between charge stations (all CRE-2110 models,
  SRE-2010E/EOS)
- L1 — Seat is swiveled
- L2 — Carriage at top of rail (upper limit engaged)
- L3 — Carriage at bottom of rail (lower limit engaged)
- L6 — Carriage on mid-park (CRE/SRE-2010E or folding rail only)
- L8 — Carriage is/was recently on soft stop
- O1/O2 — Up/Down rocker command input recently
- O4/O5 — Up/Down remote command input recently
- P1/P2 — Rail folded up/down
- P3 — Rail disable switch activated
- P8 — Rail actuator/motor running

**Problem codes:**
- A6/A7 — Obstruction sensed and reversed to clear obstruction
- C4 — Unit not charging when parked (all CRE-2110, SRE-2010E/EOS)
- C5/C6 — Batteries bad or not being charged
- D1 — Speed pot jumper not plugged in, or bad speed pot (old CRE-2110E only)
- D2 — Need to erase and reprogram remotes
- **D4 — Brake not releasing, or over-speed engaged mechanically only**
  (the code to check first for "won't move")
- D7 — Critically low voltage (bad or fully discharged batteries)
- D8 — Remote needs to be programmed; F code (all) = bad board
- P7 — Rail hit an obstruction and reversed
- P9 — Rail actuator/motor was running and has stopped/disconnected
- P0 — Rail PCB lost communication with main PCB

**Normal codes that can look alarming but aren't:**
- C3 when parked at either end and not seeing charge contacts
- L1 when seat is in riding position and doesn't see swivel safety switch
- L2/L3 showing at the "wrong" end — check installation orientation first

## General "unit does not operate" checklist

Before diving into codes: check circuit breaker (foreign-object jam or
overload are the two most common trip causes), battery voltage (16-28VDC
normal range, D7 below that), footrest safety switches (sliding tray must
move freely), and seat swivel position (unit won't run unless the seat
faces the open side of the stairs — this is correct behavior, not a fault).

## See also

[[SRE-2010]], [[SRE-3000]], [[CRE-2110]], [[Overspeed-Safety-Brake]]
