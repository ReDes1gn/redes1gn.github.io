# Changelog

All notable changes to the RēDesign landing page are recorded here.
The format is based on [Keep a Changelog](https://keepachangelog.com/), and the
project uses [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-07-06

### Changed
- Swapped the hero's mocked-up card wall for a real screenshot of the RēDesign control panel.
- Swapped the filterable sample gallery for a real screenshot of the viewer on a live run: one dashboard reimagined a dozen ways by Claude and GPT across three presets, each result tagged with its model, preset, and cost.

### Removed
- The fake redesign cards and the gallery's model filter, plus all the CSS and JavaScript they left behind.

## [1.0.0] - 2026-07-06

First public release, live at https://redes1gn.github.io/.

### Added
- Single self-contained `index.html`: sticky nav, a hero with a fanned "gallery wall" of sample redesigns, a how-it-works walkthrough, the models and prompt presets, a features grid, a filterable gallery, and a footer.
- Dark theme with a violet accent and the pink-to-gold brand gradient, set in Inter.
- A 1200x630 social share card (`og-image.png`) with full Open Graph and Twitter Card tags, so shared links unfurl with a preview.
- SVG and ICO favicons, plus `.nojekyll` for clean GitHub Pages serving.

### Changed
- Rewrote the copy in a plain, conversational voice and trimmed it down.
- Made every model name generic (Claude, GPT, Gemini, DeepSeek, Qwen, plus your own) so it does not go stale as models change.

### Removed
- Every em-dash.
