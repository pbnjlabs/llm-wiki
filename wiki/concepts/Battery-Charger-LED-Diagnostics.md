---
type: concept
tags: [vpl, bruno, pride, battery, charger, troubleshooting]
---

# Battery Charger LED Diagnostics

Charger indicator tables from the manuals: Bruno's VPL charger and
Pride's mobility chargers. Golden's chargers are on
[[Golden-Battery-Charging]] and [[TruCharge-Diagnostics]].

## Bruno VPL charger

A 4-LED (Power/red, Charge/yellow, Float/green, Fault/red) diagnostic
table for the VPL battery charger. Confirmed identical across
[[VPL-3100B]] and [[VPL-3200B]] — same table appears in both install
manuals and both operator manuals, word-for-word.

| Power (Red) | Charge (Yellow) | Float (Green) | Fault (Red) | Status | Solution |
|---|---|---|---|---|---|
| ON (2s) | ON (2s) | ON (2s) | ON (2s) | Initial power up | — |
| ON | OFF | OFF | OFF | Charger not connected to battery | Check battery connections |
| ON | OFF | OFF | ON | Output shorted, battery reversed | Properly reconnect batteries |
| ON | FLASH | OFF | OFF | Soft-start charging | — |
| ON | ON | OFF | OFF | Charger at max voltage/delivering max current | — |
| ON | ON | FLASH | OFF | Batteries close to fully charged | — |
| FLASH | OFF | OFF | OFF | Batteries connected, AC disconnected | Check AC outlet, plug in |
| ON | OFF | ON | OFF | Batteries fully charged | — |
| ON | OFF | OFF | FLASH | Batteries defective/heavily sulfated | Replace batteries |
| ON | OFF | OFF | FLASH | Internal over-temp shutdown | Unplug, disconnect battery, wait 1-2 min, reconnect; replace batteries if it won't recharge |
| FLASH | OFF | OFF | FLASH | Over-temp shutdown | Same as above |
| ON | FLASH | FLASH | FLASH | Internal charger fuse blown (VPL-3100B only lists this row) | Replace charger |

Bruno's older VPL troubleshooting guides (2010–2011) add: **all four
lights flashing** → unplug the charger from the wall and from the
batteries for about a minute, then reconnect; still flashing → replace
the charger. **Only the power light flashing** → AC lost (matches the
table). See [[Tech Tip - Low-Rise DC VPL Troubleshooting Guides (2010-2011)]].

Note: the "over-temp shutdown" row appears with two different LED
combinations across the two manuals' printings (ON/OFF/OFF/FLASH in one
listing, FLASH/OFF/OFF/FLASH in another) — treat either as the same fault
class (thermal shutdown) rather than two distinct states; the remedy is
identical.

## Pride scooter and power chair chargers

From [[Charger Indicator Codes Quick Reference (INFINFB2586)]] (Rev A,
Dec 2010). **Match the Pride part number on the charger label**: the
same color means different things on different chargers (red is "power
on" on some, "fault" on others, "charging" on the 5 A Guest). Newer
chargers may not be on this 2010 sheet.

| Charger (part no.) | Power light | Status / single light |
|---|---|---|
| 2 A off-board (old ELECHG1001; new ELECHG1007 or ELECHG1015) | Green = AC connected; red = error, short, voltage too low or blown fuse | Red = fast charging; green = full; off = disconnected, battery voltage too low or blown fuse |
| 3 A off-board (ELEASMB5713) | Green = AC connected; red = error (short, reversed leads) | Red = fast charging; green = full; off = batteries disconnected or voltage too low |
| 4 A Guest onboard (old ELE110V1029) | — | Green = full; **"extended green / no green LED" after more than 24 h = fault** (Pride's wording) |
| 4 A Battery Maximizer onboard (power chair ELECHG1018, scooter ELECHG1019) | Green = AC connected; red = error (short, reversed leads) | Red = fast charging; green = full |
| 5 A Merits (ELECHG1000) | Red = power on; off = disconnected | Yellow = charging; green = full; off = disconnected; **red = fault** |
| 5 A Battery Maximizer (ELEASMB6293) | Green = AC connected; red = error (short, reversed leads) | Red = fast charging; green = full |
| 5 A Power Cube (ELE110V1044) | Red = power on; off = disconnected | Flashing green = 80%; solid green = full |
| 5 A Guest onboard (ELE110V1037) | — | Red = charging; red and green = 80%; green = full; **"extended green / no green LED" after more than 24 h = fault** (Pride's wording) |
| 8 A Lester (ELE110V1041) | — | Red = fault; slow green blink = under 80%; fast green blink = over 80%; solid green = full |
| 8 A CTE (ELEASMB5669) | — | Green flash = power on; red flash = error; orange = charging; orange flash = under 80%; green/orange flash = 80%; green = full |

**Newer Pride chargers** ([[Pride Battery Charger Manual (2022)]],
13 chargers): **UPG** 24 V SLA chargers (2, 3.5, 5, 8 A) and UPG
lithium chargers (Go-Go Endurance / EVO 613, 8 A LFP) flash **red
blink codes**: continuous = 12 h timeout (charger too small or a bad
battery); **1 every 3 s = battery under 14 V, won't start**; 2 = reverse
polarity; 3 = overvoltage (charger over 30 V); 4 = overcurrent. Steady
red = charging, flashing green = float, steady green = done. The 3.5 A
and up have an **AGM/GEL switch**; the 5 and 8 A need **15 h** for a
full charge and cut off at 20 h. Battery Maximizer and ACI chargers:
**red over 24 h = fault**. Lithium travel chargers (Metco NL07C,
Intertek LS-018C20) stop and pulse if pre-charge runs too long (1 h /
5 h = failed pack). 4C24080A (8 A): red flash = defect, orange =
charging, green/orange = 80%.

**Testing a Pride charger** (Pride's 2004
[[Technical Troubleshooting Guide - Battery Guide (2004)|Battery Guide]]):
plug the charger into the wall, unplug its **3-pin DC harness**, and
read the **two outside pins** on the charger side: **25–30 VDC** = the
charger is putting out. The other half of the connector should show
battery voltage. A charger can still show "full" and never charge
([[2026-10-05 GP162 bad charger stays green]], a Golden unit). Pride
chargers won't start on batteries near 0 V
([[Power-Chair-Troubleshooting]]).

## See also

[[VPL-3100B]], [[VPL-3200B]], [[Bruno]], [[VPL-Troubleshooting]],
[[Mobility-Batteries]], [[Power-Chair-Troubleshooting]],
[[Golden-Battery-Charging]], [[Pride]]
