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

  9. Stated counts match the files they describe (figures, glossary terms,
     quotations, misconceptions, study guides, deck sizes, focus-study files
     and card decks).
 10. Optional, needs network: every external link answers (403 and 429 are
     accepted, as in the CI link sweep).

Run from anywhere:  python3 scripts/check_repo.py [--external]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")
# The template's links are written for a file that will live in eras/<era>/.
SKIP_LINKS = {"templates/philosopher-template.md", "zh/templates/philosopher-template.md"}

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

# 9. stated counts match the files they describe.
def read(path):
    return open(path, encoding="utf-8").read()


def count_lines(path, pattern):
    return sum(1 for line in open(path, encoding="utf-8") if re.match(pattern, line))


def expect(path, pattern, actual, what):
    """Every number captured by `pattern` in `path` must equal `actual`."""
    found = re.findall(pattern, read(path))
    if not found:
        err(f"{path}: count check could not find the stated number of {what}")
    for n in found:
        if int(n.replace(",", "")) != actual:
            err(f"{path}: says {n} {what}, but there are {actual}")


figures = len(idx)
guides = len([p for p in glob.glob("study/*.md")
              if not os.path.basename(p).startswith(("README", "answers-"))])
signature = sum(1 for p in glob.glob("eras/*/*.md") if "## Signature arguments" in read(p))
expect("README.md", r"all (\d+) figures", figures, "figures")
expect("philosophers/README.md", r"all (\d+) figures", figures, "figures")
expect("learning-path.md", r"The library covers (\d+) figures", figures, "figures")
expect("README.md", r"(\d+) terms in plain language", count_lines("glossary.md", r"- \*\*"), "glossary terms")
expect("README.md", r"(\d+) famous lines", count_lines("quotes-in-context.md", r"### "), "quotations")
expect("README.md", r"(\d+) errors to unlearn", count_lines("misconceptions.md", r"\d+\. \*\*"), "misconceptions")
expect("README.md", r"Work-level study guides \((\d+)\)", guides, "study guides")
expect("study/cards/README.md", r"(\d+) study guides", guides, "study guides")
expect("study/cards/README.md", r"(\d+) core entries", signature, "core entries with Signature arguments")
for deck in sorted(glob.glob("study/cards/*.tsv")):
    expect("study/cards/README.md", r"`" + re.escape(os.path.basename(deck)) + r"` \| (\d+) \|",
           count_lines(deck, r".*\S"), f"cards in {os.path.basename(deck)}")

# Focus-study registry: one row per dossier, and each row's file and card counts.
registry = read("focus-studies/README.md")
dossiers = sorted(d for d in glob.glob("focus-studies/*/") if os.path.exists(d + "README.md"))
for d in dossiers:
    slug = os.path.basename(d.rstrip("/"))
    row = re.search(r"^\|[^\n]*\]\(" + re.escape(slug) + r"/README\.md\)[^\n]*$", registry, re.M)
    if not row:
        err(f"focus-studies/README.md: no registry row for {slug}/")
        continue
    md = len(glob.glob(d + "*.md"))
    cards = count_lines(d + "cards.tsv", r".*\S") if os.path.exists(d + "cards.tsv") else 0
    m = re.search(r"(\d+) files", row.group(0))
    if m and int(m.group(1)) != md:
        err(f"focus-studies/README.md: {slug} row says {m.group(1)} files, but there are {md}")
    m = re.search(r"(\d+)-card deck", row.group(0))
    if m and int(m.group(1)) != cards:
        err(f"focus-studies/README.md: {slug} row says a {m.group(1)}-card deck, but cards.tsv has {cards}")
    readme = read(d + "README.md")
    m = re.search(r"(\d+) cards \(", readme)
    if m and int(m.group(1)) != cards:
        err(f"{d}README.md: says {m.group(1)} cards, but cards.tsv has {cards}")

# 10. external links (opt-in, needs network): python3 scripts/check_repo.py --external
# Same policy as the CI lychee job: 403 (bot-blocking sites) and 429 (rate
# limits) are not dead links; this repo's release assets need authentication.
if "--external" in sys.argv:
    import concurrent.futures
    import urllib.error
    import urllib.request

    URL = re.compile(r"\]\((https?://[^)\s]+)\)")
    where = {}
    for path in md_files():
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            for u in URL.findall(strip_code(line)):
                where.setdefault(u.split("#")[0], f"{path}:{n}")
    skip = re.compile(r"^https://github\.com/eric496/western-philosophy/releases")

    def status(url):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (link check)"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status
        except urllib.error.HTTPError as e:
            return e.code
        except Exception as e:  # DNS failure, timeout, TLS error
            return type(e).__name__

    urls = sorted(u for u in where if not skip.match(u))
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for url, code in zip(urls, pool.map(status, urls)):
            # urllib follows most redirects itself but not 308, which lands here.
            if not (isinstance(code, int) and (200 <= code < 400 or code in (403, 429))):
                err(f"{where[url]}: external link returned {code}: {url}")
    print(f"checked {len(urls)} external links")

for e in errors:
    print("ERROR:", e)
print(f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)
