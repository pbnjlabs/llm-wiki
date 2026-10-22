---
type: field-note
manufacturer: Golden
model: GC440
date: 2026-10-22
status: open
tags: [golden, gc440, companion, scooter, flash-code-8, motor-harness, connector, burnt, field-note]
---

# 2026-10-22 — GC440: powers up, 8 beeps, won't move (burnt motor connector)

**Status: open.** PMS field experience on a Golden
[[GC240-340-440-540-Companion]] (GC440).

> **Key takeaways (per the human):** *(to be added)*

## Unit

- Golden **GC440 Companion** scooter, serial **QCA15N0466**.
- **The serial label under the floor mat was rubbed off.** The tech
  flipped the scooter over to read the serial on the **bottom of the
  frame**.
- Year not confirmed. If "15" is a year code it's a **pre-2024 GC440**
  (Dynamics DR90-A01 controller, pre-2024 parts list), but that's
  unconfirmed.

## Symptom

- **Intermittent.** Key on: the scooter has power, then **beeps 8 times
  and won't drive**.
- On the Companion's Dynamics R-Series controller, **8 = motor voltage
  fault (open circuit)** ([[Flash-Beep-Diagnostics]]). Golden's service
  guide: "an internal problem with the motor or its wiring."

## Checked

1. Found the **first connector from the motor burnt and melting**. That
   is most likely the motor/brake plug **12a** where it meets the **rear
   intermediate motor harness (10b)**, on the right side of the rear
   frame.

## Root cause

*(Pending.)* A burnt, melting connector on the motor circuit matches a
**high-resistance (loose, corroded or poorly seated) contact** that
heated under drive current and now opens intermittently: code 8.

## Fix

*(Pending.)*

## Parts used

*(Pending.)* Likely candidates, from the Companion parts breakdown
([[Companion Illustrated Parts Breakdown 2021 (GC240, GC340, GC440)]]):

| Part | What |
|---|---|
| **SE06E604** | Harness, motor **rear** intermediate (240/340/440) |
| **SE06E606** | Harness, motor **front** intermediate (240/340/440) |
| MBX-CMBAR-2 | Motor/brake assembly (2013 service guide part number), if the motor-side plug or wiring is damaged |

Confirm against the scooter's year, since there is a pre-2024 and a
2024+ parts list.

## Takeaways

*(Key takeaways per the human go first.)*

Golden's **Flash Code #8 tree** ([[Companion Service Guide (GC240, GC340, GC440)]], p. 18):
1. **Seat and rear shroud off**, tiller down, scooter on its side,
   controller cover off.
2. **Unplug the front intermediate motor harness (11c/11d) at the
   controller and measure across it.** 50 Ω or less (as low as 0.2 Ω)
   but not shorted means the motor circuit is good: **replace the
   controller.** Out of range: keep going.
3. **Unplug the motor (12a) from the rear intermediate harness (10b)**
   and check continuity 11c/11d → 10b. 10 Ω or less: go to step 6.
   Open: continue.
4. Batteries out, **split the frame**. **Inspect the intermediate harness
   connectors for discoloration or corrosion, and replace any that are
   discolored or corroded.** The printed wording of this step is inverted
   ("No? Replace").
5. **"Quarter test":** slide a quarter into the + and − contacts of the
   front intermediate harness connector. If they don't grip it firmly,
   replace the front harness. Then check continuity of both harnesses
   (10 Ω or less).
6. Check the **12a** pins, then measure **pin 1 (thick red) to pin 2
   (thick black)**. 50 Ω or less (not shorted): replace the controller.
   Out of range: pull the **motor brushes** (broken springs, cracked
   carbon, discolored wire or contacts mean new brushes). Brushes fine:
   **replace the motor/brake assembly.**

**For a burnt connector:** replace the harness (or both halves of the
plug) rather than re-terminating just one side. Check the mating pins
on the motor side too. A melted plug can leave a scorched pin that
burns the new one.

## See also

[[GC240-340-440-540-Companion]], [[Flash-Beep-Diagnostics]],
[[Companion Service Guide (GC240, GC340, GC440)]], [[Golden]]
