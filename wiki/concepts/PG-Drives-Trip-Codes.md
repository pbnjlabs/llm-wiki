---
type: concept
tags: [diagnostics, pg-drives, trip-codes, s-drive, vr2, vsi, pilot-plus, controller]
---

# PG Drives Trip Codes

The **4-digit trip codes** PG Drives Technology (PGDT) controllers
report to a **PG programmer**, from the [[PG Drives Mobility Diagnostic
Guide]] (2017). Covers **newVSI, VSI, VR2, Pilot+, S-Drive, EGIS and
Solo**. Golden uses the **S-Drive** on the [[GA541-Avenger]] and the
**VR2** on the [[GP162-LiteRider-Envy]] PTC variant.

These are **programmer codes**. The bar/flash code a user sees on the
**TruCharge display** is on [[TruCharge-Diagnostics]]; use the
programmer code for detail.

**Rules for every code:**

- **No serviceable parts in PG controllers.** If the fault stays after
  checking wiring and parts, the controller (or power/joystick module)
  goes back to **PGDT or a PGDT-approved service center**. Opening it
  voids the warranty.
- Check **all connections to motors, brakes, batteries and the
  controller** before blaming the controller.
- Dual-motor chairs: left/right outputs may be **swapped in
  programming**, so check both sides.
- After any repair, run the **basic tests** below.

## Codes

| Code(s) | Trip | What to check |
|---|---|---|
| 0A00 | **Sleep mode** (TruCharge or status LED blinks once every 2.5 s) | Not a fault. Switch off and on. Sleep time is programmable (Operation group); a VR2 turns fully off. |
| 0300, 0810, 0814–0817, 0E07, 0E08 | **Throttle trip** (scooters) | Throttle and its connections. S-Drive: 0300 speed-limit pot wiper open (limited speed, non-trip); 0815 throttle pot reference disconnected; 0E07 wiper shorted to a reference; 0E08 wiper open. EGIS: 0814 high ref (pin 12) disconnected; 0816/0817 wiper shorted to high (pins 7 & 12) / low (pins 7 & 5) ref. |
| 1320 | **Current limit active** | Controller ran above its current limit threshold longer than the limit time. Logged for the technician. |
| 1330 | **Motor stall timeout** | Throttle deflected but can't move (slope too steep, curb too high, trapped). Current is cut and brake applied to protect the motor. Logged. |
| 1500–1506 | **Solenoid brake trip** | Brakes and their connections. S-Drive: 1500 short, 1502 open. VSI: 1501 short, 1502 open. EGIS: 1500 open, 1501 short, 1502 over-current. VR2 / Pilot+: 1505 left brake, 1506 right brake. |
| 1600, 1601 | **High battery voltage** (above **35 V**) | Usually overcharging or bad battery connections. |
| 1D02 | **Front-end reconfiguration** | A throttle parameter was written to. Switch off and on; clear it from the system log. |
| 1D05 | **Joystick stationary too long** | Joystick held still too long; drive stops to protect motors. Switch off and on. |
| 1E03, 1E08 | **Off-board charger connected (Inhibit 2)** | TruCharge gauge "steps up". Disconnect the charger. |
| 1E04, 1E09 | **Inhibit 2 active** | Wiring and switches on Inhibit 2 (speed limiting on VSI; actuator functions on VR2/S-Drive; Pilot+ pin 3, e.g. seat height switch or on-board charger). |
| 1E05, 1E0A | **Inhibit 3 (on-board charger) active** | On-board charger and its wiring (VR2: pin 2 of the control socket). |
| 2C00 | **Low battery voltage** (below **16 V**) | Battery condition and connections. |
| 2C02 | **Low battery lockout** | Battery condition, charge level, connections. Logged. |
| 2F00, 710D, 7146 | **Joystick deflected at power-up** | User pushing the joystick before the gauge stops blinking. If it persists, the joystick (module) is faulty. |
| 2F01 | **Throttle displaced at power-up** (scooters) | Same idea for the throttle. Then adjust the throttle pot deadband; then replace the throttle. |
| 3000, 714D, 7147 | **Attendant joystick deflected at power-up** | Attendant's joystick off center at switch-on. |
| 3B00 / 3C00 | **Left / right motor disconnected** | That motor, its connectors and wiring. |
| 3B01 | **Motor disconnected** (single motor) | Motor, connectors, wiring. |
| 3D00, 3D01 / 3E00, 3E01 | **Left / right motor wiring trip** | Motor connection **shorted to a battery connection**. Motor connectors and wiring. |
| 3D02, 3D03 | **Motor wiring trip** (single motor) | Same, single-motor controllers. |
| 5300 | **Programmable setting changed** (S-Drive) | A parameter was changed. Switch off and on. |
| 5400, 7113, 7124, 7126, 7133 | **Communications trip** | Cable between power module and joystick module (VR2/Pilot+), or VSI to dual module. Check continuity. VSI: disconnect the dual module and restart to drive. |
| 7000, 7001 | **Freewheel mode engaged** | Freewheel switch operated while driving or on at switch-on. Check the switch, then cables. |
| 7102 | **Power loss** (to joystick) | Cable continuity; then the joystick module. |
| 7100–7117 (group) | **Joystick module trip** | VR2: 7100/7101 loss of comms, 7102 loss of power (joystick cable, ribbon cable if authorized); 7103/7104 internal trip (ribbon cable seated at joystick and PCB). Joystick replacement only by someone authorized by the chair maker. |
| 7107 | **Primary joystick deflected** | User's joystick off center while the attendant module is in control. Center it and cycle power. |
| 7140, 7142 | **Dual communications trip** | Cables between joystick, attendant module and power module. |
| 714A–7175 (group) | **Dual module trip** | Internal attendant module fault; return it to PGDT. |
| 7164 | **Attendant joystick orientation error** | Redo the orientation sequence (in the guide). |
| 7A00 | **Actuator motor disconnected** | Actuator motors, connectors, wiring. |
| 7A01, 7A02, 7A03 | **Actuator motor wiring trip** | Actuator wiring shorted to a battery connection. |
| 7B00 | **Dual module connected while on** | Switch off, connect the attendant module, switch on. |
| 7125–7137 (group) | **Omni+ trip / input device** | Omni+ faulty or not getting a valid input signal. 712A: sip-and-puff calibration; 7136: analog input calibration (steps in the guide). |
| 7821, 7902 | **Thermal foldback** | Controller too hot; current limited or goes to standby to cool. Logged. |
| 7825 | **Thermal shutdown** | Power cut and brakes applied. Logged. |
| Any other code | Possibly internal to the controller | Check all connections first; poor battery connections can cause intermittent codes. |

