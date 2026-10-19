---
type: model
manufacturer: Pride
model: Q6-Edge-3-Stretto
tags: [pride, wheelchair, mid-wheel-drive]
---

# Q6 Edge 3 Stretto

Mid-wheel-drive power wheelchair from Pride Mobility (Quantum Rehab
division), US/UK/AU markets. Newer/higher-spec platform than the [[J6]]:

- Class B (Group 3), 300 lb weight capacity
- Max speed 6.25 mph (4 mph UK-only; 3.5 mph while iLevel is engaged)
- Range 15.9 mi (40Ah batteries) / 20.3 mi (55Ah batteries)
- Turning radius 21 in, ground clearance 2.9 in
- Two motor Mid-Wheel 6 drive, "Intelligent Braking" electronic
  regenerative + disc park brake, SRS (Smooth Ride Suspension)
- 14 in or 12.5 in drive wheels, pneumatic or flat-free
- Two 12V sealed lead-acid deep-cycle batteries (AGM/Gel-Cell/Hybrid Gel),
  40Ah or 55Ah, 8-amp off-board charger (vs. J6's 5-amp)
- Max rated slope 7.5°, max obstacle climb 3.5 in, sound <65 dB

## Documents

- [[Q6 Edge 3 Stretto Specifications]] — spec sheet
- [[Q6 Edge 3 Stretto Operator Manual]] — assembly, comfort adjustments,
  batteries/charging, care and maintenance, cleaning/disinfection
- [[Q6 Edge Basic Troubleshooting]] — symptom-based troubleshooting
  (written for the general Q6 Edge family, covers Q-Logic/NE+/NE
  electronics)
- [[Q6 Edge 3 Stretto Parts Replacement Guide (INFMANU5103)]] (Rev B,
  2023) — removal and torque for seating, wheels, casters, suspension,
  motors, batteries, power module, breaker and iLevel base

## Controller

The 2025 [[Quantum End-to-End Chart (INFINFB4546, 2025)]] offers it with
**75 A QLNES or 120 A Q-Logic 3** (2-pole motors). The Q-Logic 3 manuals
on file were filed with this model, but **check the hand control**: an
LED-only joystick is QLNES. Per the chart, the 6.25 mph top speed needs
Q-Logic 3. See [[Joystick-Controllers]] for operation and programming
and [[Q-Logic-Fault-Codes]] for codes.

Other 2025 chart figures: base **126.4 lb**; batteries 40 Ah (31 lb
each) or NF-22 (36 lb each); casters **5 in front, 6 in rear,
flat-free**; width 20.47 in with 12.5 in drive wheels (the spec sheet
says 20.75 in); 12 in iLevel at 3.5 mph; Group 3 (K0848/K0849,
K0856/K0857, K0861); FSS V797D-70001.

## iLevel

Full rules, indicators and parts across the Edge family: [[iLevel]].

Optional power-elevating-seat feature, mounted for max stability. When
engaged: speed capped at 3.5 mph, front caster movement inhibited by iLevel
boots (climbing ability restricted to 1–1.5 in), seat can still tilt/
recline up to 20° while elevated. Indoor/flat-hardscape use only — not
rated for uneven or outdoor terrain. Full inhibit behavior (elevate
lockout, recline lockout, etc.) is defined in the
[[Tru-Balance-3-Power-Positioning]] inhibit matrix, which this model can
also be built with instead of/alongside iLevel.

## Service (parts guide)

Torque values side by side with the other Pride chairs:
[[Pride-Parts-Replacement]]. Stretto-specific points:
- Lug nuts **22–27 N·m**; split-rim screws 4–5 N·m with Loctite 242.
- Motor (3 screws to mount and backing plate) and motor mount
  **15–20 N·m**. **5-spoke hubs use the top mount holes, 3-spoke the
  bottom.**
- Caster fork nut 25–30 N·m with a **new nut**; caster axle nut
  12–16 N·m; caster arms 15–20; suspension pivot pins and damper ball
  studs 10–15.
- Battery stops: **55 Ah** stops adjust side to side in slotted holes
  (2–5 N·m); **40 Ah** batteries need the stop removed to come out
  (4–6 N·m).
- Seat interface 32–38 N·m (TB Flex 15–20); towers 22–28.
- iLevel caster-arm stop backing plate: **sloped edges up**. TRU-Balance
  4 iLevel seat assembly on the Stretto needs its **spacer**
  ([[Tru-Balance-4-Power-Positioning]]).
- Power module port maps for **NE/NE+ and Q-Logic 3** are in the guide
  (p. 22), which also shows an NE/NE+ joystick in chair prep; the 2025
  chart lists QLNES or Q-Logic 3. Check the hand control.

## iLevel retrofit

A Stretto without iLevel can be converted (INFINFB4312, 2020): new
seat base and towers, suspension limiter with the iLevel switch,
caster-arm stop (sloped edges up), REAC lift intermediate board; Q-Logic
3 + AAM or NE+ with AM1/AM2/LAM2; reprogram. Don't power on until every
harness and bus cable is connected
([[iLevel Retrofit Instructions (Edge 2.0-3, Edge HD-Z, Stretto)]]).

## Known quirks/gotchas

- Transit securement is **either** a WTORS strap tie-down (ANSI/RESNA
  WC/Vol.4 §18) **or** a docking-type system (§19) — the manual is explicit
  these are two distinct approved methods, not interchangeable ad hoc.
- The OM's cleaning/disinfection section (2022 revision) is notably more
  detailed than the J6 OM's (2018 revision) — see [[J6]] for the
  cross-reference. If in doubt on approved disinfectants for any Pride
  chair, this manual's list is the more current one on file.
- Battery access differs from the J6: squeeze-release front cover +
  rotating rear shroud clips + quick-release battery connectors, vs. J6's
  fastener-based shrouds.

## Field notes

None for the Stretto. The 2026-09-25 iLevel no-power job was a
**standard** Edge 3, now on its own page: [[Q6-Edge-3]].

## See also

- [[Pride]]
- [[Joystick-Controllers]]
- [[Power-Chair-Troubleshooting]] (symptom-first, incl. Q-Logic 3 error codes)
- [[Tru-Balance-3-Power-Positioning]], [[Tru-Balance-4-Power-Positioning]]
- [[Pride-Parts-Replacement]]
- [[J6]]
- [[Q6-Edge]], [[Q6-Edge-3]], [[Q6-Edge-4]], [[Pride-Power-Chair-Lineup]]

Ramp compatibility: see [[Ramp-Slope-and-Length]] for which ramp ratios this model's rated incline allows.
