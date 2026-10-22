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
against its own manual. (The [[SRE-3050 Tech Support Guide]] reprints the
same table, still without an SRE-3050 column. Its beep list matches the
SRE-3000 audible column, and Bruno's [[TechMate Stairlift Troubleshooter]]
treats SRE-3050 beeps the same way.)

**For the step-by-step fix behind each code, see
[[Stairlift-Troubleshooting]].**

Bruno also has a plain-language tech tip on these codes,
[[Tech Tip - Stairlift Code Translations]] (2020). It agrees with the
table below, and adds a few beeps (listed under the display table).

## Code translations

**Normal codes** (not a failure — many display during normal operation):
- A1 — Power swivel switch enabled (CRE-2110 only)
- A2 — Seat in the up position (seat fold switch closed); listed in the
  2026 SRE-2010 owner's manual
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
- A6/A7 — Obstruction sensed and reversed to clear obstruction (the 2026
  SRE-2010 owner's manual: A7 = seat or footrest jammed, actuator stalled;
  the 2026 CRE-2110 owner's manual splits them: **A6 seat jammed, A7
  footrest jammed**)
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

## Display table: d, F and C codes with their beeps

From the full visual/audible table in the [[SRE-2010 Tech Support Guide]]
(dated 7-17-2020 inside the guide). C = chirp, B = beep, L = long beep.
Elan (SRE-3000/3050) gives the same beeps with no display.

| Display | Meaning | Beeps |
|---|---|---|
| C3 | Off-charge and not parked (fault) | BBBBL (4 short, 1 long) |
| C4 | Parked, charger not detected | BBBLL (3 short, 2 long) |
| C5 | Battery voltage critical (~16V) | BBLLL (2 short, 3 long) |
| C6 | Battery voltage low (<18V) | — |
| d1 | Speed pot fail (open) | — |
| d2 | Transmitter ID memory full | BLL |
| d3 | Program memory bad checksum | — |
| **d4** | **Over-current fault** (in practice: brake not releasing, see above) | CCCC (4 short) |
| d5 | Over-temperature fault | CCC (3 short) |
| d6 | Speed override on high temperature | — |
| d7 | Low voltage stop | CCCCC (5 short) |
| d8 | Unlearned remote | — |
| F1–F8 | Relay/FET faults (F2 = safety relay shorted). Any F code = board | — |

**Conflict:** Bruno's TechMate labels **d6 as over-current**. The manual's
table says **d4**. The manual wins. TechMate's d5 (over-temperature) and
d7 (low voltage) match.

**Quiet mode (ILS-01446):** a CRE-2110 or SRE-2010 that makes no
diagnostic sound may be in **Mode 3** (DIP 1 on, DIP 2 off). Single-user
mode on the Elite is DIP 1 and 2; on the Elan it's a jumper on the two
right-hand pins ([[ILS - Stairlift Diagnostic Mode and Charger LED Sheets]]).
The **2026 Elite install manuals** give the full 4-gang table: multi-user
= 1 OFF/2 OFF, **single-user = 2 ON only**, quiet = 1 ON only, **battery
warnings only = both ON**, and #3 ON = right-hand ([[SRE-2010 Install Manual]]).
That table wins over the ambiguous ILS wording. The **SRE-5000** uses DIP
1 = single-user and DIP 2 = right-hand.

**More beeps** (from the 2020 code-translations tech tip):
- **1 short beep every 3 s** = seat safety switch open (seat not in the
  riding position).
- **1 beep each time the rocker or a remote is pressed** = the up or down
  limit circuit is open.
- **1 short, 2 long** = transmitter memory full (d2 in the table).

The tip also lists **L7** (unit is or was recently running), which isn't
in the manual's table, and calls **L8** "carriage at the end of the rail"
where the manual says "soft stop". Same thing in practice.

Bruno's newer **SRE-5000** has its own scheme: a green and a red LED plus
chirp/beep/long tones (C-L, C-C-L, B-B-L-L…). The full Rev 7 table (25
codes) is on [[SRE-5000 Tech Support Guide]]. Symptom flow is on
[[Stairlift-Troubleshooting]].

## Legacy Electra-Ride beep codes (SRE-1550, SRE-2000, SRE-2750, CRE-2100)

The 2007–2011 manuals use a 4-gang DIP switch: #1/#2 set the mode
(multi-user, single-user, quiet, battery warnings only), #3 sets the
hand, and **#4 sets the coast delay** (600 ms, or 900 ms ON for remote
dropouts). Codes:

| Beeps | Meaning |
|---|---|
| Chirp | Power-up, or a safety device activated |
| Chirp every 3 s | Seat safety open (multi-user) |
| **4 short + 1 long**, every 3 min | Stopped off the charge bumper |
| **3 short + 2 long**, every 4 min | Battery voltage drop |
| **2 short + 3 long**, every minute | Battery critical (under 16 V) |
| 3 beeps / pause (SRE-2000); 2 beeps / pause / 5 (SRE-2750, SRE-1550) | Switch held at power-up |
| 1 short + 2 long | Transmitter memory full |

Sources: [[SRE-2000 Installation Manual (2007)]], [[SRE-2750 Installation Manual (2011)]],
[[SRE-1550 Installation Manual (2009)]], [[CRE-2100 Installation Manual (2009)]].

## General "unit does not operate" checklist

Before diving into codes: check circuit breaker (foreign-object jam or
overload are the two most common trip causes), battery voltage (16-28VDC
normal range, D7 below that), footrest safety switches (sliding tray must
move freely), and seat swivel position (unit won't run unless the seat
faces the open side of the stairs — this is correct behavior, not a fault).

## See also

[[SRE-2010]], [[SRE-3000]], [[CRE-2110]], [[Overspeed-Safety-Brake]],
[[Stairlift-Troubleshooting]], [[TechMate Stairlift Troubleshooter]],
[[Tech Tip - Stairlift Code Translations]], [[Troubleshooting]]
