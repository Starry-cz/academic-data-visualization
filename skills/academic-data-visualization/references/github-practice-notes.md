# Lessons Adopted from Mature Visualization Repositories

Use these notes as design constraints, not as visual styles to copy mechanically.

## figures4papers

- Learn from real scripts that have supported published figures.
- Separate reusable design theory and API conventions from project-specific examples.
- Preserve the distinction between end-to-end code assets and figures completed partly in external software.

## SciPilot Figure Skill

- Profile the data and clarify the argument before plotting.
- Actively intercept small-sample mean bars, misleading dual axes, categorical points joined as trends, rainbow maps, and overloaded figures.
- Render, inspect, revise, and render again; source-code review alone cannot catch clipping, overlap, or weak hierarchy.

## SciencePlots

- Compose context-specific styles rather than maintaining one universal theme.
- Separate journal, presentation, grayscale, and language/font concerns.
- Treat fonts and external LaTeX/CJK requirements as explicit dependencies.

## Repository-specific extensions

- Do not equate a style preset with scientific validity.
- Bind verification to input fixtures, entrypoints, outputs, package versions, and QA evidence.
- Keep publication, keynote, report, and poster checks profile-specific.
- Require source data, computed metric metadata, alt text, and provenance alongside the image.
