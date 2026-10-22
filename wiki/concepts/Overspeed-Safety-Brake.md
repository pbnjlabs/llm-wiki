---
type: concept
tags: [safety, stairlift, ceiling-lift, vpl, platform-lift, overspeed, bruno, prism, harmar]
---

# Overspeed Safety Governor

A safety mechanism that halts a lift if its speed becomes excessive,
preventing free-fall/runaway — independent of the primary drive/control
electronics. Documented so far across three manufacturers and **five
distinct mechanisms** (Harmar alone uses three different ones on three
different product lines):

- **Bruno** straight-rail stairlifts (confirmed on [[SRE-2010]],
  [[SRE-3000]], [[SRE-3050]] — same mechanism, same documentation reused
  near-verbatim across all three models' tech support/install guides) —
  a **centrifugal** governor, **field-resettable**, see below.
- **Prism** [[C-450-C-625]] ceiling lift (see
  [[C-450 C-625 Technical Manual]]) — described as "universal, failsafe,"
  triggered when a worn motor output shaft/worm wheel causes abnormal
  acceleration. Unlike Bruno's version, the Prism manual gives no field
  reset procedure — recovery is **motor replacement**.
- **Harmar** [[HighlanderII]] VPL — not a centrifugal governor but an
  **Over-Speed Governor (OSG) switch** mounted at the bottom of the ACME
  drive screw, sharing a normally-closed circuit with the pit switch.
  Tripped by "a failure causing drive screw overspeed"; the install
  manual documents it only as a bench/functional test step (manually
  depress the OSG switch, verify travel is prevented and status LEDs go
  solid red) — no field reset or recovery procedure is given beyond
  "Service is required" when the shared pit/OSG circuit shows open. See
  [[HighlanderII]] for the full status-code context. **Confirmed standard
  equipment**, not optional, per its Highlander II order form.
- **Harmar** [[Helix]] curved stairlift — a *third* mechanism again,
  distinct from Harmar's own OSG switch on the VPL: a **mechanical
  jammer**, not a governor at all. Moving a release arm drops a jammer
  block between the gear rack and the drive sprocket, and a limit switch
  cuts power at the same time. **Field-resettable** — push the jammer
  back into its normal position and reset the release (see
  [[Helix Install Manual]] for the illustrated procedure). A shipping
  bolt holds the mechanism inert until removed during install; the
  install checklist explicitly verifies its removal. Confirmed standard
  equipment on both commercial and residential Helix units (ASME
  18.1-2017 compliant) per its order form — see
  [[Harmar Evaluation and Order Forms]]. Wiring schematics complicate this
  picture: a 2014 ("Helix III") schematic labels the assembly a
  "Parachute Centrifugal Brake" while a 2021 schematic calls it an
  "Overspeed Safety Switch"/"OSG" — possibly a centrifugally-triggered
  jammer (trigger like Bruno's governor, stopping action like the jammer
  above) rather than a pure switch, and/or a naming change over time; not
  reconciled. See [[Harmar Wiring Schematics]].
- **Harmar** [[Pinnacle-SL300]] / [[Pinnacle-SL600]] straight-rail
  stairlifts — an **integrated mechanical pawl brake**, standard: at high
  rpm a pawl springs open and catches a housing bolt, stopping the
  chassis **within ½ revolution** once descent passes **70 ft/min**.
  Works without power. Source is a dealer sheet ([[Harmar Product Insights (2021-2023)]]); no reset
  procedure is given there.

The rest of this page documents the Bruno reset/testing procedure in
detail; the Prism, HighlanderII-OSG, and Helix-jammer mechanisms are
summarized above only as fully as their respective manuals document them.

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

**SRE-3000 on the rail** (tech tip): take the safety flap cover off (two
screws, key side), push the overspeed fully right then fully left, then
with the power on bring it back so the switch roller sits in the centre
of the valley. A click and the power-up beep mean it's reset
([[Tech Tip - SRE-3000 Overspeed Reset on the Rail]]).

**Legacy manuals (2007–2009):** the [[SRE-2000]] and [[CRE-2100]] use a
**two-lever reset**:
1. Rotate the overspeed switch lever while pushing the wires in (too far
   and it won't reset).
2. Turn the cam lever just until it engages.

On the commercial [[SRE-1550]], align the white marks on the cam and
housing before fitting the carriage. Rotate the cam back to its detent
after a service trip; **a real trip means pulling the drive and returning
it**. The 2019 [[SRE-3000]] manual uses the ¼ in socket reset (CW for LH,
CCW for RH).

**Older Bruno models** (test-fixture tip): CRE-2100, CRE-2110 and SRE-2000
reset by rotating the cam and repositioning the activating pin;
SRE-1540/1550 by moving the carriage up with the large gearbox pulley and
resetting the cam under the carriage.

## Regulatory testing

Separate from a field reset — used for compliance inspection. Requires an
"overspeed trip key" (Bruno kit, e.g. SRV-3000-002) inserted into the
flange cover slot to intentionally trip the switch under a loaded carriage
run, confirming the governor actually engages under load. (Kit
SRV-3000-002 holds both the overspeed key and the manual back-up tool,
per the SRE-3000 manual.)

**Current method (ILS-01446 Rev 4, 2026):**
- **SRE-2010C/EC/EOS/OS, SRE-3000, SRE-3050, SRE-5000:** seat, footrest,
  drive cover and safety panels off (seat and footrest back on), run down
  on the remote and push the **overspeed trip key** into the flange cover
  slot. Replacement key **SRE-20770**. Reset, reassemble, retest.
- **CRE-2110C/OS, wheel-driven overspeed:** while running down, press the
  reset arm with a ruler.
- **CRE-2110C/EC/EOS/OS, gear-driven overspeed:** on a straight section,
  a **magnet retriever** (1.5 lb pull minimum, 5/16 in head max) in the
  manual trip pocket while running down; trips within inches. Reset:
  breaker off, 8 mm ratchet counter-clockwise on the motor hex shaft,
  rotate the OS trip plate to neutral (groove in line with the hole).
  The 2026 CRE-2110 and CRE-2110E install manuals give the same reset
  and drop the 2018 manual's two-lever procedure
  ([[CRE-2110 Install Manual (2026)]]).
- **SRE-2010EC/EOS (2026 outdoor manual):** turn the gear motor
  **clockwise with a 5/16 in socket** to move up, and the switch
  self-resets. If it doesn't, slide off the overspeed cover and center
  the roller in the cam valley ([[SRE-2010E Install Manual]]).
- **SRE-5000:** right-hand safety panel and motor-side cap off; rotate
  the cover until the wheel sits in the notch; if it's stuck, ¼ in socket
  or SRV-3000-002, CW for LH and CCW for RH ([[SRE-5000 Tech Support Guide]]).
- Intervals: yearly test (A18.1 10.3.1), and every **5 years** with a
  **dated metal tag** on the safety carrier plus a **125% rated load brake
  test** (10.3.3).
- A replacement CRE overspeed assembly (SRV-2110-022L/R) comes with a
  factory **Overspeed Certificate CRE-01176**: keep it for inspectors
  ([[ILS - CRE-2110 Drive and Overspeed Sheets]]).

Source: [[ILS-01446 Maintenance Control Plan for CRE-SRE Chair Lifts]].
Older sheets: [[ILS - Stairlift Overspeed Test Sheets]] (96 V fixture
lead chart, SRE-2010C slotted flange cover and N/O-to-N/C reset).

Bruno's tech tips add three other test methods, for other models. All
of them: lift **unoccupied**, stairs blocked, nobody on the down side,
state/local load and witness rules followed, test weights strapped down
(not with the seat belt) about **20% on the footrest, 80% on the seat**.

| Model | Method | Pass |
|---|---|---|
| **SRE-2010C** | Kit **SRV-2010-018** drop test: spur gear pulled, carriage hung on a quick-release belt from a test end cap, released to free-fall. Spur gear refitted hot (360 °F induction heater) | Stops within **1.5 in (38 mm)**; date written on the spur gear |
| **SRE-1550** | **Duct tape**: tape on the overspeed up to its mark, run down ¾–1½ in, yank the tape tail | Trips and cuts all power |
| **SRE-1550 / SRE-2000** | **Test fixture** FIX-00381–385 drives the motor at over 96 VDC downhill | Trips and stops abruptly |

Sources: [[Tech Tip - SRE-2010C Overspeed Test (SRV-2010-018)]],
[[Tech Tip - Legacy SRE-1540, SRE-1550 and SRE-2000]]. Trip range for the
old CRE-2100 (hand-written on its spec sheet): carriage **46–72 ft/min**
([[CRE-2100]]).

## See also

[[SRE-2010]], [[SRE-3000]], [[SRE-3050]], [[CRE-2100]], [[Stairlift-Maintenance]], [[Bruno]], [[C-450-C-625]],
[[Prism]], [[HighlanderII]], [[Helix]], [[Harmar]]
