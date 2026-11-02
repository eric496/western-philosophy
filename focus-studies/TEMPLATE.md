# Focus Study Template — The Blueprint

This file specifies what gets built when a philosopher is added to `focus-studies/`. It is a specification for the builder, not a document to copy into a dossier. Each dossier is written fresh, from research, for its figure — the file set and standards below are fixed; the contents are the figure's own.

## Folder and naming

- Folder: `focus-studies/<slug>/`, where `<slug>` matches the figure's entry filename without the extension (e.g. `immanuel-kant`, `simone-de-beauvoir`). Grouped entries in the library (e.g. Anscombe & Foot) get one dossier per person if requested individually, or a joint dossier under the grouped slug if requested jointly.
- Files: `README.md`, `01-life-and-times.md`, `02-works-and-texts.md`, `03-system-and-concepts.md`, `04-arguments.md`, `05-conversations.md`, `06-reception-and-debates.md`, `07-study-plan.md`, `08-bibliography.md`, `cards.tsv`. A file may be split (e.g. `04-arguments.md` into two parts) for a figure with an unusually large corpus, but never merged away — the set above is the minimum.

## Per-file specification

### README.md (dossier home, ~800–1,200 words)
The figure in one paragraph; why this thinker rewards weeks of study; the dossier's map (one line per file, linked); the study plan at a glance (weeks, hours, where it plugs into the learning path); links to the library entry, any `study/` guides for the figure's works, and the dossier's card deck.

### 01-life-and-times.md (~2,000–3,000 words)
Full biography with the historical world attached: education, teachers, rivals, patrons and censors, the works' occasions, late life and death, posthumous publication fate where relevant. Ends with a dated chronology table. Claims that rest on legend or late sources are flagged as such (house rule: the record, hedged where the record is thin).

### 02-works-and-texts.md (~1,500–2,500 words)
Every work that matters, in the order the dossier will read them: one entry per work — date (house imprint style), what it argues, its difficulty, its place in the figure's development. Editions and translations named per work: which to use, which to avoid, and why (consistent with the learning path's edition rulings; where the path is silent, the dossier rules and says so). Manuscript/ Nachlass cautions where they apply (e.g. a "book" the figure never published is labeled as such).

### 03-system-and-concepts.md (~2,500–4,000 words)
The architecture: the figure's central question(s), the load-bearing concepts defined in their own terms before any criticism, how the concepts interlock, the system's known internal tensions. Includes a figure-specific glossary (10–25 terms) formatted like `glossary.md`, with the figure's own usage distinguished from later textbook usage.

### 04-arguments.md (~3,000–5,000 words)
The argumentative core. Every major argument — expect 6–12 for a major figure — reconstructed in numbered premises in the style of the entries' Signature arguments sections: the reconstruction, the textual basis (work and section), the strongest standard objection, and the best reply (the figure's own where they gave one, the literature's where they didn't, labeled as such). Interpretive disputes about what the argument even is are presented as disputes with the main readings named.

### 05-conversations.md (~1,500–2,500 words)
Backward: the traditions and named figures the thinker answers, with the specific points of contact. Sideways: contemporaries, correspondences, public disputes. Forward: students, schools, and the named respondents — each linked to that figure's library entry, so the dossier plugs into the repo's reply chains rather than retelling them. One section traces the figure through the nine problems of `themes.md`: where their position appears in each relevant thread.

### 06-reception-and-debates.md (~1,500–2,500 words)
Reception by era (immediate, nineteenth century, twentieth, current), the schools and movements that claim the figure, and the live scholarly controversies stated at the current state of the question — who holds what, on what evidence. Closes with the standard misconceptions in full form (the entry's "Misreadings to avoid" is the summary; this is the long version) and any myths about the life that the record does not support.

### 07-study-plan.md (the working document)
A complete, schedulable plan, sized to the figure (typically 4–8 weeks at the learning path's weekly rhythm; the dossier's README states the total hours honestly, including media and review time):
- Week-by-week table: primary reading (work, sections, page targets in the named edition), the dossier files to read alongside, media assignments with episode/lecture identifiers (podcasts and courses already verified in the round-6 research where they exist; anything new must be verified before it is assigned).
- Checkpoints per week: book-closed questions, with answers or pointers to the dossier section that answers them.
- Reconstruction prompts at the learning path's cadence (+2 days / +1 week / +3 weeks, successive relearning) and the card routine: the dossier's `cards.tsv` enters the [Anki](https://apps.ankiweb.net) [FSRS](https://docs.ankiweb.net/deck-options.html) queue as the figure's weeks begin.
- One capstone essay (800–1,200 words) with 3–5 prompts that require the whole dossier, plus the stage gate-essay relationship if the figure is a learning-path core figure.
- A closing mastery checklist: "You are done when you can…" — 8–12 can-do statements in the learning path's style.

### 08-bibliography.md (~1,000–1,500 words)
Annotated, tiered: (1) primary texts and editions; (2) first secondary books to read, in order; (3) advanced and specialist literature; (4) reference — [SEP](https://plato.stanford.edu/)/[IEP](https://iep.utm.edu/) articles with links, [PhilPapers](https://philpapers.org/) category pointers, relevant journals or companions (Cambridge Companions and the like) where they exist; (5) the media list with URLs (podcast series and episode ranges, lecture courses, audiobooks). Every annotation says what the item is for and what it costs in time or money where that is known.

### cards.tsv
Figure-specific deck in the `study/cards/` format: exactly 3 tab-separated fields (Front, Back, Tags), argument cards built from `04-arguments.md` plus concept cards from `03-system-and-concepts.md`; tags `figure::<slug> type::argument|concept focus::<slug>`. Import and review follow `study/cards/README.md` (FSRS).

### Audio companion (produced with the dossier, stored outside the repo)
Narrate the five content files (`01`, `03`, `04`, `05`, `06`) from the finished dossier text. Speech prep: strip markup, links (keep link text), tables, and footer navigation; spell section symbols out ("section 52"); expand the figure's citation conventions into speech (Spinoza's E1P14 → "part one, proposition fourteen"; Nietzsche's work abbreviations expanded before section numbers); keep quotations and hedges exactly as written. One natural production voice throughout (Helio, at 90% speed — Eric's chosen voice and pace, set 2026-11-02 after a sample; re-render on request if he changes either). Files land in the Muse library at `focus-study-audio/<slug>/<file-stem>.mp3` and are published to the repo as GitHub Release assets (the push channel is text-only; a release per audio batch, assets named `<slug>-<file-stem>.mp3`), with the dossier README's table linking each episode's download URL. The dossier `README.md` gains an **Audio companion** section listing the five episodes with their durations. If a narrated file is later substantially revised, regenerate its episode in the same push-cycle and update the listed duration.

## Standards (all repo rules apply, plus these)

1. Research before writing: the dossier is built from the library entry, any existing `study/` guides, the SEP/IEP articles, and targeted checks of dates, editions, and media availability — the same verification discipline as the repo's audit rounds. Facts that cannot be verified are hedged or omitted, never smoothed over.
2. Nothing in the dossier contradicts the library entry, the guides, or the learning path; where the dossier's deeper research corrects them, the correction is made in those files too, in the same push, and flagged in the delivery summary.
3. All internal links resolve; the dossier is registered in `focus-studies/README.md`'s registry in the same push.
4. Word counts above are guides, not quotas — completeness for this figure beats hitting a number.
