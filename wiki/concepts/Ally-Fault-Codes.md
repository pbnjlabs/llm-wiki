---
type: concept
tags: [diagnostics, golden, ally, power-wheelchair, bluetooth, folding]
---

# Ally Fault Codes (GP303, GP304, GP305)

The Golden **Ally** family ([[GP303-Ally]], [[GP304-Ally-Pro]],
[[GP305-Ally-Sport]]) uses a **display joystick with numbered fault
codes and voice prompts**. It's a different scheme from every other
Golden table ([[Golden]] lists them). The manuals call the controller a
"40 Amp Remote" and don't name its maker. Sources:
[[Ally Owners Manual (GP303)]], [[Ally Pro Owners Manual (GP304)]],
[[Ally Sport Owners Manual (GP305)]]; the tables are the same in all three.

## Display codes

The code shows on the joystick screen at power-up.

| Code | Fault | Check |
|---|---|---|
| E1 | Joystick button | A button stuck down |
| 20, 21, 22, 23 | Joystick electrical | Wiring and harnesses |
| 24 | Joystick not centered at power-up | Restart without touching the joystick |
| E6 | Joystick-to-controller wiring | Wiring and harnesses |
| E7 | Bluetooth connection | Restart both devices; pair again |
| 40 | Left motor brake | **Left freewheel lever** not locked |
| 41 | Right motor brake | **Right freewheel lever** not locked |
| 80 | Low voltage | Charge |
| 88 | Pre-charge fault | Follow the charging procedure |
| 90 | "High voltage" | The text describes an **overload**: brakes releasing properly? Over the weight limit or **6°**? Turn off, let it cool, reduce load or slope |
| 93, 96 | Both motors | Wiring, motors, anything jammed in the wheels |
| 81, 84, 85, 92, 94 | Right motor | Right motor and harness |
| 82, 86, 87, 91, 95 | Left motor | Left motor and harness |

The code-90 text gives 330 lb in the Ally manual but 265 lb in the Ally
Pro and Ally Sport manuals. The Ally Pro is rated 330 lb, so its copy is
an error. Go by each chair's spec page.

## Voice prompts worth knowing

| Prompt | Meaning |
|---|---|
| "Brake open" | A motor brake is released: a **freewheel lever is down** |
| "Drive protection" / "Machine protection" / "Rocker protection" | Drive, machine or **joystick** failure |
| "Low battery, please charge" | Under 20% |
| "Lock" / "Unlock" | Joystick locked (press power once while on) |
| "Wheelchair has been locked by Bluetooth" | Locked from the app |
| "Start the remote control" | Someone is driving it from the app |
| "Enter / Quit novice mode" | Speed limited to settings 1–2 |
| "Upgrading" / "Upgrade complete" / "Upgrade failed" | App-pushed firmware update |

## Things that look like faults but aren't

- **Won't drive with freewheel levers down**: it stays stopped until both
  are locked (40/41, "Brake open").
- **Novice mode** caps speed at 2 (Fn button; W on the Ally Sport).
- **Cruise control** keeps it moving forward with the joystick centered.
  Pull back to cancel.
- **Joystick locked** from the joystick or from the app.
- **Sleep mode** time is set in the app.

## The phone app

Bluetooth 4.1 with AES-128. It can drive the chair, change speed, lock
it, power it off, turn on cruise control, set the sleep timer, voice
volume, speed-gear memory and remote power-on. When pairing, the
joystick and the phone show the same code; pair one chair at a time.
If the phone loses control, use the joystick and keep other wireless
devices 10 ft away.

## See also

[[GP303-Ally]], [[GP304-Ally-Pro]], [[GP305-Ally-Sport]],
[[Freewheel-Mode]], [[Power-Chair-Troubleshooting]], [[Golden]]
