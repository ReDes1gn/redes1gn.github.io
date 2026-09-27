# Screenshotting the page

`scripts/copy-budget.mjs` measures the page. To *see* a change, take a full-page screenshot,
but not with an ordinary browser capture: sections use a reveal-on-scroll effect (`.rv` /
`.rv.in` in `index.html`), so a capture taken before the observer fires can show sections
offset from where they end up.

## What a trustworthy capture does

Whatever tool you use, it should do all of this before a single pixel is captured:

1. Run a headless Chrome, so nothing depends on a browser window being frontmost.
2. Emulate `prefers-reduced-motion: reduce`. This page already honours it: the reveal
   transform only applies under `prefers-reduced-motion: no-preference`.
3. Force every animation and transition to its finished state (for this page, give every
   `.rv` element the `.in` class, or inject `transition: none !important`).
4. Scroll the whole document once to trip any IntersectionObserver, then return to the top.
5. Wait for fonts, for every image to decode, and for layout to stop changing.

A capture that shows a blank band or an undecoded image is not a real result; redo it rather
than trust it.

## The shared tool

The owner's machines have a script that does exactly the steps above: `shotpage.mjs`, kept in
the shared tools of the claude-memory repo (`home/tools/shot/shotpage.mjs`, mirrored locally
under the Claude profile's `tools/shot/`). It drives the system Chrome through
`playwright-core`:

```sh
node shotpage.mjs index.html -o out.png                  # full page
node shotpage.mjs index.html --sel "#pricing" -o out.png  # one section
node shotpage.mjs index.html --each-section outdir/       # every <section>, one file each
node shotpage.mjs index.html --width 1400 --mobile        # viewport control
```

It exits non-zero when the capture cannot be trusted (blank frame, image never decoded, layout
still moving). Without that tool, any Playwright or Puppeteer script that follows the five steps
gives the same result.
