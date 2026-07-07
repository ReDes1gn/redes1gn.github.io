# Changelog

All notable changes to the RēDesign landing page are recorded here.
The format is based on [Keep a Changelog](https://keepachangelog.com/), and the
project uses [Semantic Versioning](https://semver.org/).

## [1.2.1] - 2026-07-06

### Changed
- Tightened the desktop hero: the fanned sample cards now hug the input screenshot instead of floating far above and below it.
- Rebuilt the mobile hero as a story you can read top to bottom: the input screenshot, a "every model sends back its own redesign" connector, one labeled sample card per model, and a link that jumps to the real results in the gallery. The four duplicate cards stay desktop-only.

### Fixed
- On mobile, the little model chips were anchored to the page instead of their own cards, so they all piled up in one spot near the bottom of the hero.

## [1.2.0] - 2026-07-06

### Changed
- Brought back the colorful hero card wall from 1.0.0. The raw app screenshots that replaced it in 1.1.0 read as flat and out of place there.
- The gallery keeps its card design and model filter, but every thumbnail is now a real output: eight actual redesigns of the sample dashboard by Claude, GPT, Gemini and Qwen, captured straight from a live run.
- The control panel screenshot moved to the features section, cropped tight and framed, where it backs up the "real tool" claim instead of carrying the hero.

### Removed
- The DeepSeek gallery filter, since the showcased run has no DeepSeek output. The models section still lists it.

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
