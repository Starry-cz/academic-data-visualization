# Academic Data Visualization — Claude Code Installation

The Claude Code skill is at `academic-data-visualization/`. Install via symlink:

```bash
ln -s $(pwd)/academic-data-visualization ~/.claude/skills/academic-data-visualization
```

Or copy:
```bash
cp -r academic-data-visualization ~/.claude/skills/academic-data-visualization
```

After installation, Claude Code auto-triggers on: "make a volcano plot", "画个热图",
"review this figure for Nature", etc.

The skill checks `academic-data-visualization/assets/figures/<type>/` for production scripts before
generating any code. Add your own scripts there to extend figure type coverage.

Generated: 2026-07-29 11:29 UTC
