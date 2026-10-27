#!/usr/bin/env python3
"""Build the wiki's Mobility Scooters Direct parts catalog pages.

Reads what scripts/msd_pull.py saved under MANUALS/MobilityScootersDirect/
and writes one source page per brand:
  wiki/sources/<Folder>/General/Parts Catalog - Mobility Scooters Direct (<Brand>).md

Each page has a part-number table per site model list (linked to the
wiki model page via scripts/msd_model_map.json), then the parts that are
in no model list. Gallery images that look like line drawings (parts
diagrams) are flagged; the test is cached in drawings.json
(solidity, colour count, white share; see is_drawing).

Usage:  python3 scripts/msd_catalog.py [pull date YYYY-MM-DD]
"""
import json
import os
import re
import sys
from datetime import date

from PIL import Image, ImageFilter

RAW = "MANUALS/MobilityScootersDirect"
MAP = "scripts/msd_model_map.json"
SITE = "https://www.mobilityscootersdirect.com"
# brand -> (wiki sources folder, brand parts page, tags)
PAGES = {
    "Pride": ("Pride", "/more/parts/by-brand/pride-parts.html", "pride"),
    "Quantum": ("Pride", "/more/parts/by-brand/quantum-parts.html", "quantum, pride"),
    "Golden": ("Golden", "/more/parts/by-brand/golden-technologies-parts.html", "golden"),
    "Harmar": ("Harmar", "/more/parts/by-brand/harmar-parts.html", "harmar"),
}
TOP = {  # the brand-wide "all parts" lists, not model lists
    "Pride Mobility Parts", "Quantum Parts", "Golden Technologies Parts", "Harmar Lift Parts",
}


def features(path):
    """(solidity, colours, white) for one image.

    solidity: share of non-white pixels that survive a 5x5 erosion (low for
    line art). colours: distinct 4-bit colours in a 200 px thumbnail. white:
    share of near-white pixels.
    """
    im = Image.open(path).convert("L")
    im.thumbnail((900, 900))
    mask = im.point(lambda v: 255 if v < 225 else 0)
    nw = mask.histogram()[255]
    core = mask.filter(ImageFilter.MinFilter(5)).histogram()[255]
    solid = core / nw if nw else 1.0
    rgb = Image.open(path).convert("RGB")
    rgb.thumbnail((200, 200))
    px = [(r >> 4, g >> 4, b >> 4) for r, g, b in rgb.getdata()]
    white = sum(1 for p in px if min(p) >= 14) / len(px)
    return [round(solid, 3), len(set(px)), round(white, 3)]


def is_drawing(f):
    """Thin lines, or a few flat colours on a white background (Pride's coloured parts art)."""
    solid, colours, white = f
    return solid < 0.35 or (solid < 0.6 and white > 0.6) or (colours <= 40 and white > 0.8)


def drawings_for(products):
    path = os.path.join(RAW, "drawings.json")
    cache = json.load(open(path)) if os.path.exists(path) else {}
    for p in products:
        for u in p["images"]:
            f = os.path.join(RAW, "images", p["pull_brand"], u.rsplit("/", 1)[-1])
            if isinstance(cache.get(f), list) or not os.path.exists(f):
                continue
            try:
                cache[f] = features(f)
            except Exception:
                cache[f] = [1.0, 999, 0.0]
    json.dump(cache, open(path, "w"), indent=0)
    return cache


def cell(s):
    return (s or "").replace("|", "/").strip()


def row(p, cache):
    draw = [f.rsplit("/", 1)[-1] for f in
            (os.path.join(RAW, "images", p["pull_brand"], u.rsplit("/", 1)[-1]) for u in p["images"])
            if is_drawing(cache.get(f, [1.0, 999, 0.0]))]
    pn = p.get("part_number") or ""
    if p.get("oem", "").lower().startswith("no"):
        pn += " (not OEM)"
    return f"| {cell(p.get('name'))} | `{cell(pn)}` | {', '.join(f'`{d}`' for d in draw)} | [link]({p['url']}) |"


