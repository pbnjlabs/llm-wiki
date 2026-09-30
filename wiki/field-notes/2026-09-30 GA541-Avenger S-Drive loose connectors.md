---
type: field-note
manufacturer: Golden
model: GA541
date: 2026-09-30
status: resolved
tags: [golden, ga541, avenger, s-drive, pg-drives, connectors, intermittent, power-loss, field-note]
---

# 2026-09-30 — GA541 Avenger: loses power over bumps (S-Drive connectors)

**Status: resolved (known issue and fix).** This isn't a single job. It's
PMS field experience with the Avenger's **PG S-Drive** controller,
recorded so techs recognize it. The manuals don't cover it.

## Unit

- Golden [[GA541-Avenger]], any unit with the **PG Drives S-Drive**
  controller ([[PG Drives S-Drive Brochure]]).

## Symptom

**The scooter loses power when it goes over bumps**, then may come back.
It's intermittent, so it may not show up on a bench test.

## Checked

- **Look for strained wires** leading into the S-Drive connectors: wires
  pulled tight, bent hard at the connector, or tugging on it.
- Check that each connector is fully seated.

## Root cause

**The design flaw is the strain on the wires going into the S-Drive
connectors.** The wiring is routed so it pulls on the connectors, and
**that strain can't be relieved**; it's built into the design (PMS field
experience). Over time the pull works the connectors loose, and a
partly unseated connector loses contact when the scooter jolts over a
bump, so the scooter cuts out.

PG's own guide lists **poor battery connections** as a cause of
intermittent trips and says to check all connections to the motor,
brakes, batteries and controller before blaming the controller
([[PG-Drives-Trip-Codes]]).

## Fix

1. **Unplug and reseat the S-Drive connectors.**
2. Test drive over bumps to confirm the power stays on.

**The strain on the wires can't be relieved**, so reseating is the fix,
and **the problem can come back**. Tell the customer it may recur and to
call if the scooter starts cutting out again.

Because PG controllers have **no serviceable parts**, don't open the
S-Drive. If reseating doesn't fix it, follow [[PG-Drives-Trip-Codes]]
before replacing the controller.

## Parts used

None (reseat only).

## Takeaways

- **Avenger cutting out over bumps: check and reseat the S-Drive
  connectors first**, and look for strained wires leading into them.
- It's intermittent, so a scooter that works in the shop may still have
  the problem. Reproduce it by driving over bumps.
- **Don't try to reroute or relieve the wiring**; the strain is part of
  the design and can't be fixed. Expect repeat visits.

## See also

- [[GA541-Avenger]]
- [[PG Drives S-Drive Brochure]]
- [[PG-Drives-Trip-Codes]]
- [[TruCharge-Diagnostics]]
