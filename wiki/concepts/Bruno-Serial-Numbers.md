---
type: concept
tags: [bruno, serial-number, stairlift, vpl, vehicle-lift]
---

# Bruno Serial Numbers

How to read a Bruno serial number, and where to find it on a stairlift.
From Bruno's dealer-portal tech tips: [[Tech Tip - How to Decode a Bruno Serial Number]]
(2014) and [[Tech Tip - SRE-3000 Serial Numbers and Carriage Decals]].
TechMate also starts every session with the serial number
([[TechMate Stairlift Troubleshooter]], [[TechMate VPL Troubleshooter]]).

## Layout: YY MM PP M SSSS

Example **12 01 03 2 0123**:

| Digits | Meaning | Example |
|---|---|---|
| YY | Year built | 12 = 2012 |
| MM | Month built | 01 = January |
| PP | Product group | 03 (see below) |
| M | Model group (used from 2012) | 2 (see below) |
| SSSS | Unit number in that month's production for that line | 0123 = the 123rd |

**Product groups (PP):** 01 lift, 02 scooter/power chair, 03
elevator/VPL, 04 part order (line), 05 part order (service stock), 06
**ASL-700 Chariot** (also has its own **VIN**; see [[ASL-700]]).

**Model groups (M):** 0 general, 2 **SRE-2010 Elite** (from date code
1202), 3 **SRE-3000 Elan** (1202), 4 **CRE** (about 1308), 5 **VPL**
(1307), 9 scooters built for Bruno outside the USA (Taiwan).

Bruno's own example pairs product group 03 with model group 2 (Elite), so
don't read too much into the product group on stairlifts. The year,
month and model digits are the useful part.

**Checked against a real unit:** the 2020 VPL-3100B in
[[2026-10-14 VPL-3100B squealing and jamming on rotted fascia]] has
serial **20060350524**: 2020, June, group 03 (VPL), model 5 (VPL), unit
0524. It fits.

## Stairlift component date codes

Seats, footrests and folding rails carry a **month/year + code** label
instead of a serial number (e.g. **01/13 S1** = standard SRE-2010 seat
built January 2013):

| Code | Part |
|---|---|
| S1 / S2 | Standard seat / power seat |
| F1 / F2 | Manual / power footrest |
| R1 / R2 | Manual / power folding rail |

The skin pack carries an employee ID and a date code.

## Where the serial is on an SRE-3000 (Elan)

- On the **carriage**: back of the battery housing, on the motor, and on
  the board mounting panel.
- A loose decal with the serial and date of manufacture is **zip-tied to
  the carriage circuit breaker**. The installer sticks it in the window
  of the **data plate under the seat** (the seat isn't tied to one
  carriage).
- The **product registration sheet** is in the carriage carton. Only the
  carriage box carries the serial.

PMS photographs the serial number at every porch lift install
([[VPL-Installation]]) and identifies field-note units by model and serial
only (no customer details).

## See also

[[Bruno]], [[SRE-3000]], [[Stairlift-Troubleshooting]], [[VPL-Troubleshooting]]
