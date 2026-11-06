# German: sentence and card authoring guide

**Repository:** `25d-228/meiki-deck-de-DE`  
**Repository reference path:** `LANGUAGE_GUIDE.md` at the root of this repository

**Production locale:** `de-DE`  
**Scope:** A1–C2-oriented German with a separate DACH recognition and domain-specialization layer.

## 0. Reference boundary

This guide defines the language curriculum, exact stage/card schedule, short-sentence limits and learner support. The supplied root `EXECUTOR.md` binds the repository; `docs/WORKFLOW.md` is the local copy of the one shared operating procedure and all repeated templates. Read those files in this checkout. Do not design another workflow or search elsewhere for instructions.

One local EXECUTOR plans the entire language, defines its language-specific fields, creates issues, coordinates fresh Terra authors and separate batch editors, completes one final editorial pass per stage, applies corrections, performs basic card-content checks, and merges completed stages into this repository's own `main`. There is no separate language orchestrator. Start authorizes the complete local text process, including these required content reviews; use the shared procedure for commits, pushes, PRs and merges without intermediate handoffs.

The root guide is already supplied here. Keep it at `LANGUAGE_GUIDE.md`; do not request another attachment or move it into a subfolder. Linguistic checks, editorial judgment and repair examples supply criteria for authors, separate batch editors and the final editorial pass. The shared workflow defines that one review procedure; do not invent extra review layers from individual guide headings. Common environment, English working language, privacy, package isolation and report rules belong to `docs/WORKFLOW.md` and are the same for every executor.

## 1. Purpose and required deliverables

