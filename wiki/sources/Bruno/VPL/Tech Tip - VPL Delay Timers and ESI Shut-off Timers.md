---
type: source
manufacturer: Bruno
doc_type: Tech Tip
source: "MANUALS/Bruno/Tech Tips/VPL/VPL DELAY TIMERS.pdf; MANUALS/Bruno/Tech Tips/VPL/TALL VPL ESI Timers Ron Dries.pdf; MANUALS/Bruno/Tech Tips/VPL/VPL Shutoff Timer Notes.pdf"
url: https://www.brunopartner.com/er26ya59sp/tech-tips.aspx
date: 2016-01-13
tags: [bruno, vpl, tech-tip, timers, interlocks, electric-strike, door-operators]
---

# Tech Tip - VPL Delay Timers and ESI Shut-off Timers

Three Bruno notes (portal tech-tips 141, 125, 151) on the **timers** that power door interlocks, electric strikes and door operators for a set time at a landing.

**Delay timers (residential and commercial):**
- A "one-shot" timer: the start input (Y1) going low then high switches its relay for the set time. Bruno triggers it from the landing call buttons.
- **Required** on every **residential** VPL with a platform gate operator, landing gate operator or door operator; **recommended** for electric strike interlocks. **Commercial** VPLs have a relay that does this, so a timer is only recommended there for **electric strikes** (longer strike life).
- Why: keeping power on an interlock shortens its life. The timer gives the user time to get through, then cuts power.
- **One per landing** on residential units. It can run a door interlock (**not** Waupaca EMI III or Honeywell RDI2), a door, gate or platform-gate operator, or a door with both (Bruno's door operators power the interlock themselves).
- Factory settings: **3 s for door operators, 6 s for interlocks**; adjustable in the field up to about 30 s.
- **Door locked at your landing?** Press the landing button for at least 1 s to restart the timer.

**ESI (electric strike interlock) timers on tall VPLs:** the timer starts only when **both** the landing's interlock limit switch in the tower **and** a call or platform button are made. It then unlocks for the set time (6 s factory) and times out. **Its LED blinking with only the limit made just means it has power**, not that it's active, so testing by pressing only the tower switch looks like a dead timer.

**ESI shut-off timer kits (tall VPLs only, field-retrofittable, 24 VDC or 24 VAC):** VPL-K-3222 single, VPL-K-3223 dual, VPL-K-3225 add-on (up to 3 per enclosure). Recommended at each landing with an electric strike (e.g. the Von Duprin on the flush-mount doors); each landing also needs the extra limit switch from its interlock wiring kit. **Not needed for EMI interlocks (Waupaca, Porta, Honeywell RDI2) or GAL interlocks.** Two knobs: time range (e.g. 1–10 s) and percentage of range (6 ≈ 6 s).

Feeds: [[Gate-and-Door-Interlocks]], [[VPL-Troubleshooting]]
