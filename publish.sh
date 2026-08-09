#!/usr/bin/env bash
# Publish legal/support HTML to GitHub Pages via the gh-pages branch on rectoly-site.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT
cp "$ROOT"/{.nojekyll,index.html,privacy.html,terms.html,support.html} "$WORKDIR/"
cp -R "$ROOT/privacy" "$WORKDIR/privacy"
cd "$WORKDIR"
git init -q
git checkout -b gh-pages
git add .
git -c user.name='hawk-takaki-takemura' -c user.email='hawk-takaki-takemura@users.noreply.github.com' \
  commit -q -m "Publish Rectoly legal pages"
git remote add origin git@github.com:hawk-takaki-takemura/rectoly-site.git
git push -u origin gh-pages --force
echo "Published: https://hawk-takaki-takemura.github.io/rectoly-site/"