## Faults with no code

| Symptom | Likely causes |
|---|---|
| Won't switch on | Battery connections to the controller; then the controller |
| Drives slowly | Wrong programming; a speed limit active (e.g. raised seat); faulty motor or brake |
| Won't drive straight; one motor or brake very warm | Faulty motor or brake |
| Batteries run down fast | Worn batteries; faulty or wrong charger; wrong battery type; a motor or brake jamming. Cold weather cuts range (the gauge still reads correctly). |
| Actuators don't respond | How many; connections; test the actuator with direct power; then the ALM (Pilot+) or power module (VR2) |
| Lights don't respond | Connections and bulbs; then the ALM (Pilot+) or lighting module (VSI) |

## Basic tests after a repair

1. **General inspection:** connectors mated; cables undamaged; joystick
   gaiter undamaged (look, don't handle); everything mounted, screws not
   overtightened.
2. **Brake test** (level floor, 1 m clear all around): switch on; the
   TruCharge display stays on or flashes slowly after 1 s; push the
   joystick/throttle slowly until the brakes release, then let go. **Each
   brake must engage within 2 seconds.** Repeat backward, and left and
   right on wheelchairs.
3. **Drive test:** all directions at minimum speed, then at maximum.
4. **Gradient test** (with a helper to stop tipping): up the maximum rated
   gradient; release and check it stops and holds **without the front
   wheels lifting**; restart smoothly; repeat reversing down.

Related: [[TruCharge-Diagnostics]], [[Joystick-Controllers]],
[[PG Drives S-Drive Brochure]]
