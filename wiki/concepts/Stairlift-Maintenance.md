---
type: concept
tags: [stairlift, maintenance, bruno, grease, battery, overspeed, joint-commission]
---

# Stairlift Maintenance (Bruno)

Yearly service on Bruno stairlifts: what to check, which grease, batteries
and remotes, and overspeed testing. Built from the model manuals and
Bruno's dealer-portal tech tips. **The model's own manual wins** over the
tech tips, which are mostly 2008–2016.

PMS follows the Joint Commission DMEPOS standards: preventive maintenance
**at set intervals, per the manufacturer**, and a record of it
([[Joint-Commission-DMEPOS]]). For stairlifts, "per the manufacturer"
means the yearly list below.

## How often

**At least once a year**, by an authorized Bruno dealer. The SRE-3050
operator manual tells the owner to have it "examined, cleaned and
lubricated" yearly ([[SRE-3050 Operator Manual]]). Regrease the gear rack
more often on heavily used or harsh-environment units.

**ASME A18.1-2017 units:** the SRE-3050 install manual and tech support
guide point to Bruno's **ILS-01446, Maintenance Control Plan for CRE/SRE
Chair Lifts**, for units that need ASME A18.1-2017 or newer compliance.
It's now on file (Rev 4, 04/20/26):
[[ILS-01446 Maintenance Control Plan for CRE-SRE Chair Lifts]]. It covers
**every CRE and SRE model** and must be **kept with the unit's manuals**
for inspectors.

| What | How often (ILS-01446) |
|---|---|
| Operational checklist (controls, stops, diagnostics, belt, charger, seat switch, safety panels, wheels, key switch, breaker, noise, clean rail and contacts) | **Weekly**, by authorized personnel (optional for residential Section 7 lifts) |
| Clean rail charge contacts (rubbing alcohol) | Every 6 months |
| Rail mount hardware, **regrease gear rack (PTFE)** | Yearly |
| Routine inspection and tests (A18.1 10.2) | **6 months commercial (Section 4), 1 year residential (Section 7)** |
| Periodic tests: safety panels, governor/overspeed, normal and final stops (10.3.1) | **Yearly** |
| Governor test with a dated metal tag; **brake test at 125% of rated load** (10.3.3) | **Every 5 years** |
| Keep the checklist log and the maintenance/repair log (malfunctions, accidents, work done) | **5 years minimum** |

Rail: clean with **Pledge**; contacts and soft-stop strips with
**rubbing alcohol**. A cyclic clunk or squeak about every 5 in is a flat
or damaged wheel.

## Yearly checklist

The SRE-3000 manual's list ([[SRE-3000 Installation Manual]]) is the
fullest; the CRE-2110 manual and Bruno's 2008 sheet
([[Tech Tip - Stairlift Yearly Maintenance and Customer Checklist]]) are
shorter versions of it.

- [ ] Clean rails, gear rack and wheels; **regrease the gear rack**.
- [ ] Rail wear: there should be no groove. (2008 sheet: dry or worn
  belts on belt-drive units; lubricate.)
- [ ] Clean the **charging contacts** on carriage and rail ends with
  lightweight Scotch-Brite. Check the charging system for corrosion or
  wear.
- [ ] **Battery load test**. Batteries charging and holding charge.
- [ ] Safety switches: **overspeed operation**, limit switches, footrest,
  carriage, seat rotation switch.
- [ ] Armrest (rocker) switch, barrier-arm switches, key switch.
- [ ] **Charger output**, load test on the remotes: voltage while
  travelling up, against the contacts, away from them; contacts and
  lights.
