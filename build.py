#!/usr/bin/env python3
"""Build the Persian RTL static mirror site into ./site/.

Usage:
    uv run --with markdown -- python3 build.py

Reads Markdown from ./content-fa/*.md, wraps it in an RTL layout that mirrors
the original book site, and writes static HTML to ./site/ ready for GitHub Pages.
Images are hotlinked to the original site (with attribution); no image files
are copied into this repo.
"""
from __future__ import annotations

import markdown
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).parent
CONTENT = ROOT / "content-fa"
SITE = ROOT / "site"
ASSETS = ROOT / "assets"
ORIGIN = "https://lazyvim-ambitious-devs.phillips.codes"

SITE_NAME = "لزی‌ویم برای توسعه‌دهندگان بلندپرواز"
TRANSLATOR = "مهدی خادم"
TRANSLATOR_EN = "Mehdi Khadem"

CHAPTERS: list[tuple[int, str]] = [
    (1, "مقدمه و نصب"),
    (2, "ویرایش مُدال"),
    (3, "جابه‌جایی در ویرایشگر"),
    (4, "باز کردن فایل‌ها"),
    (5, "مبانی افزونه‌ها"),
    (6, "ویرایش پایه"),
    (7, "آبجکت‌ها و حالت operator-pending"),
    (8, "کلیپ‌برد، رجیسترها و حالت‌های ویژوال"),
    (9, "بافرها، پنجره‌ها، تب‌ها و سشن‌ها"),
    (10, "پشتیبانی از زبان‌های برنامه‌نویسی"),
    (11, "جابه‌جایی میان فایل‌های سورس"),
    (12, "جست‌وجو..."),
    (13, "...و جایگزینی"),
    (14, "ترفندهای متفرقه ویرایش"),
    (15, "کنترل نسخه (گیت)"),
    (16, "پیکربندی هوش مصنوعی"),
    (17, "دیباگ کردن"),
    (18, "تست‌نویسی"),
    (19, "راهنمای جامع پیکربندی افزونه‌ها"),
    (20, "قدم بعدی کجاست"),
]

INFO_PAGES: list[tuple[str, str]] = [
    ("purchase", "خرید و حمایت"),
    ("subscribe", "به‌روزرسانی‌ها"),
    ("errata", "غلط‌نامه"),
    ("colophon", "شناسنامه"),
]

FA_DIGITS = "۰۱۲۳۴۵۶۷۸۹"


def fa_num(n: int) -> str:
    return "".join(FA_DIGITS[int(d)] for d in str(n))


# ---------------------------------------------------------------- templates

def head(title: str, root: str, desc: str) -> str:
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {SITE_NAME}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{root}/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}/assets/css/style.css">"""


def sidebar(root: str) -> str:
    toc_items = "\n".join(
        f'<li data-title="فصل {fa_num(n)} {t} chapter {n}">'
        f'<a href="{root}/course/chapter-{n}/">'
        f'<span class="chap-num">فصل {fa_num(n)}</span><br>'
        f'<span class="chap-title">{t}</span></a></li>'
        for n, t in CHAPTERS
    )
    info_items = "\n".join(
        f'<li data-title="{t}"><a href="{root}/course/{slug}/">{t}</a></li>'
        for slug, t in INFO_PAGES
    )
    return f"""<nav class="sidebar" id="sidebar" aria-label="ناوبری کتاب">
<h1>{SITE_NAME}</h1>
<input class="toc-search" id="toc-search" type="search" placeholder="جست‌وجو در فهرست..." aria-label="جست‌وجو در فهرست">
<ul>
<li data-title="خانه home"><a href="{root}/">🏠 خانه</a></li>
<li data-title="فهرست کتاب course"><a href="{root}/course/">📖 فهرست کتاب</a></li>
{info_items}
</ul>
<h2>فهرست مطالب</h2>
<ul>
{toc_items}
</ul>
</nav>"""


def footer(root: str) -> str:
    return f"""<footer class="site-footer">
<p>© ۲۰۲۴–۲۰۲۶ <a href="{ORIGIN}/">Dusty Phillips</a> (اثر اصلی، انگلیسی). ترجمهٔ فارسی: <strong>{TRANSLATOR} ({TRANSLATOR_EN})</strong> — ترجمه‌ای آموزشی و غیرتجاری.</p>
<p>📕 لطفاً از نویسندهٔ اصلی حمایت کنید: <a href="{root}/course/purchase/">خرید و حمایت</a> · <a href="https://github.com/sponsors/dusty-phillips">GitHub Sponsor</a> · <a href="https://www.patreon.com/dustyphillipscodes">Patreon</a> · <a href="{ORIGIN}/">سایت اصلی کتاب (انگلیسی)</a></p>
<p>تصاویر این سایت از سایت اصلی بارگذاری می‌شوند و متعلق به نویسنده‌اند.</p>
</footer>"""


