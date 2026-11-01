# Flashcard Decks

Anki-importable card decks built from material already in this repository. Following the retention system in the [learning path](../../learning-path.md) (§2.1), these are **argument cards, not fact cards**: every front is a *do*-prompt that demands reconstruction or explanation, never a bare "who/when/what" recall cue. Dates and definitions are deliberately not carded — the path's bet is that what needs to survive is the ability to rebuild an argument and answer its standard objection.

## The decks

| File | Cards | What it is |
|---|---|---|
| `argument-cards-core.tsv` | 40 | One card per signature argument of the 20 core entries — two per figure. Front: "Reconstruct X's argument …: numbered premises, conclusion, then the standard objection and the reply." Back: a compact model answer (premises in brief, conclusion, one objection, one reply), 107–125 words. |
| `checkpoint-cards.tsv` | 278 | One card per checkpoint question in the 18 study guides. Front: the guide's question. Back: the guide's own answer, lightly condensed (7–86 words; all under ~120). |

The learning path budgets roughly 150 argument cards across the whole course (~5 per core author). The 40-card argument deck is the *core* deck — the two signature arguments per entry that the entries themselves single out — and is the one to keep up with daily. The checkpoint deck is a larger companion for use while working through each guide; treat it as per-guide revision material rather than a second daily obligation.

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

## Review cadence

The learning path's schedule for a figure's argument cards is: **+2 days, +1 week, +3 weeks after finishing the figure, and once more at the end of the stage**. Two workable ways to run that:

- **Simplest (recommended):** add a figure's cards to your rotation when you finish the entry (and the guide, if it has one), and let Anki's spaced-repetition scheduler handle the intervals. Its expanding schedule approximates the path's cadence without manual bookkeeping.
- **Literal cadence:** use the tags to pull one figure's cards into a filtered/custom-study deck at the +2-day, +1-week, and +3-week marks, and run a stage-end filtered deck over the whole stage's `era::` or `figure::` tags before moving on.

Either way, review actively, as the path insists: reconstruct the argument aloud or on paper *before* flipping the card, then compare against the back — including the objection and the reply, which are part of the answer, not optional extras.

## How the decks were generated

- **Argument cards** were built from the "Signature arguments" sections of the 20 core entries: Plato, Aristotle, Anselm, Avicenna, Aquinas, Descartes, Spinoza, Locke, Hume, Kant, Rousseau, Hegel, Marx, Nietzsche, Russell, the late Wittgenstein, Popper, Kuhn, Rawls, and Foucault (`eras/…`). Each entry's section contains exactly two reconstructed arguments, each already followed by a standard objection and a reply; the card back is a faithful compression of that material to ~120 words, keeping every premise, the conclusion, and both the objection and the reply.
- **Checkpoint cards** were built from the checkpoint questions **with their answers** at the end of all 18 study guides in `study/` (14–18 questions per guide). The guide's own answer is used, with markdown formatting stripped and wording condensed only where needed to stay under ~120 words — most answers were already short and needed no shortening. (The shortest, Hobbes on the causes of quarrel, is seven words and complete as written in the guide.)

No card asserts anything that is not in its source entry or guide; where a source presents a scholarly dispute as open (several replies end that way), the card says so rather than picking a side.
