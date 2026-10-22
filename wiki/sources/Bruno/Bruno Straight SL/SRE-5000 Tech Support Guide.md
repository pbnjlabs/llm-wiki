---
type: source
manufacturer: Bruno
model: SRE-5000
doc_type: Tech Support Guide
source: "MANUALS/Bruno/Bruno Straight SL/SRE-5000-TS Tech Support Guide 09-17-2026.pdf"
date: 2026-09-17
tags: [stairlift, bruno, sre-5000, elan, troubleshooting, diagnostics, folding-rail]
---

# SRE-5000 Tech Support Guide (SRE-5000-TS, 09-17-2026)

Bruno's field service guide for the Elan **SRE-5000**, SRE-5000G and
SRE-5000CAN (44 pages). It bundles these sheets:
- ILS-01617 specs, Rev 1 04/20/26 ([[ILS - SRE-5000 Specifications]]).
- ILS-01644 remote reprogramming, Rev 1 09/01/26.
- ILS-01653 charger LEDs.
- ILS-01512 rail mounting, Rev 1 04/30/26
  ([[ILS-01512 SRE Rail Mounting Guidance (2026)]]).
- ILS-01614, ILS-01615 (5000G, metric) and ILS-01616 (power options)
  technical drawings.

It also has the exploded views and wiring schematics for the 5000, 5000G
and 5000CAN. Bruno says the guide will grow; reload it from Brunopartner.

**Overspeed reset:**
1. Remove the **right-hand safety panel** (2 Phillips) and the access cap
   on the motor side.
2. Rotate the overspeed cover until the wheel sits in the notch.
3. If it won't rotate, turn the motor shaft extension with a ¼ in socket
   or SRV-3000-002: **CW for LH, CCW for RH**. This moves the carriage up.
4. Check the drive for damage, then drive the carriage off the rail for
   a full inspection.

**DIP switches:** **1 = single-user (ON), 2 = right-hand (ON).** Both are
OFF from the factory.

**Remotes (ILS-01644):**
- Remote DIP 1/2 gives 4 channels (default 1 up, 2 down).
- To relearn:
  1. Breaker on and wait for the beep.
  2. Hold LEARN/ERASE **10 s** to erase. Both LEDs flash 3 s.
  3. Hold LEARN/ERASE and tap a remote button aimed at the IR eye.
  4. The green LED goes solid for 3 s when it has learned.

**Troubleshooting chart:**
- **Battery voltage should be 16–28 VDC.**
- Remotes run backwards (slow up, fast down) = **right-hand install not
  set** (DIP 2).
- Erratic on the remote = swivel switch, or aim the remote better.
- Erratic on the paddle = footrest tray dragging, or debris on the rail.
- Won't stop at the bumper = limit switches.
- Chatter = wipe the rail and put a little grease on the rack only.

**PCB and gear motor matching (ECN8485).** On **19 Aug 2026** the
gearbox ratio changed and the PCB firmware changed with it:

| Carriage serial | Correct PCB (firmware) |
|---|---|
| **26080361089 or earlier** | PCB-00180 rev P3 (14787) or PCB-00194 rev 0 (14815) |
| **26080361090 or later** | PCB-00180 **rev 1** (14802) |

- **New board on an old carriage:** fast down, drops into slow mode,
  **stops suddenly going down**. Worst at **45° or more, riders over
  250 lb, or full batteries**.
- **Old board on a new carriage:** slow down travel, **relay clicking
  while parked at the top charging**, and a charger fault.
- This matches the SRV-5000-018 / SRV-5000-001 kit split on
  [[Bruno-Serial-Numbers]].

**Remotes dead but the paddle works:** the brown and blue **motor leads
are too close to the IR sensor**. Route them to the right of the PCB
connector and tuck them between the PCB bracket and the gear motor, or
run them vertically.

**Diagnostics (Rev 7, 9/4/2026).** A green and a red LED under the seat,
plus tones (C = chirp 0.25 s, B = beep 0.5 s, L = long 1.5 s, P = pause
1 s). "45 s / 4 min" means first at 45 s, then every 4 min.

