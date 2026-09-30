---
type: source
manufacturer: PG Drives Technology
doc_type: Tech Support Guide
source: "MANUALS/Golden/pgdt_mobility_diagnostics.pdf"
date: 2017-08-15
tags: [pg-drives, pgdt, diagnostics, trip-codes, s-drive, vr2, vsi, pilot-plus, controller, golden]
---

# PG Drives Mobility Diagnostic Guide

PG Drives Technology's **"Mobility Diagnostic Guide"** for its
controllers: **newVSI, VSI, VR2, Pilot+, S-Drive, EGIS and Solo**. 32
pages, text PDF, created 2017-08-15. Filed under Golden/General because
Golden uses PG controllers (the S-Drive on the [[GA541-Avenger]], the
VR2 on the [[GP162-LiteRider-Envy]] PTC variant). The code tables are
collected on [[PG-Drives-Trip-Codes]].

## What it covers

- **4-digit hex trip codes** as read with a **PG programmer** (e.g.
  `2C00` low battery), grouped by fault, with notes per controller
  family. "Unrecognized Error" on the programmer means its software
  needs updating.
- **Other conditions** that don't show as a trip code: won't switch on,
  drives slowly, won't drive straight, one motor or brake very warm,
  batteries discharge quickly, actuators or lights don't respond.
- **Basic tests after any repair:** general inspection, brake test,
  drive test and gradient test.
- Calibration steps for the **Omni+** sip-and-puff and analog inputs,
  and the **dual attendant joystick orientation** sequence.

## Rules repeated throughout

- **PG controllers have no serviceable parts.** A defective controller
  goes back to PG Drives Technology or a PGDT-approved service
  organization. **Opening or adjusting it voids the warranty** and is
  forbidden.
- Diagnostics should be done only by technicians with in-depth knowledge
  of PG controllers.
- Before returning a controller for an unlisted code, **check all
  connections to motors, brakes, batteries and the controller**; poor
  battery connections can cause intermittent trips.
- On dual-motor chairs, the controller can be programmed to swap left
  and right motor outputs, so a "left motor" code may mean the right
  motor.

## Feeds

- [[PG-Drives-Trip-Codes]]
- [[TruCharge-Diagnostics]]
- [[GA541-Avenger]], [[GP162-LiteRider-Envy]]
- [[Golden]]

Raw PDF: `MANUALS/Golden/pgdt_mobility_diagnostics.pdf`
