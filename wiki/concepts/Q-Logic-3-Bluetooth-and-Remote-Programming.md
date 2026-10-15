---
type: concept
tags: [pride, quantum, q-logic-3, q-logic-3e, qlnes, bluetooth, econ-w, econ-i, interactive-assist, mouse, switch-control, gyroset]
---

# Q-Logic 3 Bluetooth and Remote Programming

Everything Quantum's Q-Logic 3 (and 3e, and QLNES) does over
Bluetooth: programming from a PC or iPhone, letting the chair drive a
phone or computer as a mouse or switch, **remote diagnostics with
Interactive Assist**, and hooking up the GyroSet Vigo head control.

Sources: [[Econ-W User Level Programming Guide (INFMANU5125)]],
[[Econ-I User Level Programming Guide (INFMANU5146)]],
[[Interactive Assist Dealer Manual (INFMANU5036)]],
[[Q-Logic 3 Bluetooth Startup Guide (INFINFB4485)]] (and its 2018
predecessor), [[GyroSet Vigo Setup for Q-Logic 3 (INFINFB4305)]],
[[QLNES Basic Operation Instructions (INFMANU5366)]], plus the
provider-level [[Q-Logic 3 Programming Guide]].

## Turning on programmer access at the chair

- **Q-Logic 3:** go to the **Aux** screen (mode command, or Home button
  then two left inputs), highlight **"Econ/Interactive Assist"**, give a
  right input to tick it, note the **chair ID** at the top of the
  screen. Another right input turns it off.
- **Q-Logic 3e:** **Settings** screen, right input to Bluetooth, forward
  input turns it on; the ID is at the bottom.
- **QLNES:** hold **on/off for 3 s** (Bluetooth LED blinks).
- Every connection must be **accepted at the chair with a forward
  input**. Pairing a new phone/PC also shows matching codes on both;
  accept on both.

## Programming apps and access levels

| App | Platform | Connects by | Access |
|---|---|---|---|
| **Econ-W** | Windows (quantumrehab.com) | Bluetooth, or USB-to-XLR CANbus cable (dealer only) | User level without log-in; **dealer level and above need a log-in** |
| **Econ-I** | iOS (App Store) | Bluetooth | User level ("Continue without Log-in") |
| **Q-Logic 3 HHP** | hand-held | cable | Dealer (once registered on the Cloud; [[Q-Logic-Firmware-Updates]]) |

Changes in Econ-W apply **in real time**, so you can tune while the
client drives, and over Bluetooth you're not tethered by a cable.

Useful screens in both apps:
- **Device List / System:** every module's **part number, build date,
  serial number, hardware and software version**. Check this before
  ordering a part.
- **Battery Statistics:** charging history. Good evidence when the call
  is "it won't hold a charge".
- **.xpa files:** save the chair's configuration (Econ-I can email it).
- Photo album, IR remote menus (TV, lights, etc.), **set clock** (Econ-W).

## Interactive Assist (remote diagnostics)

Lets a provider look at a Q-Logic 3 (or QLNES) chair **without a truck
roll**.

1. User enables "Econ/Interactive Assist" on the Aux screen and opens
   the **Interactive Assist** app (Android 5.0+, iOS 9+; by Curtis
   Instruments), taps "Start search for devices" and picks the chair
   with the matching ID.
2. The app shows a **channel and passcode**; the user gives them to the
   provider (the app can call or email the provider from its contact
   info).
3. Provider: in Econ-W click the Interactive Assist icon, enter channel
   and passcode. The chair asks the user to **accept with a forward
   input**.
4. Session lasts **1 hour**. Econ-W shows connection quality (green /
   yellow / red), remote user, access level and time left.

What the provider gets:
- **Dealer-to-user (normal):** view all parameters, seat configurator
  and Mapped IO; **change only user-level parameters** (set Econ-W's
  access level to "user" first), photo album and IR. Plus **error list**,
  live monitor values (under 0.5 s delay), **battery statistics**, a
  live copy of the chair's screen, the access/change log and a **chat**
  with the user.
- **Provider-to-provider:** a provider on site logs in to the app
  (different log-in from the remote Econ-W) and the remote provider gets
  **dealer write access**.

Quantum's required acknowledgment: give the channel/passcode only to a
trusted provider; only qualified technicians use it; use it to read
settings, troubleshoot and change **non-performance** settings; it
**doesn't replace a face-to-face evaluation and programming**. The
manual's sample chat is a typical win: the error log showed repeated
"out of center at power-up" because the user pushed the joystick
before the drive screen came up.

## The chair as a mouse or switch (phones, tablets, PCs)

A provider must first enable the function and how clicks work with a
programmer. Then:

- **Android or Windows (mouse):** Aux > Bluetooth Operation > tick
  **Mouse**. Home > right > **Mouse Connections > New** shows the ID.
  Pair **"MouseXXXX"** on the device; confirm with a forward command on
  the chair.
- **iPhone/iPad, Switch Control:** Aux > Bluetooth Operation > tick
  **Assistive Switch Control**. Pair **"SwitchControlXXXX"**, then in
  iOS Accessibility > Switch Control > Switches > Add New Switch >
  External, give each joystick direction (4, plus 4 "long" commands).
  Manual or single-switch step scanning is often easier than the default
  auto scanning.
- **iPhone/iPad, AssistiveTouch (iOS 15.4.1+):** pair as a **mouse**
  (Settings > Accessibility > Touch > AssistiveTouch > Devices >
  Bluetooth Devices > MouseXXXX). Chair dwell works as-is; to use iOS
  dwell instead, set the chair's **Mouse Clicks to Switches**. On the
  **QL3 EX** hand control, Key I and Key II can become left/right click:
  Econ-W > Handcontrol > Button Operation > **Custom MIO**, then Mapped
  I/O > Mouse Left/Right Click, then assign them in AssistiveTouch >
  Customize Additional Buttons.
- Gray icons = unpaired, blue = paired. Leave the mouse screen with the
  on/off lever up, Key I, Home or Key II.

## GyroSet Vigo (head-motion drive control)

Third-party (Now Technologies) gyroscopic head control. Chain: **Vigo
→ Bluetooth → Cubo → micro-USB → GyroSet Link → 9-pin D-sub on the
Enhanced Display or SCIM**. Program: Enhanced Display > Input
Configuration > **Proportional**, then Proportional Input >
**Proportional Calibration** and have the client **move their head
slowly in two circles** with the Vigo on. Econ-W does the same over the
USB-to-XLR CANbus cable (chair shows Output Inhibited, then System
Ready). Quantum doesn't support diagnosing the Vigo itself; that's
Now Technologies.

## See also

[[Joystick-Controllers]], [[Q-Logic 3 Programming Guide]],
[[Q-Logic-Fault-Codes]], [[Q-Logic-Firmware-Updates]],
[[Power-Chair-Troubleshooting]]
