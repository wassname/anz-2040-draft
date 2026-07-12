#!/usr/bin/env python3
"""Build tree.svg from data/tree.json. No dependencies beyond stdlib, no JS in the
output. Layout is automatic from each item's `tier` (row) and `order` (left-to-right),
so there are no hand-tuned coordinates to drift. Box width fits its title and subtitle;
probability mass is shown by edge width, with exact values in path tooltips. Every item is an <a> into its prose section and carries a
<title> tooltip. The viewBox makes it scale to any screen width (phones included).
-- claude (opus) + wassname, 2026-07"""
import json, math, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((ROOT / "data" / "tree.json").read_text())
KINDS = d["kinds"]
CV = d["canvas"]
W = CV["w"]
FLOOR, PSCALE, NH, GAP = CV["floor_w"], CV["p_scale"], CV["node_h"], CV["gap"]
CHOICE_W, ROW_H, TOP = CV["choice_w"], CV["row_h"], CV["top"]
TITLE = d.get("title", "")
TITLE_H = 82 if TITLE else 0   # hero heading band at the top (ai-2040 "Choose a Path" style)

def width(n):
    # Claude: probability is carried by flow-weighted edges and tooltips, not node size,
    # which cannot stay proportional when text lengths differ.
    fit = max(len(n["title"]) * 7.3, len(n.get("sub", "")) * 5.7) + 26
    return max(fit, CHOICE_W)

# ---- layout: place each tier's nodes left-to-right, centred on the canvas ----
tiers = {}
for n in d["nodes"]:
    tiers.setdefault(n["tier"], []).append(n)
pos = {}  # id -> (cx, cy, w)
for t, row in tiers.items():
    row.sort(key=lambda n: n["order"])
    widths = [width(n) for n in row]
    total = sum(widths) + GAP * (len(row) - 1)
    x = (W - total) / 2
    cy = TOP + TITLE_H + t * ROW_H
    for n, w in zip(row, widths):
        pos[n["id"]] = (x + w / 2, cy, w)
        x += w + GAP

H = TOP + TITLE_H + (max(tiers) + 1) * ROW_H
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.0f}" '
       f'font-family="Georgia, serif" font-size="14">',
       f'<rect width="{W}" height="{H:.0f}" fill="#fffff8"/>']
if TITLE:
    out.append(f'<text x="{W/2:.0f}" y="{TOP+42:.0f}" text-anchor="middle" font-size="28" '
               f'font-weight="bold" fill="#111">{html.escape(TITLE)}</text>')

def edge_pts(a, b):
    ax, ay, aw = pos[a]; bx, by, bw = pos[b]
    if by > ay:   # child below: leave bottom, enter top
        return ax, ay + NH / 2, bx, by - NH / 2
    if by < ay:   # child above (back-edge): leave top, enter bottom
        return ax, ay - NH / 2, bx, by + NH / 2
    # same row: side to side
    return (ax + aw / 2, ay, bx - bw / 2, by) if bx > ax else (ax - aw / 2, ay, bx + bw / 2, by)

def edge_path(e):
    a, b = e["from"], e["to"]
    ax, ay, aw = pos[a]
    bx, by, bw = pos[b]
    route = e.get("route")
    if route == "outside-right":
        x1, x2 = ax + aw / 2, bx + bw / 2
        lane = max(x1, x2) + 55
        return f"M{x1:.0f},{ay:.0f} C{lane:.0f},{ay:.0f} {lane:.0f},{by:.0f} {x2:.0f},{by:.0f}", (lane, (ay + by) / 2)
    if route == "outside-left":
        x1, x2 = ax - aw / 2, bx - bw / 2
        lane = min(x1, x2) - 45
        return f"M{x1:.0f},{ay:.0f} C{lane:.0f},{ay:.0f} {lane:.0f},{by:.0f} {x2:.0f},{by:.0f}", (lane, (ay + by) / 2)
    x1, y1, x2, y2 = edge_pts(a, b)
    my = (y1 + y2) / 2
    path = f"M{x1:.0f},{y1:.0f} C{x1:.0f},{my:.0f} {x2:.0f},{my:.0f} {x2:.0f},{y2:.0f}"
    lf = 0.30 if abs(y2 - y1) > ROW_H else 0.5
    return path, (x1 + lf * (x2 - x1), y1 + lf * (y2 - y1) - 2)

FLOWSCALE = 26   # edge thickness = flow (probability mass through the edge) * this
edge_labels = []
for e in d["edges"]:
    path, label_pos = edge_path(e)
    sw = max(1.0, e.get("flow", 0.02) * FLOWSCALE)   # thick where the mass pours, thin in the trickle
    dash = ' stroke-dasharray="5 5"' if e.get("dashed") else ""
    path_start = (f'<path d="{path}" fill="none" stroke="#a9a99f" '
                  f'stroke-width="{sw:.1f}"{dash}>')
    if e.get("tooltip"):
        out.append(f'{path_start}<title>{html.escape(e["tooltip"])}</title></path>')
    else:
        out.append(f'{path_start}</path>')
    if e.get("label") and not e.get("dashed"):       # dashed (secondary) edges stay unlabelled
        # place the label near the source (in the gap just below the parent) so labels on
        # tier-skipping edges don't land on top of the boxes in the row they cross
        # adjacent edges: label at the midpoint (siblings have spread apart there, so they
        # don't overlap). tier-skipping edges: push the label near the source, into the gap
        # below the parent, so it doesn't land on the boxes in the row it crosses.
        edge_labels.append((*label_pos, e["label"]))
# draw labels last, each on a background halo so no stroke cuts through the text
for lx, ly, lab in edge_labels:
    lw = len(lab) * 6.6 + 10
    out.append(f'<rect x="{lx-lw/2:.0f}" y="{ly-12:.0f}" width="{lw:.0f}" height="17" fill="#fffff8"/>')
    out.append(f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" fill="#555" font-size="12.5" '
               f'font-style="italic">{html.escape(lab)}</text>')

for n in d["nodes"]:
    cx, cy, w = pos[n["id"]]
    k = KINDS[n["kind"]]
    x, y = cx - w / 2, cy - NH / 2
    rx = 22 if n["kind"] == "outcome" else 4          # pill endings, square choices/risks
    sw = 3.6 if n["kind"] == "hazard" else 2.2        # thicker borders so the category colour reads; heaviest on risks
    tip = html.escape(f'{n["title"]} — {n["sub"]}' if n.get("sub") else n["title"])
    out.append(f'<a href="{n["href"]}"><title>{tip}</title>')
    # ai-2040 style: box fill matches the page background so only the category-coloured
    # border shows (pure white would read as a patch on the cream page)
    out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{NH}" rx="{rx}" '
               f'fill="#fffff8" stroke="{k["stroke"]}" stroke-width="{sw}"/>')
    ty = cy + (4 if not n.get("sub") else -3)
    out.append(f'<text x="{cx:.0f}" y="{ty:.0f}" text-anchor="middle" font-weight="bold" '
               f'font-size="13">{html.escape(n["title"])}</text>')
    if n.get("sub"):
        out.append(f'<text x="{cx:.0f}" y="{cy+13:.0f}" text-anchor="middle" fill="#333" '
                   f'font-size="11">{html.escape(n["sub"])}</text>')
    out.append('</a>')

out.append('</svg>')
(ROOT / "tree.svg").write_text("\n".join(out))
print(f"wrote tree.svg: {len(d['nodes'])} nodes, {len(d['edges'])} edges, canvas {W}x{H:.0f}")
