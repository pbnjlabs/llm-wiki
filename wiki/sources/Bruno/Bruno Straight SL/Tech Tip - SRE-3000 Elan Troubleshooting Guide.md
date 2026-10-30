---
type: source
manufacturer: Bruno
model: SRE-3000
doc_type: Tech Tip
source: "MANUALS/Bruno/Tech Tips/Stairlifts/Stairlift SRE 3000 Elan Troubleshooting Guide.pdf"
url: https://www.brunopartner.com/er26ya59sp/tech-tips.aspx
date: 2016-01-13
tags: [bruno, stairlift, sre-3000, elan, tech-tip, troubleshooting]
---

# Tech Tip - SRE-3000 Elan Troubleshooting Guide

> **Later version:** [[Training - SRE-3050 Elan Troubleshooting Guide]] (10/17/19, Bruno training library) adds a motor brake test and a phone-camera remote test, and gives one motor-voltage figure (20 V+ at 26 V resting).

2-page "unit does not operate" checklist for the SRE-3000 Elan (portal tech-tips 51 and 161 link this same file).

1. **Battery:** load test. **At least 23 V to run up, 21 V to run down.** The controller cuts out under load at **about 16 V**.
2. **Charger LED** red, yellow or green? None → incoming power. The unit must be **on for 3 s** before the board starts charging. The charger needs **at least 4 V** from the batteries to turn on, and turns on below **26.5 V**. With the charger connected, then disconnected, the battery voltage should differ by **at least 1 VDC**. No difference with the red light on → check every lead back to the board, clean the contacts, then replace the charger.
3. Inspect and clean carriage and rail contacts. Battery voltage should be there if the board's charge circuit and fuse are good.
4. Board B+/B− **18 V or more**? No → breaker, battery fuse, final limit or overspeed.
5. **Key switch** horizontal = on. Off gives a limit beep both ways (it's in series with the limit common).
6. Limits: jump the 3 pins (both armrests down). Barrier-arm switches only affect the rocker, so test with a remote too.
7. Seat switch / rocker (5-wire harness): jump the 2 pins nearest the board corner, then centre pin to either outer pin. **Never jump all the pins together**, it can damage the board.
8. **Motor voltage** (blue/brown leads): rest 25–27.5 V; at 25 V+ expect **23–24 V up, 12–13 V or more down**. Direct power to the motor only very briefly (the brake overheats). Doesn't run → motor. Low or none → board.
9. IR inputs: red wire to battery ground = **5 V**.

Feeds: [[SRE-3000]], [[Stairlift-Troubleshooting]]
