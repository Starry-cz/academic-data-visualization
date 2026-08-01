# Font policy

Verified templates require an explicitly installed sans-serif font.

- `Arial`: use the operating-system installation subject to the platform licence; this repository does not redistribute it.
- `Liberation Sans`: accepted as the open, metric-compatible CI font and distributed by its upstream package under the SIL Open Font License.

The renderer records the selected font in `figure-metadata.json` and fails if no approved font is available. It does not silently substitute an undeclared font.
