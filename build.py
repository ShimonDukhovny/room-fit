#!/usr/bin/env python3
"""Build the standalone app from the single source page.

src/room-fit.html is written as a Claude artifact fragment: the artifact host wraps it in its own
<!doctype>/<head>/<body>. This script does that wrapping for the copies that run without Claude,
writing index.html: the file to double-click on a Mac, and the page GitHub Pages serves.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = (ROOT / "src" / "room-fit.html").read_text(encoding="utf-8")

# everything before the first page element is head material: <title>, font links, <style>
split = src.index('<div class="wrap">')
head, body = src[:split].strip(), src[split:].strip()

# the same base the artifact host provides: charset, viewport, light scheme, safe-area padding, reset
base = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
  :root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
  body { margin: 0; font: 14px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; background: #f7f7f5; }
  img { max-width: 100%; }
  [hidden] { display: none !important; }
</style>"""

page = f"""<!doctype html>
<html lang="en">
<head>
{base}
{head}
</head>
<body>
{body}
</body>
</html>
"""
(ROOT / "index.html").write_text(page, encoding="utf-8")
print(f"wrote index.html ({len(page):,} bytes)")
