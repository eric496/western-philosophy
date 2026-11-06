#!/usr/bin/env python3
"""Offline consistency checks for this repo. Exits 1 if any check fails.

Checks:
  1. Every relative markdown link resolves to an existing file or folder.
  2. index.md, tracker.md and timeline.md list the same figures, in the same
     order, with the same dates, each linked to the same entry file.
  3. Every entry file under eras/ is linked from index.md.
  4. Every card deck (*.tsv) has exactly 3 tab-separated columns per row.
  5. Portrait images come from Wikimedia Commons (not English Wikipedia's
     local fair-use uploads under /wikipedia/en/).
  6. No quote-collection website is cited as a source.
  7. No curly quotation mark is closed by a straight one, or the reverse.
  8. No quotation appears in two places in different words (quotation drift).
     Intended variants are listed in scripts/quote-variants.txt.

Run from anywhere:  python3 scripts/check_repo.py
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")
# The template's links are written for a file that will live in eras/<era>/.
SKIP_LINKS = {"templates/philosopher-template.md"}

errors = []


def err(msg):
    errors.append(msg)


def md_files():
    return sorted(p for p in glob.glob("**/*.md", recursive=True) if not p.startswith(".git"))


def strip_code(text):
    """Drop fenced code blocks and inline code so example links are ignored."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


# 1. relative links
for path in md_files():
    if path in SKIP_LINKS:
        continue
    for m in LINK.finditer(strip_code(open(path, encoding="utf-8").read())):
        url = m.group(1)
        if re.match(r"^[a-z]+:", url) or url.startswith("#"):
            continue
        target = url.split("#")[0]
        if target and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
            err(f"{path}: broken relative link -> {url}")


# 2. hub consistency
def norm(s):
    return re.sub(r"\s+", "", s)


def parse_index():
    rows = []
    for line in open("index.md", encoding="utf-8"):
        m = re.match(r"\| (\d+) \| (.+?) \| (.+?) \|", line)
        if m:
            rows.append((m.group(2), m.group(3)))
    return rows


def parse_list(path, pat, name_grp, date_grp):
    rows = []
    for line in open(path, encoding="utf-8"):
        m = re.match(pat, line)
        if m:
            rows.append((m.group(name_grp), m.group(date_grp)))
    return rows


def first_link(cell):
    m = re.search(r"\]\((eras/[^)#]+)", cell)
    return m.group(1) if m else None


def base_name(cell):
    """Name text with link markup removed, for comparing across hubs."""
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cell)
    return re.sub(r"\s*\(.*\)$", "", s).strip()


idx = parse_index()
trk = parse_list("tracker.md", r"- \[ \] \*\*(.+?)\*\* \((.+?)\) —", 1, 2)
tl = parse_list("timeline.md", r"- \*\*(.+?) — (.+?)\*\* \(", 2, 1)
if not (len(idx) == len(trk) == len(tl)):
    err(f"hub row counts differ: index {len(idx)}, tracker {len(trk)}, timeline {len(tl)}")
for i, (a, b, c) in enumerate(zip(idx, trk, tl), 1):
    if not (base_name(a[0]) == base_name(b[0]) == base_name(c[0])):
        err(f"row {i}: names differ: {base_name(a[0])!r} / {base_name(b[0])!r} / {base_name(c[0])!r}")
    # The tracker may append a second figure's dates after ';' (e.g. Gorgias).
    da, db, dc = norm(a[1]), norm(b[1].split(";")[0]), norm(c[1])
    if not (da.split("(")[0] == db == dc):
        err(f"row {i} ({base_name(a[0])}): dates differ: {a[1]!r} / {b[1]!r} / {c[1]!r}")
    la, lb, lc = first_link(a[0]), first_link(b[0]), first_link(c[0])
    if not la:
        err(f"row {i} ({base_name(a[0])}): index name is not linked to an entry")
    elif not (la == lb == lc):
        err(f"row {i} ({base_name(a[0])}): entry links differ: {la} / {lb} / {lc}")

# 3. every entry reachable from the index
index_text = open("index.md", encoding="utf-8").read()
for entry in sorted(glob.glob("eras/*/*.md")):
    if entry.endswith("README.md") or "sidebars-" in os.path.basename(entry):
        continue
    if f"]({entry})" not in index_text:
        err(f"{entry}: not linked from index.md")

