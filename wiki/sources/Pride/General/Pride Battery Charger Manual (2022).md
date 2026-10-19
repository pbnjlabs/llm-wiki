---
type: source
manufacturer: Pride
doc_type: Operator Manual
source: "MANUALS/Pride/General/battery-charger-manual.pdf"
date: 2022
tags: [pride, charger, battery, lithium, led, fault-codes]
---

# Pride Battery Charger Manual (compilation, 2022)

50-page compilation of the charger owner's manuals Pride ships
(document 0003780, dated 02/03/22 or 03/22). From the Basic
Troubleshooting section of the PQ-365 dealer library. Thirteen chargers:

| Charger | Use | Notes |
|---|---|---|
| UPG 24BC2000T (2 A) | SLA 7–18 Ah | Power LED red = on, green = charging; Charging LED red = fast, off = float. 29.6 V fast, 27.6 V float |
| UPG 24BC3500T-4 (3.5 A) | SLA 12–35 Ah | **AGM/GEL switch** (bulk 29.6 / 28.6 V). Red blink fault codes (below). 20 h DOE cutoff |
| UPG 24BC5000T-4 (5 A) | SLA 18–50 Ah | Same codes; LED off = no batteries (under 9 V). Full charge needs **15 h** |
| UPG 24BC8000T-4 (8 A) | SLA 24–85 Ah | Same codes; 15 h for a full charge |
| Battery Maximizer EA1065-P (2 A) | Lead-acid | Power green = AC, red = error (short, reversed); Charge red = fast, green = full. **Red over 24 h = unplug, fault** |
| Battery Maximizer EA24030-9C / EA1148B (3 / 5 A) | **Victory 10** | Same pattern as EA1065-P |
| High Power HP0060W (2 A) | **Jazzy Passport** lithium | Red = power on, battery not connected; orange = charging; green = full |
| Metco NL07C-25HT (29.2 V 2.5 A) | Go-Go Folding Scooter lithium | Pre-charge over 1 h = stops, status pulses (failed pack) |
| Intertek LS-018C20 (29.4 V 2.5 A) | Go-Go Folding Scooter lithium | Red/green alternating = overcurrent or zero-volt pre-charge; short = 16 ms red / 496 ms green; pre-charge over 5 h = pack error |
| ACI Super Power ACI245000 (5 A) | Lead-acid | Red over 24 h = fault. Max 29 V |
| 4C24080A (28.8 V 8 A) | — | Green flash = on, orange flash = pre-charge, orange = charging, green/orange = 80%, green = full, **red flash = defect** |
| HP1202L3 (36 V 2 A) | **iRIDE** lithium | Red = charging, green = full |
| UPG 24BC3500L-1 (ELE2008644) | **Go-Go Endurance / Jazzy EVO 613** lithium | 28.8 V, 8–35 Ah; same blink codes |
| UPG 24BC8000L-1 (ELE2300934) | Lithium (LFP) 16–100 Ah | Magnetic connector with its own LED; same blink codes |

**UPG red blink codes** (3.5 A, 5 A, 8 A and the lithium UPGs):

| Red LED | Fault |
|---|---|
| Continuous blinking | 12-hour charge timeout (charger too small or a bad battery) |
| 1 blink every 3 s | **Battery voltage under 14 V: charging won't start** (lithium 8 A: 9–17 V) |
| 2 blinks every 3 s | Batteries connected in reverse polarity |
| 3 blinks every 3 s | Overvoltage (charger over 30 V output) |
| 4 blinks every 3 s | Overcurrent |

The "won't start under 14 V" rule is the reason a Pride charger
won't wake batteries run down near zero ([[Power-Chair-Troubleshooting]] §2).

Feeds into: [[Battery-Charger-LED-Diagnostics]], [[Mobility-Batteries]].
