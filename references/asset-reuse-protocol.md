# Production Asset Reuse Protocol

Use this protocol after the figure plan and backend have been fixed. Its purpose is to reuse proven layout and mark decisions without forcing incompatible data into an old script.

## 1. Route the requested chart

1. Read `figure-type-catalog.md` to identify the information task and implementation status.
2. Resolve the user language with `chart-alias-index.md` and obtain the canonical chart ID.
3. Check the selected record in `chart-registry.yaml`.
4. If the status is `production_template`, read `directory-map.md` and follow the declared `asset_path`.
5. Open `asset.yaml`, the candidate script, and its companion PNG before deciding to reuse it.
6. If the status is `reusable_pattern` or `on_demand`, do not invent an asset path; classify the work as visual adaptation or new implementation.

Do not route from a vague filename match when the catalogue contains an exact entry.

```text
用户语言
→ alias index
→ canonical chart
→ implementation status
→ production asset directory（仅当存在）
→ native reuse / visual adapt / new implementation
```

## 2. Classify reuse

| Class | Conditions | Allowed changes | Delivery label |
|---|---|---|---|
| `native reuse` | Same chart semantics, compatible data structure, backend available | Data path, user labels, declared theme tokens | Production asset reused |
| `visual adapt` | Same chart semantics, compatible dimensions, different column names or safe transforms | Column mapping, grouping field, data-safe transform, declared theme tokens | Production visual system adapted |
| `new implementation` | No semantic match or incompatible data structure | Build a chart-specific script using shared typography, colour, and export contracts | New implementation |

The reuse class describes provenance, not quality. Every class must pass the same QA protocol.

## 3. Semantic compatibility gate

Before mapping columns, answer:

- What does the production script actually encode?
- What does the user need to compare or infer?
- Are the number and type of dimensions compatible?
- Does the script imply pairing, hierarchy, time, composition, or spatial structure that the user data does not contain?

Column renaming cannot repair a semantic mismatch. For example, a two-dimensional joint-density plot is not a reusable template for several independent one-dimensional distributions.

## 4. Data compatibility gate

Check the candidate script for:

- logarithms or log axes: all relevant inputs must be positive;
- normalization: the source range must be finite and non-zero;
- square roots or ratios: domains and denominators must be valid;
- binning or KDE: the sample count and value range must support the estimator;
- paired or repeated-measure operations: identifiers and pairing must be present;
- fixed category orders: every expected category must be mapped explicitly.

If a transform is incompatible, either use a scientifically justified alternative or classify the panel as a new implementation. Document the change.

## 5. Native reuse

1. Copy the complete production script into the working directory.
2. Change only the input path, user-facing labels, and selected theme tokens.
3. Run it with its native backend.
4. Verify that all expected outputs exist and are non-empty.
5. Preserve its PDF/SVG output as the editable panel master.

If execution fails, record the reason and reclassify the panel; do not silently replace it with a simplified drawing.

## 6. Visual adaptation

Present the mapping before rendering:

```text
Production x → user column:
Production y → user column:
Production group → user column:
Changed transform:
Preserved layout / annotation / export rules:
```

Preserve the production script's chart semantics, panel geometry, annotation logic, and statistical overlays. Adapt only the confirmed data entry points and necessary data-safe transforms.

## 7. New implementation and cross-type borrowing

Borrow only low-level visual parameters from a semantically related asset:

| Requested type | Useful source | Transfer only |
|---|---|---|
| RDA | PCA | point size, alpha, ellipse treatment |
| KDE / density | Ridge or KernelDensity | line/fill hierarchy, bandwidth presentation |
| Forest | Bar comparison | line weight, marker hierarchy, label spacing |
| Heatmap | CorrelationMatrix | colour-bar typography and neutral ink |
| Scatter with fit | MarginalDensity | point alpha, fit-line weight, direct labels |

Never borrow a data transformation, statistical test, or annotation merely because its appearance is attractive.

## 8. Composition and editability

- Prefer native vector composition when all panels are vector-compatible.
- When the composition engine embeds a PNG with `imshow`, the composite PDF/SVG contains rasterized panel content.
- Deliver each native panel's vector file alongside the composite proof.
- State which panels are rasterized; do not call the composite fully editable.
- Render all mixed-language panels at their final physical dimensions and at least 450 dpi.

## 9. Asset confirmation record

Place a concise record in the work script or QA report:

```text
Panel (a): [type] → [asset path] → [native reuse / visual adapt / new implementation]
Backend: [Python / R]
Editable master: [path / unavailable]
Rasterized in composite: [yes / no]
Reason: [one sentence]
```
