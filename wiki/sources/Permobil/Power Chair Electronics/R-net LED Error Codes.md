---
type: source
manufacturer: Permobil
model: R-net controllers (PG Drives Technology)
doc_type: Troubleshooting Tool
source: "MANUALS/Permobil/Power Chair Electronics/r-net-led-error-codes.pdf"
date:
tags: [r-net, pg-drives, power-chair, led-codes, diagnostics]
---

# R-net LED Error Codes

One-page PG Drives Technology sheet for the **R-net** joystick's battery-gauge
LED flash codes (count the LEDs lit). R-net is used on Permobil power chairs.

| LEDs | Meaning |
|---|---|
| 1 | Battery needs charging or a bad battery connection |
| 2 | Left motor bad connection |
| 3 | Left motor short to a battery connection (service agent) |
| 4 | Right motor bad connection |
| 5 | Right motor short to a battery connection (service agent) |
| 6 | Driving inhibited by an external signal (depends on the chair) |
| 7 | Joystick fault: center it before switching on |
| 8 | Possible control system fault: check connections |
| 9 | Parking brakes bad connection: check brake and motor connections |
| 10 | Excessive voltage, usually a poor battery connection |
| 7 + S | Communication fault: joystick cable |
| Actuator flash | Actuator trip: find which actuator, check its wiring |

Left/right motor as wired; may be swapped in programming.

## Feeds

[[PG-Drives-Trip-Codes]], [[R-net-Diagnostics]], [[Permobil]]. Full PGDT manual: [[R-net Technical Manual (SK77981-6)]]. Permobil's own manuals word 6 LEDs as "battery charger connected".
