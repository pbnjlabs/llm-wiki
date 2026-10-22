---
type: source
manufacturer: Bruno
doc_type: IPB
source: "MANUALS/Bruno/Parts/ (14 drawings, see _manifest.md)"
url: https://www.brunopartner.com/er26ya59sp/parts.aspx
date: 2026-08-13
tags: [bruno, parts, ipb, exploded-view, stairlift, sre-5000, elan]
---

# Parts Drawings - SRE-5000 Elan

Bruno's assembly drawings (exploded views with parts tables), pulled 2026-10-22 from the Brunopartner parts lookup (Service → Parts Lookup by Serial #). That lookup only takes an exact serial number, so the set was rebuilt from each model's top-level drawing, following assemblies three levels down ([[Bruno-Parts-Lookup]]). **These are Bruno's current revisions**: for an older unit, run its serial on the portal for the parts list as built, or check the manual's exploded view. Dealer prices on the portal are manufacturer suggestions and are not recorded here.

No model-level SRE-5000 drawing exists; the set starts from the carriage with transmitters **SRE-50195WG** (→ carriage **SRE-50120WG**), seat SRE-50070WG, footrest SRE-50095WG, power footrest SRE-50133WG, power swivel SRE-50175LWG, and the rail/folding-rail kits.

- **Gear motor MDC-24035** (24 VDC with brake, keyless gear), **carriage PCB PCB-00180** in motor controller **SRE-50098**. Match the board revision to the serial; see [[SRE-5000]] (gearbox change ECN8485).
- **Batteries 2 × BTR-12010** (12 V 3.2 Ah AGM), circuit breaker sub-assembly SRE-50052, overspeed gear SRE-50113, wheels SRE-50200, IR sensor SRE-50188, remotes **TMR-00004**.
- Options: power footrest actuator **ADC-24008** with aux PCB **PCB-00179**; power swivel actuator SRE-30608 with aux PCB **PCB-00178**; paddle switch SRE-50071WG; gear rack segment SRE-50005.

## Drawings

Each drawing is an exploded view with an item/qty/part/description table. Open the PDF in `MANUALS/Bruno/Parts/<part>.pdf`. "Level" 0 is the model or seed drawing; 1–3 are sub-assemblies found inside it.

| Level | Part | Description | Rev (date) | Pages | Parent |
|---|---|---|---|---|---|
| 0 | SRE-50070WG | top-level drawing | P3 (2026-05-12) | 7 | — |
| 0 | SRE-50095WG | top-level drawing | P1 (2026-03-24) | 4 | — |
| 0 | SRE-50133WG | top-level drawing | P3 (2026-03-24) | 5 | — |
| 0 | SRE-50175LWG | top-level drawing | P2 (2026-02-12) | 4 | — |
| 0 | SRE-50195WG | top-level drawing | 0 (2026-02-04) | 1 | — |
| 0 | SRE-K-5008WG | top-level drawing | P6 (2026-04-16) | 2 | — |
| 0 | SRE-K-5011WG | top-level drawing | P3 (2026-03-17) | 2 | — |
| 1 | SRE-50120WG | CARRIAGE ASSEMBLY (NA)(WARM GREY) | 1 (2026-08-06) | 7 | SRE-50195WG |
| 1 | SRE-50144 | POWER FOOTREST BOARD ASSEMBLY | 0 (2026-02-17) | 1 | SRE-50133WG |
| 1 | SRE-50181 | SEAT POST/SEAT PIVOT PIN ASSEMBLY | 0 (2025-12-04) | 1 | SRE-50133WG |
| 1 | SRE-K-5014 | FOOTREST/SEAT INSTALLATION KIT (POWER SWIVEL) | 0 (2025-10-17) | 2 | SRE-50175LWG |
| 1 | SRE-K-5015WG | FOLDING RAIL ADJUSTABLE STANDFOOT KIT (WARM GREY) | 1 (2026-08-13) | 3 | SRE-K-5008WG |
| 1 | SRE-K-5036 | POWER FOOTREST WIRING KIT | 0 (2025-12-12) | 1 | SRE-50133WG |
| 2 | SRE-50098 | MOTOR CONTROLLER ASSEMBLY (NA) |  | 1 | SRE-50120WG |

## Key service parts

Motors, boards, chargers, batteries, belts, brakes, actuators, switches, remotes, harnesses, gears, nuts, bearings, springs and wheels pulled from the drawings above (hardware omitted). "In" = the drawing(s) that list it.

