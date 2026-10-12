---
type: concept
tags: [diagnostics, golden, dynamic-controls, shark, power-wheelchair]
---

# Shark Controller Diagnostics (Dynamic Controls)

The **Dynamic Shark** controller's 11-code flash table. It comes from
the [[Compass HD Service Guide (GP620)]] (2017), the first document on
file with Shark codes. Shark is a **Dynamic Controls** product. It is
the "SHARK" named in the older GP605 supplements and in
[[Golden-Joystick-Side-Conversion]].

Applies to: [[GP6xx-Compass]], meaning the **GP620** Compass HD and
**older GP605** Compass Sports. The 2017 GP605 guide uses LiNX instead,
so check which controller is fitted.

The **amber wrench LED** on the remote flashes the count.

| Code | Fault | What to do |
|---|---|---|
| 1 | User fault | **Stall** (drive command but the wheels can't turn): power-cycle. **Thermal rollback:** let it cool about 15 min, then power-cycle. If it happens often in normal use, check for a sticking park brake or motor. |
| 2 | Battery fault | Check battery voltage (Step 1). If it persists, return the controller. |
| 3 / 4 | M1 / M2 motor fault | Swap M1 and M2 (if the connectors are un-keyed). If the code follows the motor, the motor is bad; if not, the controller is. **Cold motor 0.3–50 Ω**, measured on the outside pins. **Controller M1/M2 outputs about 22 kΩ** with the battery disconnected. |
| 5 / 6 | M1 / M2 park brake fault | Is the brake (freewheel) lever disengaged? Re-engage it and power-cycle. **Brake 40–80 Ω**, measured on the middle pins of the motor connector. |
| 7 | Remote fault | Holding the power button more than 4 s at power-up sets this on purpose; it is a test of the emergency stop. Power-cycle. Otherwise check battery voltage and wiring. |
| 8 | Controller fault | Check battery and wiring; then return the controller. |
| 9 | Communications fault | Check the bus cable and pins. |
| 10 | Unknown fault | Return the controller. |
| 11 | Incompatible control unit | The controller and remote branding must match. |

**Battery gauge conditions:**
- **Left red LED flashing:** extremely low battery. Charge for 8 h or
  more.
- **Right-to-left chase:** Shark is **locked**. To unlock, turn it on and
  press the **horn twice within 10 s**.
- **Left-to-right chase:** charge inhibit. Remove the charger.
- **All speed LEDs flashing slowly:** OONAPU (out of neutral at
  power-up). Release the joystick. If it persists, **calibrate the
  joystick with the DX-HHP**: connect through the DK-ADAPT adapter to
  the charger port, choose TECH, password **262**, PROG until
  "Calibrate Joystick?", choose YES, deflect in each prompted direction
  twice, then EXIT and power-cycle.

**Battery load test:** drive with someone in the chair and probe the
charger port's outer pins. It should hold at about **24 VDC or more**
after the initial drop. If it keeps falling, replace both batteries.

## See also

[[GP6xx-Compass]], [[LiNX-Diagnostics]], [[Flash-Beep-Diagnostics]],
[[Golden-Joystick-Side-Conversion]], [[Golden]]
