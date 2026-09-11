---
type: concept
tags: [safety, stairlift, ceiling-lift, overspeed, bruno, prism]
---

# Overspeed Safety Governor

A centrifugal-force mechanical safety brake that stops a lift carriage if
its speed becomes excessive, preventing free-fall/runaway — independent of
the primary drive/control electronics. Documented so far on two
manufacturers' products with different reset behavior:

- **Bruno** straight-rail stairlifts (confirmed on [[SRE-2010]],
  [[SRE-3000]], [[SRE-3050]] — same mechanism, same documentation reused
  near-verbatim across all three models' tech support/install guides) —
  **field-resettable**, see below.
- **Prism** [[C-450-C-625]] ceiling lift (see
  [[C-450 C-625 Technical Manual]]) — described as "universal, failsafe,"
  triggered when a worn motor output shaft/worm wheel causes abnormal
  acceleration. Unlike Bruno's version, the Prism manual gives no field
  reset procedure — recovery is **motor replacement**.

The rest of this page documents the Bruno reset/testing procedure; no
equivalent step-by-step exists yet for the Prism mechanism beyond "replace
the motor."

## How it works (Bruno)

- When tripped, a notched wheel inside the overspeed housing moves off
  center (out of its "valley" position) and a switch prevents the unit
  from operating until reset.
- The switch **must be manually reset** before the carriage will move
  again.

## Reset procedure (common across SRE-2010/3000/3050)

1. Remove the access cap on the motor side of the carriage (and, on
   SRE-3050/newer carriages, a right-hand safety panel held by 2 Phillips
   screws).
2. Rotate the overspeed cover back to its normal (not-tripped) position,
   or:
3. If it won't rotate by hand, use a 1/4" socket tool or Bruno's manual
   back-up tool (kit SRV-3000-002) on the motor shaft extension to move
   the carriage upward — **clockwise for left-hand installs,
   counterclockwise for right-hand installs**.
4. Check for drive-system damage before resuming normal operation; if
   undamaged, run the carriage off the rail with the rocker switch for a
   fuller inspection.
5. If the switch won't reset: remove front covers, seat, footrest, and
   drive cover; center the switch roller in the cam valley by turning the
   cam ring; inspect/repair the drive system and carriage, or return for
   factory service.

## Regulatory testing

Separate from a field reset — used for compliance inspection. Requires an
"overspeed trip key" (Bruno kit, e.g. SRV-3000-002) inserted into the
flange cover slot to intentionally trip the switch under a loaded carriage
run, confirming the governor actually engages under load.

## See also

[[SRE-2010]], [[SRE-3000]], [[SRE-3050]], [[Bruno]], [[C-450-C-625]],
[[Prism]]