def chapter_layout(title: str, root: str, body_html: str, pager: str, desc: str) -> str:
    return f"""<!doctype html>
<html lang="fa" dir="rtl">
<head>
{head(title, root, desc)}
</head>
<body>
<div class="container">
<button class="hamburger" id="hamburger" type="button">☰ {SITE_NAME}</button>
{sidebar(root)}
<div class="content"><main class="prose">
{body_html}
<div class="notice translator"><strong>دربارهٔ این ترجمه:</strong> این صفحه ترجمهٔ فارسی از کتاب <em>LazyVim for Ambitious Developers</em> اثر Dusty Phillips است (مترجم: {TRANSLATOR}). متن اصلی و تصاویر متعلق به نویسنده‌اند؛ لطفاً برای حمایت از ایشان به صفحهٔ <a href="{root}/course/purchase/">خرید و حمایت</a> سر بزنید.</div>
<div class="pager">{pager}</div>
</main>
{footer(root)}
</div>
</div>
<script src="{root}/assets/js/main.js"></script>
</body>
</html>
"""


def landing_layout(body_html: str) -> str:
    return f"""<!doctype html>
<html lang="fa" dir="rtl">
<head>
{head(SITE_NAME, ".", "ترجمهٔ فارسی کتاب لزی‌ویم برای توسعه‌دهندگان بلندپرواز اثر داستی فیلیپس — مترجم: مهدی خادم")}
</head>
<body>
<div class="landing">
{body_html}
{footer(".")}
</div>
<script src="./assets/js/main.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- markdown

def render_md(path: pathlib.Path, root: str) -> str:
    text = path.read_text(encoding="utf-8")
    # Drop the duplicated chapter-title H2 right after the H1 we require
    # (translators kept the original `## [Chapter N. ...]` heading).
    text = re.sub(r"^## \[?فصل [۰-۹0-9].*$\n?", "", text, count=1, flags=re.MULTILINE)
    md = markdown.Markdown(extensions=["fenced_code", "tables", "toc", "sane_lists"])
    html = md.convert(text)
    # Admonition-style tables (empty header row) become note boxes.
    html = re.sub(
        r"<table>\s*<thead>\s*<tr>\s*(?:<th></th>\s*)+</tr>\s*</thead>",
        '<table class="note">',
        html,
    )
    # Hotlink images to the original site (attributed, no redistribution).
    html = html.replace('src="/images/', f'src="{ORIGIN}/images/')
    # Rewrite absolute internal links to site-relative ones.
    html = html.replace('href="/course/', f'href="{root}/course/')
    html = html.replace('href="/"', f'href="{root}/"')
    html = html.replace('src="/assets/', f'src="{root}/assets/')
    # Keep code copyable: nothing to do here (JS adds buttons).
    return html


def first_paragraph(path: pathlib.Path, limit: int = 150) -> str:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    # strip markdown syntax crudely for a meta description
    text = re.sub(r"[#>*`\[\]()!]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


# ---------------------------------------------------------------- pages

LANDING_BODY = """<header>
<h1>لزی‌ویم برای توسعه‌دهندگان بلندپرواز</h1>
<h2 class="subtitle">(دوره‌ای برای کنجکاوان ویرایشگر)</h2>
<nav class="topnav">
<a href="./course/">📖 خواندن کتاب</a>
<a href="./course/purchase/">💛 خرید و حمایت</a>
<a href="./course/subscribe/">✉️ به‌روزرسانی‌ها</a>
<a href="./course/errata/">🖊️ غلط‌نامه</a>
<a href="./course/colophon/">ℹ️ شناسنامه</a>
<a href="https://lazyvim-ambitious-devs.phillips.codes/">🌐 نسخهٔ اصلی (انگلیسی)</a>
</nav>
<section class="card-container">
<section style="display:contents">
<div class="card"><div style="font-size:2em">🎓</div><h3>آسان</h3><p>ویرایش مُدال که می‌توانید یاد بگیرید</p></div>
<div class="card"><div style="font-size:2em">🤩</div><h3>سرگرم‌کننده</h3><p>یادگیری لذت‌بخش ویم</p></div>
</section>
<div class="cover-box">
<div class="vim-logo">VIM</div>
<div class="book-title">لزی‌ویم برای<br>توسعه‌دهندگان بلندپرواز</div>
<div class="book-sub">ترجمهٔ فارسی · مترجم: مهدی خادم<br>اثر اصلی: Dusty Phillips</div>
</div>
<section style="display:contents">
<div class="card"><div style="font-size:2em">🍎</div><h3>سالم</h3><p>کاهش آسیب‌های ناشی از تکرار (RSI)</p></div>
<div class="card"><div style="font-size:2em">🚀</div><h3>دست‌ساز</h3><p>بدون محتوای هوش مصنوعی</p></div>
</section>
</section>
<div class="cta"><a class="btn" href="./course/">خواندن آنلاین (رایگان)</a><a class="btn secondary" href="./course/purchase/">خرید یا حمایت</a></div>
</header>
<section class="content">
<h2>دربارهٔ کتاب</h2>
<p>ویم دهه‌هاست ویرایشگر منتخب توسعه‌دهندگان حرفه‌ای است، اما همیشه به سخت بودن یادگیری و سخت‌تر بودن پیکربندی‌اش معروف بوده است.</p>
<p style="font-weight:700">دیگر نه!</p>
<p>توزیع <a href="https://www.lazyvim.org/">LazyVim</a> یک تجربهٔ آماده و لذت‌بخش ساخته که با هر IDE مدرنی برابری می‌کند. پیکربندی یا لازم نیست یا ساده است.</p>
<p>با این کار مشکل «پیکربندی» حل می‌شود، اما برای استفادهٔ مؤثر از LazyVim، ابتدا باید خود LazyVim را بلد باشید.</p>
<p>این کتاب برای توسعه‌دهندگانی نوشته شده که می‌خواهند ویرایش مُدال با Neovim را سریع یاد بگیرند. روان و قابل‌هضم است، اما مهم‌تر از همه، جامع است: حاصل بیش از دو دهه تجربهٔ ویم با همان طنز ملایم داستی فیلیپس.</p>
</section>
<section class="content">
<h2>دربارهٔ نویسنده</h2>
<p><strong>Dusty Phillips</strong> توسعه‌دهندهٔ نرم‌افزار و نویسنده است. معروف‌ترین کتاب او، <em>Python Object Oriented Programming</em> اکنون به چاپ چهارم رسیده است. او از نوجوانی با QBasic و Visual Basic و Java برنامه‌نویسی را شروع کرد و خیلی پیش از مد شدن پایتون، به‌طور حرفه‌ای سراغ آن رفت؛ او اولین کسی بود که دربارهٔ پایتون ۳ کتاب نوشت و در آوردن پایتون ۳ به اینستاگرام و فیسبوک نقش داشت.</p>
<p>داستی با همسرش در نیوبرانزویک کانادا زندگی می‌کند و اخیراً با هم پلتفرم <a href="https://www.fablehenge.com/">Fablehenge</a> را برای نویسندگان رمان ساخته‌اند.</p>
</section>
<section class="content">
<div class="notice translator"><h3>دربارهٔ این ترجمهٔ فارسی</h3>
<p>این سایت ترجمهٔ فارسی و غیرتجاری کتاب <em>LazyVim for Ambitious Developers</em> است. مترجم: <strong>مهدی خادم (Mehdi Khadem)</strong>. حقوق اثر اصلی متعلق به نویسنده، <strong>Dusty Phillips</strong> است.</p>
<p>🌐 نسخهٔ اصلی (انگلیسی): <a href="https://lazyvim-ambitious-devs.phillips.codes/">lazyvim-ambitious-devs.phillips.codes</a></p>
<p>اگر این ترجمه برایتان مفید بود، لطفاً از نویسندهٔ اصلی با <a href="./course/purchase/">خرید کتاب یا حمایت مالی</a> پشتیبانی کنید تا این اثر ارزشمند رایگان بماند.</p></div>
</section>
<section class="content">
<h2>حمایت</h2>
<p>از <a href="./course/purchase/">حمایت</a> شما در پلتفرم‌های مختلف، یا خرید نسخهٔ الکترونیکی یا چاپی کتاب استقبال می‌کنم. اینجا به‌اندازهٔ یک کتاب درسی محتوا هست؛ لطفاً به هر اندازه که منصفانه می‌دانید ارزش‌گذاری کنید. <em>(— داستی فیلیپس)</em></p>
</section>
<section class="content">
<h2>چرخهٔ به‌روزرسانی</h2>
<p>وقتی به‌روزرسانی‌های مهمی در کتاب انجام شود، ابتدا در Patreon منتشر می‌شوند و حداقل دو هفته بعد به وب‌سایت می‌رسند.</p>
<p>کتاب‌های الکترونیکی و چاپی خریداری‌شده با فاصلهٔ بیشتری به‌روز می‌شوند. وقتی تغییری بزرگ در LazyVim رخ دهد که چاپ جدیدی از کتاب را ایجاب کند، با شابک جدید به‌عنوان «ویراست دوم» منتشر خواهد شد.</p>
</section>
<div class="cta"><a class="btn" href="./course/">خواندن آنلاین (رایگان)</a><a class="btn secondary" href="./course/purchase/">خرید یا حمایت</a></div>
"""


def build() -> None:
    if not CONTENT.exists():
        raise SystemExit("content-fa/ directory not found. Add Persian markdown files first.")
    SITE.mkdir(parents=True, exist_ok=True)

    # assets
    if ASSETS.exists():
        shutil.copytree(ASSETS, SITE / "assets", dirs_exist_ok=True)
    (SITE / ".nojekyll").write_text("", encoding="utf-8")

    # landing
    (SITE / "index.html").write_text(landing_layout(LANDING_BODY), encoding="utf-8")

    # course index
    chapter_links = "\n".join(
        f'<li data-title="فصل {fa_num(n)} {t}"><a href="./chapter-{n}/"><strong>فصل {fa_num(n)}</strong> — {t}</a></li>'
        for n, t in CHAPTERS
    )
    info_links = "\n".join(
        f'<li><a href="./{slug}/">{t}</a></li>' for slug, t in INFO_PAGES
    )
    course_body = f"""<h1>فهرست کتاب</h1>
