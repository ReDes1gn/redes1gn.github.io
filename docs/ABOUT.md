# ReDesign site

> The single-file, no-build marketing site for RēDesign, an AI tool that redesigns UI screenshots via LLMs.

<!-- odin:about HAND-OWNED above the GENERATED marker. Edit freely; `odin codex about --ingest` carries it back into Odin's Codex. -->

## What it is

RēDesign is the marketing and documentation landing page for an AI UI redesign tool. Users can learn how the tool works, explore available AI models, view example redesigns, and access setup instructions. The entire site is a single self-contained HTML file with no build step, served via GitHub Pages to redesign.lunarwerx.com.

## Things not to forget

_The intricacies worth remembering: the gotchas, the half-built parts, the decisions whose
reason lives nowhere else. Odin never overwrites this section._

- The whole page is one self-contained ~98KB index.html with no build step, no framework, and no npm dependencies - all CSS lives in a single inline style block, so any new section's styles go there too. anchors: `index.html:26`
- The site is not purely static markup - it ships 5 separate inline script blocks (hero run animation/replay, gallery model filter, image lightbox/zoom, setup-command copy-to-clipboard), so treat it as having real client-side behavior when editing. anchors: `index.html:836`
- pricing.md is a real page that is built and listed in sitemap.xml, but index.html has zero links or references to it anywhere, so visitors can only find it by guessing the URL or via search engines. anchors: `pricing.md:1`
- llms.txt and llms-full.txt exist to give AI agents/LLM search a structured summary of the product, but like pricing.md they are listed in sitemap.xml without any on-page link from index.html. anchors: `llms.txt:1`
- The footer's 'last updated' date is a hardcoded string that has to be manually bumped by hand whenever the page changes - it is not derived from git history or CHANGELOG.md, so it silently goes stale. anchors: `index.html:1520`
- CHANGELOG.md exists in the repo but is never surfaced on the site itself - there is no blog or changelog feed linked from the page, so release notes only reach people who browse the repo directly. anchors: `CHANGELOG.md:1`

<!-- odin:about GENERATED BEGIN - rewritten by `odin codex about --publish`; edit the Codex, not this -->

## What Odin knows about this project

Everything from here down is generated from this project's Codex dossier
(`codex/projects/redes1gn-github-io.md` in the Odin clone) and is **rewritten on every publish** -
edit the dossier, not this block. Everything ABOVE the marker is yours.

### At a glance

- **Ships as:** static site - single self-contained HTML file served via GitHub Pages
- **Live at:** https://redesign.lunarwerx.com/
- **Entry points:** `site_root`
- **Deploys via:** github-pages
- **Domain:** AI design automation, UI/UX redesign, multi-model LLM comparison, design tools, screenshot analysis
- **Remote:** https://github.com/ReDes1gn/redes1gn.github.io.git

### Architecture

- `index.html` - The entire landing page with hero, workflow explanation, model showcase, gallery, FAQ, and setup instructions all inline
- `og-image.png` - 1200x630 social share card for Open Graph and Twitter embeds
- `icon.svg, favicon.ico` - Site branding icons (favicon and Apple touch icon)
- `shots/` - Sample redesign screenshots used in the gallery showcase
- `docs/` - Documentation pages (if any; structure inferred from derived block)

### Features

11 recorded - 11 shipped, 0 partial, 0 planned. Each `path:line` is where the feature is DEFINED, checked by `odin codex check`.

**Shipped**

- **Hero section with animated intro** - Eye-catching hero section at page top with the RēDesign logo animated in gradient and clear value proposition. - `index.html:1070`, `index.html:1095`
- **Step-by-step workflow explanation** - Four-step visual explanation of the RēDesign process: Drop a screenshot, Pick models and presets, Hit run, Judge the wall. - `index.html:1203`, `index.html:1206`
- **AI models showcase** - Displays the available AI models supported by RēDesign (Claude, GPT, Gemini, DeepSeek, Qwen, and custom models). - `index.html:1239`, `index.html:1242`
- **Redesign gallery with interactive viewer** - Browsable gallery of example redesigns with a filter control and a readout showing the current selection. Users can view sample before/after comparisons. - `index.html:1269`, `index.html:1284`
- **Instrument features explanation** - Describes technical capabilities including side-by-side viewer, reference images, self-healing keys, sandboxed rendering, local execution, and reproducible workflows. - `index.html:1331`, `index.html:1334`
- **Setup and installation guide** - Installation instructions section explaining that RēDesign is one file with no install required, includes copyable setup commands. - `index.html:1386`, `index.html:1389`
- **Product comparison section** - Positioning information showing how RēDesign fits relative to other design and AI tools. - `index.html:1416`, `index.html:1419`
- **FAQ section** - Frequently asked questions covering pricing, supported models, custom models, privacy, OS support, offline capability, and differentiation from direct LLM usage. - `index.html:1440`, `index.html:1443`
- **Responsive design system** - Full responsive design from 375px mobile to wide desktop with light/dark color palettes, gradient branding (pink-to-gold), and focus-visible keyboard navigation. - `index.html:26`, `index.html:78`
- **Pricing reference page** - A standalone pricing.md page explaining the tool itself is free/MIT and the only real cost is the user's own AI API usage; served at the site root and listed in sitemap.xml, but not linked from index.html's nav or FAQ (undiscoverable from the page itself). - `pricing.md:1`
- **Agent-readable site summary (llms.txt)** - llms.txt and llms-full.txt serve a structured, machine-readable product summary (what it does, key facts, links) at the site root for AI agents/LLM search per the llms.txt convention; listed in sitemap.xml but not linked from index.html. - `llms.txt:1`, `llms-full.txt:1`

### Where to add a new one

- **a new gallery item or sample redesign** - Add a new item to the gallery div (id='gallery') with image, title, and model attribution; update the gallery filter logic if needed anchors: `index.html:1284`
- **a new FAQ question** - Add an h3 and following p inside the FAQ section; the page's accordion-style interaction will apply automatically anchors: `index.html:1440`
- **a new section or page content** - Add a new section element with an id, write inline CSS for layout (all styles are in the <style> block), add any SVG illustrations inline anchors: `index.html:26`

### Gaps and wants

_Withheld: this repository is public, and the gap list is not published outside the private index._
_Read it with `python odin.py codex brief redes1gn-github-io` in the Odin clone._

---

_Generated by `odin codex about --publish redes1gn-github-io` on 2026-09-09 from a Codex dossier stamped 2026-09-04. Regenerate after the product moves; `odin codex about` reports drift._
<!-- odin:about GENERATED END sha=25add2dabb4d -->
