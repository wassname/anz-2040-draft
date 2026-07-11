#!/usr/bin/env python3
"""Build index.html from anz-2040.md. One static file, no build step on GitHub's side
and no runtime JavaScript. Prose goes through pandoc (gfm, so it matches GitHub's own
rendering and keeps quotes verbatim); the linked tree.svg image is replaced by the same
SVG inlined into the page, so its <a> links to
each section and <title> tooltips work. CSS is hand-rolled tufte, borrowing ai-2040's
palette (global.css is a Tailwind *source* file and can't be served as-is).
-- claude (opus) + wassname, 2026-07"""
import re, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
md = (ROOT / "anz-2040.md").read_text()

# Claude: Strip internal credit and local-evidence notes from the public page.
md = re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)

# Claude: Inline the linked SVG so its links work in the standalone page.
tree_link = "[![ANZ 2040: choices and possible futures](tree.svg)](tree.svg)"
assert md.count(tree_link) == 1, f"expected exactly one tree link, found {md.count(tree_link)}"
md = md.replace(tree_link, "@@TREE@@")

body = subprocess.run(
    ["pandoc", "-f", "gfm", "-t", "html", "--wrap=none"],
    input=md, capture_output=True, text=True, check=True,
).stdout
svg = (ROOT / "tree.svg").read_text()
# Claude: Crash when an SVG link no longer matches a prose heading.
heading_ids = set(re.findall(r'<h[23] id="([^"]+)"', body))
svg_targets = set(re.findall(r'href="#([^"]+)"', svg))
missing_targets = svg_targets - heading_ids
assert not missing_targets, f"tree.svg links to missing headings: {sorted(missing_targets)}"
body = body.replace("<p>@@TREE@@</p>", f'<figure class="tree">{svg}</figure>')

CSS = """
:root { --bg:#fffff8; --fg:#111; --muted:#666; --rule:#ccc; --accent:#2A623D; }
html { font-size: 17px; }
body { max-width: 42em; margin: 4rem auto; padding: 0 1.25rem;
  background: var(--bg); color: var(--fg);
  font-family: Georgia, 'Times New Roman', serif; line-height: 1.55; }
h1,h2,h3 { font-weight: normal; line-height: 1.2; margin: 2.2rem 0 0.6rem; }
h1 { font-size: 2rem; } h2 { font-size: 1.5rem; border-bottom: 1px solid var(--rule); padding-bottom: .2rem; }
h3 { font-size: 1.2rem; color: #333; }
a { color: var(--accent); text-decoration: none; } a:hover { text-decoration: underline; }
blockquote { margin: 1rem 0 1rem 1.2rem; padding-left: 1rem; border-left: 3px solid var(--rule);
  color: #333; font-size: .95rem; }
table { border-collapse: collapse; margin: 1.2rem 0; font-size: .92rem; }
th,td { text-align: left; padding: .35rem .8rem; border-bottom: 1px solid var(--rule); }
thead th { border-bottom: 2px solid #999; }
code { font-family: ui-monospace, Menlo, Consolas, monospace; font-size: .88em; }
/* the tree is a tall, narrow two-per-row flow; cap its width and centre it so the text
   stays a legible size (a wide canvas stretched to the column would shrink the text) */
.tree { margin: 1.5rem auto; max-width: 560px; overflow-x: auto; }
.tree svg { width: 100%; height: auto; display: block; }
hr { border: none; border-top: 1px solid var(--rule); margin: 2.5rem 0; }
footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--rule);
  color: var(--muted); font-size: .85rem; }
"""

HTML = f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ANZ 2040: the decisions we still get to make</title>
<style>{CSS}</style>
</head>
<body>
{body}
<footer>Built by claude (fable 5) and wassname from the
<a href="https://ai-2040.com">AI 2040 / Plan A</a> supplements. Source and mirrors in the
<a href="sources/">repository</a>.</footer>
</body>
</html>
"""
(ROOT / "index.html").write_text(HTML)
print(f"wrote index.html ({len(HTML)} bytes), inlined tree.svg ({len(svg)} chars)")
