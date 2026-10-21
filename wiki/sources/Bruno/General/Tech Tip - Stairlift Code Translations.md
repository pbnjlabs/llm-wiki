---
type: source
manufacturer: Bruno
doc_type: Tech Tip
source: "MANUALS/Bruno/Tech Tips/Stairlifts/Code-Translations.pdf"
url: https://www.brunopartner.com/er26ya59sp/tech-tips.aspx
date: 2020-07-21
tags: [bruno, stairlift, tech-tip, diagnostics, sre-2010, cre-2110]
---

# Tech Tip - Stairlift Code Translations

2-page Bruno Technical Service write-up (2020; portal tech-tip 214, "Diagnostic Codes for the SRE-2010 and CRE-2110") explaining the code display. Its main point: **a code isn't necessarily a failure**. Many show during normal running.

- **Normal:** C1 parked/charging, C2 running, C3 parked between charge stations (SRE-2010E, CRE-2110), L1 seat swivelled, L2 top, L3 bottom, L6 mid-park (CRE/SRE-2010E or folding rail), **L7 running**, **L8 at the end of the rail**, O1/O2 rocker, O4/O5 remote input.
- **Problem:** C4 not charging when parked, C5/C6 batteries bad or not charging, D1 speed pot jumper or pot (old units), D2 erase and reprogram remotes, **D4 brake not releasing or overspeed engaged mechanically only**, D7 bad batteries, D8 remote needs programming, any F = board, P0 communication (bad connection in the comm circuit).
- **Normal codes that shouldn't be there:** C3 parked at an end, L1 in the riding position, L2 at the bottom or L3 at the top.
- **Beeps:** 3 short 2 long = parked, charger not detected; 2 short 3 long = battery critical (~16 V); **1 short every 3 s = seat safety open**; **1 beep on rocker/remote = up or down limit open**; 3 short over-temperature; 4 short over-current; 5 short low voltage stop; **1 short 2 long = transmitter memory full**.

Agrees with the manuals' table except two small wording differences (L7 isn't in the manual; L8 there is "soft stop"). See [[Diagnostic-Codes]].

Feeds: [[Diagnostic-Codes]], [[Stairlift-Troubleshooting]]