| Part | Description | In |
|---|---|---|
| ADC-24008 | 24VDC ACTUATOR 1.57" (40mm) STROKE (SRE-5000 PF) | SRE-50133WG |
| BLT-00037 | BLACK RETRACTABLE LAP BELT | SRE-50070WG |
| BTR-12010 | 12V 3.2AH SLA BATTERY (AGM)(.187 TERMINALS) | SRE-50120WG |
| MDC-24035 | 24VDC GEARMOTOR W/BRAKE & KEYLESS GEAR (SRE-5000) | SRE-50120WG |
| PBS-00136 | SPST PUSHBUTTON SWITCH (POS. BREAK) | SRE-50095WG, SRE-50120WG, SRE-50133WG, SRE-50175LWG |
| PBS-00145 | SPST NC PUSHBUTTON SWITCH .75A (.250 X .032 TERM.) | SRE-50070WG |
| PBS-00148 | SPST NC PUSHBUTTON SWITCH .75A (.250 X .032 TERM. SNAP-IN) | SRE-50120WG, SRE-K-5036 |
| PCB-00178 | POWER SEAT SWIVEL AUX. PCB (ROHS) | SRE-50175LWG |
| PCB-00179 | POWER FOLDING FOOTREST AUX. PCB (ROHS) | SRE-50144 |
| PCB-00180 | STRAIGHT RAIL CARRIAGE PCB (ROHS) | SRE-50098 |
| SPR-00101 | COMPRESSION SPRING (.6" OD X .055" WD X 1.25" LG) | SRE-50070WG |
| SRE-21308WG | SEAT BELT BRACKET (WARM GREY) | SRE-50070WG |
| SRE-30237 | PIVOT SWITCH NUT BAR | SRE-50120WG, SRE-50175LWG |
| SRE-30396R | RH TORSION SPRING - FOOTREST | SRE-50133WG |
| SRE-30454 | ARMREST HARNESS | SRE-50070WG |
| SRE-30499 | SEAT CONTROL HARNESS (SRE-3050) | SRE-50070WG |
| SRE-30595 | SWITCH MOUNT PLATE (POWER SWIVEL) | SRE-50175LWG |
| SRE-30608 | POWER SWIVEL ACTUATOR ASSEMBLY (SRE-3050) | SRE-50175LWG |
| SRE-50005 | 8 PITCH GEAR RACK SEGMENT (5/16" WIDTH) | SRE-K-5011WG |
| SRE-50035LWG | BARRIER ARM SWITCH COVER LH | SRE-50070WG |
| SRE-50035RWG | BARRIER ARM SWITCH COVER RH | SRE-50070WG |
| SRE-50045 | FOOTREST LIMIT SWITCH HARNESS (SRE-5000) | SRE-50095WG, SRE-50133WG |
| SRE-50046 | CARRIAGE CHARGE HARNESS | SRE-50120WG |
| SRE-50047 | BATTERY JUMPER (SRE-5000) | SRE-50120WG |
| SRE-50048 | IR SENSOR HARNESS #1 (SRE-5000) | SRE-50120WG |
| SRE-50049 | IR SENSOR HARNESS #2 (SRE-5000) | SRE-50120WG |
| SRE-50052 | CIRCUIT BREAKER SUB-ASSEMBLY | SRE-50120WG |
| SRE-50053 | CARRIAGE POWER HARNESS | SRE-50120WG |
| SRE-50054 | BATTERY HARNESS (SRE-5000) | SRE-50120WG |
| SRE-50055 | CARRIAGE LIMIT SWITCH HARNESS (SRE-5000) | SRE-50120WG |
| SRE-50056 | PCB GROUND HARNESS (SRE-5000) | SRE-50120WG |
| SRE-50057 | CARRIAGE CONTROL/SEAT AUX. HARNESS (SRE-5000) | SRE-50120WG |
| SRE-50060 | MID SWITCHES HARNESS | SRE-50120WG |
| SRE-50061 | SEAT SWIVEL HARNESS (SRE-5000) | SRE-50070WG |
| SRE-50071WG | PADDLE SWITCH ASSEMBLY | SRE-50070WG |
| SRE-50098 | MOTOR CONTROLLER ASSEMBLY (NA) | SRE-50120WG |
| SRE-50099 | MOTOR CONTROLLER MTG. BRACKET (GALV.) | SRE-50098 |
| SRE-50104 | BATTERY BRACKET | SRE-50120WG |
| SRE-50112 | GEAR GUARD | SRE-50120WG |
| SRE-50113 | OVERSPEED GEAR | SRE-50120WG |
| SRE-50126 | ACTUATOR BRACKET | SRE-50133WG |
| SRE-50154 | SEAT SWIVEL HARNESS (POWER FOOTREST) | SRE-K-5036 |
| SRE-50155 | SEAT SWIVEL HARNESS (POWER SWIVEL/FOOTREST) | SRE-50175LWG |
| SRE-50156 | FOOTREST AUX. HARNESS | SRE-K-5036 |
| SRE-50174L | LH ACTUATOR MOUNT WELDMENT (POWER SWIVEL) | SRE-50175LWG |
| SRE-50188 | IR SENSOR ASSEMBLY (ROHS) | SRE-50120WG |
| SRE-50200 | WHEEL ASSEMBLY Ø1.355 X .625 | SRE-50120WG |
| TMR-00004 | IR TRANSMITTER ASSEMBLY W/2 'AA' BATTERIES | SRE-50195WG |

Feeds: [[SRE-5000]], [[Bruno-Parts-Lookup]]
