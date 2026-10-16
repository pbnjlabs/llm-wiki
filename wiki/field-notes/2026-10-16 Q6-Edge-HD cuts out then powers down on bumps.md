---
type: field-note
manufacturer: Pride
model: Q6-Edge-HD
date: 2026-10-16
status: resolved
tags: [pride, quantum, q6-edge, q6-edge-hd, power-chair, q-logic-3, bus-cable, joystick-out-of-center, intermittent, power-loss, bumps, field-note]
---

# 2026-10-16 — Q6 Edge HD: cuts out, then powers down, on bumps (coiled bus cable)

**Status: resolved.**

> [!important] Key takeaways (per the human)
> - **With this symptom, check the cable connections first, before a
>   firmware update.** The update took **over an hour**; rerouting the
>   cable took **10 minutes**.
> - **Not make-specific: this can happen on any make or model.** A bus
>   cable routed wrong (here, coiled around a body panel) can cause
>   intermittent shutdowns over bumps.

A Quantum Q6 Edge HD stopped for a moment over bumps,
and later powered down completely. The error log showed repeated
**"joystick out of center"**. A firmware update didn't fix it. The cause
was a **bus cable coiled around the rear lower body panel**. Rerouting
the cable fixed it.

## Unit

- Pride / Quantum **[[Q6-Edge-HD]]**, **no iLevel**
- Serial #: **jc703824141020**
- Controller: **Q-Logic 3** (confirmed)

## Symptom

- **At first:** the chair **stopped momentarily** while driving on
  bumpy terrain, then carried on.
- **Later:** it **powered down** on bumpy terrain.
- **Joystick display:** an **X inside a red dot** at the **top left** of
  the screen, and the **battery indicator blinked as if it were
  charging**.

## Checked

1. **Error log through the Econ-M app.** The tech connected the phone to
   the chair over Bluetooth and read the log: **repeated "joystick out
   of center"** entries. (The wiki's Bluetooth page covers Econ-W and
   Econ-I; Econ-M is the phone app the tech used. See
   [[Q-Logic-3-Bluetooth-and-Remote-Programming]].)
2. **Firmware update, 1.5.35 → 2.0.16 (over an hour).** Updating
   usually clears this kind of software fault (PMS experience), but
   **this time it didn't**.
   ([[Q-Logic-Firmware-Updates]])
3. **Called Pride tech support.** They said **it could be a bad
   connection from the joystick to the power control module**.
4. **Traced the bus cables to the power module.** One **bus cable was
   coiled around the rear lower body panel**, which made the panel hard
   to remove to reach the connection at the power module.

On Q-Logic 3, "joystick out of center" is code **#35 or #36** (the
manuals number it differently; [[Q-Logic-Fault-Codes]]). The manual's
fix is "release the joystick and power-cycle", which doesn't help when
the cause is the wiring. Nearby codes do point at the cables: **#34 bus
voltage dropped** (reseat the hand control cable) and **#65 inactive
input device not centered** (check the bus cables).

## Root cause

**A bus cable coiled around the rear lower body panel** caused the
intermittent failure. Over bumps it interrupted the joystick's signal
to the power module, so the controller logged "joystick out of center"
and stopped the chair. As the problem got worse, it powered the chair
down.

**Same kind of issue as the Avenger's S-Drive flaw** (per the human):
wiring routed so the connection is under strain, and bumps break
contact. See [[2026-09-30 GA541-Avenger S-Drive loose connectors]].

## Fix

**Rerouted the bus cable** so it no longer wraps around the rear lower
body panel (**about 10 minutes**). Problem fixed.

## Parts used

None (reroute only). Firmware updated to 2.0.16.

## Takeaways

- **Key (per the human): check the cable connections first** with this
  symptom. The firmware update took **1 hour+**; rerouting the cable
  took **10 minutes**.
- **Key (per the human): not make-specific.** This can happen on any
  make or model.
- If "joystick out of center" shows up only over bumps and a firmware
  update doesn't clear it, **check the bus cable routing and the
  joystick-to-power-module connection**.
- The Econ app's **error log** shows the fault history, so it catches
  repeated faults that come and go.

## See also

- [[Power-Chair-Troubleshooting]] (§6: cuts out over bumps)
- [[Joystick-Controllers]] (Q-Logic 3 error codes)
- [[Q-Logic-Fault-Codes]]
- [[Q-Logic-Firmware-Updates]]
- [[Q-Logic-3-Bluetooth-and-Remote-Programming]]
- [[Q6 Edge Basic Troubleshooting]]
- [[2026-09-30 GA541-Avenger S-Drive loose connectors]] (same kind of issue: strained wiring at the S-Drive connectors)
- [[2026-09-25 Q6-Edge-3 iLevel no power]] (frayed joystick cable on a Q6 Edge 3)
