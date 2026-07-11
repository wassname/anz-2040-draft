# ANZ 2040 site build. `just` with no target builds everything.
default: build

# build the whole site (tree first because HTML inlines it)
build: tree html

# index.html from anz-2040.md: prose via pandoc, with tree.svg inlined
html:
    python3 scripts/build_html.py

# tree.svg: the probability-sized decision tree, from data/tree.json
tree:
    python3 scripts/build_tree.py

# serve locally so relative links work (localhost:8080)
serve: build
    uvx python -m http.server 8080
