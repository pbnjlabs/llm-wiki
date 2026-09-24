# Performance Medical Supply — Technical Manual Wiki

This project maintains a persistent, LLM-curated wiki over Performance Medical
Supply's equipment technical manuals: stair lifts, vehicle/porch lifts, and
power wheelchairs/scooters from Bruno, Golden Technologies, Pride Mobility,
and Prism. The goal is a knowledge base a tech or CSR can query quickly
("how do I replace the brake on a GL110?", "what's the charging procedure for
an MRC24-4LX?") without re-reading PDFs from scratch every time, and where
knowledge that's common across models (shared batteries, controllers, brake
kits) is synthesized once instead of scattered across dozens of manuals.

You (the agent) own the `wiki/` layer completely. The human curates sources,
asks questions, and directs what to emphasize — you do the reading,
summarizing, cross-referencing, and bookkeeping.

## Layers

- **`MANUALS/`** — raw sources. Original PDFs, organized
  `MANUALS/<Manufacturer>/<Product Line>/<file>.pdf`. **Immutable** — read
  only, never edit, move, or rename anything in here. This is the source of
  truth; if a wiki page and a manual disagree, the manual wins and the wiki
  page needs fixing.
- **`wiki/`** — the wiki itself. Obsidian-flavored markdown you own and
  maintain entirely.
- **This file** — the schema. Update it as we discover better conventions.

## Wiki structure

```
wiki/
  index.md              content catalog — the entry point for every query
  log.md                append-only chronological record of ingests/queries/lints
  manufacturers/         one page per manufacturer
    Bruno.md
    Golden.md
    Pride.md
    Prism.md
  models/                one page per product/model
    SRE-3050.md
    VPL-3100B.md
    GA541-Avenger.md
    Q6-Edge-3.md
    ...
  concepts/              cross-cutting technical topics shared across models
    Battery-Charging.md
    Brake-Replacement.md
    Joystick-Controllers.md
    Seat-Systems.md
    Troubleshooting.md
    ...
  sources/               one summary page per raw manual, organized by
                         manufacturer then product-line subdirectory
    Bruno/Bruno Curved SL/2110-TS Tech Support Guide.md
    Golden/Companion/Companion Service Guide (GC240, GC340, GC440).md
    ...
```

Every manufacturer under `sources/` gets its own product-line
subdirectories — never a flat folder of files, even for a first/small
ingest. Derive the subdirectory names from that manufacturer's own
`manufacturers/<Name>.md` page (its model-family/product-line groupings),
not from however the raw files happen to be organized under `MANUALS/`
(which may be flat, or split differently, or even misfiled into another
manufacturer's folder — see the Harmar-doc-under-Bruno and
AutoSlide/Open-Sesame cases). Always include a catch-all `General`
subdirectory for docs that are genuinely cross-cutting/not tied to one
product line (accessories, chargers, warranty text, etc.) rather than
forcing them into a product-line folder they don't belong in.

### Page conventions

