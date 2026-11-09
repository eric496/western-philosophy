# Flashcard Decks

[Anki](https://apps.ankiweb.net)-importable card decks built from material already in this repository. Following the retention system in the [learning path](../../learning-path.md) (§2.1), these are **argument cards, not fact cards**: every front is a *do*-prompt that demands reconstruction or explanation, never a bare "who/when/what" recall cue. Dates and definitions are deliberately not carded — the path's bet is that what needs to survive is the ability to rebuild an argument and answer its standard objection.

## The decks

| File | Cards | What it is |
|---|---|---|
| `argument-cards-core.tsv` | 40 | One card per signature argument of the 20 core entries — two per figure. Front: "Reconstruct X's argument …: numbered premises, conclusion, then the standard objection and the reply." Back: a compact model answer (premises in brief, conclusion, one objection, one reply), 107–125 words. |
| `checkpoint-cards.tsv` | 278 | One card per checkpoint question in the 18 study guides. Front: the guide's question. Back: the guide's own answer, lightly condensed (7–86 words; all under ~120). |

The learning path budgets roughly 150 argument cards across the whole course (~5 per core author, the rest self-made). The 40-card argument deck is the *core* deck — the two signature arguments per entry that the entries themselves single out — and is the one to keep up with daily. The checkpoint deck is a larger companion for use while working through each guide; treat it as per-guide revision material rather than a second daily obligation. Import each figure's cards **when you finish that figure** (or its guide), never as a day-one dump of all 318.

## Format and importing into Anki

Both files are plain TSV (tab-separated values), UTF-8, one card per line, **exactly three fields per line**:

1. **Front** — the prompt.
2. **Back** — the model answer.
3. **Tags** — space-separated Anki tags.

Tag schemes:

- Argument cards: `era::<era> figure::<slug> type::argument` (e.g. `era::medieval figure::aquinas type::argument`).
- Checkpoint cards: `guide::<guide-slug> figure::<slug> type::checkpoint` (e.g. `guide::hume-enquiry figure::hume type::checkpoint`). Kant has two guides (`kant-critique`, `kant-groundwork`), both tagged `figure::kant`; the Wittgenstein guide is tagged `figure::wittgenstein-late`, matching the entry slug.

To import: in Anki, *File → Import*, choose the `.tsv`, set the separator to **Tab**, map the three fields to Front / Back / Tags of a Basic note type, and **tick "Allow HTML in fields"**. That last step matters for the argument deck: its backs use `<br>` line breaks to keep the numbered premises, the conclusion, and the **Objection:** / **Reply:** lines visually separate while staying on a single TSV line, plus a little `<i>`/`<b>` markup. Without HTML enabled you will see the tags literally. The checkpoint deck's backs are plain flowing text and import cleanly either way.

Import each deck into its own Anki deck (or one deck with the tags above — the tags are enough to build filtered decks per figure or per guide).

## Review cadence — FSRS and the daily queue

The learning path (round 6 revision, §2.1–§2.2) schedules these cards with [**FSRS**](https://docs.ankiweb.net/deck-options.html), Anki's current scheduler — *not* with the hand-run +2d/+1wk/+3wk marks an earlier version of the path prescribed for cards. Those marks now govern blank-page reconstructions and checkpoints only (successive relearning, learning-path §2.3); they no longer schedule cards, and hand-scheduling cards fights the scheduler. Run it like this:

- **Setup (once, in Deck Options):** turn **FSRS on** — it is a toggle; do not assume it is already active. **Desired retention 0.90** (do not raise it; workload climbs steeply above 0.90). **Learning and relearning steps short — `10m` (or the default `1m 10m`), never 1 day or more.** Leave maximum reviews uncapped; control intake through new cards, not by hiding due reviews. After your first ~300–400 reviews, click **Optimize** in the FSRS section, and re-optimize about monthly. Do not copy anyone else's parameters.
- **Daily queue:** clear the due queue in **~10 minutes, ~6 days a week**, separate from your study sessions. At this plan's pace — a handful of new cards in a week, far under the ~5/day cap — the queue stays small. **If a backlog ever forms, stop adding new cards until it clears.**
- **Buttons:** press **Again** on any failed recall, always. Pressing *Hard* for a failure makes FSRS record a successful-but-effortful recall and inflates all future intervals.
- **Filtered decks still have a job — the reconstruction session's job, not the scheduler's.** Pulling a stage's `era::` or `figure::` tags into a custom-study deck is a fine way to run a stage-end review sweep alongside the §2.3 spaced reconstructions. Just don't use them to impose a manual calendar on the cards themselves.

However you review, review actively, as the path insists: reconstruct the argument aloud or on paper *before* flipping the card, then compare against the back — including the objection and the reply, which are part of the answer, not optional extras.

## How the decks were generated

- **Argument cards** were built from the "Signature arguments" sections of the 20 core entries: Plato, Aristotle, Anselm, Avicenna, Aquinas, Descartes, Spinoza, Locke, Hume, Kant, Rousseau, Hegel, Marx, Nietzsche, Russell, the late Wittgenstein, Popper, Kuhn, Rawls, and Foucault (`eras/…`). Each entry's section contains exactly two reconstructed arguments, each already followed by a standard objection and a reply; the card back is a faithful compression of that material to ~120 words, keeping every premise, the conclusion, and both the objection and the reply.
- **Checkpoint cards** were built from the checkpoint questions **with their answers** at the end of all 18 study guides in `study/` (14–18 questions per guide). The guide's own answer is used, with markdown formatting stripped and wording condensed only where needed to stay under ~120 words — most answers were already short and needed no shortening. (The shortest, Hobbes on the causes of quarrel, is seven words and complete as written in the guide.)

No card asserts anything that is not in its source entry or guide; where a source presents a scholarly dispute as open (several replies end that way), the card says so rather than picking a side.
