---
type: source
manufacturer: Pride
doc_type: Quick Reference
source: "MANUALS/Pride/Controllers/Q-Logic/infinfb2435_q-logic_firmware_upgrade_quick_operational_sheet.pdf"
date: 2010-02
tags: [pride, quantum, q-logic, ne-plus, firmware, pcps]
---

# Q-Logic Firmware Update Reference Guide (INFINFB2435)

10-page illustrated guide to updating **Q-Logic and NE+** firmware with
the **PC Programming Station**, INFINFB2435/Rev A/February 2010.

Steps: set a **device firmware search path** once (Options > Settings);
connect the USB programming cable to any charger port; connect; **save
the client's program first** (File > Save As); Update Firmware, tick the
modules, **untick "Migrate actual program after update"**, Start
Update; **don't power off** until "Please switch the system off and on.
All updates finished." (the hand control or display may go dark while
the bars keep building); disconnect, power off 5 s, reconnect; then
**restore the power base program (.CPF) with Advanced Cloning on**,
repeat for the actuator module; finally restore the client's own file
**with Advanced Cloning off**. Firmware and .CPF files come from
prideservice.com (dealer login).

Feeds into: [[Q-Logic-Firmware-Updates]].
