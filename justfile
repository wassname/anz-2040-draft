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

# rebuild and publish a clean snapshot to the public repo (keeps sources/ mirrors,
# never publishes docs/). Works without this repo being a git remote of the site.
deploy: build
    #!/usr/bin/env bash
    set -euo pipefail
    D=$(mktemp -d)
    git clone -q https://github.com/wassname/anz-2040-draft.git "$D"
    for f in README.md justfile .gitignore .nojekyll global.css anz-2040.md index.html tree.svg; do cp "$f" "$D/"; done
    cp scripts/build_html.py scripts/build_tree.py "$D/scripts/"
    cp data/tree.json "$D/data/"
    cp -r sources/ai2040-pages sources/resources "$D/sources/"
    cd "$D"
    git add README.md justfile .gitignore .nojekyll global.css anz-2040.md index.html tree.svg scripts data sources
    git -c user.name=wassname -c user.email=claude@wassname.org commit -q -m "site update" \
      && git push -q && echo "deployed: https://wassname.github.io/anz-2040-draft/" \
      || echo "no changes to deploy"
