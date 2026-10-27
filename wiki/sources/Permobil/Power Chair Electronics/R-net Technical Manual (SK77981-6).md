---
type: source
manufacturer: Permobil
model: R-net control system (PG Drives Technology)
doc_type: Service Guide
source: "MANUALS/Permobil/Power Chair Electronics/r-net-electronics-technical-manual-v6.pdf"
date: 2009
tags: [r-net, pg-drives, power-chair, diagnostics, trip-codes, programming, obp, wiring]
---

# R-net Technical Manual (SK77981/6)

PG Drives Technology's **R-net Technical Manual**, issue 6 (© 2009, 168
pp.), filed with the Permobil electronics because Permobil chairs use
R-net. Six chapters: **Operation** (JSM controls, LCD screens, locking,
battery gauge), **Installation** (mounting, wiring, wire gauges, circuit
breakers, production tests), **Programming** (OBP and the OEM parameter
list), **ELPM 90, JSM-LED and seating module**, **Encoder module** and
**Diagnostics**. The service content is distilled on
[[R-net-Diagnostics]].

## Key service facts

- **Trip codes** (LCD JSM or a DTT): the screen shows the **module** (PM,
  JSM, ISM), **trip text** and a **4-digit trip code**. The full trip
  text list and the codes the manual gives are on [[R-net-Diagnostics]].
- **System log:** every trip, with counts, by module: OBP → System →
  Diagnostics, a DTT or the PC Programmer.
- **Low battery** trips below **16 V**, **high battery** above **35 V**.
- **Locking:** keypad (hold On/Off 1 s to the beep, joystick forward to
  a beep, back to a beep, long beep) or a PGDT key in the charger socket.
  Locked LED JSM: speed LEDs ripple left to right.
- **OBP entry:** with a PGDT dongle in the bus, or by keycode (hold
  Horn, then On/Off to a short bleep; release Horn, keep On/Off for two
  more bleeps; release for a long bleep). **Not possible on an LED
  JSM.** Which method works is set at the factory.
- **Wire gauges** (under 1 m runs): 60 A and 80/90 A PM: battery 6 mm²,
  motor 4 mm²; **120 A PM: battery and motor 8 mm²**; brakes 0.5,
  actuators 1.5, lighting 0.5, inhibit 0.22 mm². 105 °C PVC on battery and
  motor wires.
- **Battery circuit breaker** in series (e.g. between the two 12 V
  batteries): **50 A for a 60 A PM, 90 A for 80/90 A and 120 A PMs**;
  must hold 15 s stalled (ISO 7176-14). A motor breaker must have an
  auxiliary switch that disconnects the brake.
- **No serviceable parts** in the modules; repairs go to PGDT or an
  approved centre.
- **Basic tests after any repair:** general inspection, brake test (each
  brake heard within **2 s**, four directions), drive test (min and max
  speed), gradient test (stops without the front lifting), lights
  (indicators **1.5 Hz ± 0.5**, one bulb out → **3 Hz**), actuators
  (direction, end-stops stall the motor), inhibit test (charger plugged
  in = no drive).

**Manual error:** section 3.26 gives **3C00** for "M2 Sensor Error",
the same code it gives for **M2 Motor Error** in 3.5 (M1 Sensor Error
is 2001). Treat 3C00 as the M2 motor trip and check the encoder
separately if one is fitted.

## Feeds into

[[R-net-Diagnostics]], [[PG-Drives-Trip-Codes]], [[R-net LED Error Codes]],
[[Joystick-Controllers]], [[Permobil]]
