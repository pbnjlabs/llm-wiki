---
type: concept
tags: [pride, quantum, q-logic, q-logic-3, ne-plus, firmware, programming, pcps, hhp, cloning]
---

# Q-Logic Firmware Updates

How to update firmware on Pride/Quantum Q-Logic-family electronics and
keep the chair driving the same afterwards. Provider/technician work
only: Pride warns that the controller program sets speed, acceleration,
braking and stability.

Sources: [[Q-Logic Technical Manual (INFMANU3580)]] (Appendix E, 2008),
[[Q-Logic Firmware Update Reference Guide (INFINFB2435)]] (2010, PCPS),
[[Q-Logic Gen2 HHP Firmware Update Training (EDU0107-77)]] (hand-held
programmer), [[Updating the Q-Logic 3 HHP (EDU0107-131)]], and the 2009
compatibility charts.

## The one rule: save, update, restore with Advanced Cloning

Every legacy Q-Logic / NE+ procedure has the same shape:

1. **Save the client's current program** (.CPF) before touching
   anything.
2. Update the firmware of the chosen modules. **Don't switch the chair
   off** until the programmer says all updates are finished; the hand
   control or display may go dark while it works.
3. Power off **4–5 s**, power on, reconnect.
4. **Restore the factory program for the power base with Advanced
   Cloning ON** (then the actuator module's file, if there is one).
   Advanced Cloning writes the hidden OEM parameters the new firmware
   needs; Pride says it **must** be done after a firmware upgrade or the
   chair may not drive properly.
5. Restore the **client's own** saved program, **Advanced Cloning OFF**.
6. Power-cycle and **test every function**, including tilt and other
   actuators.

Factory program files are named for the base and seating, e.g.
"Q6000 High Torque Actuators 126.CPF" and "20_tilt_DWR1111H150.CPF"
(the AAM file is named by its configuration number,
[[Q-Logic-Seat-Configuration]]).

## Legacy Q-Logic and NE+ with the PC Programming Station

Tools: Curtis **CAN-USB interface** (ELEASMB5216), the **1314 PC
Programming Station** (1314-3302), firmware **.cag** files and program
**.cpf** files from Quantum (prideservice.com, dealer log-in). **Don't
rename .cag files**: the programmer won't recognize them. Module file
names: power base 1750-3509, hand control 1751-0009 (HW4 or HW5),
AAM 1754-6009, Enhanced Display 1753-2309, SAJ 1752-1109, Sip & Puff
1757-0009, HHP 1311-3309.

1. Make a firmware folder and add it to Options > Settings > **Device
   Firmware Search Path** (once).
2. Plug the interface into any charger/programming port (hand control,
   Enhanced Display or charger harness); power on; connect (F2 uploads
   the chair's program).
3. Save the .cpf. Click **Update Firmware**; the newest files in the
   search path fill in automatically (or pick them). Tick the modules.
   **Untick "Migrate actual program after update"** (2010 guide).
4. Start Update; the display shows IDLE MODE. Wait for "All updates
   finished".
5. Power off 4–5 s, on; refresh (F5). Open the factory .cpf, **Save to
   Connected System** (F6), tick every device **and Advanced Cloning**,
   accept the warnings (about a minute). Repeat for the AAM file.
6. Restore the client's file without Advanced Cloning. Check the System
   Overview shows the new versions (e.g. power base V1.26).

## Legacy Q-Logic with the Gen 2 hand-held programmer

Copy the .cag files into the HHP's **Firmware** folder over USB. On the
chair: **System Info** (current versions) > **File Manager > Firmware
Update**, tick modules, Select Version from Internal > Firmware,
**Migrate**: the HHP saves every module's .CPF first, then loads the
firmware and asks for a power cycle. Then **File Manager > Restore
.CPF** > Internal > Programs > base file, answer **YES to Advanced
Cloning**, power-cycle. Re-clone the saved client file if needed.

## Compatibility (2009 charts)

Each row of Pride's charts is a set of versions that work together; the
power base version picks the row ([[Q-Logic Firmware Compatibility List (2009)]], [[NE+ Firmware Compatibility List (2009)]]).

- **Q-Logic Powerbase 100:** rows for 1.17, 1.26, 1.49, 2.19, 2.26,
  2.42, 2.43, 2.45. On **1.17–1.49 the AM1, AM2, LM2 and light modules
  aren't supported**; they need 2.19 or later. HHP 2.13–2.26; PCPS 4.0.14
  build 16 through 4.0.1 build 529 (builds 527/529 for 64-bit Vista).
- **NE+ Power Base 75:** rows for 1.06, 1.09, 1.10, 1.11, with hand
  controls J/AJ/LJ, attendant, light module, AM1, AM2, LAM2. HHP
  2.25/2.26.
- Mixing versions from different rows gives incompatible-module faults
  (legacy #20, #136, #157, #234; Q-Logic 3 #42) ([[Q-Logic-Fault-Codes]]).

## Q-Logic 3

- **Programming tools:** Econ-W (Windows, cable or Bluetooth), Econ-I
  (iOS, user level) and the Q-Logic 3 HHP
  ([[Q-Logic-3-Bluetooth-and-Remote-Programming]]). Q-Logic 3 #42
  "module with incompatible firmware" means update everything to the
  **latest firmware pack**; #220 is a failed hardware-version check
  during an update.
- **Updating the Q-Logic 3 HHP itself:** drag the two emailed files
  onto the HHP (it mounts as a removable disk), replug to start the
  update, then **register** it: plug into a Q-Logic 3 chair, Register
  gives a 12-digit key; enter it on the Quantum **Cloud** (Device
  Management > Registration of HHP(1313) > Add), type the code the
  Cloud returns into the HHP (dashes included; **move the cursor to
  Space before OK**), then set the HHP to **Dealer**.
- No Q-Logic 3 chair-firmware procedure is on file.

## See also

[[Joystick-Controllers]], [[Q-Logic-Fault-Codes]],
[[Q-Logic-Seat-Configuration]],
[[Q-Logic-3-Bluetooth-and-Remote-Programming]]
