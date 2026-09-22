"""Re-encode the page's heavy assets into the smaller files index.html references.

Deterministic and idempotent: run it again after adding or replacing a screenshot.

  python scripts/optimize-assets.py

What it does, and why (measured 2026-09-22, phone on slow 4G):
  * shots/gallery/*.png and shots/app.png -> .webp at quality 90 (same 726x462 / 890x689
    pixels; ~6x smaller, PSNR 37-41 dB, no visible change). The PNG masters stay in the repo
    as the source; the page only references the .webp files.
  * favicon.ico: the 256x256 frame was an uncompressed BMP (364 KB, fetched on every cold
    visit). Rewritten with the same frames PNG-compressed.
  * fonts/archivo-latin-ext-page.woff2: the only Latin Extended character the headline font
    draws is the macron in "RēDesign" (U+0113), and it pulled the whole 32 KB
    latin-ext file. This is a subset of that file holding just the extended characters the
    page uses; index.html declares it AFTER the full face, so the browser picks it for those
    code points and still falls back to the full file for anything else.

Needs Pillow (with WebP) and fontTools (pip install pillow fonttools brotli).
"""

import html
import io
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def webp(src: str, quality: int = 90) -> None:
    dst = os.path.splitext(src)[0] + ".webp"
    im = Image.open(src)
    im.load()
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA" if "A" in im.getbands() else "RGB")
    im.save(dst, "WEBP", quality=quality, method=6)
    print(f"{os.path.relpath(src, ROOT)}: {os.path.getsize(src) // 1024} KB -> "
          f"{os.path.relpath(dst, ROOT)}: {os.path.getsize(dst) // 1024} KB")


def favicon(path: str) -> None:
    ico = Image.open(path)
    sizes = sorted(ico.info.get("sizes", ico.ico.sizes()), reverse=True)
    frames = []
    for s in sizes:
        ico.size = s
        f = ico.copy()
        f.load()
        frames.append(f.convert("RGBA"))
    before = os.path.getsize(path)
    buf = io.BytesIO()
    frames[0].save(buf, "ICO", sizes=sizes, append_images=frames[1:])
    if len(buf.getvalue()) < before:
        with open(path, "wb") as fh:
            fh.write(buf.getvalue())
    print(f"favicon.ico: {before // 1024} KB -> {os.path.getsize(path) // 1024} KB ({len(sizes)} frames)")


def archivo_subset() -> None:
    from fontTools import subset

    raw = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    page = html.unescape(raw)

    def ranges(face_file: str) -> set:
        m = re.search(re.escape(face_file) + r"\"\) format\(\"woff2\"\);\s*unicode-range:([^;]+);", raw)
        out = set()
        if not m:
            return out
        for part in m.group(1).split(","):
            a, _, b = part.strip()[2:].partition("-")
            out.update(range(int(a, 16), int(b or a, 16) + 1))
        return out

    # characters the latin-ext split covers (the full face plus the code points carved out of
    # its range for the subset), minus those the latin face serves first
    ext_range = ranges("/fonts/archivo-latin-ext.woff2") | ranges("/fonts/archivo-latin-ext-page.woff2")
    # both cases of every character: CSS text-transform:uppercase turns the page's "ē" into "Ē"
    chars = {ord(v) for c in set(page) for v in (c, c.upper(), c.lower()) if len(v) == 1}
    ext = sorted(chars & (ext_range - ranges("/fonts/archivo-latin.woff2")))
    if not ext:
        print("archivo subset: no Latin Extended characters on the page")
        return
    src = os.path.join(ROOT, "fonts", "archivo-latin-ext.woff2")
    dst = os.path.join(ROOT, "fonts", "archivo-latin-ext-page.woff2")
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]
    opts.notdef_outline = True
    font = subset.load_font(src, opts)
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=ext)
    sub.subset(font)
    subset.save_font(font, dst, opts)
    cps = ", ".join(f"U+{c:04X}" for c in ext)
    print(f"archivo-latin-ext-page.woff2: {os.path.getsize(dst)} bytes for {cps}")
    declared = ranges("/fonts/archivo-latin-ext-page.woff2")
    if declared != set(ext) or declared & ranges("/fonts/archivo-latin-ext.woff2"):
        sys.exit(f"index.html: give the subset face unicode-range {cps} and cut exactly those "
                 "code points out of the full archivo-latin-ext face's range")


if __name__ == "__main__":
    for f in sorted(os.listdir(os.path.join(ROOT, "shots", "gallery"))):
        if f.endswith(".png"):
            webp(os.path.join(ROOT, "shots", "gallery", f))
    webp(os.path.join(ROOT, "shots", "app.png"))
    favicon(os.path.join(ROOT, "favicon.ico"))
    archivo_subset()