<div class="notice translator"><strong>ترجمهٔ فارسی</strong> کتاب <em>LazyVim for Ambitious Developers</em> اثر Dusty Phillips — مترجم: {TRANSLATOR}. نسخهٔ اصلی: <a href="{ORIGIN}/">سایت انگلیسی</a>.</div>
<h2>فصل‌ها</h2>
<ol>
{chapter_links}
</ol>
<h2>صفحات دیگر</h2>
<ul>
{info_links}
</ul>
"""
    course_dir = SITE / "course"
    course_dir.mkdir(parents=True, exist_ok=True)
    (course_dir / "index.html").write_text(
        chapter_layout("فهرست کتاب", "..", course_body,
                       f'<a href="../">→ بازگشت به خانه</a><a href="./chapter-1/">شروع فصل ۱ ←</a>',
                       "فهرست فصل‌های ترجمه فارسی کتاب لزی‌ویم"),
        encoding="utf-8",
    )

    # chapters
    missing: list[str] = []
    for i, (n, title) in enumerate(CHAPTERS):
        src = CONTENT / f"chapter-{n}.md"
        if not src.exists():
            missing.append(src.name)
            continue
        body = render_md(src, "../..")
        prev_link = (f'<a href="../chapter-{n - 1}/">→ فصل {fa_num(n - 1)}: {CHAPTERS[i - 1][1]}</a>'
                     if i > 0 else '<a href="../../course/">→ فهرست کتاب</a>')
        next_link = (f'<a href="../chapter-{n + 1}/">فصل {fa_num(n + 1)}: {CHAPTERS[i + 1][1]} ←</a>'
                     if i < len(CHAPTERS) - 1 else '<a href="../../">← بازگشت به خانه</a>')
        out_dir = course_dir / f"chapter-{n}"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(
            chapter_layout(f"فصل {fa_num(n)}. {title}", "../..", body,
                           f"{prev_link}{next_link}",
                           f"فصل {n} ترجمه فارسی: {title}"),
            encoding="utf-8",
        )

    # info pages
    for slug, title in INFO_PAGES:
        src = CONTENT / f"{slug}.md"
        if not src.exists():
            missing.append(src.name)
            continue
        body = render_md(src, "../..")
        out_dir = course_dir / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(
            chapter_layout(title, "../..", body,
                           '<a href="../../course/">→ فهرست کتاب</a><a href="../../">← خانه</a>',
                           title),
            encoding="utf-8",
        )

    # summary
    pages = sorted(p.relative_to(SITE).as_posix() for p in SITE.rglob("*.html"))
    print(f"Built {len(pages)} pages into {SITE}/")
    for p in pages:
        print("  " + p)
    if missing:
        print("MISSING translations (skipped): " + ", ".join(missing))


if __name__ == "__main__":
    build()
