---
type: concept
tags: [vpl, bruno, battery, charger, troubleshooting]
---

# Battery Charger LED Diagnostic Chart (VPL)

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

Note: the "over-temp shutdown" row appears with two different LED
combinations across the two manuals' printings (ON/OFF/OFF/FLASH in one
listing, FLASH/OFF/OFF/FLASH in another) — treat either as the same fault
class (thermal shutdown) rather than two distinct states; the remedy is
identical.

## See also

[[VPL-3100B]], [[VPL-3200B]], [[Bruno]]
