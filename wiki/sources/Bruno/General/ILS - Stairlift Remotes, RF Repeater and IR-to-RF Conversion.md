---
type: source
manufacturer: Bruno
doc_type: Instruction Sheet
source: "MANUALS/Bruno/Drawings/Stairlifts/ILS-00997.pdf; MANUALS/Bruno/Drawings/Stairlifts/ILS-01449.pdf; MANUALS/Bruno/Drawings/Stairlifts/ILS-01314.pdf; MANUALS/Bruno/Drawings/Stairlifts/ILS-01540.pdf; MANUALS/Bruno/Drawings/Stairlifts/ILS-01552.pdf; MANUALS/Bruno/Drawings/Stairlifts/ILS-01592L.pdf; MANUALS/Bruno/Drawings/Stairlifts/ILS-01592R.pdf"
url: https://www.brunopartner.com/er26ya59sp/drawings.aspx
date: 2023-12-11
tags: [bruno, stairlift, ils, remotes, rf, infrared, repeater]
---

# ILS - Stairlift Remotes, RF Repeater and IR-to-RF Conversion

Remote-control sheets.
- **ILS-00997 (2011), RF (2.4 GHz) troubleshooting**, in order: antenna connector bonded to the metal plate (scrape paint, continuity to a carriage bolt); antenna-to-cable and cable-to-PCB connections; cable continuity centre-to-centre and shield-to-shield, and **no** centre-to-shield short; switch off routers, cordless phones and other 2.4 GHz gear and retest (the system cuts out fail-safe under interference); fit the **patch antenna**; new main PCB and re-learn the original remotes; only then the new remotes.
- **ILS-01449 (4-15-2022), RF repeater:** power it, key switch on; learn the repeater's call/sends to the carriage (LEARN/ERASE under the seat, about 12 s to clear). Interference: SCAN/PROGRAM finds the clearest channel (13, 15 default, 17, 21 shown on LEDs S1/S2); set every remote's DIP 1/2 to match S1/S2. Reset: key off, unplug, hold DISPLAY CHANNEL while powering up.
- **ILS-01540 / ILS-01552, Elan and Elite IR remote reprogramming:** remote DIP **SW3** has four channels (default 1 up, 2 down). Clear: hold LEARN/ERASE until the LED goes out (about 12 s). Learn: hold LEARN/ERASE and press a remote button until the LED goes out (2–5 s). **All remotes on the same DIP setting work after learning one.** Elite: the board is under the seat hinge plate (LH: lower control cover; RH: upper).
- **ILS-01314, IR transmitter wall bracket TMR-00005:** anchors and screws; an optional extra screw stops the remote being pulled out.
- **ILS-01592L/R (12/11/23), CRE-2110 IR-to-RF conversion**, kits **SRV-2110-029L/R**: ESD strap; swap the IR control panel for the **RF control panel CRE-01175L/RWG (keyed)** with the circuit breaker moved across; fit antenna kit CRE-K-2110; test RF remotes.

Feeds: [[Stairlift-Troubleshooting]], [[SRE-2010]], [[SRE-3050]], [[CRE-2110]]
