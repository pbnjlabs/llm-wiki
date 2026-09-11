---
type: source
manufacturer: Golden
model: GP162
doc_type: Service Guide
source: "MANUALS/Golden/GP162 LiteRider PTC Golden SG 05.16.2014.pdf"
date: 2014-05-16
tags: [golden, gp162, literider-ptc, service-guide, vr2, truecharge]
---

# LiteRider PTC Service Guide (GP162, PG VR2 Controller)

50-page service guide/IPB for the GP162 "LiteRider PTC" — the **PG VR2
controller** variant of GP162, as opposed to the LiNX-controller variant
covered by [[LiteRider Envy LiNX Owners Manual (GP162)]] and
[[LiteRider Envy LiNX Supplemental Insert (GP162)]]. Two identical raw
files exist on disk with different filenames
("GP162 LiteRider PTC Golden SG 05.16.2014.pdf" and
"LITERIDER PTC_GP162_ SG_REVA_ 051614.pdf") — confirmed **byte-identical
by MD5 checksum**, so this page covers both filenames as one document.

Contents:
- Setup/adjustment and a "How to Read a TruCharge Battery Gauge" section
  — same 5-LED (1 red/2 amber/2 green) hardware and steady-state
  charge-level readout convention as GA541 and the LiNX variant, confirming
  "TruCharge" is Golden's brand for this LED battery-gauge hardware/display
  convention broadly, not one specific controller's feature.
- **10-bar PG VR2 flash-code fault table** — same 10-code architecture as
  [[TruCharge-Diagnostics]] (confirmed on GA541), but adapted for a
  wheelchair's independent left/right drive motors rather than a scooter's
  single drive:

| Bar | Fault |
|---|---|
| 1 | Low battery voltage (bad connection) |
| 2 | Left motor bad connection |
| 3 | Left motor short circuit |
| 4 | Right motor bad connection |
| 5 | Right motor short circuit |
| 6 | Charger connected, or other external signal preventing drive |
| 7 | Joystick fault (must be centered at power-on) |
| 8 | Control system fault |
| 9 | Parking brake bad connection |
| 10 | High battery voltage |

  This is the same PG-Drives-family 10-bar architecture as GA541's table
  (low=1, high=10, brake near 9, joystick/throttle near 7, controller at 8)
  but splits GA541's single motor/brake codes (2,3,4,9) into left/right
  pairs (2-5) to match the wheelchair's dual-motor layout — see
  [[TruCharge-Diagnostics]], now broadened to note this variant.
- Illustrated parts breakdown pages (27-50): vehicle/body, front frame,
  footplate, rear/wheel assemblies, caster arm, seat assembly — not
  itemized here, reference the PDF directly for part numbers.

Feeds: [[GP162-LiteRider-Envy]], [[TruCharge-Diagnostics]]
