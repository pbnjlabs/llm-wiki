---
type: source
manufacturer: Adaptive Switch Laboratories
model: ASL 110 FUSION
doc_type: Install Manual
source: "MANUALS/ASL/ASL-110-User-Installation-Guide-LinX-2023-Final.pdf; MANUALS/ASL/ASL-110-User-Installation-Guide-Q-Logic-2023-Final.pdf; MANUALS/ASL/ASL-110-User-Installation-Guide-R-Net-2023-Final.pdf; MANUALS/ASL/ASL-110-User-Installation-Guide-Permobil.pdf"
date: 2023-08
tags: [asl, head-array, install, programming, linx, q-logic, r-net, permobil]
---

# ASL 110 FUSION User Installation Guides (LiNX, Q-Logic, R-net, Permobil)

Four two-page **user installation guides** for the [[ASL 110 FUSION Head Array Instruction Manual (Rev 3-2022)]]:
**LiNX**, **Q-Logic Q3** and **R-net** (rev 8-2023) and **Permobil**
(rev 3-2022). Page 1 is the same install; page 2 is the controller
programming. Feeds [[Alternative-Drive-Controls]].

## Install (all four)

Kit: ASL 110 with **930R** swing-away and **320BK** switch, **606** mount
bar, **165** display/programmer, **683** magnetic mount, **618FD**
swing-away armrest mount for the display (Permobil: Permobil mounting
block hardware and the **BodiLink head support receiver** instead).

1. Slide the ASL 606 into the seat back mount (Permobil: the BodiLink
   receiver) and tighten the lever.
2. **Shorten the ASL 606 if the back can't recline fully:** mount at the
   client's height, recline and watch the clearance, cut with a
   **hacksaw**, file the edges, refit the plug.
3. Plug the FUSION 9-pin into: **LiNX = the Input Module**; **Q-Logic =
   the Enhanced Display**; **R-net / Permobil = Port 1 on the Omni2 Input
   Section** (always the SID port).
4. ASL 165 into the Molex port on the bottom of the FUSION interface.
5. Route cables so seating can't pull or pinch them; **run every seat
   function to its end range before delivery.** Tighten all adjustment
   points periodically.
6. Display: mount, route the cable (Permobil: under the armrest in the
   cable guides), power the chair/Omni2, turn on the FUSION if it
   doesn't come on with the chair, and **check it works before the
   patient sits in the chair.**

Tools: **5/32 in Allen** (swing-away rod length and position), **3/16 in
Allen**, **7/16 in open-end** (wing spot pad angle), hacksaw, file.

## Programming

**R-net (and Permobil), from OBP:** input devices profiles 3 and 4 are
usually set up for Omni. Omni → Port 1: **SID = 3 Prp**; Switches:
**Switch Detect OFF, Switch Long 3, Switch Medium 1, Double Click Time
0.6** (Active Double Click lets you test timing with the user); Controls:
**Actuator Axis L/R or R/L** (e.g. left steps through actuators, right
runs one) and **Axis Direction Toggle Time** (tap the right pad to
reverse the actuator; lengthen it if the client can't get off the pad
within 0.5 s). User switch: hold **1 s = R-net menu**, **3 s = sleep**, a
tap wakes it; double-tap can open the menu instead. A switch in the
FUSION mode port does the same.

**Q-Logic Q3:** Program Adjustments → Enhanced Display → Input
Configuration → **3-Directional Proportional Head (must be selected)**;
Proportional Input: **Center Dead Band ON**; 3-Direction Arrow Toggle:
**Disable Toggle in Drive**; Device Timing: **Device Double Command
Disabled**; D-Sub (9-pin): **Mode Switch Short = Toggle, Long = Mode,
Double = Inactive**. See [[Joystick-Controllers]] (Q-Logic 3 input devices).

**LiNX:** ASL profile, Profile User → Input Module. 4XX joystick or 5XX
display: right jack socket (J2) tip **Input Type = Button**, **Stop While
Driving and Seating ON**, **Input Debounce 0.0**. IN500: User
Configuration = **Proportional Head Array**; Input Pin 6: Stop While
Driving and Seating ON, Momentary, **Short Press = Next Function, Long
Press = Next Profile**. ASL recommends **Stop While Driving and Seating
ON** when next function is selected. See [[LiNX-Diagnostics]].

ASL 165 warning: its mount has a **magnet that can affect ICDs and
pacemakers** nearby.

## Feeds into

[[Alternative-Drive-Controls]], [[R-net-Diagnostics]], [[Joystick-Controllers]],
[[LiNX-Diagnostics]], [[Adaptive-Switch-Laboratories]]
