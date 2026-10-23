---
type: source
manufacturer: Harmar
doc_type: Training Video
source: "MANUALS/Harmar/Videos/Harmar-#32 The Electronic Components of the Residential Vertical Platform Lift.mp4"
transcript: "MANUALS/Harmar/Videos/_work/32-the-electronic-components-of-the-residential-vertical-platform-lift/transcript.txt"
tags: [harmar, vpl, rpl, platform-lift, electrical, controller, video]
---

# Video: Electronic Components of the Residential VPL (RPL)

Harmar training video #32, 1:36, by a Harmar Technical Services tech.
A tour of the controller box on Harmar's **RPL** (residential platform
lift), the generation before the [[HighlanderII]]. Harmar's 2021 VPL
product insight calls the RPL and CPL its older platform lifts
([[Harmar Product Insights (2021-2023)]]). **No RPL manual is on file.**
No date.

## Controller layout (left to right)

| Time | Part | What it does |
|---|---|---|
| 0:10 | **Up relay**, **down relay**, **safety relay** | Motor direction and the safety cut-out |
| 0:17 | **Bridge rectifier** | AC to DC for the **90 V DC motor** |
| 0:30 | **Transformer** | **110 V AC to 24 V AC** for the limit switches and the top-landing gate interlock |
| 0:45 | **Incoming power / terminal strip** | Where the transformer feeds the limits and interlock |
| 0:57 | **15 A resettable breaker** | High voltage (motor side) |
| 0:57 | **3 A resettable breaker** | Low voltage (24 V control side) |
| 1:11 | Plugs, left to right | **Top call/send, bottom call/send, travel cable, safety pan** (jumper fitted when shipped; see [[Video - How to Wire a Safety Pan on a VPL]]), **top landing gate, limit switches** |

## Use

Useful for a no-run RPL: check both resettable breakers first, then the
24 V transformer output (a dead transformer kills every limit and the
interlock), then the relays. The Highlander II has a different board;
use its own manual for that ([[HighlanderII]], [[VPL-Troubleshooting]]).

## Feeds into
[[VPL-Troubleshooting]], [[Circuit-Breakers-and-Fuses]], [[Harmar]]
