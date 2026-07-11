# ANZ 2040: the decision tree

The [AI 2040 / Plan A](https://ai-2040.com) forecast, retold from an Australia and New
Zealand middle-power point of view: a decision tree of the choices Canberra and
Wellington actually face as AI gets more powerful, with named endings and our own
probability estimates. Genre is [AI 2027](https://ai-2027.com) and
[Europe 2031](https://europe2031.ai). This is a draft.

## Build

The site is one static `index.html` with no build step on GitHub's side. To regenerate
it locally:

```sh
just build        # or: python3 scripts/build_html.py && python3 scripts/build_tree.py
just serve        # build, then serve at http://localhost:8080
```

- `anz-2040.md` is the source document.
- `scripts/build_html.py` turns it into `index.html`: prose via pandoc, the decision
  tree via [mermaid.js](https://mermaid.js.org/) loaded from a CDN, CSS inline.
- `scripts/build_tree.py` turns `data/tree.json` into `tree.svg`, a probability-sized
  view of the same tree (node area tracks our estimated probability). It is a separate,
  simplified view, not generated from the mermaid tree.
- `sources/` holds the AI-2040 supplements and outside references the document cites.

## Credit

Built on the AI-2040 supplements by the [AI Futures Project](https://ai-2040.com), used
with full credit. Sources and one-line summaries are in
[`sources/INDEX.md`](sources/resources/INDEX.md).