**Fixed deliverable: 8 stages; 8,700 accepted sentence cards.** The exact stage schedule is defined in [Section 4.1](#fixed-stages).

Write original, natural **full sentences with one focused typed-cloze target**, not a personal study timetable. Each accepted record must teach a defined word, sense, grammatical distinction, or compact construction in a recoverable situation.

The text source defines the complete sentence, one hidden span, its typed answer, and concise learner support. It is not a user-interface implementation. One source record yields one cloze card; do not multiply counts through unrequested reverse or alternate-mode cards.

Deliver sentence records and a compact coverage map for this language alone. **This executor’s complete assignment is text-source production and local completion.** Finish the sentences, clozes, answers, useful annotations/readings, and necessary corrections. Follow the shared author/editor process, complete final editorial pass, correction, basic-check and self-merge procedure for every stage. At completion, post totals and merged PR links, close the local text plans, report `TEXT_ACCEPTED`, and stop. Pronunciation requirements concern textual learner support; this guide does not certify learner proficiency.

---

## 2. Production model, script, and register

Use **educated contemporary Standard German as used in Germany (`de-DE`)** for production. This is the project selection within the guide’s Germany/Austria/Switzerland options. Keep spelling, pronunciation, ordinary vocabulary, and social conventions coherent.

From B1-oriented work onward, plan labeled recognition of Austrian and Swiss Standard German and relevant northern, central, or southern usage. Swiss Standard German is not interchangeable with Swiss German dialect comprehension. Do not assemble a synthetic production model from several standards or introduce a dialect as neutral German.

---

### 2.1. Short sentences: mandatory length contract

Keep **advanced meaning, not advanced length**. The following caps apply to the **entire `common.sentence` field per card**, with its cloze restored. They include both sides of a contrast, all quoted speech, and both turns/sentences of a micro-context. They are not separate allowances per clause. No advanced, literary, domain, quotation, or politeness exception raises a cap.

| Production stages | Preferred full-text length | Hard full-text maximum |
|---|---|---|
| `00–01` | 4–9 words | **12 words AND 90 characters** |
| `02` | 6–12 words | **16 words AND 120 characters** |
| `03–07` | 8–14 words | **20 words AND 150 characters** |

**Hidden span:** normally 1–3 words; hard maximum **5 words AND 40 characters**. Apply the same ceiling to each explicit accepted answer. This ceiling does not make an arbitrary fragment, entire predicate, or unrelated group of words a good cloze. A compact conventional whole utterance can be an editorially justified exception to the visible-context rule, but not to either length cap.

Preferred bands are drafting guidance, not minimums or quotas. Naturally shorter utterances are welcome. Do not pad them or write every card near the maximum. Advanced stages keep the same upper ceiling; difficulty comes from the selected sense, grammar, collocation, register, or pragmatic distinction.

**Characters:** normalize to NFC, then count every non-whitespace Unicode code point, **including punctuation, digits, and Latin text**. Use `sum(not ch.isspace() for ch in unicodedata.normalize("NFC", text))`. This definition is for the length check only; cloze boundaries still respect grapheme clusters. Do not strip punctuation, change standard spelling, use abbreviations, or compress numerals to game the count. Readings and answer-side notes are not part of `common.sentence`, but must never hide required front-side context.

**Words:** count maximal Unicode letter/number sequences, allowing internal straight or curly apostrophes. Hyphens, slashes, and dashes separate units; punctuation-only pieces do not count as words. Thus contractions/elisions remain natural, while hyphenation cannot join several words into one for this check. Use a small standard-library counter, for example `re.findall(r"[^\W_]+(?:['’][^\W_]+)*", NFC_text)`. This is an operational count, not a linguistic segmentation theory. Both the word limit and character limit must pass.

Use **one short sentence by default**. At most two short sentences or two short conversational turns may form the source text when essential to interpretation; their **combined** text must fit the same cap. Do not add an uncounted preamble, a front-side `context` field, a screenshot, or an answer-side explanation as a way around the limit. Keep one primary target. Avoid stacked relative clauses, embedded chains, several unexplained participants, and unrelated facts. A brief subordinate or contrasting clause is allowed when it demonstrates the target.

Before accepting a card, verify that the source makes the relevant event/referent and the target's sense, relation, time, or social force interpretable. Remove decorative setup, not the governor, antecedent, negation, comparison, condition, or other essential cue. Text need not exclude every imaginable synonym, but the intended target must be natural and demonstrate the assigned use. Do not substitute an arbitrary fragment or ambiguous sense for useful context.

Keep the verb bracket or subordinate-clause verb intact. Limit modifiers between a governor and its dependent; do not remove the article/case evidence being tested. The character ceiling prevents a nominal compound chain from hiding behind a small word count.

If a candidate exceeds the cap, **rewrite the situation or choose another concise example of the same assigned learning point**. Do not truncate it, delete the objective, lower the stage count, or cram several targets into a shorter string. A long-source objective becomes a brief, self-contained demonstration of attribution, stance, contrast, or mediation—not a compressed essay. If no valid short realization can be found, record the specific conflict for review; only HUMAN may approve a specification change. Rejected cards are repaired or replaced within the fixed allocation.

Use these limits in the AUTHOR and REVIEW prompts and the stage's basic content check. Fix overlength records; no length-statistics report, separate service, repeated full audit, or extra commit is required. **Every card must fit the hard caps and retain adequate context.**

### 2.2. Illustrative concise card shapes

These examples illustrate compact, understandable contexts. They are not approved production cards, a vocabulary shortlist, or a replacement for the fixed curriculum. Stage placement must respect prerequisites.

| Complete source text | Focused cloze | Why the context is sufficient |
|---|---|---|
| Ich warte vor dem Kino auf meine Schwester. | `auf` | The verb and object demonstrate the government pattern. |
| Die Zusage gilt nur, sofern die Finanzierung gesichert ist. | `sofern` | The condition is explicit in a compact subordinate clause. |
| Sein Lob klang herablassend, obwohl er es freundlich meinte. | `herablassend` | Tone and intention are contrasted without a miniature essay. |

### 2.3. Research basis and limits of the policy

The numerical caps in Section 2.1 are **project authoring decisions**, not experimentally established optimums, official proficiency requirements, or word-for-character equivalences. The reviewed evidence does not validate these exact thresholds for this sentence-card authoring task. The policy deliberately keeps the reading burden small while preserving the target's meaning and context. Do not turn a working-memory span into a sentence-word quota.

Sentence-length research notes supplied with this guide, dated 25 October 2026:

| Source | What it informs here |
|---|---|
| [Mulder et al. (2019), Applied Psycholinguistics](https://doi.org/10.1017/S0142716418000504) | Supportive sentence contexts improved vocabulary gains. |
| [van den Broek et al. (2018), Language Learning](https://doi.org/10.1111/lang.12285) | Context inference and retrieval produced different retention outcomes. |
| [Futrell et al. (2015), PNAS](https://doi.org/10.1073/pnas.1502134112) | Cross-linguistic dependency evidence; not a flashcard-length trial. |
| [Woźniak, SuperMemo formulation guidance](https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge) | Practitioner guidance: focused retrieval and economical wording. |
| [US Veterans Affairs, sentence guidance](https://design.va.gov/content-style-guide/plain-language/use-short-sentences) | General-content advice: at most 25 words, not a learning optimum. |

These sources address different tasks and populations. Their use here is a design synthesis, not a direct experiment on these cards. More context is not automatically better retention, and less context is not automatically better teaching. Preserve interpretable meaning and a focused target; do not infer a requirement for context-free guessing from a different experimental task. The exact caps, stage mapping, counting method, and rejection rules are the project policy.

---

## 3. Curriculum framework and limits of card evidence

Preserve **Goethe-Zertifikat A1 → A2 → B1 → B2 → C1 → C2** as the guide’s general reference route. **TestDaF** is a separate B2–C1-oriented academic-admission route, not another name for the whole progression. Foundation supports A1; near-native domain use is distinct from a C2 result. Sentence guides do not establish current test specifications or official vocabulary totals.

---

## 4. Prerequisites and whole-language coverage

Before generation, the language-plan issue must preserve the full fixed schedule and complete learning-point inventory below. Allocate each objective to exact stage card slots and ID ranges, with the relevant guide subsection, linguistic contrast, context, prerequisites and production/recognition role. A stage title or short core-vocabulary list is insufficient. The shared workflow defines publication, issue templates, process and checks; this section defines the linguistic scope to put into them.

For each objective, identify the prior language needed to understand the visible context. Do not make every difficult word a simultaneous new target, rely silently on later stages, or count incidental visible exposure as hidden retrieval. Count cards, lemmas, senses, constructions and relevant script measures separately. Exact counts alone do not prove vocabulary breadth or proficiency.

<a id="fixed-stages"></a>

### 4.1. Fixed production stages and exact card counts

Create **8 stages and exactly 8,700 accepted cards** for German, in the order below. These are deliverable counts, not ranges, caps, optional targets, or a sampled “core” collection. Each card is one original sentence record with one focused cloze; do not count annotations, incidental words, alternate answers, ancillary outputs, or reverse cards as additional cards.

**Allocation basis:** A dedicated foundation preserves sound–spelling and sentence-frame work. Subsequent allocations expand noun/government networks, case and adjective contrasts, clause architecture, lexical compounds, register, and DACH recognition; separate C2 and domain stages retain rhetorical and socially situated depth.

**Status of the numbers:** the counts and stage splits are project authoring allocations. They are not quantities prescribed by the source’s examination bodies, guarantees of proficiency, an exhaustive dictionary, or measured optimal learning loads. HUMAN’s approval to start production adopts this written schedule; the agents do not choose different counts while writing issues.

| Stage | Fixed deck display name | Required guide coverage | Exact cards | Batches (up to 40 cards) | Cumulative cards |
|---|---|---|---:|---:|---:|
| `00` | German 00 — Sound, spelling, and sentence foundations | Sections 6.1 | 200 | 5 | 200 |
| `01` | German 01 — A1 basic communication | Sections 6.2 | 600 | 15 | 800 |
| `02` | German 02 — A2 routine communication | Sections 6.3 | 900 | 23 (22 × 40 + 20) | 1,700 |
| `03` | German 03 — B1 independent communication | Sections 6.4 | 1,200 | 30 | 2,900 |
| `04` | German 04 — B2 extended communication | Sections 6.5 | 1,400 | 35 | 4,300 |
| `05` | German 05 — C1 precise communication | Sections 6.6 | 1,600 | 40 | 5,900 |
| `06` | German 06 — C2 precision, rhetoric, and mediation | Sections 6.7 | 1,800 | 45 | 7,700 |
| `07` | German 07 — Social, professional, and cultural depth | Sections 6.8 | 1,000 | 25 | 8,700 |
| **Total** | **8 stages** | **All eight milestone inventories, plus cross-cutting requirements** | **8,700** | **218** | **8,700** |

Use source IDs `de-<stage>-0001` through `de-<stage>-NNNN`, where `NNNN` is that stage’s exact count, zero-padded to four digits. Use `cards/<locale>/<stage>.json` and `coverage/<locale>/<stage>.md`; the production locale is `de-DE`. Deck IDs are `deck:<locale>:<stage>`. Within-stage ordering is intentional. Every stage depends only on the relevant preceding stages listed in this guide.

The batch column uses 40-card batches plus a smaller final batch when needed; a parenthesized expression shows that split. Never round a stage count up to fill a batch or down to omit the remainder. Batch size is an execution arrangement, not a requirement for 40 cards per learning point or topic. Use this split normally. If an actual runner limit prevents a batch, split only that affected batch and retain its IDs. Each authored batch receives a separate fresh editor. After assembly, one complete final pass covers every card and mapping in partitions of at most 400 cards, as specified in the shared workflow. The same executor resolves findings, checks completion and merges; no language orchestrator or additional review layer is added.

#### Required distribution across stages

- **Stage 00:** Cover useful sound–spelling contrasts, stress, basic V2 and bracket frames, articles, negation, questions, modals, and separable components.
- **Stage 01:** Cover noun packages, nominative/accusative, pronouns, present/modal/separable verbs, imperative, early dative and perfect uses, and everyday transactions.
- **Stage 02:** Cover dative, location/destination, perfect and common preterites, reflexives, comparison, adjective forms, relatives, subordinate/infinitive clauses, and government.
- **Stage 03:** Cover case/government breadth, adjective systems, relatives, passive, narrative preterite, Konjunktiv II, da/wo compounds, connectors, information order, and modal particles.
- **Stage 04:** Develop extended phrases, participial and infinitive structures, reported speech, past hypotheses, noun–verb collocations, nominal/verbal style, register, and DACH recognition.
- **Stage 05:** Cover source synthesis, stance, advanced collocations, precise clause architecture, academic/professional language, mitigation, register shifts, and region-aware comprehension.
- **Stage 06:** Cover idioms, argument reconstruction, literature/rhetoric, humor and implication, diplomatic/adversarial language, editing, and register-sensitive interpretation.
- **Stage 07:** Cover distinct community and domain senses, relationships, responsibilities, negotiations, cultural discussion, and broad labeled DACH recognition.

#### Preserve counts and substantive coverage when writing issues

Copy this complete stage table and total into the language-plan issue. Build a detailed coverage allocation under each stage: reference every substantive milestone/system requirement, state the hidden distinction or lexical family, identify contexts and prerequisites, and allocate an exact number of card slots to each authoring block. Block totals must equal the stage count, and stage totals must equal the language total. Each block brief must include its Section 2.1 sentence/cloze caps and the context cues needed to demonstrate its targets. Blocks may span several batches and have unequal sizes. A card slot has one primary learning point; overlapping secondary coverage does not make it count twice.

**Do not make a compact selection of learning points.** Do not replace the full inventory with a short representative list, a “minimum viable” curriculum, the easiest grammar forms, a handful of umbrella headings, or only the most convenient vocabulary. Concise HUMAN messages, focused clozes, and minimal tooling do not imply reduced curriculum coverage. Preserve lexical senses, constructions, contrast sets, collocations, meaningful inflectional uses, register, recognition-only distinctions, and ordinary/social/professional/cultural range. An item left visible is not thereby taught as the hidden retrieval target.

Multiple cards may develop one important expression through genuinely different senses, complement patterns, grammatical choices, collocations, registers, or communicative functions. Do not require global answer-string uniqueness. Do not fill a fixed count with cosmetic name/noun substitutions, redundant sentences, extra-long blanks, arbitrary conjugation tables, or multiple unrequested card modes.

**No agent may reduce, merge, omit, transfer, or redefine a stage’s count without an explicit HUMAN-approved amendment to this guide.** An early claim that coverage is “already sufficient,” low model output, review deletions, context limits, execution time, or fewer chosen learning points does not change the requirement. Repair or replace rejected cards within the same IDs and scope; do not submit an undersized stage as complete. If a genuine coverage/count conflict remains, record the specific gap and proposed adjustment, preserve accepted work, and request only the necessary HUMAN decision rather than padding, silently increasing, or silently reducing counts.

Only count a stage as accepted when **its exact card count is met, every planned allocation has corresponding coverage entries, the basic content check passes, and no known requirement remains unresolved**. This completion decision is not independent linguistic verification. Reconcile this once at stage completion using ordinary source checks and coverage tables; do not build a separate quota service or repeat the whole check after every batch.

### 4.2. Language-specific prerequisite checks

Do not assume Dutch, another Germanic language, or English cognates establish German gender, government, endings, or syntax. Map case selection, noun gender/plural, clause frame, and sound separately. A familiar-looking compound may have a lexicalized meaning; check it before assigning coverage credit.

Make verb-second order and useful noun phrases available early. Do not require isolated mastery of every declension table before meaningful sentences, and do not use unrestricted advanced noun phrases as incidental A1 support.

---

## 5. Essential systems to represent in sentences

### Nouns and government
Teach nouns with gender, plural, a useful case frame, and collocation. Add an unpredictable genitive singular when needed. The source’s **der Tisch — die Tische**, **am Tisch sitzen**, **auf den Tisch legen**, and **den Tisch decken** illustrate different lexical and grammatical uses, not four automatic cards for every noun.

Cover government such as **mit + dative**, **für + accusative**, **jemandem helfen**, **warten auf + accusative**, **sich erinnern an + accusative**, **teilnehmen an + dative**, **abhängig von + dative**, **stolz auf + accusative**, **jemanden um etwas bitten**, and **jemandem etwas erklären**. For two-way prepositions, distinguish location from destination; do not teach “movement means accusative.”

### Clause architecture
Build German sentences directly around the frame: main-clause verb second, verb-first questions/commands, the sentence bracket, and verb-final subordinate clauses. Distinguish coordinating **und/aber/oder/denn**, first-field **deshalb/trotzdem/dann**, and subordinating **weil/obwohl/wenn/dass**. The middle field carries information structure; it is not an English sentence with a verb moved afterward.

### Separable verbs and compounds
Record infinitive, separation, participle, and relevant stress. Contrast the source’s **UMfahren/umFAHren** senses only after verification in an actual context; do not apply the pattern indiscriminately. For **Antrag**, select useful **stellen/bearbeiten/ablehnen**, compound, and nominalization uses with their real meaning, gender, and register.

### Spoken and written language
Cover reductions, contractions **zum/zur/im/am/ins**, weak forms, linking, particles **doch/mal/ja/halt/eben/denn**, reformulation, and register. Modal-particle meanings need an interpretable conversational situation, not a permanent English-equivalent label.

---

## 6. Milestone curriculum and sentence briefs

These eight headings organize the curriculum content. **The fixed production schedule in Section 4.1 defines the actual stage IDs, names, exact card counts, and mapping to these headings.** Use that mapping without merging or dropping a stage. Where two stages share a milestone, divide its full inventory according to their stated emphases; where foundation is integrated into A1, retain both inventories. Cross-cutting requirements in Sections 5 and 7–13 remain mandatory.

The inventories below retain the source’s language topics. A topic such as long-source synthesis, rapid group discussion, or handwriting must be mapped to its teachable sentence component and its outside-card limitation; do not pretend the card performs the entire task. The **sentence brief**, **hidden target**, and **authoring criterion** are authoring adaptations. Apply them during authoring, batch editing and the complete final editorial pass. They are not learner examinations or permission to add a separate review process for each topic.

### 6.1. Foundation

**Curriculum reference:** Sound–spelling and sentence foundation

#### Required language and situation inventory

Include:

- German letter–sound correspondences;
- long versus short vowels;
- tense versus lax vowel quality;
- **ü** and **ö**;
- the two common realizations of **ch**;
- German **r** in your target model;
- final devoicing;
- initial consonant clusters;
- word stress;
- glottal onset and phrase boundaries;
- basic reduction of unstressed **-e, -en, -er**.

High-value contrasts include:

- *füllen / fühlen*;
- *Hölle / Höhle*;
- *bitten / bieten*;
- *Stadt / Staat*;
- *können / kennen*.

Keep German sound specifications distinct from English spelling-based guesses.

**Initial grammar**

Include elementary sentence grammar alongside sound:

- present tense;
- *sein, haben, werden*;
- main-clause verb-second order;
- yes/no and question-word questions;
- nominative and basic accusative;
- definite and indefinite articles;
- negation with *nicht* and *kein*;
- common modal verbs;
- numbers, time, dates, prices;
- basic separable verbs.

#### Authoring brief

**Sentence contexts:** Identity, clarification, quantities, questions, and short clauses with the basic bracket.

**Focused hidden targets:** A sound–spelling word, article, present/modal form, negation, or separable component.

**Authoring criterion:** Keep V2 and useful phrases visible from the start; do not stage an alphabet-only detour.

### 6.2. Basic communication

**Curriculum reference:** A1

#### Required language and situation inventory

Include:

- nominative and accusative article systems;
- personal and possessive pronouns;
- present tense of regular and common irregular verbs;
- modal verbs;
- separable verbs;
- imperative forms;
- basic dative in frequent chunks;
- *es gibt*;
- local prepositions;
- coordinating conjunctions;
- introduction to *weil* and *dass* clauses;
- conversational past with *haben* and *sein*;
- adjective use after *sein* and before nouns in fixed phrases.

#### Authoring brief

**Sentence contexts:** Family, home, routine, work/study, shopping, transport, appointments, health requests, events, and plans.

**Focused hidden targets:** An article/case choice, present verb, modal, imperative, es gibt component, or introductory perfect.

**Authoring criterion:** Use dative and adjective phrases within the stated early scope; do not force every ending equally.

### 6.3. Routine communication

**Curriculum reference:** A2

#### Required language and situation inventory

Include:

- full dative article and pronoun system;
- common accusative and dative prepositions;
- two-way prepositions through location/destination contrasts;
- past participles and *Perfekt*;
- simple past of *sein, haben,* and modal verbs;
- reflexive verbs;
- comparative and superlative;
- adjective endings in high-frequency frames;
- relative clauses in nominative and accusative;
- subordinate clauses with *weil, dass, wenn, obwohl*;
- infinitive constructions with *zu*;
- indirect questions;
- common verb–preposition combinations.

#### Authoring brief

**Sentence contexts:** Recent events, practical problems, requests for solutions, comparisons, and connected messages.

**Focused hidden targets:** Dative, location/destination contrast, perfect/preterite component, reflexive form, adjective ending, or clause connector.

**Authoring criterion:** Check subordinate verb position, the actual governor, and pronoun reference.

### 6.4. Independent communication

**Curriculum reference:** B1

#### Required language and situation inventory

Include:

- nominative, accusative, dative, and common genitive functions;
- adjective endings across frequent article patterns;
- relative clauses in all common cases;
- passive voice;
- *Präteritum* in narrative and formal writing;
- *Konjunktiv II* for requests, hypotheses, and politeness;
- indirect speech recognition;
- da- and wo-compounds;
- extended verb–preposition government;
- connectors for cause, consequence, contrast, concession, and condition;
- natural ordering of pronouns, objects, time, manner, and place;
- common modal particles.

#### Authoring brief

**Sentence contexts:** Narratives, explanations, opinions, formal/informal messages, and practical repair.

**Focused hidden targets:** Genitive/common case use, passive, Konjunktiv II, relative component, da/wo compound, or particle.

**Authoring criterion:** Keep information order natural and reported-speech recognition distinct from a full productive system.

### 6.5. Upper-intermediate operation

**Curriculum reference:** B2

#### Required language and situation inventory

Include:

- stable case and adjective accuracy under pressure;
- extended noun phrases;
- participial modifiers in reading and formal writing;
- passive alternatives and impersonal constructions;
- advanced infinitive clauses;
- reported speech and *Konjunktiv I* recognition;
- *Konjunktiv II* past forms;
- noun–verb collocations;
- nominal style versus verbal style;
- precise connectors;
- discourse particles and conversational softening;
- flexible information structure in the middle field;
- spoken reductions and regional accent tolerance.

#### Authoring brief

**Sentence contexts:** General arguments, professional meetings, telephone interaction, source comparisons, and proposals.

**Focused hidden targets:** Nominal/verbal style, a participial component, passive alternative, precise connector, or past hypothetical form.

**Authoring criterion:** Include written and spoken contexts; a long noun phrase must not become an arbitrary oversized cloze.

### 6.6. Advanced development

**Curriculum reference:** C1

#### Required language and situation inventory

Include:

- source synthesis;
- implicit meaning and stance;
- precise qualification;
- reformulation without lexical repetition;
- complex sentence architecture without loss of clarity;
- idiomatic noun–verb combinations;
- formal academic and professional writing;
- register switching;
- disagreement, criticism, and mitigation;
- fast unscripted group listening;
- Austrian and Swiss standard comprehension;
- professional presentations and meetings.

#### Authoring brief

**Sentence contexts:** Professional and academic sources, qualified disagreement, reformulation, and DACH recognition.

**Focused hidden targets:** A precise collocation, source relation, register shift, or complex-clause component.

**Authoring criterion:** Keep clarity, attribution, and actual scope; not every advanced sentence should be nominal or bureaucratic.

### 6.7. Proficient integration

**Curriculum reference:** C2

#### Required language and situation inventory

Select the specific advanced distinctions that remain uncovered; do not equate course completion with coverage.

Maintain coverage entries for:

- collocations;
- case and government;
- sentence architecture;
- register;
- modal particles;
- formal nominal style;
- spoken reductions;
- pronunciation and prosody;
- Austrian and Swiss usage;
- idioms;
- cultural references;
- recurring personal errors.

**Integrated language functions**

Include:

- synthesis of several long sources;
- reconstruction of complex arguments;
- literary and rhetorical analysis;
- humor, irony, understatement, and indirect criticism;
- rapid multi-speaker interaction;
- unfamiliar accents;
- advanced editing;
- persuasive, diplomatic, and adversarial language;
- spontaneous professional explanation outside rehearsed topics.

#### Authoring brief

**Sentence contexts:** Rhetorical and literary cases, mediation, irony, indirect criticism, adversarial or diplomatic responses, and editing.

**Focused hidden targets:** One focused rhetorical component, lexical distinction, or meaning-preserving repair.

**Authoring criterion:** The visible situation must support the effect; a card cannot stand in for a full multi-source presentation.

### 6.8. Domain-specific near-native command

**Curriculum reference:** Selected professional, social, and cultural domains

#### Required language and situation inventory

Include:

1. **One professional identity in German.**
2. **One stable social community.**
3. **One target standard variety.**
4. **Broad receptive familiarity with DACH variation.**
5. **Several cultural fields developed through sustained participation.**

Use language situations drawn from:

- working or studying in German;
- recurring group activities;
- friendships maintained principally in German;
- conflict, negotiation, and problem-solving;
- formal and informal messaging;
- literature and long-form journalism;
- comedy and conversational analysis;
- native editorial feedback;
- advanced prosody coaching;
- repeated participation in the same institutions and relationships.

#### Authoring brief

**Sentence contexts:** Responsibilities, relationships, negotiations, cultural references, and region-aware professional communication.

**Focused hidden targets:** A verified domain or pragmatic distinction in the selected German production model.

**Authoring criterion:** Keep DACH recognition broad but labeled; do not claim dialect or native participation from these sentence cards.

---

## 7. Pronunciation-aware sentence selection

Choose words and sentences that expose the required sound–form distinction while remaining natural and comprehensible. Document the intended reading, stress or tone, phrase boundary, emphasis, and register as written learner support when needed. Keep each annotation attached to its actual target or explicitly declared sentence scope; a spelling check alone does not establish phonological accuracy.

Keep ordinary written answers separate from phonetic aids. Verify textual readings and relevant pronunciation claims against the exact form, sense, and production variety. Do not add pedagogical stress marks to ordinary spelling unless the guide requires them there. Written annotations do not establish practical pronunciation or multi-speaker comprehension.

### Language-specific requirements

Cover long/short and tense/lax vowels, **ü/ö**, **ich-Laut/ach-Laut**, the selected **r**, final devoicing, clusters, stress, glottal onset/phrase boundaries, and reduced **-e/-en/-er**. The source’s **füllen/fühlen, Hölle/Höhle, bitten/bieten, Stadt/Staat, können/kennen** are contrast seeds.

Review prefix and compound stress in context. Keep normal orthography, capitalization, **ä/ö/ü**, and **ß** in the answer; pronunciation support must not silently rewrite them. Written pronunciation support must account for vowel quality/length, endings, consonants, stress, and phrase grouping, not one conspicuous sound.

---

## 8. Spoken-language sentence composition

Write language that can be understood as an utterance, not a collection of glosses. Use audible grammatical and lexical distinctions in their real phrases. All necessary information must be inside the sentence or a short self-contained exchange; a back-side note cannot invent the missing situation.

The text need not exclude every imaginable synonym, but the assigned canonical target must be natural, interpretable in context, and aligned with the intended learning point. Do not add every plausible synonym as an accepted written variant.

### Language-specific requirements

Select sentences with real verb brackets, weak articles/pronouns, case endings, separable prefixes, discourse particles, and reformulation. Preserve the inflection carrying the learning point and keep regional recognition separate from the fixed production variety.

---

## 9. Reading, script, and genre in sentences

Select a suitable genre and keep the whole card within the hard limits in Section 2.1. Use a short, self-contained situation with controlled supporting language. Advanced scope, stance, or reference must remain interpretable inside the same cap; rewrite the example rather than making the maximum longer. Sentence brevity never authorizes reducing the learning-point inventory or card count.

Do not copy books, transcripts, examination questions, or corpus sentences into the deck. Use references to understand a pattern and write an original situation. A literary or source-comparison card must contain the short evidence it asks the learner to interpret.

### Language-specific requirements

Use original practical messages, narrative, accessible nonfiction, journalism-style arguments, and professional texts. Review the finite verb, bracket, noun-phrase head, case governor, reference, and clause relations. Analyze compounds to help selection, but never assume the meaning is just the sum of the components.

---

## 10. Contrastive cloze design

Specify the intended sense or contrast **before** choosing the blank. Hide one word or a compact useful contiguous construction, leaving the substantive proposition and necessary context visible. A compact fixed utterance can be a justified exception; a long predicate or whole rewritten passage is not.

Distinguish meaningful contrast from padding. Changing only a name, noun, tense, or topic does not automatically create a new learning point. Repeated answer strings are allowed for substantively different senses, frames, or pragmatic functions. Do not enlarge a cloze to make it globally unique.

Keep `answer == cloze`, require one exact occurrence in `common.sentence`, preserve Unicode grapheme boundaries, and document intentional morphological targets. For a discontinuous construction, hide a learning-bearing component rather than every word between its parts.

### Language-specific requirements

Build useful noun-phrase contrasts across case, number, article, and adjective patterns, and clause contrasts across main/subordinate, modal, and perfect frames. A full ending table is not a sentence curriculum.

For a separable verb or sentence bracket, hide one contiguous learning-bearing component while leaving the other component visible, or choose a naturally contiguous form appropriate to the objective. Do not conceal intervening objects and adverbials merely to put the whole verb in one blank. For case government, retain the governor unless the governor itself is the retrieval target.

---

## 11. Lexical support and authoring records

The shared workflow defines the fixed `common` fields, source format and two-region boundary. **Do not redefine those mechanics here.** Every production card is one object containing `common` and `language_specific`; the local executor defines only the linguistic interior of `language_specific` in the all-stage plan before generation.

### 11.1. Local binding and support design

**Local constants:** `common.locale` is `de-DE`; source prefix is `de`; the exact stage IDs are `00`, `01`, `02`, `03`, `04`, `05`, `06`, `07`. Both regions must be present; the language plan's field definition states when the specific region may be empty.

Before generation, define the specific-field names, types, scope (target/lemma/sentence), applicability, notation, and learner labels in the language-plan issue. A small field table and one filled card example are enough; no schema engine or separate validation framework is required. No specific-field name is preselected by this guide. Use that definition consistently in generation.

Select only support that helps learners understand, pronounce, distinguish or use the hidden target in context. Preserve the actual grammatical, lexical, reading/stress/pronunciation and social information required by Sections 2 and 5–10. An empty illustrative region does not authorize omitting needed support. Do not duplicate common fields or store process evidence, extra front context, arbitrary dictionary entries or unverified linguistic claims.

State when each property is required or omitted and what it describes. A necessary change to these fields is a local linguistic decision; update the plan and affected cards without rebuilding shared procedures or rewriting good content. Explanatory prose remains English; quoted forms and readings use the required script/notation.

### 11.2. Illustrative card shape

This example illustrates the agreed source structure, not an accepted production card. The empty specific region is a design placeholder; complete the local example with whatever useful support the approved local definition actually requires.

```json
{
  "common": {
    "schema_version": 2,
    "id": "de-01-0001",
    "locale": "de-DE",
    "sentence": "Ich warte vor dem Kino auf meine Schwester.",
    "cloze": "auf",
    "answer": "auf",
    "accepted_answers": [],
    "lemma": "auf",
    "meaning": "for",
    "part_of_speech": "preposition",
    "note": "Warten auf takes an accusative complement; meine Schwester names the person being awaited."
  },
  "language_specific": {}
}
```

### Additional sentence-design examples

These illustrate focused spans, not an accepted sentence bank. Apply the same language and source checks to production content.

| Full sentence | Hidden span | Design point |
|---|---|---|
| Das Kind sitzt auf dem Stuhl. | `auf dem Stuhl` | A compact location phrase; distinguish its case function from a destination. |
| Ich rufe dich nach dem Essen an. | `rufe` | The separable component an stays visible; the target does not swallow the intervening sentence. |


---


## 12. Social context and editorial judgment

Where a choice depends on social context, make the relevant speaker, listener, relationship, authority, urgency, and purpose recoverable. Use natural vocatives, a compact situational clause, or a brief attributed exchange rather than English metadata masquerading as spoken target-language text. Do not require an unsupported extra front-side field.

Separate grammar errors, unnatural collocation, unsuitable register, pronunciation problems, and valid regional alternatives. A stylistic preference is not automatically a grammatical ban. If a source claim or an example is uncertain, record the uncertainty and verify it before using that feature in production.

Specify purpose and relationship for **du/Sie**, requests, criticism, workplace small talk, telephone language, and particles. Distinguish neutral spoken language from a formal written formulation. A merely possible German sentence is not automatically idiomatic for that setting.

---

## 13. Writing and editing requirements

Use English for reasoning, planning, and review explanations. Compose the sentence itself naturally in the target language; do not translate a stock English sentence list. A learner exercise that prohibits generated prose does not prohibit the executor’s assigned authoring work. The operating language and the language of linguistic content are separate requirements.

For editing cards, write a short original source situation and a meaning-preserving repair. Hide the repaired word or compact construction rather than the entire revised sentence. Preserve actor, beneficiary, timeline, number, comparison, source attribution, uncertainty, and commitment unless the visible task explicitly changes them. Do not present invented statements as quotations from real people, research, or news.

Check gender, case, adjective endings, verb placement, tense/mood, government, word choice, collocation, register, punctuation, and English-shaped information order. In source summaries, preserve who asserts a claim and its degree of certainty. In concision tasks, do not remove a material modifier or turn a limited claim into a universal one.

---

## 14. Content acceptance and coverage reconciliation

A record is acceptable only when its sentence is natural, its target demonstrates the assigned learning point, necessary context is visible, all support describes the actual hidden form/use accurately, and every hard length cap passes. Complete every fixed stage slot; repair or replace rejected examples within the same IDs and intended scope. Numerical completion alone is not sufficient.

When authoring, keep sentence, cloze, canonical/accepted answers, lemma, meaning, grammatical label, locally defined support and coverage mapping consistent. Check prerequisites and distribution across everyday, social, professional, cultural and intellectual contexts. Distinguish useful repeated forms from cosmetic duplicates. Do not silently waive an unmet guide requirement as an aspiration; separate truly outside-card outcomes from missing teachable coverage.

Use one fresh **Terra 6.1 / high AUTHOR and a separate fresh EDITOR per batch**, followed by **one complete final editorial pass over every assembled stage card and coverage mapping**, in fresh partitions of at most 400 cards. All role instructions come from `docs/WORKFLOW.md`; this guide supplies the linguistic criteria, not a separate operational template. Resolve material findings before the final basic content check and stage merge. Apply precise justified reviewer corrections directly; use AUTHOR plus EDITOR only for affected records needing new wording. Do not repeat the complete final pass for narrow corrections or add specialist/repair agents. Record a concise summary of reviewed batches/ranges and finding dispositions in the PR, with raw responses kept locally under `/tmp`. The same executor then self-merges under repository rules and continues without another handoff. `TEXT_ACCEPTED` requires the complete editorial process as well as structural checks; it is not native-human certification or a guarantee of perfect language. Shared issues and reports remain ordinary text, not a testing or verification platform.

---

## 15. References by authoring purpose

The following reference roles and links come from the supplied language curriculum. They are **not newly checked claims of availability, editions, examination rules, or approval for copying content**. Inspect the relevant material before using it to support a disputed language decision. Do not require purchases, account creation, new tools, or downloads merely because a resource is named.

Use curriculum references for scope, dictionaries/grammars for forms and usage, spoken material for register and pronunciation, and examination references for task boundaries. Note a reference in the plan or review when it supports a material linguistic decision. Reading a reference does not authorize reproducing its exercises, recorded voices, or sentence collection.

Use **Netzwerk neu → Aspekte neu**, or **Schritte international Neu → Kontext**, as alternative source-listed scope routes. **Grammatik aktiv**, **Phonothek intensiv**, Goethe/DW materials, PONS/Langenscheidt, Duden/DWDS, Easy German, Nachrichtenleicht, ARD/Deutschlandfunk/ARTE, and examination references supply distinct kinds of evidence. Do not turn their exercise sequences into copied sentences.

| Reference | Authoring use |
|---|---|
| [Netzwerk neu — publisher](https://www.klett-sprachen.de/netzwerk-neu/r-1/605) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Aspekte neu — publisher](https://www.klett-sprachen.de/aspekte-neu/r-1/15) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Cornelsen](https://www.cornelsen.de/reihen/grammatik-aktiv-deutsch-als-fremdsprache-120002420000) | Check the selected form, sense, construction, or register. |
| [Deutsche Welle](https://learngerman.dw.com/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Goethe-Institut](https://www.goethe.de/en/spr/ueb.html) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Goethe-Institut](https://aussprachetraining.goethe.de/) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Easy German](https://www.easygerman.org/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [Nachrichtenleicht](https://www.nachrichtenleicht.de/) | Compare curriculum scope, genre, or contextual usage for original sentences. |
| [DWDS](https://www.dwds.de/) | Check the selected form, sense, construction, or register. |
| [YouGlish](https://youglish.com/german) | Check the actual pronunciation, prosody, or variety of selected language. |
| [Goethe exam training](https://www.goethe.de/en/spr/prf/ueb.html) | Check the stated task/framework boundary; do not copy examination items. |
| [Goethe-Institut](https://www.goethe.de/en/spr/prf.html) | Check the stated task/framework boundary; do not copy examination items. |
| [TestDaF](https://www.testdaf.de/de/) | Compare curriculum scope, genre, or contextual usage for original sentences. |

---

## 16. Card failure modes and repairs

An overlength source text or hidden span is a rejection, even when its grammar is correct. Rewrite a shorter demonstration of the same learning point. A short but ambiguous, telegraphic, or context-free card also requires correction. Neither is repaired by lowering the fixed count.

| Reject or investigate | Required repair |
|---|---|
| Bare noun without gender or plural support | Supply the useful lexical package. |
| Movement automatically selects accusative | Check location/destination and the actual construction. |
| Discontinuous verb hidden with all intervening words | Retarget one meaningful contiguous component. |
| V2 or final verb is patched onto translated English | Write from the German clause frame. |
| Modal particles glossed as permanent word equations | Provide discourse and relationship context. |
| DACH forms mixed into one production standard | Label recognition and keep de-DE conventions coherent. |
| A copied sentence, translation list, or mechanical substitution grid | Write an original situation with a defensible hidden learning point. |
| A whole proposition or several independent targets are hidden | Retarget one useful unit and keep the necessary context visible. |
| The source does not establish a claimed rule or level inventory | Record the gap and verify the claim before using it; distinguish proposed additions. |


---

## 17. Basis, adaptations, and unresolved scope

**Content basis:** this self-contained German authoring specification preserves its language-system inventories, eight milestone groupings, endpoint distinctions, and stated coverage landmarks. The fixed production schedule is in Section 4.1. The repository scope is `25d-228/meiki-deck-de-DE`; the guide requires no separate proficiency-plan or conversation attachment.

**Authoring adaptations:** sentence briefs, focused-target rules, JSON design examples, coverage mapping, and authoring quality requirements implement the Meiki project’s card interaction. They are not official examination criteria or claims that the supplied proficiency guide specified this exact card format. Project production choices and English support are explicit in Sections 2–4 and 11. The exact stage counts and stage splits in Section 4.1 are explicit project production allocations, not official examination quotas or measured optimal learning quantities. Where the curriculum does not enumerate every lexical item, develop that inventory transparently within the fixed allocation; do not reduce the count or silently replace the curriculum.

| Supplied guide sections | Authoring treatment |
|---|---|
| 1–3: goal, variety, framework | Retained as production scope, recognition boundaries, and limits on proficiency claims. |
| 4–5: diagnosis and essential systems | Converted to prerequisite analysis and sentence-selection requirements. |
| 6: eight milestone inventories | Knowledge topics and endpoint distinctions retained; learner comprehension/production tasks become sentence briefs and focused targets. |
| 7–11: sound, listening, reading, grammar, vocabulary | Converted to sentence composition, cloze design, annotations, and written pronunciation support. |
| 12–13: interaction, feedback, writing | Converted to social-context and editorial criteria used in the shared author/editor/final-pass process, not separate topic audits or tutor/learner assignments. |
| 14: assessment | Converted to card-acceptance criteria, separate batch editing, one complete final editorial pass and basic completion checks; no native-human review or learner performance certification is claimed. |
| 15–16: resources and failures | Kept as reference roles and card-rejection/repair criteria, without purchasing or study schedules. |
| 17: source notes | Replaced by this self-contained basis and adaptation record; no absent chat or earlier guide is required. |

**Reference boundary:** Section 15 preserves curriculum and usage references; their current availability and every linguistic claim have not been rechecked for this package. Section 2.3 separately identifies the research consulted for the length policy. Verify material uncertain usage before production through permitted tools. A reference list does not authorize installations or release publication.

---
