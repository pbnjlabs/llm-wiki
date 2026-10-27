#!/usr/bin/env python3
"""Pull OEM part numbers and parts drawings from Mobility Scooters Direct.

mobilityscootersdirect.com is a third-party parts retailer. Its product
pages give the OEM part number, the compatible models and a gallery that
is often a cut-out of the manufacturer's own parts drawing. This pulls,
read-only, for the brands the wiki covers:

  1. the brand's parts category pages (model -> products), paged 25 at a time
  2. every product page for the brand listed in the site's sitemap
  3. every gallery image

Nothing is added to a cart or submitted. Prices are deliberately not kept.
Robots.txt allows these paths; requests are spaced out (DELAY).

Usage:  python3 scripts/msd_pull.py [MANUALS/MobilityScootersDirect]

Writes <out>/categories.json, <out>/products.jsonl (one product per line;
the run resumes where it stopped) and <out>/images/<brand>/<file>.
Raw output stays under MANUALS/ (gitignored).
"""
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

SITE = "https://www.mobilityscootersdirect.com"
DELAY = 1.5        # seconds between page requests
IMG_DELAY = 0.5    # seconds between image requests
UA = "Mozilla/5.0 (X11; Linux x86_64) PMS-wiki parts lookup"

# brand key -> (product path prefix, parts category prefixes)
BRANDS = {
    "Pride": ("/pride-mobility/", ["/more/parts/by-brand/pride-parts"]),
    "Quantum": ("/quantum/", ["/more/parts/by-brand/quantum-parts"]),
    "Golden": ("/golden-technologies/", ["/more/parts/by-brand/golden-technologies-parts"]),
    "Harmar": ("/harmar/", ["/more/parts/by-brand/harmar-parts",
                            "/more/parts/vehicle-lift-parts/vehicle-lift-parts-by-brand/harmar-lift-parts"]),
}


def get(url, binary=False, delay=DELAY):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            time.sleep(delay)
            return data if binary else data.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(10 * (attempt + 1))
        except Exception:
            time.sleep(10 * (attempt + 1))
    return None


def text(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def sitemap():
    xml = get(SITE + "/sitemap.xml")
    return re.findall(r"<loc>(.*?)</loc>", xml)


def parse_product(url, h):
    p = {"url": url}
    m = re.search(r'<script type="application/ld\+json">(\{"@context[^<]*"@type":"Product".*?)</script>', h, re.S)
    if m:
        try:
            ld = json.loads(m.group(1))
            p["name"] = ld.get("name")
            p["brand"] = (ld.get("brand") or {}).get("name")
            for k, v in ld.items():
                if "sku" in k or "mpn" in k:
                    p["part_number"] = v
        except json.JSONDecodeError:
            pass
    m = re.search(r'<div class="sku_brand">(.*?)</div>', h, re.S)
    if m:
        p["model_line"] = text(m.group(1))   # e.g. "Model: Pride Mobility | FRMASMB14082"
    m = re.search(r'class="product description product-item-description">(.*?)</div>', h, re.S)
    if m:
        bullets = [text(b) for b in m.group(1).split("<br")]
        bullets = [re.sub(r"^/?>?\s*-\s*", "", b).strip() for b in bullets if b]
        oem = [b for b in bullets if b.lower().startswith("oem replacement")]
        if oem:
            p["oem"] = oem[0].split(":", 1)[-1].strip()
        p["bullets"] = [b for b in bullets if b and not re.search(
            r"price|tax-free|free shipping|ships within", b, re.I)]
    m = re.search(r"Compatible with the following units:(.*?)<h2", h, re.S)
    if m:
        p["compatible"] = [{"name": text(n), "href": a}
                           for a, n in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', m.group(1))]
    m = re.search(r"Additional Parts for This Model(.*?)</p>", h, re.S)
    if m:
        a = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', m.group(1))
        if a:
            p["model_parts_page"] = {"name": text(a.group(2)), "href": a.group(1)}
    imgs = []
    for u in re.findall(r'"full":"([^"]+)"', h):
        u = u.replace("\\/", "/")
        if u not in imgs:
            imgs.append(u)
    p["images"] = imgs
    return p


def crawl_categories(locs, out):
    path = os.path.join(out, "categories.json")
    cats = json.load(open(path)) if os.path.exists(path) else {}
    for brand, (_, prefixes) in BRANDS.items():
        for c in [l for l in locs if any(pre in l for pre in prefixes)]:
            if c in cats:
                continue
            members, page = [], 1
            while True:
                h = get(f"{c}?product_list_limit=25&p={page}")
                if not h:
                    break
                title = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
                # each grid card is a <form class="item product product-item ...">;
                # its first link is the product (sidebars and upsells are outside)
                for card in h.split('class="item product product-item')[1:]:
                    a = re.search(r'href="(https://www\.mobilityscootersdirect\.com/[^"]+\.html)"', card)
                    if a and a.group(1) not in members:
                        members.append(a.group(1))
                tot = re.findall(r'toolbar-number">(\d+)', h)
                if len(tot) < 3 or int(tot[1]) >= int(tot[2]):
                    break
                page += 1
            cats[c] = {"brand": brand, "title": text(title.group(1)) if title else "", "products": members}
            json.dump(cats, open(path, "w"), indent=1)
            print(f"category {brand}: {cats[c]['title']} ({len(members)})", flush=True)
    return cats


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "MANUALS/MobilityScootersDirect"
    os.makedirs(out, exist_ok=True)
    locs = sitemap()
    global productset
    productset = {l for l in locs if l.count("/") == 4 and l.endswith(".html")}
    cats = crawl_categories(locs, out)

    ppath = os.path.join(out, "products.jsonl")
    done = set()
    if os.path.exists(ppath):
        done = {json.loads(l)["url"] for l in open(ppath)}
    for brand, (prefix, _) in BRANDS.items():
        urls = sorted({l for l in productset if prefix in l} |
                      {u for c in cats.values() if c["brand"] == brand for u in c["products"]})
        for u in urls:
            if u in done:
                continue
            h = get(u)
            if not h:
                continue
            p = parse_product(u, h)
            p["pull_brand"] = brand
            p["categories"] = [c for c, v in cats.items() if u in v["products"]]
            with open(ppath, "a") as f:
                f.write(json.dumps(p) + "\n")
            done.add(u)
            print(f"product {brand}: {p.get('part_number')} {p.get('name')}", flush=True)

    for line in open(ppath):
        p = json.loads(line)
        d = os.path.join(out, "images", p["pull_brand"])
        os.makedirs(d, exist_ok=True)
        for u in p["images"]:
            f = os.path.join(d, u.rsplit("/", 1)[-1])
            if os.path.exists(f):
                continue
            data = get(u, binary=True, delay=IMG_DELAY)
            if data:
                open(f, "wb").write(data)
    print("done", flush=True)


if __name__ == "__main__":
    main()
