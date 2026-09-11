---
type: model
manufacturer: Harmar
model: Highlander II with Enclosure
tags: [vpl, platform-lift, harmar]
---

# Highlander II with Enclosure

Harmar's enclosed vertical platform lift (VPL) product family: **VPL400,
VPL600, VPL800, VPL1000, VPL1200, VPL1400** series (taller units — 1000
and up — carry a lower 12-cycles/hour duty rating vs. 24/hour for
400-800). AC-powered (115V/15A/1φ/60Hz), ACME-screw-driven, 750 lb max
payload.

## Architecture
- 2/3 Hp gearmotor, 26:1 worm-drive gearbox, 25% duty cycle (45-min max
  continuous run, then 2h15m rest)
- Electromagnetic "fail-safe" holding brake (24VDC releases it) plus an
  eddy-current E-Brake resistor for down-direction deceleration
- Optional battery backup: 2× (VPL400/600) or 4× (VPL800-1400) 12V SLA
  batteries in series/parallel to 24V, 60A fuse, 24V/2A 4-stage charger,
  1500W inverter (120V modified sine wave) — auto-wakes every 8 hours to
  check batteries, 5-second wake-up delay on button press
- Over-Speed Governor (OSG) switch at the bottom of the ACME screw halts
  the platform on drive-screw overspeed — see [[Overspeed-Safety-Brake]]
  for how this compares to Bruno's and Prism's centrifugal governors
- Safety pan (11 switches), pit switch, float switch (flood detection —
  25 trips or 2 weeks triggers out-of-service), top/bottom/mid landing
  switches, final limit switch

## Status indicator
4 LEDs on the top cap (green/amber/red combinations — roughly 25 distinct
states in the install manual's full table vs. a condensed subset in the
owner's manual). Covers normal operation, backup-power states, minor
faults (service required, still operable), and major faults (lift
disabled). The control board also carries a parallel 32-LED diagnostic
array (4 duplicate top-cap indicators + 3.3V/24V power + 26 individual
circuit-status LEDs) for bench-level troubleshooting, plus 3 momentary
switches (brake/reset/service) and 3 permanent cuttable configuration
jumpers (3-stop/TG/AUX).

## Emergency lowering
A manual lowering tool (1/4" socket + 3/8" ratchet or cordless drill)
turns clockwise at a manual-override point under the top cap — the
platform can only be lowered this way, not raised (the torque required to
raise is substantially higher). A person other than the trapped occupant
must perform this from outside the platform, at the top of the tower.

## Documents on file
- [[Highlander II with Enclosure Owner's Manual]] (2021 Rev A)
- [[Highlander II with Enclosure Installation and Service Manual]] (2022
  Rev B) — primary technical reference; the owner's manual's status-code
  table and maintenance sections are a condensed subset of this
  document's

## Warranty
3-year parts warranty (labor excluded), covers VPL400-1400 with
enclosure — see [[Harmar-Warranty]].

## See also
[[Harmar]], [[Overspeed-Safety-Brake]], [[Harmar-Warranty]]
