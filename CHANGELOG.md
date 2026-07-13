# Changelog

All notable changes to the RēDesign landing page are recorded here.
The format is based on [Keep a Changelog](https://keepachangelog.com/), and the
project uses [Semantic Versioning](https://semver.org/).

## [2.0.0] - 2026-07-13

Complete visual redesign. Six full candidate designs were generated and scored by
independent judging passes on first impression, craft, and product storytelling; the
"Swiss instrument" direction won and the best pieces of the others were folded in.

### Added
- Click any screenshot (the eight specimens, the hero film strip outputs, or the control
  panel) to enlarge it in a framed lightbox with a placard caption. Esc, the close
  button, or clicking outside dismisses it.
- The gallery filter now animates: leaving cards fade down and out, arriving cards deal
  back in with a short stagger. Instant under reduced motion.

### Changed
- Calmed the visual hierarchy so the page has one clear path for the eye instead of a
  dozen equal-weight boxes at first paint (progressive disclosure). Above the fold, the
  DOC/LICENSE/HOST/MAKER band, the calibration strip's labels, and the hero's
  LATENCY/COST list are gone, leaving headline, a thin gradient rule, one line of pitch,
  one button, then the real run. Each section header drops its second (right-side) label,
  the drafting grid is lightened to a whisper, and the heavy 2px section rules become 1px.
- Regenerated `og-image.png` as a light spec-sheet share card: the logo, the poster
  headline, the calibration strip, the "Automated Figma. A team of turbo developers on
  tap." line, and a row of four real outputs. Replaces the old dark card.
- Repointed the pitch at what the tool is for. The hero lede now leads with the value
  ("Paste a screenshot and get a wall of directions back, all at once. It is automated
  Figma, a team of turbo developers on tap...") instead of describing the mechanism, and
  the install section labels the macOS build as Apple silicon.
- New identity: a light "spec sheet" design on warm paper with ink typography (Archivo
  900 poster headline, Fragment Mono micro-labels, one Fraunces italic accent), a
  page-wide drafting grid, ruler ticks, lettered section codes (Sec. A through F), and
  the brand gradient quarantined into a single full-bleed "calibration strip" with its
  hex endpoints printed on it. Replaces the dark violet-glow theme.
- The hero now proves the product above the fold: a run-console bar (the input filename,
  all five model chips, a "run complete" readout, a working replay control and a gradient
  progress bar) sits on top of a film strip holding the schematic of the input beside
  four of the real outputs, dealt in with a staggered animation on load.
- The gallery hangs the eight real outputs as framed specimens with placard captions
  (index, model dot, preset), plus the existing model filter and a live
  "Showing 08 / 08" readout.
- Models are now a spec table (including how each one sees the screenshot), presets are
  a numbered index, the control panel screenshot sits between drafting corner marks, and
  features read as a numbered ledger.
- Install now leads with the prebuilt one-file releases (Windows, Linux, macOS) under
  "One file. No install.", with a download button; the syntax-colored copy-button
  terminal stays as the from-source path. The hero's primary button is the download too,
  with GitHub kept in the nav, install band and footer.
- Trimmed for pace after review: the hero spec ledger keeps only its two best lines
  (latency and cost), the prompt presets fold into the models section as one italic
  index line, the feature ledger drops the two rows the hero and models table already
  cover, and the duplicate captions under the table, the gallery and in the colophon
  are gone. Sections reletter to A through E. A second pass then roughly halved the
  body copy in every section.
- Every scroll reveal is transform-only, so all content stays visible even with
  JavaScript off, in reader modes, or under reduced motion.

### Removed
- The fanned mock-card hero wall; the real outputs carry the page now.

## [1.2.3] - 2026-07-06

### Added
- The four cards revealed by "Show all eight" (or a model filter) now fade and rise in with a short staggered animation. It runs once and respects reduced-motion preferences.

## [1.2.2] - 2026-07-06

### Changed
- On small screens the gallery now starts at four cards with a "Show all eight" button, so the page is not one endless scroll. Tapping the button, or any model filter, reveals the rest. Desktop still shows all eight at once.

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
