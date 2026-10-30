#!/usr/bin/env python3
"""Gembally サイトのビルド。

_src/pages/*.html の本文に共通のヘッダー・フッター・CTAを付けて、サイト直下に書き出す。
各ページの1行目に設定を書く：
<!-- title: ページ名 | description: 説明文 | nav: ナビのキー | cta: on/off -->

使い方： python3 _src/build.py
"""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
SITE = "https://gembally.com/"
BRAND = "Gembally（ゲンバリー）"

NAV = [
    ("philosophy", "philosophy.html", "考え方"),
    ("services", "services.html", "できること"),
    ("pricing", "pricing.html", "料金"),
    ("about", "about.html", "代表紹介"),
    ("faq", "faq.html", "よくある質問"),
]
NOTE_URL = "#"  # noteのURLが決まったら差し替え
NOTE_LINK = f'<a href="{NOTE_URL}">記事（note）</a>' if NOTE_URL != "#" else ""  # 未設定の間はフッターに出さない

LOGO = (
    '<img class="logo-color" src="assets/gembally-logo-horizontal-color.svg" alt="Gembally" width="{w}" height="{h}">'
    '<img class="logo-white" src="assets/gembally-logo-horizontal-white.svg" alt="Gembally" width="{w}" height="{h}">'
)


def nav_links(active, cls=""):
    out = []
    for key, href, label in NAV:
        cur = ' aria-current="page"' if key == active else ""
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return "\n      ".join(out)


def header(active):
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="wordmark" href="index.html" aria-label="Gembally トップへ">{LOGO.format(w=144, h=34)}</a>
    <nav class="nav" aria-label="メインメニュー">
      {nav_links(active)}
    </nav>
    <a class="btn small" href="contact.html">無料で話してみる</a>
    <details class="menu">
      <summary>メニュー</summary>
      <nav aria-label="メインメニュー（スマホ）">
        <a href="index.html"{' aria-current="page"' if active == "home" else ""}>トップ</a>
        {nav_links(active)}
        <a class="menu-cta" href="contact.html">無料で話してみる</a>
      </nav>
    </details>
  </div>
</header>"""


CTA = """<section class="cta-band">
  <div class="wrap">
    <div>
      <h2>まずは60分、<span class="hl">話してみませんか。</span></h2>
      <p>初回相談は無料です。無理な営業はしません。お互いの相性を確かめる時間として、気軽にご利用ください。</p>
    </div>
    <div class="actions">
      <a class="btn" href="contact.html">無料初回相談を申し込む</a>
      <a class="btn ghost" href="pricing.html">料金を見る</a>
    </div>
  </div>
</section>"""


def footer():
    menu = "\n        ".join(f'<a href="{h}">{l}</a>' for _, h, l in NAV)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div>
      <a class="wordmark" href="index.html" aria-label="Gembally トップへ">{LOGO.format(w=127, h=30)}</a>
      <p style="margin-top:.6rem">現場を変える、ともに挑む。</p>
    </div>
    <div class="cols">
      <nav class="col" aria-label="フッターメニュー">
        <b>メニュー</b>
        <a href="index.html">トップ</a>
        {menu}
      </nav>
      <nav class="col" aria-label="お問い合わせ">
        <b>お問い合わせ</b>
        <a href="contact.html">無料初回相談を申し込む</a>
        <a href="mailto:contact@gembally.com">contact@gembally.com</a>
      </nav>
      <nav class="col" aria-label="その他">
        <b>その他</b>
        {NOTE_LINK}
        <a href="privacy.html">プライバシーポリシー</a>
      </nav>
    </div>
    <p>© 2026 Gembally</p>
  </div>
</footer>"""


def page(name, meta, body):
    title = meta["title"]
    full_title = f"{BRAND}｜現場を変える、ともに挑む。" if name == "index" else f"{title}｜{BRAND}"
    url = SITE if name == "index" else f"{SITE}{name}"
    desc = meta["description"]
    cta = "" if meta.get("cta") == "off" else CTA
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="ja_JP">
<meta property="og:image" content="{SITE}ogp.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#141c5c">
<link rel="canonical" href="{url}">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&display=swap">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>

{header(meta["nav"])}

<main id="top">
{body.strip()}
</main>

{cta}

{footer()}

</body>
</html>
"""


def parse(path):
    text = path.read_text(encoding="utf-8")
    first, body = text.split("\n", 1)
    m = re.match(r"<!--(.*)-->", first.strip())
    meta = {}
    for part in m.group(1).split("|"):
        k, v = part.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, body


def main():
    css = (SRC / "base.css").read_text(encoding="utf-8") + (SRC / "pages.css").read_text(encoding="utf-8")
    (OUT / "assets").mkdir(exist_ok=True)
    (OUT / "assets" / "style.css").write_text(css, encoding="utf-8")
    for path in sorted((SRC / "pages").glob("*.html")):
        meta, body = parse(path)
        (OUT / path.name).write_text(page(path.stem, meta, body), encoding="utf-8")
        print("built", path.name)


if __name__ == "__main__":
    main()