# 4. card decks
for deck in sorted(glob.glob("**/*.tsv", recursive=True)):
    for n, line in enumerate(open(deck, encoding="utf-8"), 1):
        if line.strip() and len(line.rstrip("\n").split("\t")) != 3:
            err(f"{deck}:{n}: expected 3 tab-separated columns")

# 5. image sources
for path in md_files():
    for m in re.finditer(r"!\[[^\]]*\]\((https?://[^)\s]+)\)", open(path, encoding="utf-8").read()):
        if "/wikipedia/en/" in m.group(1):
            err(f"{path}: image is an English-Wikipedia local (usually fair-use) upload: {m.group(1)}")

# 6. quote-collection websites are never a source
QUOTE_SITES = re.compile(r"goodreads\.com|azquotes\.com|brainyquote\.com|quotefancy\.com", re.I)
for path in md_files():
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if QUOTE_SITES.search(line):
            err(f"{path}:{n}: cites a quote-collection website; cite the work itself")

# 7. mismatched quotation marks: a curly quote closed by a straight one, or the reverse
MIXED = re.compile(r"“[^”\"\n]*\"|\"[^\"“”\n]*”")
text_files = md_files() + sorted(glob.glob("**/*.tsv", recursive=True))
for path in text_files:
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if MIXED.search(strip_code(line)):
            err(f"{path}:{n}: mismatched curly and straight quotation marks")

# 8. quotation drift: the same quotation worded differently in two places.
# Punctuation, capitals and italics are ignored, and so is quoting a shorter
# stretch of the same passage. Intended differences (examples that differ
# only by "not", or a list of rival translations) go in scripts/quote-variants.txt.
QUOTE = re.compile(r"\"(\S[^\"\n]{28,398}\S)\"|“(\S[^”\n]{28,398}\S)”")
variants_file = "scripts/quote-variants.txt"
VARIANTS = []
if os.path.exists(variants_file):
    VARIANTS = [l.strip().lower() for l in open(variants_file, encoding="utf-8")
                if l.strip() and not l.startswith("#")]


def qnorm(s):
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower().replace("’", "").replace("'", ""))
    return re.sub(r"\s+", " ", s).strip()


quotes = []
for path in text_files:
    if path.startswith("templates/"):
        continue
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        for m in QUOTE.finditer(strip_code(line)):
            raw = m.group(1) or m.group(2)
            # A "match" that spans a markdown link is the text between two
            # quoted titles, not a quotation.
            if "](" in raw:
                continue
            q = qnorm(raw)
            # Pieces between ellipses, so an elided quotation still matches.
            parts = [qnorm(x) for x in re.split(r"\.\.\.|…|\[\.\.\.\]", raw) if qnorm(x)]
            if len(q.split()) >= 8 and not any(v in q for v in VARIANTS):
                quotes.append((q, path, n, parts))

grams = {}
for i, (q, _, _, _) in enumerate(quotes):
    w = q.split()
    for k in range(len(w) - 3):
        grams.setdefault(" ".join(w[k:k + 4]), set()).add(i)

import difflib  # noqa: E402

pairs = set()
for ids in grams.values():
    if 1 < len(ids) <= 40:
        ids = sorted(ids)
        pairs.update((a, b) for x, a in enumerate(ids) for b in ids[x + 1:])
for a, b in sorted(pairs):
    qa, qb = quotes[a][0], quotes[b][0]
    if qa in qb or qb in qa:
        continue
    if all(x in qb for x in quotes[a][3]) or all(x in qa for x in quotes[b][3]):
        continue
    short, long_ = sorted((qa, qb), key=len)
    sm = difflib.SequenceMatcher(None, short, long_, autojunk=False)
    m = sm.find_longest_match(0, len(short), 0, len(long_))
    start = max(0, m.b - m.a)
    window = long_[start:start + len(short) + 10]
    if difflib.SequenceMatcher(None, short, window, autojunk=False).ratio() >= 0.85:
        err(f"quotation drift: {quotes[a][1]}:{quotes[a][2]} and {quotes[b][1]}:{quotes[b][2]} "
            f"quote the same passage in different words")

for e in errors:
    print("ERROR:", e)
print(f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)
