# RēDesign

**One screenshot in. A wall of AI redesigns out.**

The public landing page for RēDesign, live at **[redesign.lunarwerx.com](https://redesign.lunarwerx.com/)**.

[![Discord](https://img.shields.io/badge/Discord-join_the_community-5865F2?logo=discord&logoColor=white)](https://discord.gg/PsWpeNUzhk)

![RēDesign share card](og-image.png)

## What this is

RēDesign takes a single UI screenshot, runs it past a bunch of top AI models at the same time (Claude, GPT, Gemini, DeepSeek, Qwen, plus any you add yourself), and gives you a browsable wall of self-contained HTML redesigns to compare side by side with the original.

This repository is just the marketing site for it. The whole thing is one self-contained `index.html` served by GitHub Pages.

## Live site

> **https://redesign.lunarwerx.com/**

## How it is built

- **One self-contained file.** All of the CSS and every illustration (SVG) live inline in `index.html`. What is in the file is exactly what ships.
- **No build step, no framework, no dependencies.** Nothing to install, nothing to compile.
- **One network request.** The only thing the page fetches is the Inter font from Google Fonts. Everything else is local.
- **Hosted on GitHub Pages** straight from the `main` branch. The `.nojekyll` file tells Pages to serve the files as-is instead of running them through Jekyll.
- **Responsive** from a 375px phone up to a wide desktop, with a light and dark friendly palette, a violet accent, and the pink-to-gold brand gradient.

## What is in here

| File | What it is |
| --- | --- |
| `index.html` | The entire landing page |
| `og-image.png` | 1200x630 social share card (Open Graph / Twitter) |
| `icon.svg`, `favicon.ico` | Site icons |
| `.nojekyll` | Serve files as-is on GitHub Pages, skip Jekyll |
| `CHANGELOG.md` | What changed and when |

## Preview it locally

Any static file server works. For example:

```sh
npx serve .
# or
python -m http.server 8000
```

Then open the URL it prints.

## Updating the page

Edit `index.html` and push to `main`. GitHub Pages redeploys in about a minute. To regenerate the share card, re-render the card template to `og-image.png` at 1200x630.

## Related

The RēDesign application itself (the tool that does the work) lives at **[LunarWerxs/ReDesign](https://github.com/LunarWerxs/ReDesign)**.

## Checks

`scripts/copy-budget.mjs` runs in CI on every push that touches the page, and locally with
`node scripts/copy-budget.mjs`. It enforces two things the owner cares about:

- **No em-dashes in visitor-facing copy.** A hard zero. Use a comma, colon, semicolon or a
  full stop. Dashes inside `<style>` or `<script>` comments are ignored.
- **The page does not quietly grow back.** Length is a ratchet against the baseline in
  `scripts/copy-budget.json`, not a fixed bar, so the page may shrink freely and drift up a
  little. Cut copy on purpose? Re-record it with `node scripts/copy-budget.mjs --update` and
  commit the new baseline.

It measures what a visitor actually reads, so collapsed `<details>`, elements with a `hidden`
attribute and `<noscript>` do not count. A naive word count reads about three times high.

To see a change rather than measure it, use `~/.claude/tools/shot/shotpage.mjs`, which
screenshots the page with the scroll-reveal animations forced to their finished state.