- [ ] Speed and ride quality.
- [ ] Seat belt wear and operation.
- [ ] Exposed wiring: cuts or abrasions.
- [ ] Seat swivel moves easily and locks.
- [ ] Critical hardware at its torque values.
- [ ] **Replace the 9 V call/send transmitter batteries** (SRE-3000
  manual; Bruno's RF remote tip says the same, yearly).

Owner care between visits (SRE-3050): keep the rail channel clean, wipe
the rail (not the gear rack) with Pledge lemon or a similar wax cleaner
monthly, and keep the charger plugged in.

## Grease

| Source | Gear rack grease |
|---|---|
| [[SRE-3050 Install Manual]] (2026) | **PTFE grease (provided)**, thin layer, gear rack only |
| [[SRE-3000 Installation Manual]] (2015) | **White lithium**, gear rack only (Lubriplate on the end-cap screws; Magnalube on one slotted part) |
| [[CRE-2110 Install Manual]] (2018) | **White lithium**, rack teeth only, about once a year |
| TechMate ([[Stairlift-Troubleshooting]]) | Magnalube, after cleaning off old grease and dust |
| [[Tech Tip - Stairlift Grease Specifications]] (older) | Lubriplate **130-AA** shipped; **630-AA** for high temperatures |
| [[Tech Tip - SRE-2010 Quick Install Guide (Old Style Rail)]] | Lubriplate, a bead 6 in on, 6 in off |
| [[ILS-01446 Maintenance Control Plan for CRE-SRE Chair Lifts]] (2026) | **PTFE, gear rack teeth only, yearly, all CRE and SRE models** |

**Settled (2026-10-21):** Bruno's current maintenance control plan
(ILS-01446 Rev 4, April 2026) says **PTFE grease on the gear rack for
every CRE and SRE unit**. It's newer than the 2015 SRE-3000 and 2018
CRE-2110 manuals' white lithium, so **use PTFE**. The Lubriplate and
Magnalube notes are older or from TechMate. Bearings in the SRE-2010
wheel kit get Magnalube-G ([[ILS - Stairlift Carriage Wheels]]).

## Batteries

House standard: **replace every battery in the unit**, as a matched set
([[Mobility-Batteries]]).

| Model | Batteries |
|---|---|
| [[SRE-3000]] | 2 × 12 V **3 Ah**, Bruno BTR-12008 = **MK ES3-12** ([[Tech Tip - SRE-3000 Battery (MK ES3-12, BTR-12008)]]) |
| [[SRE-3050]] | 2 × 12 V 3 Ah sealed lead-acid (part number not confirmed) |
| [[SRE-2010]], [[CRE-2110]], [[CRE-2100]] | 2 × 12 V **7 Ah** sealed lead-acid |

- **Life:** about **3–5 years**, shorter with deep discharges (heavy
  rider, many trips). An Elan gets about **10–15 trips** per charge
  ([[Tech Tip - SRE-3000 Battery Life]]).
- Keep the charger plugged in. The ES3-12 should only be charged at
  0–40 °C (32–104 °F).
- **Elan run limits:** at least 23 V to go up, 21 V down; the controller
  cuts out under load at about 16 V
  ([[Tech Tip - SRE-3000 Elan Troubleshooting Guide]]).

## Remotes

9 V alkaline (Energizer, Rayovac, Duracell). A remote still works down to
4 V. Replace yearly. High-power X-Bee Pro remotes drain batteries faster.
See [[Tech Tip - Stairlift RF Remote Battery Issues]].

## Overspeed testing

Field reset and the trip-key test are on [[Overspeed-Safety-Brake]];
ILS-01446 gives the current field test for every model (trip key
**SRE-20770** for SRE units; ruler on the reset arm or a magnet retriever
for CRE units). Where the final limit must be tested with the end cap on,
see [[ILS - Final Limit Compression System]]. The tech tips add two older methods: the
**SRE-2010C drop test** with kit **SRV-2010-018** (must stop within
1.5 in) and, for SRE-1540/1550/2000, the **duct-tape** and **96 V test
fixture** methods. Follow state and local load and witness rules.

## Savaria K2 / K2 Plus

The K2 install guide and K2 Plus Maintenance Control Program set **6-month**
checks (limits, sensors, seat, remotes; everything on the K2 Plus MCP) and
yearly technician items on the K2 (overspeed, rollers, rack, brackets).
**Rollers: Super Lube synthetic or wet graphite grease; swivel: wheel bearing
grease; replace angle rollers every 3 years.** Seat post bolts 40 ft-lb.
Outdoor units every 6 months (3 in extreme environments): Nu Finish wax,
Fluid Film, dielectric grease on the charging strips. See [[K2]] and
[[K2-Plus]].

The owner's manuals add: **K2** ([[K2 Stairlift Owner's Manual (001022)]], 2016) owner checks every **3
months** (monthly in adverse environments), technician items every 6
months, angle rollers every 36 months. **K2 Plus** ([[K2 Plus Stairlift Owner's Manual (001188)]], 2024)
**commercial every 6 months; residential yearly for normal use (up to 10
cycles a day), every 6 months for heavy (25) or excessive (40) use**.

## Joint Commission

Record each visit (date, checks done, parts, batteries). At delivery,
Bruno's 2008 sheet doubled as the **customer inspection and training
checklist**: undamaged seat, rail and paint; charger light on; shown the
warranty, belt, rocker, footrest and final limit switches, lights,
breaker, swivel latch and remotes. That covers the Joint Commission's
setup and patient-training points ([[Joint-Commission-DMEPOS]]).
ILS-01446's weekly checklist log and maintenance/repair log (kept 5
years) are a ready-made format for the Joint Commission's maintenance
records.

## See also

[[Stairlift-Troubleshooting]], [[Diagnostic-Codes]], [[Folding-Rail]],
[[Overspeed-Safety-Brake]], [[Mobility-Batteries]], [[Bruno]]
