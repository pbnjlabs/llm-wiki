---
type: source
manufacturer: Bruno
doc_type: Web Article
source: "MANUALS/Clippings/SRE 30502010 Power Folding Rail Logic Board Update.md"
url: https://preview.mailerlite.io/emails/webview/1139128/201142981176067743?signature=791d70bade3061712971b523dd593ae8cfba6ceb7d3ee688b3bc04151c8c56f5
date: 2026-10-13
tags: [bruno, stairlift, sre-3050, sre-2010, folding-rail, power-folding-rail, pcb, limit-switch, dealer-notice, clipping]
---

# SRE-3050 and SRE-2010 Power Folding Rail Logic Board Update

A **Bruno email to authorized dealers**, saved with Obsidian Web Clipper
on 2026-10-13. The email itself isn't dated, so the date above is the
clipping date. It's a web clipping, so by wiki rules it ranks below the
manuals. But it's an official Bruno product-change notice, it's newer
than every Bruno manual on file, and nothing in it conflicts with them.
None of the manuals mention either board number.

## What changed

On **future SRE-3050 (Elan) and SRE-2010 (Elite) power folding rails**,
Bruno is updating the **circuit board logic and the down limit switch
configuration**. The goal is to **stop the carriage moving by accident
at the mid-park** when there's an **open circuit**, such as a broken wire
or an unplugged connector.

- **Board:** the auxiliary power folding rail PCB assembly is now
  **PCB-00193**. It **was PCB-00157**.
- **How to tell which you have:** a **notch around the down limit
  switch** on the folding rail bracket, and the rail's circuit board
  labeled **PCB-00193**. The email's photo shows the old flat bracket
  ("from") and the notched one ("to"), and the label's position on the
  board.
- **Manual folding rails aren't affected.**
- Bruno says the updated schematics will be posted on **Brunopartner**.

## The schematic in the email

The "power folding rail ass'y" diagram marks two changes: the board
(PCB-00193, was PCB-00157) and the **down limit switch symbol**, which is
redrawn. The new symbol looks like a normally closed switch where the old
one looked normally open. That would mean a broken wire now reads as
"at limit" instead of "clear", which fits Bruno's stated goal, **but the
email doesn't say so. That reading is the wiki's.**

Wire colors from the diagram, useful when tracing a fault:

| Circuit | Wires |
|---|---|
| Disable switch (shown in run position) | Orange ×2 |
| Up limit | White, green |
| Down limit | Blue, brown |
| Mid-park | Purple |
| LED | Yellow, black |
| Charge strips (upper and lower), charger | Red, black |
| Folding rail motor (PFRM) | Black, red |

The diagram shows the motor connections separately for left-hand and
right-hand rails.

Raw files: `MANUALS/Clippings/SRE 30502010 Power Folding Rail Logic Board Update.md`,
plus the email's two images saved next to it
(`… - notch and PCB.png`, `… - schematic.jpg`), since the online copies
may not last.

Feeds: [[Folding-Rail]], [[SRE-3050]], [[SRE-2010]]