| # | Code | LEDs (green / red) | Tones | Cause |
|---|---|---|---|---|
| 0 | Motor running | off / off | none | |
| 1 | Parked and charging | solid / off | none | |
| 2 | End of rail | 1 blink / off | S, M | Middle plus top or bottom terminal switch open |
| 3 | Slow-down switch | 2 / off | none | One terminal switch open |
| 4 | Seat safety open | 3 / off | C-P-P-P every 3 s (multi-user) | |
| 5, 6 | Up / down safety open | 4, 5 / off | S, M | |
| 7 | Mid-park | off / flashing | none | Top and bottom terminal switches open |
| 8 | Actuator running | solid / flashing | beep every 1 s (folding rail) | |
| 9, 10 | Upper / lower limit reached (options) | 1, 2 / flashing | none | |
| 11 | Option over-current | 3 / flashing | none | Fold rail 2 A (or 0.65 A rise in 0.1 s); footrest 0.35 A; swivel 0.675 A out / 1.1 A in |
| 12 | Aux board communication fault | 4 / flashing | none | |
| 13 | Fold actuator not running | 5 / flashing | none | |
| 14 | **Terminal switch fault** | 1 / solid | **C-L** (45 s / 4 min) | All terminal switches open |
| 15 | **Limit switch fault** | 2 / solid | **C-C-L** | Both upper and lower safeties open |
| 16 | **Over-temperature** | 3 / solid | **C-C-C** every 15 s | CPU **55 °C or more** |
| 17 | **Over-current** | 4 / solid | **C-C-C-C** | Drive above **16 A up / 4.25 A down** |
| 18 | **Low battery** | 5 / solid | **B-B-L-L** (45 s / 4 min) | **Below 19.2 V** |
| 19 | **Parked, no charger** | off / solid | **B-B-B-L-L** | No charger and below 24.5 V |
| 20 | **Final limit state** | flashing / solid | **C-C-C-L** | Middle terminal switch plus upper safety open |
| 21 | **Controller failure** | flashing / flashing | **C-C** every 15 s | Drive circuit component failure |
| 22 | **Low-voltage stop** | solid / solid | **C-C-C-C-C** | Stopped, below 19.2 V |
| 23–25 | Learn / erased / learned | flashing / off; flashing / flashing; solid / off | none | |

- **Multiple buttons held:** B-B-P, then one tone per input. The order
  is up paddle, down paddle, learn/erase, remote up, remote down, and
  **L marks the active one**. For example B-B-P-L-B-B-B-B = up paddle
  held at start-up. There are 5 tones at start-up and 3 once running.
- The install manual's "battery critical, 2 short + 3 long" is
  **superseded** by B-B-L-L here.

**Charger LED (ILS-01653):**
- None = no AC or a bad charger.
- Red = AC on.
- **Flashing red** = bad batteries (load test).
- Yellow or green = OK.
- **Flashing green** = reverse polarity; check the rail wiring.

**Power folding rail:**
- **Modes:** it ships in **continuous mode** and slows through mid-park.
  **Mid-park stop mode** stops there while the rail folds; the rider
  presses again to go on. To change modes, take the **push-pin cover**
  off the fold circuit board and set the **DIP switch** there. On the
  **remote it always stops at mid-park**, whatever the DIP setting.
- **Dead actuator, temporary use:**
  1. Remove the fold side panel (2 locking pins).
  2. With the rail up, pull the quick-connect pin and unplug the
     actuator leads at the board.
  3. Lower the rail by hand, refit the covers, and **zip-tie the arm
     down**.
- **Obstruction sensitivity:**
  1. Pry off the lift-arm end cap near the pivot.
  2. Turn the set screw with a **3 mm** key. **Clockwise = more
     sensitive.**
- **Troubleshooting:**
  - Won't fold, or stops at mid-park: check the DIP setting, clean the
    contact fingers and strips, and check the **lower switches at the
    pivot arm base**.
  - Won't lift: check carriage power and the actuator.
  - Slow: low batteries.
  - Not charging at the bottom of the fold: check the finger contact and
    the connectors.

Feeds: [[SRE-5000]], [[Stairlift-Troubleshooting]], [[Diagnostic-Codes]], [[Folding-Rail]], [[Overspeed-Safety-Brake]], [[Bruno-Serial-Numbers]], [[Rail-Mounting-Guidance]], [[Battery-Charger-LED-Diagnostics]]
