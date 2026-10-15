#!/usr/bin/env python3
"""Pull Bruno's TechMate troubleshooting trees and render them as Markdown.

TechMate (Bruno dealer portal → TECHMATE) is a set of Zingtree decision
trees. The dealer page links to the entry tree; every sub-tree is fetched
read-only from Zingtree's tree JSON endpoint. Nothing is submitted, so no
"Contact Bruno" emails or session records are created.

Usage:  python3 scripts/techmate_pull.py [MANUALS/Bruno/TechMate]

Writes <out>/json/<tree_id>.json (raw) and <out>/<Group>/<name>.md
(readable outline: every node, its question, text, media links and where
each answer goes). Raw output stays under MANUALS/ (gitignored): it's
Bruno dealer-portal content.
"""
import html
import json
import os
import re
import sys
import time
import urllib.request

ROOT_TREE = "594359908000"  # "Initial Traffic Diversion SRE Version 2"
API = "https://zingtree.com/api/json.php?tree_id={}"


def fetch(tree_id, jdir):
    path = os.path.join(jdir, f"{tree_id}.json")
    if not os.path.exists(path):
        req = urllib.request.Request(API.format(tree_id), headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        with open(path, "wb") as f:
            f.write(data)
        time.sleep(0.3)
    with open(path) as f:
        return json.load(f)


def norm(tid):
    return tid if len(tid) > 9 else tid + "000"


def tree_refs(tree):
    refs = set()
    for n in (tree.get("nodes") or {}).values():
        if n.get("open_tree_id") not in (None, "", "0"):
            refs.add(norm(n["open_tree_id"]))
        for m in re.findall(r"zingtree\.com\\?/(?:live|deploy|show)\\?/(\d{6,12})", json.dumps(n)):
            refs.add(norm(m))
    return refs


def crawl(jdir):
    trees, queue = {}, [ROOT_TREE]
    while queue:
        tid = queue.pop(0)
        if tid in trees:
            continue
        trees[tid] = fetch(tid, jdir)
        queue.extend(sorted(tree_refs(trees[tid]) - set(trees)))
    return trees


def to_text(s):
    """HTML → plain text, keeping images, videos and links as Markdown."""
    s = s or ""
    s = re.sub(r'<iframe[^>]*src="([^"]+)"[^>]*>.*?</iframe>',
               lambda m: f" [video: https:{m.group(1).split('?')[0]}] " if m.group(1).startswith("//")
               else f" [video: {m.group(1).split('?')[0]}] ", s, flags=re.S)
    s = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', lambda m: f" [image: {m.group(1)}] ", s)
    s = re.sub(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f"{m.group(2)} <{m.group(1)}>", s, flags=re.S)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = re.sub(r"<(br|/p|/div|/h\d|/tr)[^>]*>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("‌", "").replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    return "\n".join(l.strip() for l in s.splitlines() if l.strip())


def safe(name):
    return re.sub(r'[\\/:*?"<>|]+', "-", name).strip(" .-")


def group(name):
    return "VPL" if name.upper().startswith(("VPL", "NEW VPL")) else (
        "Stairlift" if "STAIRLIFT" in name.upper() or name.startswith(("5000", "Broken")) else "Entry")


def render(tid, tree, names):
    nodes = tree.get("nodes") or {}
    title = lambda nid: to_text(nodes.get(nid, {}).get("page_title", "")) or f"node {nid}"
    # Breadth-first from the root so the outline reads in tree order.
    order, queue = [], [tree.get("root_node_id")]
    while queue:
        nid = queue.pop(0)
        if nid in order or nid not in nodes:
            continue
        order.append(nid)
        queue.extend(b.get("button_link") for b in nodes[nid].get("buttons") or [])
        if nodes[nid].get("continuation_node_id") not in (None, "", "0"):
            queue.append(nodes[nid]["continuation_node_id"])
    order += [n for n in nodes if n not in order]

    out = [f"# TechMate — {tree.get('name')}", "",
           f"Zingtree tree `{tid}` · root node {tree.get('root_node_id')} · {len(nodes)} nodes", ""]
    for nid in order:
        n = nodes[nid]
        out.append(f"## [{nid}] {title(nid)} ({n['type']})")
        if n["type"] == "Email":
            out += ["_Sends an email to Bruno (contact/order/feedback). Not rendered._", ""]
            continue
        if n["type"] == "Tree":
            t, tn = norm(n.get("open_tree_id", "0")), n.get("open_tree_node_id", "0")
            out.append(f"→ Opens tree **{names.get(t, t)}** (`{t}`)" + (f" at node {tn}" if tn not in ("", "0") else ""))
        if n["type"] == "Link" and n.get("link"):
            out.append(f"→ Link: {n['link'].split('?')[0]}")
        if n.get("question"):
            out.append(f"**Q: {to_text(n['question'])}**")
        body = to_text(n.get("content"))
        if body:
            out.append(body)
        for f in n.get("formfields") or []:
            label = to_text(f.get("label") or f.get("name") or "")
            if label:
                out.append(f"- form field: {label} (`{f.get('name', '')}`)")
        for b in n.get("buttons") or []:
            dest = b.get("button_link")
            dname = f"[{dest}] {title(dest)}" if dest in nodes else f"[{dest}]"
            if n["type"] == "Scoring":
                cond = html.unescape(b.get("logic_expression") or "") or ("otherwise" if b.get("op") == "def" else b.get("button_text") or "?")
                out.append(f"- if `{cond}` → {dname}")
            else:
                out.append(f"- **{to_text(b.get('button_text'))}** → {dname}")
        if n.get("continuation_node_id") not in (None, "", "0"):
            out.append(f"- (continues) → [{n['continuation_node_id']}] {title(n['continuation_node_id'])}")
        out.append("")
    return "\n".join(out)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "MANUALS/Bruno/TechMate"
    jdir = os.path.join(out, "json")
    os.makedirs(jdir, exist_ok=True)
    trees = crawl(jdir)
    names = {tid: t.get("name", tid) for tid, t in trees.items()}
    for tid, tree in trees.items():
        if not tree.get("nodes") or tree.get("name") == "Tree Deleted":
            continue
        gdir = os.path.join(out, group(tree["name"]))
        os.makedirs(gdir, exist_ok=True)
        with open(os.path.join(gdir, f"{safe(tree['name'])}.md"), "w") as f:
            f.write(render(tid, tree, names))
    print(f"{len(trees)} trees → {out}")


if __name__ == "__main__":
    main()
