---
type: source
manufacturer: Bruno
doc_type: Troubleshooting Tool
source: "MANUALS/Bruno/TechMate/VPL/"
url: https://www.brunopartner.com/
date: 2026-10-15
tags: [bruno, vpl, troubleshooting, techmate, dealer-portal, vpl-3100b, vpl-3200b]
---

# TechMate VPL Troubleshooter

The VPL half of Bruno's dealer-portal troubleshooter (brunopartner.com,
dealer login, **TECHMATE** menu). It works like the stairlift half
([[TechMate Stairlift Troubleshooter]]): enter a serial, it picks the
model group, then one multiple-choice question at a time with photos and
videos. **Same weight:** Bruno-authored, above clippings, below the
manuals. No revision date; the date above is the pull date.

The same buttons send your session to Bruno and should only be clicked
on purpose: "Contact Bruno for Assistance", "My Problem Has Been
Resolved", the survey, and "order a part now? → Yes".

## Model groups

TechMate sorts VPLs by model and serial. Older boards inside a group are
sent straight to Bruno Technical Service.

| TechMate group | Models | Wiki page | Supported serials (older = call Bruno) |
|---|---|---|---|
| Short residential **DC** | VPL-3153B, VPL-3175B | [[VPL-3100B]] | 3153B from 12070300110, 3175B from 12070300109 |
| Tall residential (DC) | VPL-3210B, 3212B, 3214B | [[VPL-3200B]] | Current board from 15070350265 (3210B) / 15070350274 (3212B) / 15070350271 (3214B). Older back to 12070300097/…112/…156 use the short residential board: "troubleshoot it like a short". Earlier = call Bruno |
| Short residential **AC** | VPL-3153, VPL-3175 (no B) | none | 3153 from 17090350001, 3175 from 17090350008 |
| Short commercial (DC) | VPL-3353B, VPL-3375B | none | 3353B from 16010350319, 3375B from 16010350324 |
| Tall commercial (DC) | VPL-3310B, 3312B, 3314B | none | all |

The AC and commercial models have no manual or model page in the wiki.

## What's in it (35 VPL trees)

| Tree | Covers |
|---|---|
| Starting Point | Charger lights → platform position → platform control up/down → call/send up/down → routes by which inputs work |
| No Response Quick | AC outlet (AC units) or charger lights (DC), E-stop, upper gate wheel, door held shut, safety pan, top cover switch |
| No Response (short res DC / tall res-comm DC / short comm DC / short res AC) | The main **voltage walk down the safety chain** at the board's screw terminals, from the batteries to the relays (or the AC board's E1–E18 lights) |
| Top Cover Switch, E-Stop/NSS, Upper Gate/Door, Platform/Lower Gate/Door, Mid Stop, Up/Down Limit, Safety Pan, Pit Switch, Emergency Lower | One tree per circuit in the chain |
| Up Call, Down Call, Bad Call | Key switch, rocker, platform control cable vs travelling cable, 8-pin corrosion |
| Response | Click, hum, repeated clicking, squeal: relay/solenoid, motor, screw and drive nuts, belts |
| Running on its own (4 versions) | Short in the call circuit or stuck relay: isolate by unplugging JP harnesses |
| Short (3 versions) | Board fuse keeps blowing: isolate the short to ground |
| Full Length, Stopping | Noise and deflection (pads, bearing block, lift nuts), intermittent stopping |
| Charging | Charger power light, outlet, charger |

Condensed into [[VPL-Troubleshooting]].

## Checked against the manuals

No conflicts found. The VPL install and operator manuals' troubleshooting
tables are short (E-stop, fuse, limits, charger LEDs); TechMate goes much
further and agrees with them. Both say to put **dielectric grease** on
connectors. TechMate's charger steps use the same LEDs as
[[Battery-Charger-LED-Diagnostics]].

Small inconsistencies inside TechMate (noted, not conflicts):
- Tall units' emergency-lowering test point: the main tree says 52–67
  (residential) or 50–67 (commercial); the emergency-lower tree checks
  51–67 for the pit switch, then 52–67 or 50–67. Treat 50/51/52 as the
  start of the chain and follow the photos in the raw outline.
- One call/send node's Yes/No answers lead the wrong way (a continuity
  "yes" goes to "no continuity"). The steps themselves are clear.

## Raw files

- `MANUALS/Bruno/TechMate/VPL/*.md`: readable outlines of all 35 trees.
- `MANUALS/Bruno/TechMate/json/`: raw tree data.
- Refresh with `python3 scripts/techmate_pull.py`.

Feeds: [[VPL-Troubleshooting]], [[Troubleshooting]], [[VPL-3100B]],
[[VPL-3200B]], [[Gate-and-Door-Interlocks]], [[Bruno]]
