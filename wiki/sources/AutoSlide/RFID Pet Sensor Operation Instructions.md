---
type: source
manufacturer: AutoSlide
model: AutoSlide
doc_type: Accessory Operation Instructions
source: "MANUALS/Open Sesame/autoslide-V2-RFID-Instructions.pdf"
tags: [autoslide, automatic-door, rfid, pet-sensor, misfiled]
---

# RFID Sensor Operation Instructions (AutoSlide K9 Pet Tag)

9-page operation manual for AutoSlide's RFID pet-door accessory: a wall-
mounted RFID transmitter plus two battery-powered "K9 Smart Pet Tag" fobs,
wired into the pet Sensor port on an **AutoSlide/Multidrive Controller**
(confirming "Multidrive" as a second controller/product name used by
AutoSlide, distinct from the standard drive system documented in
[[AutoSlide Installation Manual (Standard, iLock, Elite, Elite iLock)]]).

**Filing note:** this document is physically located at
`MANUALS/Open Sesame/autoslide-V2-RFID-Instructions.pdf` — the folder name
"Open Sesame" doesn't match its content, which is entirely AutoSlide-branded
(AutoSlide logo throughout, `autoslide.com` support contact). Likely either
a misfile (similar to the pre-existing [[Harmar]]-doc-under-Bruno-folder
case) or "Open Sesame" is a distributor/reseller name Performance Medical
Supply uses for this accessory bundle — not confirmed either way. Not moved,
per the raw-sources-are-immutable convention; flagging here for the human to
clarify.

## Covers

- Box contents: RFID transmitter, 2× K9 Smart Pet Tag fobs (battery
  required, not included pre-inserted), 2× weatherproof pouches, wall-mount
  screws, connector cable, long/short connection cables.
- Physical install: wall-mount the transmitter housing, route the cable
  along the door frame to the AutoSlide/Multidrive controller's pet Sensor
  port (front bottom-port or rear-port wiring options, the latter for
  new-construction/remodel work).
- Jumper settings: single jumper must stay attached for relay operation;
  double-switch jumper selects Normally Open vs. Normally Closed relay
  contact type.
- Learning/pairing a new Tag: hold the transmitter's hidden "Learn" button,
  bring the Tag into range, red LED flashes 3× to confirm — same
  Sensor-Learn pairing pattern used for wireless wall buttons in the main
  install manual.
- Erasing all tags: hold the Learn button 10 seconds until the red LED
  turns off.
- LED behavior: 3 blue flashes on initial power-up then off; solid/flashing
  red = learning mode / tag transmission; blue = relay activated.
- Activation range: default ~8.2ft/2.5m, adjustable per-tag (hold the Tag's
  own button ~3 sec at the desired range until its LED goes solid, release).
  Tag can also force-activate by button press from outside range, at the
  cost of faster battery drain.
- Dual-sensor placement diagram for dogs: a higher box (A) triggers only
  when the dog is standing; a lower box (B) triggers whether standing or
  sitting — lets an installer choose whether the door stays open while a pet
  lies down near it.
- Troubleshooting note: sensor placement near a thick wall can create an
  inside/outside trigger-distance mismatch (a dog on the far/outside face of
  a thick wall may sit outside the tag's programmed range even though a dog
  on the near/inside face is well within it) — recommends programming the
  maximum trigger distance high enough to cover the thicker side.

## Feeds into
[[AutoSlide-Drive-System]]