- Obsidian-style: YAML frontmatter + `[[wikilinks]]` between pages.
- Frontmatter fields (use what applies, skip what doesn't):
  ```yaml
  ---
  type: manufacturer | model | concept | source
  manufacturer: Bruno
  model: SRE-3050          # models only
  doc_type: Install Manual | Operator Manual | Tech Support Guide | IPB | Service Guide | Web Article
  source: "MANUALS/Bruno/Bruno Straight SL/3050-I SRE-3050 Install Manual 06-22-2026.pdf"
  date: 2026-06-22          # manual's revision date, not today's date
  tags: [stairlift, bruno]
  ---
  ```
- **Model pages** are the main unit of value: spec summary, what documents
  exist for it (linked to `sources/` pages), common procedures, known
  quirks/gotchas, and links to relevant `concepts/` pages.
- **Concept pages** aggregate a topic across models (e.g. "how battery
  charging works" summarizing Golden's, Bruno's, and Pride's charging
  procedures side by side, noting where they differ). This is where the wiki
  earns its keep over just having the PDFs — a tech shouldn't have to know
  which manual to open if the concept page already has the answer.
- **Source pages** are short: what the document covers, its doc type/date,
  and which model/concept pages it feeds into. Link back to the raw PDF path
  (don't copy the PDF content in — summarize and cite).
- Model/manufacturer names in filenames should match the `MANUALS/` folder
  and part-number naming as closely as practical (e.g. `SRE-3050.md`, not
  `Bruno Stair Lift 3050.md`) so cross-referencing stays mechanical.

### Web clippings

The human sometimes saves manufacturer web pages with Obsidian Web
Clipper into the vault-root `Clippings/` folder (Markdown with
`source:` URL / `published:` frontmatter). To ingest them, copy them into
`MANUALS/Clippings/` as raw sources and leave the originals in place.
Then file source pages under `sources/<Manufacturer>/<Product Line>/`
like any manual, with `doc_type: Web Article`, `url:` set to the
original URL, and `date:` set to the article's published date.
Clippings are marketing or consumer guidance, so they carry **less
weight than a manual**. Say so on the pages they feed, and let any
manual override them.

## Operations

### Ingest

1. Read the source PDF(s) from `MANUALS/`. Manuals can run long — use the
   `pages` parameter on Read in batches (max 20 pages/call) rather than
   assuming a single read captures everything, especially for install
   manuals and IPBs. If the raw files aren't under this repo's `MANUALS/`
   yet (e.g. the human dropped them somewhere else on disk), copy them in
   first, preserving whatever folder name/structure they came with —
   `MANUALS/` is gitignored, so this never touches git.
2. Discuss key takeaways with the human before writing anything (unless
   they've asked for a batch/unsupervised pass).
3. Write/update the `sources/` page for this document, filed under
   `sources/<Manufacturer>/<Product Line>/` — pick (or create) the
   product-line subdirectory by actual content, never leave a manufacturer's
   sources flat and never mirror a misleading raw folder name verbatim (see
   the Wiki structure section above).
4. Create or update the relevant `models/` page(s).
5. Update any `concepts/` pages this document touches (e.g. a new charger
   manual updates `Battery-Charging.md`).
6. Update `wiki/index.md`.
7. Append an entry to `wiki/log.md`.
8. Commit and push (see Git section below) — this is an automatic part of
   ingest, not a separate step to ask about.

A single manual might touch 3-6 pages (its source page, one model page, one
or two concept pages, plus the index). Default to ingesting one manual (or
one tight cluster, e.g. a model's full doc set) at a time and staying
involved, per the human's stated preference — don't silently batch-ingest
the whole `MANUALS/` tree unless explicitly asked to.

### Query

1. Read `wiki/index.md` first to find candidate pages — don't grep the raw
   PDFs directly unless the wiki doesn't yet cover the answer.
2. Drill into the relevant `models/`/`concepts/`/`sources/` pages.
3. Answer with citations back to the specific manual (path + section/page
   if known). The `source:` field on the relevant `sources/` page gives
   the path relative to the repo root — `MANUALS/` is gitignored and
   **local to each device** (not synced by git or the sync task), so
   before offering a link, check the file actually exists on disk here
   (e.g. `ls` the resolved path). If it exists, include a `file://` link
   using this device's absolute path (e.g.
   `file:///home/lu/Work/llm-wiki/MANUALS/Bruno/...pdf`) alongside the
   relative path for reference. If it does **not** exist locally, say so
   plainly instead of printing a link — e.g. "source PDF not cached on
   this device; relative path: `MANUALS/Bruno/...pdf`" — never emit a
   `file://` link you haven't confirmed resolves on this machine. Link
   every manual an answer draws on if it synthesizes more than one,
   applying this check to each.
4. If the answer is worth keeping (a synthesis, comparison, or something not
   already captured), offer to file it back into the wiki as a new or
   updated page rather than letting it disappear into chat history.

### Graphics in query answers

Citing the page number (e.g. "see Figure 4B on page 7") is good enough
by default — it avoids generating extra files for every text-answerable
question, and the human can open the source PDF themselves. Extract an
actual image **only** when the graphic is the content and text would
lose real information: wiring diagrams, exploded parts/BOM views,
troubleshooting flowcharts, install-step photo sequences, etc.

To extract: `pdftoppm -png -f <page> -l <page> -r 150 "<source pdf>"
"assets/<Manufacturer>/<pdf-basename>-p<page>"` (poppler-utils, already
installed). Save under `assets/<Manufacturer>/` — this directory is
gitignored just like `MANUALS/`, so it never touches git; it's a local
cache, not a wiki layer. Give the human a `file://` link to the
extracted PNG (absolute path) alongside the usual source-PDF link and
page citation.

### Lint

When asked to health-check the wiki, look for:
- Manuals present in `MANUALS/` with no corresponding `sources/` page
  (nothing yet ingested).
- Model pages missing despite having manuals on disk.
- Orphan pages with no inbound links.
- Concepts mentioned repeatedly across model pages but lacking their own
  `concepts/` page.
- Contradictions between pages, or claims a newer manual revision has
  superseded (compare `date` frontmatter).

## Log format

Each `log.md` entry starts with a consistent prefix so it's greppable:

```
## [YYYY-MM-DD] ingest | <Manufacturer> <Model> — <doc title>
## [YYYY-MM-DD] query | <short question>
## [YYYY-MM-DD] lint | <short summary of findings>
```

`grep "^## \[" wiki/log.md | tail -5` gives the last 5 entries.

## Git

This directory is a git repo with a GitHub remote (`origin`). Commit wiki
changes (not raw manuals — `MANUALS/` is gitignored) as you go, and **push
automatically after every ingest/lint/reorg pass** — no need to ask each
time, this is standing authorization. If `origin/master` has moved (e.g. a
README edited on GitHub), rebase local commits on top rather than
force-pushing. Still don't force-push, and still check with the human
before any other destructive git operation (reset --hard, discarding
uncommitted work, etc.) — the standing push authorization covers ordinary
forward commits only.
