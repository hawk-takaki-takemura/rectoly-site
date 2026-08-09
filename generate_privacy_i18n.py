#!/usr/bin/env python3
"""Generate localized Privacy Policy HTML pages from privacy_i18n.py."""

from __future__ import annotations

import html
from pathlib import Path

from privacy_i18n import LOCALES, TRANSLATIONS

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "privacy"
EMAIL = "system.takemura@gmail.com"

CSS = """
  :root {
    color-scheme: light dark;
    --bg: #ffffff;
    --fg: #1b1b1f;
    --muted: #5b5b63;
    --accent: #2f6fed;
    --card: #f4f5f7;
    --border: #e2e3e7;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #121214;
      --fg: #f1f1f3;
      --muted: #a3a3ab;
      --accent: #6ea1ff;
      --card: #1c1c1f;
      --border: #2c2c31;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--fg);
    font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  }
  main {
    max-width: 720px;
    margin: 0 auto;
    padding: 48px 24px 96px;
  }
  h1 { font-size: 1.8rem; margin-bottom: 4px; }
  .updated { color: var(--muted); font-size: 0.9rem; margin-bottom: 24px; }
  h2 { font-size: 1.15rem; margin-top: 2.2em; }
  p, li { color: var(--fg); }
  ul { padding-left: 1.2em; }
  a { color: var(--accent); }
  .langs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem 0.75rem;
    margin: 0 0 32px;
    padding: 12px 14px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    font-size: 0.88rem;
  }
  .langs .label {
    width: 100%;
    color: var(--muted);
    font-size: 0.8rem;
    margin-bottom: 2px;
  }
  .langs a[aria-current="page"] {
    font-weight: 600;
    text-decoration: none;
    color: var(--fg);
  }
  footer {
    margin-top: 4em;
    padding-top: 1.5em;
    border-top: 1px solid var(--border);
    color: var(--muted);
    font-size: 0.9rem;
  }
""".strip()


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def lang_switcher(current: str, prefix: str, languages_label: str) -> str:
    links = []
    for code, name, _dir in LOCALES:
        href = f"{prefix}{code}.html"
        label = esc(name)
        if code == current:
            links.append(f'<a href="{esc(href)}" aria-current="page">{label}</a>')
        else:
            links.append(f'<a href="{esc(href)}">{label}</a>')
    return (
        '<nav class="langs" aria-label="'
        + esc(languages_label)
        + '">\n'
        + f'  <div class="label">{esc(languages_label)}</div>\n  '
        + "\n  ".join(links)
        + "\n</nav>"
    )


def render(code: str, name: str, direction: str, *, root_en: bool = False) -> str:
    t = TRANSLATIONS[code]
    prefix = "privacy/" if root_en else ""
    switcher = lang_switcher(code, prefix, t["languages_label"])
    contact = (
        f'{esc(t["contact_before"])} '
        f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    )
    return f"""<!doctype html>
<html lang="{esc(code)}" dir="{esc(direction)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"])}</title>
<style>
{CSS}
</style>
</head>
<body>
<main>
  <h1>{esc(t["h1"])}</h1>
  <p class="updated">{esc(t["updated"])}</p>
  {switcher}

  <p>
    {esc(t["intro"])}
  </p>

  <h2>{esc(t["h2_collect"])}</h2>

  <p><strong>{esc(t["mendeley_label"])}</strong> {esc(t["mendeley_body"])}</p>

  <p><strong>{esc(t["docs_label"])}</strong> {esc(t["docs_body"])}</p>

  <p><strong>{esc(t["crash_label"])}</strong> {esc(t["crash_body"])}</p>

  <p><strong>{esc(t["analytics_label"])}</strong> {esc(t["analytics_body"])}</p>

  <p><strong>{esc(t["purchases_label"])}</strong> {esc(t["purchases_body"])}</p>

  <h2>{esc(t["h2_dont"])}</h2>
  <ul>
    <li>{esc(t["dont_sell"])}</li>
    <li>{esc(t["dont_ads"])}</li>
    <li>{esc(t["dont_read"])}</li>
  </ul>

  <h2>{esc(t["h2_third"])}</h2>
  <ul>
    <li><strong>{esc(t["third_mendeley_name"])}</strong> — {esc(t["third_mendeley_desc"])}</li>
    <li><strong>{esc(t["third_icloud_name"])}</strong> — {esc(t["third_icloud_desc"])}</li>
    <li><strong>{esc(t["third_sentry_name"])}</strong> — {esc(t["third_sentry_desc"])}</li>
    <li><strong>{esc(t["third_telemetry_name"])}</strong> — {esc(t["third_telemetry_desc"])}</li>
    <li><strong>{esc(t["third_storekit_name"])}</strong> — {esc(t["third_storekit_desc"])}</li>
  </ul>
  <p>{esc(t["third_note"])}</p>

  <h2>{esc(t["h2_retention"])}</h2>
  <p>
    {esc(t["retention_body"])}
  </p>

  <h2>{esc(t["h2_children"])}</h2>
  <p>{esc(t["children_body"])}</p>

  <h2>{esc(t["h2_changes"])}</h2>
  <p>{esc(t["changes_body"])}</p>

  <h2>{esc(t["h2_contact"])}</h2>
  <p>{contact}</p>

  <footer>{esc(t["footer"])}</footer>
</main>
</body>
</html>
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for code, name, direction in LOCALES:
        path = OUT_DIR / f"{code}.html"
        path.write_text(render(code, name, direction), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")

    # Canonical App Store URL: /privacy.html (English + language switcher)
    en_name = next(n for c, n, _ in LOCALES if c == "en")
    root = ROOT / "privacy.html"
    root.write_text(render("en", en_name, "ltr", root_en=True), encoding="utf-8")
    print(f"wrote {root.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
