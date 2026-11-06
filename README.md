<div dir="rtl">

# لزی‌ویم برای توسعه‌دهندگان بلندپرواز — ترجمهٔ فارسی

ترجمهٔ فارسی و غیرتجاری کتاب **[LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/)** اثر **Dusty Phillips**.

- 🌐 سایت فارسی (GitHub Pages): `https://mahdmahd.github.io/lazyvimAmbitiousDevsPersian/`
- 🌐 نسخهٔ اصلی (انگلیسی): [lazyvim-ambitious-devs.phillips.codes](https://lazyvim-ambitious-devs.phillips.codes/)
- ✍️ مترجم: **مهدی خادم (Mehdi Khadem)**

> حقوق اثر اصلی متعلق به نویسنده (Dusty Phillips) است. این ترجمه با هدف آموزشی و ترویج ویم/نئوویم در جامعهٔ فارسی‌زبان منتشر شده. لطفاً از نویسندهٔ اصلی حمایت کنید: [صفحهٔ خرید و حمایت](./content-fa/purchase.md) · [GitHub Sponsor](https://github.com/sponsors/dusty-phillips) · [Patreon](https://www.patreon.com/dustyphillipscodes)

## ساختار مخزن

| مسیر | توضیح |
|---|---|
| `content-fa/` | متن فارسی کتاب به‌صورت مارک‌داون (فصل ۱ تا ۲۰ + صفحات خرید/به‌روزرسانی/غلط‌نامه/شناسنامه) |
| `assets/` | استایل راست‌به‌چپ، فونت وزیرمتن، جاوااسکریپت و فاوآیکون |
| `build.py` | سازندهٔ سایت استاتیک (مارک‌داون ← HTML فارسی) |
| `site/` | خروجی ساخته‌شده (در گیت نیست؛ توسط GitHub Actions منتشر می‌شود) |
| `.github/workflows/pages.yml` | استقرار خودکار روی GitHub Pages |

## ساخت محلی

```bash
uv run --with markdown -- python3 build.py
# سپس site/index.html را در مرورگر باز کنید
```

پیش‌نیاز فقط پایتون ۳ و [uv](https://docs.astral.sh/uv/) است. تصاویر کتاب از سایت اصلی hotlink می‌شوند و در مخزن کپی نشده‌اند.

## استقرار

هر push به شاخهٔ `main` ورک‌فلوی `pages.yml` را اجرا می‌کند: سایت ساخته و روی GitHub Pages منتشر می‌شود. کافی است در تنظیمات مخزن (Settings → Pages) منبع روی **GitHub Actions** باشد.

## مشارکت

اگر غلط ترجمه یا تایپی دیدید، Issue باز کنید یا Pull Request بفرستید. برای غلط‌های متن اصلی، لطفاً به [فرم غلط‌نامهٔ نویسنده](https://lazyvim-ambitious-devs.phillips.codes/course/errata/) مراجعه کنید.

## مجوز

- متن اصلی کتاب: © Dusty Phillips — تمام حقوق محفوظ.
- ترجمهٔ فارسی و کد سایت: MIT (فایل `LICENSE`).

---

<div dir="ltr">

## EN — LazyVim for Ambitious Developers (Persian translation)

Non-commercial Persian translation of **[LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/)** by **Dusty Phillips**, translated by **Mehdi Khadem (مهدی خادم)**.

- FA site: `https://mahdmahd.github.io/lazyvimAmbitiousDevsPersian/`
- Original (EN): [lazyvim-ambitious-devs.phillips.codes](https://lazyvim-ambitious-devs.phillips.codes/)
- Please support the original author: [purchase/support](https://lazyvim-ambitious-devs.phillips.codes/course/purchase/) · [GitHub Sponsor](https://github.com/sponsors/dusty-phillips) · [Patreon](https://www.patreon.com/dustyphillipscodes)

Build: `uv run --with markdown -- python3 build.py` → static HTML in `site/`, deployed via `.github/workflows/pages.yml`.

</div>

</div>
