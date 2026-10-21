---
type: source
manufacturer: Bruno
model: SRE-2010
doc_type: Tech Tip
source: "MANUALS/Bruno/Tech Tips/Stairlifts/SRE 2010 Troubleshooting Guide- No Power Options.pdf"
url: https://www.brunopartner.com/er26ya59sp/tech-tips.aspx
date: 2016-01-13
tags: [bruno, stairlift, sre-2010, tech-tip, troubleshooting]
---

# Tech Tip - SRE-2010 Troubleshooting Guide (No Power Options)

3-page "unit does not operate" checklist for an SRE-2010 **without power options** (portal tech-tip 36). Same order as the Elan guide ([[Tech Tip - SRE-3000 Elan Troubleshooting Guide]]):

1. Read the 8-segment display ([[Diagnostic-Codes]]).
2. Battery voltage and load test.
3. Charger red light on? Carriage must sit on the contacts **3 s** before the board starts charging. Voltage across the carriage contacts should **rise at least 1 VDC** on the rail contacts; if not, clean contacts and connections, then replace the charger.
4. Yellow charge lights at the rail ends. Needs **18 VDC or more** to run.
5. Board B+/B− (red/black) 18 VDC+? No → breaker, final limit or overspeed.
6. Seat safety: jump the 2 pins. Limits: jump the 3 pins on the limit connector (bypasses **all** limits, keep off the end stops). Rocker: centre pin to either outer pin.
7. **Motor voltage** (blue/orange leads): resting battery 25–27 VDC; at 25 V+ expect **21 VDC up, 12 VDC or more down**. Right voltage → power the motor direct; doesn't run → motor. Low or none → board.
8. IR inputs: red wire of the IR harness to battery ground = **5 VDC**.

Feeds: [[SRE-2010]], [[Stairlift-Troubleshooting]]
