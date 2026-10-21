---
type: source
manufacturer: Bruno
model: VPL-3100B
doc_type: Tech Tip
source: "MANUALS/Bruno/Tech Tips/VPL/DC VPL Troubleshooting Guide -1st to current (revised 4-19-10).pdf; MANUALS/Bruno/Tech Tips/VPL/DC VPL Troubleshooting Guide -10040300370 to current (revised 3-19-10).pdf"
url: https://www.brunopartner.com/er26ya59sp/tech-tips.aspx
date: 2011-03-01
tags: [bruno, vpl, tech-tip, troubleshooting, dc, legacy, vpl-3153b, vpl-3175b]
---

# Tech Tip - Low-Rise DC VPL Troubleshooting Guides (2010-2011)

Two near-identical 11-page guides (rev 4/19/2010, and rev 3/1/2011 titled "10040300370 to current"; portal tech-tips 192 and 193, whose titles are swapped against the files) for **DC low-rise VPLs** (VPL-3153B/3175B, the [[VPL-3100B]] family) **before the 2012 control change**. TechMate only supports these from serial 12070300110 (3153B) / 12070300109 (3175B), so these cover the older ones.

Steps (TB1-1 is ground):
1. **24 VDC minimum** at J1 (red/black). None → breaker, final limit.
2. TB1-2: fuse (**3 A**). TB1-4: top cap switch (pull up = service position). TB5-2: platform E-stop. TB5-1: nut safety switch. TB3-5: upper gate closed. TB3-4: upper gate locked (platform **not** at the top).
3. **Jump TB2-1 to TB1-7 = up (bypasses the upper limit); TB2-1 to TB5-6 = down (bypasses the lower limits).** Starts at once.
4. **Motor:** unplug the motor leads at the top of the box and apply **12–24 VDC**: + orange / − blue runs up; reversed runs down.
5. Upper limit TB1-7 to TB1-8; up switch TB2-1 to TB1-8 (6 in or more below the top); under-panel TB5-3 to TB5-4; lower limit TB5-5 to TB5-6 (6 in or more above the bottom).
6. **Up relay:** motor unplugged, jump the green wire terminal to the upper red: it should click. Contacts (batteries and motor off, red jumper off): upper open, lower closed. **Down relay** the same with the blue wire.
7. Interlock: 24 VDC at pins 3–4 needs the bottom tower limit made; jump 1–2.
8. **Charger:** all four lights flashing → unplug from the wall **and** the batteries for about a minute; still flashing → replace the charger. Only the red power light flashing → AC lost (outlet, plug).

Bypass the gate: jump TB3-4 to TB3-6, or blue to green at the gate harness plug.

Feeds: [[VPL-3100B]], [[VPL-Troubleshooting]], [[Battery-Charger-LED-Diagnostics]]
