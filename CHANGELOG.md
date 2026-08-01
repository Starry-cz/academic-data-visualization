# Changelog

## Unreleased

- Added backward-compatible rendered-SVG colour QA with opacity compositing, role-aware 3:1 graphical checks, 4.5:1 text checks, grayscale warnings, embedded-image review prompts, and an opt-in `--strict-colors` delivery gate.
- Reframed the capability section around user situations, actions, and deliverables; moved registry coverage metrics out of the primary product story and replaced technical hero badges with backend and export capabilities.
- Reordered the bilingual README around reader intent: task-based navigation now appears before installation, the hero links directly to all 22 retained figure examples, and quick start is split into install and prompt steps.
- Rebuilt the Chinese and English README pages around an outcome-first quick start, verified capability boundaries, and a compact documentation map.
- Replaced outdated `96`-pattern and `40 / 40` trigger claims with registry-backed `714 / 714`, `34 / 34`, and `88 / 88` evidence.
- Restored the workflow hero to the top of the page and expanded the landing gallery to 22 production examples across distinct chart families.
- Standardized gallery thumbnails on square or landscape canvases and gave every README table cell an explicit width for symmetric rendering.
- Forced every Chinese and English README table to the same full content width with a transparent layout spacer, avoiding GitHub's content-width shrinkage.
- Removed the duplicate text heading below the workflow hero because the hero already carries the project title.
- Refined the hero copy, simplified the metric badges and navigation, and added a prominent Chinese/English switch while keeping Chinese as the default root README.
- Added regression tests for README-local links, published metrics, hero information hierarchy, table widths, gallery coverage, and card dimensions.

## 2.1.0

- Imported the supplied 24-category source taxonomy and mapped all 714 memberships.
- Expanded the registry from 177 to 665 canonical records after alias and duplicate normalization.
- Realigned category names and ordering with the source list, including qualitative/text, research-process, and scientific-computing categories.
- Added deterministic source import, explicit source-versus-extension provenance, and 714/714 regression checks.
- Preserved all 34 verified production templates; unimplemented additions remain reusable patterns or on-demand routes.

## 2.0.0

- Added a 24-category, 177-record canonical chart registry with 257 verifiable source memberships.
- Added JSON Schema, alias disambiguation, generated category references, coverage statistics, and registry audits.
- Migrated all 34 production asset directories to canonical IDs and added deterministic `asset.yaml` manifests.
- Added dependency-free registry, manifest, catalogue, routing, and README consistency checks.
- Added taxonomy/routing regression tests and made them required in GitHub Actions.
- Preserved the existing six atlas groups, production paths, palette library, and four-pass QA workflow.
- Recorded that the supplied execution plan declares 714 source memberships but does not include the underlying 714-entry list; no unprovided entries are claimed as mapped.
