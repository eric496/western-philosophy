# Western Philosophy — A Beginner's Self-Study Map

A structured way to pick up Western philosophy on your own: **140 key figures** across 2,500 years. Every entry is a full detailed treatment: biography, major theories and concepts explained with their reasoning, key works with dates, contributions, impact and legacy, criticisms and debates, and the first thing of theirs you should actually read.

Researched against the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/) (SEP), the [Internet Encyclopedia of Philosophy](https://iep.utm.edu/) (IEP), and [Encyclopaedia Britannica](https://www.britannica.com/) — all free. Where scholars genuinely disagree (e.g. Heidegger and Nazism, young vs mature Marx, early vs late Wittgenstein), the disagreement is flagged rather than flattened.

## Start here

1. **Skim [`timeline.md`](timeline.md)** — 2,500 years on one page; get the shape of the story.
2. **Follow [`learning-path.md`](learning-path.md)** — a hybrid spiral: a chronological spine (Stages 0–5) with five problem threads (knowledge, mind, God, ethics, politics) revisited every era. About 30 core figures are read in primary text with named beginner-friendly editions; the rest are covered at map level. Budget ≈288 desk-study hours over 64 study weeks; counted in full — desk study + the daily [Anki](https://apps.ankiweb.net) ([FSRS](https://docs.ankiweb.net/deck-options.html)) card queue + assigned podcasts and lectures — it totals ≈454 hours, i.e. 64 study weeks at ≈7 hrs/week all-in (≈17 calendar months with buffers), the same material at 4–5 hrs/week stretched over roughly two to two-and-a-half years, or a trimmed 12-month version (≈335 hrs). It is deliberately not a one-year plan at a comfortable pace, and it says so.
3. **Read era overviews in order** ([`eras/`](eras/)), opening a philosopher's entry file when the overview reaches them.
4. **Tick off [`tracker.md`](tracker.md)** as you finish each figure.

## What's in here

| File / folder | What it is |
|---|---|
| [`index.md`](index.md) | Master index: all 140 figures — dates, school, signature concept, first work to read |
| [`learning-path.md`](learning-path.md) | The study plan: hybrid-spiral stages with week/hour budgets, core vs map-level figures, per-author primary texts and editions to use (and avoid), can-do checkpoints and gate essays per stage, the spaced-retrieval system, and a failure-mode checklist |
| [`eras/01-ancient/`](eras/01-ancient/) … [`eras/05-20th-century/`](eras/05-20th-century/) | One folder per era: an overview (story of the era, within-era reading order, traps to avoid) plus one entry file per philosopher or school |
| [`philosophers/README.md`](philosophers/README.md) | Alphabetical list of all entry files |
| [`study/`](study/) | Work-level study guides (21), worked answer keys for the core entries' study questions, and Anki card decks — chapter/section guides with argument reconstructions, checkpoint questions and answers, and common misreadings |
| [`focus-studies/`](focus-studies/) | Single-philosopher deep dives, built on request: a multi-file dossier per figure (life, works, system, arguments, conversations, reception, a week-by-week study plan, bibliography, and a figure-specific card deck). See [`focus-studies/README.md`](focus-studies/README.md) for how to request one |
| [`themes.md`](themes.md) | The same history sideways: 9 recurring questions (metaphysics, epistemology, ethics, politics, mind, logic & language, aesthetics, religion, science) and who answered them |
| [`glossary.md`](glossary.md) | 84 terms in plain language (*archē*, *eudaimonia*, *epoché*, *différance*, …) |
| [`quotes-in-context.md`](quotes-in-context.md) | 37 famous lines with their exact source, speaker, wording and context, including well-known misattributions ("leap of faith", Durant's "we are what we repeatedly do") |
| [`misconceptions.md`](misconceptions.md) | 52 errors to unlearn — Stoicism is not emotion suppression, Epicureanism is not indulgence, "God is dead" is a diagnosis, not a celebration |
| [`timeline.md`](timeline.md) | Chronological list with signature concepts |
| [`tracker.md`](tracker.md) | A checkbox for every figure |
| [`sources.md`](sources.md) | SEP/IEP/Britannica entries, survey books (Kenny, Copleston, Adamson's [*History of Philosophy Without Any Gaps*](https://historyofphilosophy.net/)), free course sources |
| [`templates/philosopher-template.md`](templates/philosopher-template.md) | The entry template for adding new figures |
| [`notes/`](notes/) | Space for your own study notes |
| [`scripts/check_repo.py`](scripts/check_repo.py) | Offline consistency checks (relative links, index/tracker/timeline agreement, deck format, image sources); a ready-made GitHub Actions workflow ([`ci/checks.yml`](ci/checks.yml)) runs it on every push plus a weekly external-link sweep once it is copied to `.github/workflows/checks.yml` (adding a workflow file needs a GitHub token with the `workflow` scope, or the GitHub web editor) |

## How the entries are written

Following the research's reading policy: mostly plain-language summary, with short primary-text excerpts only where a passage is load-bearing. Every entry follows the [template](templates/philosopher-template.md), in this order: **At a glance** (dates, place, tradition, what they are known for, and the lineage line: who they respond to and who answers them), **Biography**, **Major theories and concepts**, **Key works** with dates, **Contributions**, **Impact and legacy**, **Criticisms and debates**, **Misreadings to avoid**, and **What to read first**. Core entries add **Study questions** (41 entries), and some add **Signature arguments** and **In their own words** (20 entries).

Three habits that make the material stick:

- For each figure learn **their one problem, their one signature move, and the strongest objection from the next figure** — philosophy is an argument carried on across centuries, and the entries are cross-linked that way.
- Prefer the **"read first"** text over the famous one (Russell's *Problems of Philosophy*, not *Principia Mathematica*; Beauvoir's *Ethics of Ambiguity* before *The Second Sex* — in the complete 2010 translation).
- When a summary and a claim seem to conflict, check the SEP entry linked in [`sources.md`](sources.md) — it is the arbiter used throughout.

## Honesty notes

- Dates marked **c.** are scholarly conventions, especially for ancient and medieval births (e.g. Maimonides 1135 vs 1138).
- A few publication dates genuinely differ between sources and are flagged where they occur: Hegel's *Philosophy of Right* (1820 vs 1821), Schopenhauer's *The World as Will and Representation* (1818 vs 1819).
- Labels like "rationalist vs empiricist" and "analytic vs continental" are later textbook maps — useful, but the SEP warns both must be adopted with great caution; the entries say where they mislead.
- Grouped entries exist where the school is the unit (Stoics, Skeptics, Vienna Circle, Frankfurt School, Anscombe & Foot).

*Summaries are original study notes based on the sources in [`sources.md`](sources.md); quotations from primary texts are kept short and attributed.*
