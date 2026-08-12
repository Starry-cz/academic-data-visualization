# Figure Contract

A publication-quality scientific figure is a visual argument, not an isolated plot. Before any code, color, or layout: articulate the scientific claim, map the evidence, and check for review risks. This contract must be established before Step 1 (Analyze the Request) in the Hub workflow.

## The Five-Point Contract

For every figure request, establish these five items before generating code:

### 1. Core Conclusion

Write the **one-sentence claim** the figure must defend. This is the answer to: "If the reader looks at this figure for 3 seconds, what should they conclude?"

- Good: "Knockout of Gene X reduces tumor growth by 60% in the PDX model, and this effect is rescued by WT re-expression."
- Bad: "This figure shows the results of the tumor growth experiment."

The conclusion determines what data is essential and what is noise. If you can't write the one-sentence conclusion, the figure isn't ready to be designed.

### 2. Evidence Chain

Map each planned panel to its unique contribution to the core conclusion. **Drop any panel that does not carry unique evidence.**

```
Panel a: [what it shows] → contributes [what unique evidence] to the conclusion
Panel b: [what it shows] → contributes [what unique evidence] to the conclusion
...
```

If two panels show the same data in different forms (e.g., bar chart + pie chart of the same values), merge or drop one. Redundancy signals weak narrative design to reviewers.

### 3. Figure Archetype

Classify the figure into one of four archetypes. The archetype determines layout strategy, hero panel rules, and narrative rhythm:

| Archetype | Description | Typical Layout |
|-----------|-------------|----------------|
| `quantitative grid` | Regular grid of data panels (boxplots, bars, heatmaps) | Even grid, consistent panel size, shared axes |
| `schematic-led composite` | A schematic/model panel leads, supported by data panels | Large schematic (1/3 width) + 2-3 data panels |
| `image plate + quant` | Microscopy/images paired with quantification | Image panels (larger) + adjacent quantification panels |
| `asymmetric mixed-modality` | Non-uniform layout mixing schematics, images, and data | Custom gridspec, variable panel sizes |

If unsure, default to `quantitative grid`. Most CNS figures fall into this archetype.

### 4. Delivery / Export Contract

Set the target before styling:
- **Primary profile:** [`journal_print` / `keynote_screen` / `report_web` / `poster_large`]
- **Target:** [journal, venue, report, product launch, or screen]
- **Canvas:** [physical width for print, exact pixels for screen]
- **Export format:** [editable vector master + profile-specific raster proof]
- **Colour mode:** [normally RGB unless the target explicitly requires otherwise]
- **Font:** [target-safe family and verified final-size range]

Read `delivery-profiles.md`. Do not apply manuscript typography or DPI rules to a keynote chart, and do not apply launch-style simplification to a journal figure.

### 5. Review Risk Assessment

Identify what a reviewer might challenge before they see it:

- **Statistics:** Are statistical tests clearly defined? Are error bars labeled (SD/SEM/CI)? Are p-values reported with exact values?
- **Sample size:** Is `n` clearly defined as independent experimental units rather than technical replicates? Are individual data points visible for small groups?
- **Inference:** Does the visual or headline imply causality, superiority, or generalisation beyond the design and uncertainty?
- **Color accessibility:** Is the figure interpretable in greyscale? Are red-green only pairs avoided?
- **Data traceability:** Can every data point be traced to source data?
- **Image integrity:** For microscopy/blot images — are scale bars present? Are contrast adjustments documented?
- **Model integrity:** For ML figures — are split, leakage controls, resampling unit, uncertainty, calibration, and external validation represented when relevant?
- **Screen accessibility:** For digital delivery — do text and essential graphical objects meet contrast targets, and is alt text available?

Flag any risks explicitly. A flagged risk is a checklist item; an unflagged risk becomes a reviewer comment.

## Contract Establishment Protocol

### Adaptive clarification gate

Do not present the five-point contract as a fixed intake questionnaire. First interpret all available evidence:

- the user's current request and earlier conversation turns;
- attached data, images, captions, manuscript text, code, and existing figures;
- previously confirmed backend, palette, language, journal, dimensions, and export choices;
- facts that can be read directly from the supplied files.

Create a private `known / inferred / unresolved` ledger. For every unresolved item, ask: **would a different answer materially change the supported claim, unit of analysis, chart or statistical encoding, delivery profile, or mandatory visual semantics?** Rank only those material gaps by decision impact and ask the highest-impact one to three questions. Generate their wording and content from the current task; do not reuse a fixed list simply because a contract field is empty.

Use these rules:

1. Ask **zero** questions when the context already supports a defensible figure contract.
2. Ask no more than **three** questions in the clarification round; combine tightly related gaps only when the combined question remains easy to answer.
3. Do not ask for information already stated, visible in an attachment, or reliably inferable from the surrounding manuscript or conversation.
4. Prioritise scientific blockers over aesthetic preferences. A missing observation unit outranks a preferred font; an unsupported claim outranks a preferred palette.
5. Do not pause for reversible preferences such as an unspecified library theme when the documented default can produce a safe first proof.
6. After the answers, list every non-trivial inference and default under `Assumptions`, then continue without another generic questionnaire.

Defaults must remain explicit and reversible. Match the user's language; infer the delivery context from the request when possible; otherwise use `report_web` for an exploratory first proof. Use the registered `nature-default` palette unless journal routing or user-provided colours take precedence, and follow the backend routing already defined in `SKILL.md`. Never default or infer scientific facts such as the claim, observation unit, sample size, group meaning, repeated-measure structure, or statistical result when they determine validity. If such an indispensable fact remains unavailable, identify the exact blocker instead of fabricating it.

### When to Use the Contract

- **Full contract (all 5 points):** New figure from scratch, major revision, or when the user says "I want to make a figure for my paper."
- **Abbreviated contract (conclusion + evidence only):** Quick refinement of an existing figure, or when the user provides clear specifications.
- **Skip contract:** The user explicitly asks for a quick cosmetic fix ("change the color of this bar to blue") — cosmetic-only changes don't need a new contract.

### How to Present

Present only the adaptive questions selected above. When the user's context already establishes the contract, summarise the inferred contract and assumptions briefly and proceed; do not ask for ceremonial confirmation. If the user is unsure, ask the most consequential question first and make the trade-off understandable in plain language.

### Relation to Hub Workflow

The contract is established **before** Hub Step 1 (Analyze Request). After the contract is confirmed, proceed to the normal Hub workflow:

```
Figure Contract (5 points)
    │
    ▼
Hub Step 1: Analyze Request (figure type, tool, journal)
    │
    ▼
Hub Step 2: Route or Handle
    │
    ▼
... (continue normal workflow)
```

The contract keeps the figure honest. The Hub workflow makes it beautiful. Both are needed.
