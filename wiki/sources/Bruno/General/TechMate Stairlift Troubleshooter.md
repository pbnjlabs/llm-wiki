---
type: source
manufacturer: Bruno
doc_type: Troubleshooting Tool
source: "MANUALS/Bruno/TechMate/Stairlift/"
url: https://www.brunopartner.com/
date: 2026-10-15
tags: [bruno, stairlift, troubleshooting, techmate, dealer-portal, sre-3050, sre-3000, sre-2010, cre-2110, sre-5000]
---

# TechMate Stairlift Troubleshooter

**TechMate** is Bruno's interactive troubleshooting tool for dealers. It's
on the Bruno dealer portal (brunopartner.com, dealer login, **TECHMATE**
menu) and covers stairlifts and VPLs. This page covers the **stairlift
half**. The VPL half is [[TechMate VPL Troubleshooter]].

It's a set of linked multiple-choice decision trees (built on Zingtree).
You enter a serial number, it picks the model, then it asks one question
at a time ("Does the unit run?", "Do you see 24VDC?") until it reaches a
cause and a fix, with photos and short videos along the way.

**How much weight it carries:** written by Bruno Technical Service, so
it's manufacturer guidance, above any web clipping. It has **no revision
date** and changes over time; the date above is when the wiki copy was
pulled. The SRE-5000 branches were added around May 2026 (from the photo
upload dates). Where it disagrees with a manual on file, **the manual
wins** (see Conflicts below).

## Using it

- **Serial:** enter the unit's serial. If it isn't known, Bruno says to
  enter any 11 digits (e.g. `11111111111`), then use the "continue to
  TechMate" link and pick the model by hand.
- **Models it knows:** SRE-5000, SRE-3050, SRE-3000, SRE-2010 (E, C, OS,
  EOS, G), CRE-2110 (E, C, OS, EOS, G), and "Other (older legacy models)".
- **Don't click these unless you mean it:** "Contact Bruno for
  Assistance", "My Problem Has Been Resolved", the end-of-session survey,
  and "would you like to order a part now? → Yes". They **send your
  session to Bruno** (a service case, a parts request or feedback).
- A few branches are marked **INTERNAL ONLY** or appear only for Bruno
  staff logins (e.g. CRE/SRE-2010E double remote failure, F2 code
  shortcut, broken SRE-3050 seat incident report). They're summarized
  anyway, since the steps are useful.
- UK-only branches (arm switches on Elan, Elite seat belt buckle switch,
  230VAC outlet checks) don't apply to PMS units and are left out of the
  wiki summary.

## What's in it (26 stairlift trees)

| Tree | Covers |
|---|---|
| Start | Carriage position → codes (Elite/CRE display) or beeps with no input (Elan) → rocker test → remote 1 → remote 2 → routes by which inputs work |
| Power Verification (quick + full) | No startup beep: final limit, overspeed, board fuse, in-line B− fuse, battery voltages, breaker/final limit/overspeed voltage walk, IR sensors, peripheral shorts, startup beep codes |
| Beeps Once (+ CRE version) | Single beep on command: limit circuit (red/green), key switch, footrest, shroud tabs, L2/L3, hand DIP switch, SRE-5000 terminal switches |
| Clicks Once | Relay clicks, no run: induce a beep, motor-lead voltage, motor/brushes |
| Beeps 3S / 4S | Over-temperature (board) / over-current (brake not releasing, overspeed, gearbox, breaker aux switch) |
| 5S/C4 Shallow + 5S Deep Dive | Low-voltage stop (d7, 5 short) and parked-not-charging (C4): load-drop test, battery jumper, B− harness, breaker/final limit/overspeed voltage walk |
| Charging | Charger lights (Elan and Elite chargers differ), outlet, fuses, strip/block/finger voltages, reverse polarity |
| Communication, Slow Down | P0, slowdown/mid-park problems: purple/red/black 3-pin, cleaning strips, charge block and carriage fingers, rollers |
| SSS | Seat safety switch (L1, beep every 3 s) |
| Rocker | Rocker not working: header/harness/3-pin/switch jump sequence, arm switches |
| Remote Verification, Remote (Puck Style), Remote Interference, Double Remote Failure | IR/RF remotes, phone-camera IR test, programming (d8), IR sensors, the CRE IR repeater ("puck") system, interference sources |
| Running In Both Directions | Runs but: noises, seat fold/swivel, slow (SRE-5000), broken SRE-3050 seat |
| Power Swivel, Power Footrest, Power Folding Rail, 5000 Fold Start | Power options and both power folding rail generations |
| Short Circuit (peripheral) | Blown fuse: isolate limit, key switch, rocker, charging and aux harnesses |
| SB81, Sticking paddle switch, Broken Wheel | SRE-3050 seat service bulletin 81; rocker paddle switch replacement (SRV-3050-025); broken wheel/casting (carriage replacement, safety case) |

The full steps are summarized on [[Stairlift-Troubleshooting]].

## Conflicts with the manuals

- **d6 label.** TechMate's code list says **d6 = over-current**. The
  display table in [[SRE-2010 Tech Support Guide]] says **d4 = over-current**
  (4 short beeps), d5 = over-temperature, d6 = speed override on high
  temperature. The manual wins: treat **d4** as over-current.
- **Elite/CRE brake.** TechMate's 4-short-beep tree says "replace the
  brake" for non-Elan units, but its noise tree says the Elite/CRE brake
  "cannot be replaced on its own" (replace the carriage). Unresolved; ask
  Bruno Technical Service before ordering.
- **CRE overspeed reset.** TechMate resets a tripped CRE overspeed by
  cranking counter-clockwise until the hole centers in the notch. The
  [[CRE-2110 Install Manual]] uses a two-lever reset. Follow the manual.
- **Startup beep order.** One node says the 2-short-pause-3 code's beeps
  are left rocker, right rocker, learn/erase; the power tree's 5-beep
  version reads beeps 1–2 rocker, 3 learn/erase, 4–5 remote. The manuals
  agree that long beeps mark the active switch.

Everything else checked matches the manuals: the Elan and Elite charger
LED tables, the beep list in the [[SRE-3050 Tech Support Guide]] and
[[SRE-2010 Tech Support Guide]], and the L/C/P codes on [[Diagnostic-Codes]].

## Raw files

- `MANUALS/Bruno/TechMate/Stairlift/*.md`: one readable outline per tree
  (every question, answer and where it leads, plus photo/video links).
- `MANUALS/Bruno/TechMate/json/`: the raw tree data.
- Refresh with `python3 scripts/techmate_pull.py` (read-only; it never
  submits anything to Bruno).

`MANUALS/` is per-device and not in git, so these files may not exist on
other machines.

Feeds: [[Stairlift-Troubleshooting]], [[Troubleshooting]],
[[Diagnostic-Codes]], [[SRE-3050]], [[SRE-3000]], [[SRE-2010]],
[[CRE-2110]], [[Folding-Rail]], [[Bruno]]
