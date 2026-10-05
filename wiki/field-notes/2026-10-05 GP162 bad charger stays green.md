---
type: field-note
manufacturer: Golden
model: GP162
date: 2026-10-05
status: resolved
tags: [golden, gp162, literider-envy, power-wheelchair, charger, batteries, charging, field-note]
---

# 2026-10-05 — GP162: won't hold a charge (charger light green the whole time)

**Status: resolved. The charger was bad.** PMS field experience on a
[[GP162-LiteRider-Envy]].

> **Key takeaways (per the human):**
> 1. **When the service call is "batteries not charging," check the
>    charger.**

## Unit

- Golden [[GP162-LiteRider-Envy]] power chair, serial **PCT24J0289**.
  Controller (LiNX or PG VR2) not recorded.
- Batteries: **new**, 2 × MK **ES17-12** (18 Ah per
  [[Battery Price Sheets (MK, Interstate)]]). That matches the PTC
  service guide's 18 Ah. The LiNX owner's manual lists 22 Ah.

## Symptom

- **Won't hold a charge**, even with new batteries.
- **Original charger's light is green the whole time**, from the moment
  it's plugged in. It never shows a "charging" state. On Golden's
  documented chargers, green means full: the HP8204B shows red + yellow
  while charging, and the MRC24-4LX shows red only
  ([[Golden-Battery-Charging]]).

## Checked

1. **Original charger output, unplugged from the chair: 28 V**, rated
   **3 A**. Those are normal numbers for a 24 V charger, so they didn't
   rule it out.
2. **Charger LED**: green the whole time while connected, never
   charging.
3. **Charger swap**: a known-good charger from another unit **showed
   charging** on this chair. That rules out the chair's charge path
   (port, breaker, fuse, harness) and points to the original charger.

## Root cause

**Bad original charger.** It put out normal voltage with nothing
connected, but never charged the batteries and showed green the whole
time. The new batteries were running on the charge they shipped with and
were never refilled, so they looked like they "wouldn't hold a charge."

## Fix

**Charger replaced.** The chair charges normally.

## Parts used

- Replacement 24 V off-board charger (XLR). Model and part number not
  recorded.

## Takeaways

- **Most important (see the callout at the top): when the call is
  "batteries not charging," check the charger.**
- **Charger green the whole time, even on batteries that were just
  driven down = the charger isn't charging.** Swap in a known-good
  charger to confirm. It's the fastest test.
- **A normal no-load voltage doesn't prove a charger works.** This one
  read 28 V at the plug and still never charged. Compare
  [[2026-10-01 P440 batteries no lift]], where the green light and a
  good voltage reading came from a working charger and the batteries
  were bad.
- **New batteries that "won't hold a charge" may never have been
  charged.**
- After a bad charger, give the batteries the **12-hour first charge**
  ([[LiteRider Envy LiNX Owners Manual (GP162)]]). Then check 12–14 V
  per battery and about 24 V or more at the joystick charger port while
  driving ([[LiteRider PTC Service Guide (GP162, PG VR2 Controller)]],
  PDF pp. 5 and 12).
- The charger is covered for 13 months under
  [[Golden-Wheelchair-Warranty]] (electronic assemblies), if the chair
  is still in warranty.

## See also

- [[GP162-LiteRider-Envy]]
- [[Golden-Battery-Charging]], [[Mobility-Batteries]]
- [[LiteRider PTC Service Guide (GP162, PG VR2 Controller)]]: Scenario 2
  "Batteries will not charge", PDF p. 11
  (`MANUALS/Golden/GP162 LiteRider PTC Golden SG 05.16.2014.pdf`)
- [[LiteRider Envy LiNX Owners Manual (GP162)]]: battery charging, PDF
  pp. 28–29
  (`MANUALS/Golden/GP162 LiteRider Envy LiNX Golden OM 10.09.2019.pdf`)
- [[2026-10-01 P440 batteries no lift]]
