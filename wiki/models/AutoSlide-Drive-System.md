---
type: model
manufacturer: AutoSlide
model: AutoSlide
tags: [autoslide, automatic-door]
---

# AutoSlide

Automatic sliding-door retrofit kit: a motorized drive + rack-and-pinion
track that clips onto an *existing* sliding door panel (patio door, screen
door, barn door, or pocket door) and automates opening/closing. Not a
mobility-aid model in the sense of the rest of this wiki (stairlifts,
scooters, wheelchairs, patient lifts) — it's a home-accessibility/automatic-
door product line, presumably sold by Performance Medical Supply as a
touchless-entry accessibility accessory rather than a piece of mobility
equipment.

Four hardware variants share one installation manual, distinguished by drag
force capacity and locking:

| Variant | Motor | Locking |
|---|---|---|
| Standard | silver barrel | no |
| Standard iLock | silver barrel | dynamic braking lock (chrome barrel segment) |
| Elite | black barrel, higher power | no |
| Elite iLock | black barrel, higher power | dynamic braking lock |

A friction test (pull-tester strip, Standard units only) during install
determines whether the door's drag force needs the Standard or Elite motor.

## Documents

- [[AutoSlide Installation Manual (Standard, iLock, Elite, Elite iLock)]] —
  full install/setup/troubleshooting/warranty manual for the drive system
- [[RFID Pet Sensor Operation Instructions]] — accessory pet-door sensor
  add-on, physically filed under a mismatched `MANUALS/Open Sesame/` folder
  (see that page's filing note)

## Operating modes

Four modes cycle via a front-panel Mode button, each with a status-light
color:

- **Green — Auto Mode**: everyday human use. Pet sensors disabled, no lock,
  open-assist enabled. Default/most common mode.
- **Blue — Stacker Mode**: door stays fully open by default; a sensor on
  the Stacker port can operate it like a garage door (partial open).
- **Red — Secure Mode**: iLock-only security mode. Outside sensors and
  open-assist disabled, door locked.
- **Orange — Pet Mode**: pet + inside sensors enabled, outside sensors
  optional, door locked, opens only to the smaller programmed pet width.

Four independent opening widths get programmed separately (normal/human,
Stacker, Pet), each via a DIP-switch-#1 flip-and-flip-back that starts a
learn cycle bounded by a physical doorstop/jamb.

## DIP switches (8 total)

| # | Function |
|---|---|
| 1 | Direction/Learn — right/left-handed door select; also triggers width-learn cycles |
| 2 | Slam Shut — extra power at open/close extremes (tight jambs/weatherseals); incompatible with #7 |
| 3 | Pet Learn — starts/stops the pet-width learn cycle |
| 4 | Secure Pet — disables Outside Sensor in Pet Mode, for security-conscious pet setups |
| 5 | 75% Power — for light doors (screen/pocket doors) |
| 6 | App Control — enables Bluetooth module control |
| 7 | Extra Power — for heavy doors; incompatible with #2 |
| 8 | Beep — audible feedback on open/close/mode-change |

## Mounting

Preferred mount is top-of-frame (inside or outside, matching whichever
panel side rides on the door's inner track); floor/bottom mounting is a
last resort and normally requires **rehanding** (physically swapping the
motor and control-panel sides of the unit — see the install manual's
Section 07) if used on a right-handed door. An L-shaped adapter bracket
handles walls/frames without enough header depth.

## Sensors and accessories

- **Inside / Outside / Pet / Stacker sensor ports** — see the install
  manual for per-mode enablement.
- **Wireless wall push buttons** (2 included) — paired via the same
  universal Sensor-Learn pairing sequence used for all wireless accessories.
- **RFID pet sensor kit** — see [[RFID Pet Sensor Operation Instructions]].
- **Bluetooth module + AutoPlus Hub** (phone app control) and a
  **home-automation relay/key-switch cable** — both mentioned in the FAQ,
  **no manual on file for either yet**.

## Known quirks/gotchas

- DIP #2 (Slam Shut) and DIP #7 (Extra Power) are mutually exclusive.
- A right-handed door needing a floor/bottom mount is "normally the only
  time a unit needs to be re-handed" per the manual — top-mounting avoids
  this entirely regardless of door handing.
- Every width-programming routine depends on a physical doorstop/jamb
  existing at the desired endpoint; without one, the installer must
  manually brace the door at the target position during the learn cycle.
- Warranty explicitly excludes damage from non-AutoSlide accessories and
  batteries, and any commercial/institutional use — this appears to be
  positioned as a residential/DIY product, consistent with the "no
  installer required" framing in the FAQ.

## See also

- [[AutoSlide]] — manufacturer page
