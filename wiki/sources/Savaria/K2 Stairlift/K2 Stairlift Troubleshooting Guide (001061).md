---
type: source
manufacturer: Savaria
model: K2
doc_type: Troubleshooting Guide
source: "MANUALS/Savaria/K2 Stairlift/K2 troubleshooting guide 001061_05-m11-2021.pdf"
date: 2021-11-05
tags: [savaria, k2, stairlift, troubleshooting, charging, dip-switches]
---

# K2 Stairlift Troubleshooting Guide (001061)

20-page Savaria guide (P/N 001061, 2021-11-05) for the K2's safety, control
and charging circuits, using the three carriage LEDs, a jumper set and a
multimeter. Separate tables for RH and LH units (same content).

## Covers

- **Tools:** jumper cable kit **C6290223** (6-pin OSG/final-limit jumper,
  4-pin footrest side jumper, 2-pin footrest underpan jumper), harness with
  rocker switch, multimeter, two alligator leads. Genuine Savaria parts only.
- **Charging voltage:** charger green light; **+33 V DC** between the
  rack-side and non-rack-side copper strips; 33 V at the charger leads off
  the board; batteries **24–27 V** (lower if run down), and rising when the
  supply is reconnected.
- **Charging current:** about **1–1.2 A** five seconds after power-up,
  falling to 0.9 then 0.8 A and to about **0.4 A** near full charge.
- **Won't run from the seat buttons:** safety circuit broken (power, safety
  circuit, **overspeed governor tripped**, final limits, seat swivel switch);
  obstruction in both run circuits (check footrest, safety pan and
  obstruction switches by position on the rail); obstruction in one
  direction (normal at that landing).
- **Runs one way only, or runs then stops:** obstruction in that circuit;
  check the seat direction switch wiring (**down terminal 15, up terminal
  17**); for hall calls move closer and replace the battery.
- **Remotes don't work:** hold Program Remote near pin 17 until the orange
  LED lights, press up or down until it goes out.
- **No power (no board LEDs):** main switch on top of the carriage, two
  batteries in series, **24 V (12 V each)** off the unit, battery leads tight.
- **Remotes reversed:** DIP 1. **Doesn't slow at landings:** DIP 4 ON.
  **Slow on bus line/charging strips:** DIP 4 OFF. **Slow when not
  charging:** low batteries. Turn off, wait 10 s, change the switch, power
  on.
- Seat post leaning or footrest not level: see the install guide.
- LED meanings, board layout, DIP table and wiring diagram, as in the
  install guide.

## Feeds

[[K2]], [[Stairlift-Troubleshooting]], [[Savaria]]