def main():
    pulled = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    products = {}
    for line in open(os.path.join(RAW, "products.jsonl")):
        p = json.loads(line)
        products[p["url"]] = p
    cats = json.load(open(os.path.join(RAW, "categories.json")))
    mp = json.load(open(MAP))
    cache = drawings_for(products.values())
    head = "| Part | OEM part no. | Drawing (image file) | Product page |\n|---|---|---|---|"
    summary = {}

    for brand, (folder, parts_page, tags) in PAGES.items():
        bc = {u: c for u, c in cats.items() if c["brand"] == brand}
        allparts = {u for c in bc.values() if c["title"] in TOP for u in c["products"]}
        model_lists = [(u, c) for u, c in bc.items() if c["title"] not in TOP and c["products"]]
        in_model = {u for _, c in model_lists for u in c["products"]}
        listed = [u for u in allparts | in_model if u in products]
        ndraw = sum(1 for u in listed if row(products[u], cache).split("|")[3].strip())
        out = []
        out.append(f"""---
type: source
manufacturer: {"Pride" if brand == "Quantum" else brand}
doc_type: Parts Catalog
source: "{RAW}/products.jsonl"
url: {SITE}{parts_page}
date: {pulled}
tags: [{tags}, parts, part-numbers, retailer]
---

# Parts Catalog - Mobility Scooters Direct ({brand})

OEM part numbers for **{brand}** parts sold by Mobility Scooters Direct
(mobilityscootersdirect.com), a **third-party retailer**. Pulled
{pulled} with `scripts/msd_pull.py`: **{len(listed)} parts**, grouped
by the site's per-model parts lists. **{ndraw}** of them have a gallery
image that looks like a parts drawing (usually a cut-out of the
manufacturer's own diagram, with a retailer watermark); the file names
are in the table, under `{RAW}/images/` (local only, not in git).

**How much to trust it.** It's a retailer, so it ranks like a web
clipping: a manufacturer manual, IPB or parts guide wins any conflict.
The site's compatibility lists are thin (often one model, sometimes just
the brand), and the per-model lists below are the retailer's grouping,
not the manufacturer's. **Confirm the part number by serial number** with
the manufacturer before ordering. Prices are deliberately left out.
See CLAUDE.md, "Third-party parts retailer".
""")
        out.append("## By model\n")
        for u, c in sorted(model_lists, key=lambda x: x[1]["title"].lower()):
            rows = [products[x] for x in c["products"] if x in products]
            if not rows:
                continue
            link = mp.get(c["title"])
            summary.setdefault(link, []).append((brand, c["title"], len(rows)))
            out.append(f"### {c['title']}\n")
            out.append((f"Wiki page: [[{link}]]. " if link else "No wiki model page. ") +
                       f"Site list: [{c['title']}]({u}).\n")
            out.append(head)
            out += [row(p, cache) for p in sorted(rows, key=lambda p: (p.get("name") or "").lower())]
            out.append("")
        rest = sorted((products[u] for u in allparts - in_model if u in products),
                      key=lambda p: (p.get("name") or "").lower())
        if rest:
            out.append("## Not in a model list\n")
            out.append("Parts on the brand's parts list that the site doesn't file under any "
                       "one model (batteries, chargers, controllers, universal parts and so on).\n")
            out.append(head)
            out += [row(p, cache) for p in rest]
            out.append("")
        d = f"wiki/sources/{folder}/General"
        os.makedirs(d, exist_ok=True)
        with open(f"{d}/Parts Catalog - Mobility Scooters Direct ({brand}).md", "w") as f:
            f.write("\n".join(out))
        print(f"{brand}: {len(listed)} parts, {ndraw} with drawings, {len(model_lists)} model lists")
    json.dump({str(k): v for k, v in summary.items()}, open(os.path.join(RAW, "model_summary.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
