---
type: source
manufacturer: Permobil
model: Permobil ICS seating (Corpus)
doc_type: Troubleshooting Tool
source: "MANUALS/Permobil/Power Chair Electronics/ics-3x-active-error-codes-in-r-net-v7-43.pdf; MANUALS/Permobil/Power Chair Electronics/ics-quick-reference-guide.pdf"
date: 2015-12-11
tags: [permobil, ics, r-net, corpus, power-seating, actuator, error-codes]
---

# Permobil ICS Error Codes and Quick Reference

Two Permobil documents for **ICS** (Integrated Control System), the seat
actuator system on Permobil Corpus seating: the **ICS error codes shown via
R-net** (5 pp., updated 2014-11-27) and the **ICS quick reference card** (V4.10,
2015-12-11).

## Error codes

Four-hex-digit IDs; the first digits say which node, the last digit the fault:

| Node (ID) | Node |
|---|---|
| 201x | Master |
| 202x–205x | Main, second, third, fourth switchbox |
| 207x / 208x / 209x | Left leg / right leg / legs actuator |
| 20Ax / 20Bx / 20Cx / 20Dx | Tilt / back / seat lift / stand |
| 20Fx | Alternate switchbox; 210x–212x options 1–3 |

| Actuator code ending | Meaning | Remedy |
|---|---|---|
| 1 | Sensor, cable to the General Module, or GM fault | Check sensor cables and connectors (12) |
| 2 | No motor detected | Motor cable and connector (13) |
| 3 | Over current, possible overload | Find where in the stroke; hard end stop? full movement without user? replace actuator (14) |
| 4 | Pinch protection activated | Check the pinch switch, its cable; meter the switch; replace switch or GM (15) |
| 5 / 6 | Moving too slow / too fast | Position feedback (SoftPot) wiring; length shown in the software vs real; replace sensor/smart actuator (16, 17) |
| 7 | Drive electronics overheated | Heavy load for a long time; let it cool (22) |
| 8 | Internal fault (or DigPot output short) | Replace the node (18) |
| 9 | Can't communicate on the LIN bus | Replace the GM or smart actuator (19) |
| A | Node required but not present | Check connections, then replace (20) |
| D | Flash parameters updated | Restart: switch off and on (21) |

Master errors: 2011 model/UI checksum or firmware mismatch, 2012 over current
idle, 2013 internal SPI, 2014 can't write flash, 2015 can't update node
parameters, 2017 restart needed, **201D unused actuator or module on the bus**
(e.g. a special system reprogrammed with a standard config: reprogram from the
factory backup). Switchbox: 2021 button pressed at start-up (ignored, not
logged), 2029 bad checksum (replace switchbox), 202D restart.

## Quick reference card (on-board configuration)

Button combinations on the switchbox (LEDs 1–8) to set: **user weight** (2+4;
eight bands from 0–110 lb to 401–450 lb), LED indication level, switchbox layout,
other general settings (actuators blocked while driving, low backrest, tilt
adapter, pause tilt at 0°, IRM, invert buttons, leg rest linked to backrest), leg
rest angle for quarter speed, seat depth, IRM positions, K450 transportation mode
(WC19) and hook position, seat width/armrest restriction, VS standing settings
and the **VS "Take Me Down" emergency un-standing** (6+8 held ~30 s). Hold button
8 for 2 s to save. Full detail in OM ICS OnBoard Configuration (not on file).

## Feeds

[[Permobil]], [[PG-Drives-Trip-Codes]]
