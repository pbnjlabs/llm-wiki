---
type: source
manufacturer: Pride
doc_type: Product Insert
source: "MANUALS/Pride/Scooters/1777306648732_NEW CURTIS.pdf"
date: 2022-01
tags: [pride, scooter, curtis, 1212, fault-codes, beep-codes]
---

# Curtis Scooter Fault Codes Insert (2022)

Two-page product insert (Rev A, Jan 2022) with **Curtis 1212/1212P**
scooter controller codes, from the Go Go section of the basic
operations library. Codes flash as two digits (e.g. 1,4 = one flash,
pause, four). Pulled from the PQ-365 owner's manuals / basic operations library on 2026-10-20.

| Code | Fault |
|---|---|
| 1,1 | Thermal (over 80 °C or under −10 °C; brake not releasing; overload) |
| 1,2 | Throttle (pot out of range, shorted) |
| 1,3 | Speed pot |
| 1,4 | Undervoltage: charge; check battery/controller connections |
| 1,5 | Overvoltage: unplug charger; slow down on hills |
| 2,1 | Main contactor driver off |
| 2,2 | EMR sequencing (1212P) / motor stalled (1212) |
| 2,3 | Main contactor welded or stuck open |
| 2,4 | Main contactor driver on |
| 2,5 | Pump SRO (1212P) |
| 3,1 | Wiring: HPD over 10 s, throttle misadjusted or broken |
| 3,2 | Brake on: brake driver shorted or coil open |
| 3,3 | Precharge: brake driver shorted, MOSFET |
| 3,4 | Brake off |
| 3,5 | HPD (high pedal disable): throttle not at rest at key-on |
| 4,1 | Current sense: controller or motor wiring short |
| 4,2 | Hardware failsafe: motor voltage out of range |
| 4,3 | EEPROM |
| 4,4 | Motor open (1212) |
| 4,5 | Battery disconnected or poor terminal connection |

Most need the provider; the user fixes are charge (1,4) and unplug the
charger (1,5).

Feeds: [[Pride-Controller-Flash-Codes]].
