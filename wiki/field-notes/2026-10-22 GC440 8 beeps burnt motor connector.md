---
type: field-note
manufacturer: Golden
model: GC440
date: 2026-10-22
status: resolved
tags: [golden, gc440, companion, scooter, flash-code-8, motor-harness, connector, burnt, field-note]
---

# 2026-10-22 — GC440: powers up, 8 beeps, won't move (burnt motor connector)

**Status: resolved (closed 2026-10-22). Not repaired: the customer
declined the quote because the cost of repair wasn't justified.** PMS field experience on a Golden
[[GC240-340-440-540-Companion]] (GC440).

> **Key takeaways (per the human):**
> 1. **Look for the serial number on the bottom of the scooter** (on the
>    frame) when the label under the mat is worn off.
> 2. **Start with the easiest troubleshooting step.** The motor connector
>    is the first and easiest thing to check. Golden's code 8 tree starts
>    at the controller in the dash, which means taking the whole tiller
>    assembly apart.

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
2. **Both halves of the connector are damaged**: the motor-side plug
   and the harness side.
3. **Quote obtained for a new motor and wiring harness.** The customer
   declined it: the cost of repair wasn't justified.

## Root cause

**Burnt, melting motor connector (both halves)** opening the motor circuit (code 8). Whether bad contact resistance or high motor current started it wasn't determined. Two ways a connector burns, and what to check to tell them
apart:
- **High resistance at the contact** (corrosion, loose or worn pins). The
  heat at the joint is **I² × R of the contact**, so even normal motor
  current cooks a bad contact. Corrosion does **not** make the motor
  draw more amps; added series resistance actually lowers the current
  slightly. It concentrates the heat in one tiny spot, which oxidizes
  the contact further and runs away until it melts.
- **High motor current** (dragging brake, binding transaxle, shorted
  windings, worn brushes or bearings, heavy loads, hills, low tires).
  Heat goes up with the **square** of current, so a healthy connector can
  overheat too. The 90 A controller (DR90-A01) limits current, and a
  sustained overload shows as **code 4** (current limit timeout).

To tell which: test the old motor per Golden's tree (resistance
pin 1–2, brushes), check the brake releases and the scooter pushes
freely in freewheel, and after the repair clamp-meter the motor current
under a normal load and a hill. A burnt, melting connector on the motor circuit matches a
**high-resistance (loose, corroded or poorly seated) contact** that
heated under drive current and now opens intermittently: code 8.

## Fix

**None. The customer declined the repair** because its cost wasn't justified. PMS quoted a new motor and wiring harness; nothing was installed.

## Parts used

None installed (repair declined). Quoted: **new motor and wiring harness** (part numbers not recorded). Both halves of the plug are burnt, and the motor-side half is the motor's own pigtail. Likely candidates, from the Companion parts breakdown
([[Companion Illustrated Parts Breakdown 2021 (GC240, GC340, GC440)]]):

| Part | What |
|---|---|
| **SE06E604** | Harness, motor **rear** intermediate (240/340/440) |
| **SE06E606** | Harness, motor **front** intermediate (240/340/440) |
| MBX-CMBAR-2 | Motor/brake assembly (2013 service guide part number), if the motor-side plug or wiring is damaged |

Confirm against the scooter's year, since there is a pre-2024 and a
2024+ parts list.

## Takeaways

**Per the human:**
1. **Serial number on the bottom of scooters.** If the label under the
   floor mat is rubbed off, flip the scooter and read the serial off the
   frame.
2. **Easiest check first.** On a code 8, **look at the motor connector
   before going into the controller**. The burnt connector was the
   first and easiest thing to check. The controller is in the dash and
   getting to it means **taking the whole tiller assembly apart**, so
   only go there once the motor-side connectors and harnesses are ruled
   out. This reverses the order of Golden's tree below, which starts at
   the controller.

**From the manual:**

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
