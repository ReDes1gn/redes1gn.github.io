"""Bytes a visitor downloads: the committed size at HEAD of the files the site serves (GitHub Pages, no build step:
the repo root minus docs/, scripts/ and dot-folders). Not counted: PNG masters that have a .webp sibling (shots/**,
see scripts/optimize-assets.py; the page references only the .webp) and license texts, which must stay in the repo.
Prints shipped_bytes=<n>."""
import subprocess

SERVED = (".html", ".css", ".js", ".mjs", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico",
          ".woff", ".woff2", ".json", ".webmanifest", ".xml", ".txt")
SKIP_DIRS = ("docs", "scripts")
listing = subprocess.run(["git", "ls-tree", "-r", "-l", "-z", "HEAD"], capture_output=True, check=True).stdout
files = {}
for entry in listing.split(b"\0"):
    if not entry:
        continue
    meta, path = entry.decode("utf-8", "replace").split("\t", 1)
    size = meta.split()[3]
    if size != "-":
        files[path] = int(size)
total = 0
for path, size in files.items():
    parts = path.split("/")
    low = path.lower()
    if not low.endswith(SERVED):
        continue
    if any(p.startswith(".") for p in parts) or parts[0] in SKIP_DIRS:
        continue
    if parts[-1].upper().startswith(("LICENSE", "COPYING")):
        continue  # license text: never fetched by the page, must not be deleted
    if low.endswith(".png") and (path[:-4] + ".webp") in files:
        continue  # source master; the page serves the .webp encoded from it
    total += size
print(f"shipped_bytes={total}")
