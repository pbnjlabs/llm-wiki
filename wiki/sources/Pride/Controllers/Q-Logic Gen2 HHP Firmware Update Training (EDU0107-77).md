---
type: source
manufacturer: Pride
doc_type: Training
source: "MANUALS/Pride/Controllers/Q-Logic/edu0107-77_rev_0_firmware_update_gen2_training.pdf"
date: unknown
tags: [pride, quantum, q-logic, firmware, hhp, training]
---

# Q-Logic Gen2 HHP Firmware Update Training (EDU0107-77)

43-slide Quantum education deck, EDU/0107-77 Rev 0 (undated; refers to
"Q-logic Downloads 2012" on prideservice.com). Updating a **Q-Logic**
chair with the **Gen 2 hand-held programmer** instead of a PC.

Needs: Gen 2 HHP, its USB cable, its chair cable, a Windows PC.
Download all firmware plus the Powerbase, AAM, AM1, AM2 and LAM2 program
files from prideservice.com (Quantum Rehab > Q-logic Downloads), copy
the firmware (.cag) into the HHP's **Firmware** folder over USB. On the
chair: System Info to read current versions; File Manager > Firmware
Update, tick modules, pick the new version from Internal > Firmware,
**Migrate**: the HHP first **saves the current .CPF of every module**,
then downloads firmware and asks for a power cycle. Then File Manager >
**Restore .CPF**, pick the base program (Internal > Programs > base
100), answer **YES to Advanced Cloning** (it overwrites hidden OEM
parameters and **must be done after upgrading firmware**), power cycle.
Re-clone the client's saved file if needed.

Feeds into: [[Q-Logic-Firmware-Updates]].
