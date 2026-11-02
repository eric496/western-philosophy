# Focus Studies — One Philosopher, In Depth

The library entries give every figure a solid, detailed portrait. A **focus study** is the next level down: a complete, multi-file dossier on a single philosopher, built to support weeks of dedicated study — everything a serious reader needs to genuinely know this thinker, in one place.

## How to request one

Tell Muse: **"Add &lt;philosopher&gt; to focus study"** (any phrasing that names the figure and this folder works). A dossier is then researched, written, verified, and pushed without further check-ins, following the blueprint in [TEMPLATE.md](TEMPLATE.md). One philosopher per request; a focus study can also be requested for a figure who has no library entry yet, in which case the entry is created first and the dossier built on top of it.

## What a focus study contains

Each dossier lives in `focus-studies/<philosopher-slug>/` and contains:

| File | Contents |
|---|---|
| `README.md` | Dossier home: the figure in brief, why they matter, how to use the dossier, the study plan at a glance, links to everything |
| `01-life-and-times.md` | Deep biography and historical context: life, milieu, teachers and rivals, correspondence and turning points, a dated chronology |
| `02-works-and-texts.md` | The complete works, guided: what each work argues and when to read it, editions and translations to use (and avoid), the dossier's reading order |
| `03-system-and-concepts.md` | The thought as a system: core concepts defined in the figure's own terms, a figure-specific glossary, how the pieces connect and where the tensions sit |
| `04-arguments.md` | Every major argument reconstructed in numbered premises, each with the standard objection and the best reply — scholarly disputes flagged as disputes |
| `05-conversations.md` | The figure in dialogue: who they answer, their contemporaries, who answers them, and the legacy lines running forward — linked into the library's entries, reply chains, and [themes](../themes.md) |
| `06-reception-and-debates.md` | Reception history and live controversies: schools formed and broken, the current state of the scholarly debates, the standard misconceptions in their full form |
| `07-study-plan.md` | The working plan: a week-by-week schedule at the [learning path](../learning-path.md)'s rhythm, primary readings with section targets, mapped podcast episodes and lectures, book-closed checkpoints, reconstruction prompts, a capstone essay, and a "you are done when you can…" mastery checklist |
| `08-bibliography.md` | Annotated bibliography: primary editions, the best secondary literature from beginner to advanced, SEP/IEP articles, and the verified media list with links |
| `cards.tsv` | A figure-specific [Anki](https://apps.ankiweb.net) deck (arguments and concepts) in the same tab-separated format as [`study/cards/`](../study/cards/README.md), for the [FSRS](https://docs.ankiweb.net/deck-options.html) queue |

Depth standard: a dossier typically runs **15,000–30,000 words** across its files — several times the library entry — at SEP/IEP-level accuracy. The repo's standing rules apply throughout: debates presented as debates, conventional dates keep "c.", primary-text quotations short and attributed (longer excerpts only from verified public-domain translations, translator credited), American English.

## Audio companions

Every dossier also has a **narrated audio edition** of its five content files — `01` Life & Times, `03` System & Concepts, `04` Arguments, `05` Conversations, `06` Reception & Debates — for listening when reading time is short. The narration is generated from the dossier text itself (markup, tables, and link clutter stripped; citations spoken naturally — "part one, proposition fourteen," not "E1P14"), in a natural production voice. `02` (editions guidance), `07` (the checklist-plan), and `08` (citations) are not narrated: they are reference apparatus, and make poor listening.

The audio files live in Eric's Muse library under `focus-study-audio/<philosopher-slug>/`, not in this git repository — audio binaries would bloat every push of the tree. Each dossier's `README.md` carries an **Audio companion** section listing its five episodes with durations, so the set belonging to a dossier is always findable from the dossier itself.

## How a focus study fits the rest of the library

A focus study is a deep detour, not a replacement. It builds on the figure's library entry (which remains the quick portrait), reuses any existing work-level guides in [`study/`](../study/) rather than duplicating them, adds its cards to the same Anki system the learning path runs, and states its own hour cost in its study plan — hours that sit *on top of* the learning path's budget for the stage where the figure belongs. The natural moment for a focus study is when the learning path reaches that figure; the dossier's study plan says where it plugs in.

## Registry

| Philosopher | Dossier | Status |
|---|---|---|
| Arthur Schopenhauer (1788–1860) | [arthur-schopenhauer/](arthur-schopenhauer/README.md) | Complete — 9 files, ~26,400 words, 29-card deck; 6-week study plan (~35 hrs all-in) upgrading the learning path's Stage 4 selections treatment; audio companion: 5 episodes, ~2 hrs 10 min |
| Baruch Spinoza (1632–1677) | [baruch-spinoza/](baruch-spinoza/README.md) | Complete — 9 files, ~30,700 words, 33-card deck; 7-week study plan (~47 hrs all-in) deepening the learning path's Stage 3 core treatment to the whole Ethics and a full TTP reading; audio companion: 5 episodes, ~2 hrs 46 min |
| Friedrich Nietzsche (1844–1900) | [friedrich-nietzsche/](friedrich-nietzsche/README.md) | Complete — 9 files, ~29,800 words, 34-card deck; 8-week study plan (~58 hrs all-in) following the learning path's Stage 4 order, designed as the Schopenhauer dossier's pair (same diagnosis, refused cure); audio companion: 5 episodes, ~2 hrs 22 min |
