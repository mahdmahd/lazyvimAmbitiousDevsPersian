# فصل ۱۸. تست‌نویسی

## [فصل ۱۸. تست‌نویسی](#_testing)

LazyVim را می‌توان با افزونهٔ Neotest پیکربندی کرد، رانر عمومی برای انتخاب و اجرای تست‌ها در زبان‌ها و فریم‌ورک‌های تست متنوع. مثل آداپتور دیباگ، Neotest به‌طور پیش‌فرض فعال نیست. اما اگر افزونه فعال باشد، بیشتر اکسترهای زبان با راه‌اندازی ازپیش‌پیکربندی‌شده عرضه می‌شوند تا تست‌نویسی خودکار کار کند.

البته جز وقتی که نمی‌کند. مثل دیباگرها، می‌بینم قابلیت‌های داخل ویرایشگر که اکستنشن‌های تست (صرف‌نظر از ویرایشگر) فراهم می‌کنند آن‌قدر حساس‌اند که به زحمت پیکربندی‌شان نمی‌ارزند. معمولاً فقط رانر تستی در حالت دیده‌بانی (watch) در ترمینال جداگانه‌ای دارم که در حال اجراست و برایم خوب کار می‌کند. قبلاً از Neotest استفاده نمی‌کردم، اما بعد از نوشتن این فصل نظرم عوض شد!

### [۱۸.۱. امتحان Neotest](#_try_neotest)

اگر هنوز نکردید (به‌عنوان بخشی از فعال کردن افزونه‌های پیشنهادی) رابط Lazy Extras را باز کنید و اکسترای `test.core` را فعال کنید. این Neotest و چند وابستگی را برایتان راه می‌اندازد.

همچنین مطمئن شوید اکسترهای هر زبانی که با آن کار می‌کنید فعال‌اند و دوباره بررسی کنید آیا شامل افزونهٔ مرتبط با تست‌اند. برای این مثال، از `neotest-python` استفاده می‌کنیم که با اکسترای `lang.python` عرضه می‌شود.

وقتی اکسترا فعال شد، دستور سطح بالای جدید «test» را در منوی حالت Space می‌بینید که با `<Space>t` در دسترس است:

![منوی تست در تم تیره](/images/book/chapter-18/menu-dark.png)

شکل ۹۷. منوی تست

همان‌طور که انتظار دارید، `<Space>tt` که راحت تایپ می‌شود مهم‌ترین دستور منوست؛ فایل فعلی را اجرا می‌کند و نتایج تست را پارس می‌کند. همچنین می‌توانید از `<Space>tr` (حرف `r` برای «Run» یعنی اجرا) وقتی مکان‌نما داخل تستی است برای اجرای همان تک‌تست استفاده کنید.

بعد از اجرای موفق تست‌ها، Neotest چند آیکون چک در رابط‌تان می‌گذارد تا ببینید موفق بودند:

![اجرای موفق تست‌ها در تم تیره](/images/book/chapter-18/success-dark.png)

شکل ۹۸. اجرای موفق تست‌ها

این اسکرین‌شات دو تست بعد از این گرفته شد که همهٔ تست‌های فایل را با `<Space>tt` اجرا کردم. یک تیک در گاتر (ناودان) هست و دیگری سمت راست تست در متن مجازی (virtual text).

### [۱۸.۲. گزارش خطا](#_error_reporting)

وقتی خطای تست وارد می‌کنیم چیزها کمی جالب‌تر می‌شوند. اول، پنجرهٔ اسکرول‌شونده‌ای با خروجی تست بالا می‌آید؛ این همان خروجی است که اگر دستور تست (`pytest` در این مورد) را از ترمینال اجرا می‌کردم می‌دیدم:

![خروجی خطای تست در تم تیره](/images/book/chapter-18/error-output-dark.png)

شکل ۹۹. خروجی خطای تست

وقتی این پنجره بعد از اجرای تست‌ها بالا می‌آید، به‌طور پیش‌فرض فوکوس نیست و می‌توانید فقط با حرکت مکان‌نما ببندیدش (شبیه پنجرهٔ دایگنوستیک). اگر ترجیح می‌دهید پنجره را فوکوس کنید (مثلاً تا بتوانید با `<Control-d>` و `<Control-u>` اسکرولش کنید)، می‌توانید از `<Space>to` استفاده کنید که `o` یعنی «output». می‌توانید هر زمانی از این کلیدبندی برای نشان دادن جدیدترین خروجی تست استفاده کنید. یا می‌توانید از `<Space>tO` (حرف `O` بزرگ) برای باز کردن خروجی در پنلی زیر ویرایشگر به‌جای پنجرهٔ شناور استفاده کنید.

|  |  |
| --- | --- |
|  | پنل خروجی Neotest اگر اکسترای `edgy` را هم فعال کرده باشید بهتر رفتار می‌کند. |

وقتی پنجرهٔ شناور فوکوس شد، باید از میان‌بر `q` برای خروج از آن استفاده کنید.

وقتی تستی در Neotest شکست می‌خورد، بدیهی است تیک کنار تست را نمی‌بینید. در عوض، ضربدر قرمز کوچکی می‌بینید. علاوه بر این، `x` داخل دایره‌ای در خط خاصی که خطا دارد و متنی مجازی (امیدوارانه) آموزنده سمت راست خط خاطی خواهد بود:

![متن مجازی خطای تست در تم تیره](/images/book/chapter-18/error-dark.png)

شکل ۱۰۰. متن مجازی خطای تست

از همه مفیدتر، پنجرهٔ `Trouble` با فهرست همهٔ تست‌های شکست‌خورده باز می‌شود. در این اسکرین‌شات، `assert False` را به دو تست مختلف در فایل اضافه کردم:

![تست‌های شکست‌خورده در Trouble در تم تیره](/images/book/chapter-18/trouble-dark.png)

شکل ۱۰۱. تست‌های شکست‌خورده در Trouble

این **فوق‌العاده** راحت است چون حالا می‌توانم با `]q` و `[q` بین تست‌های شکست‌خورده (احتمالاً در چند فایل) پیمایش کنم، یا با فوکوس پنجرهٔ `Trouble` و استفاده از حرکات پایهٔ مکان‌نما.

### [۱۸.۳. خلاصهٔ تست](#_test_summary)

`<Space>tT` با `T` بزرگ کار «اما بزرگ‌تر» انجام می‌دهد، همهٔ تست‌های پروژه‌تان را اجرا می‌کند به‌جای فقط آن‌های داخل فایل فعلی. البته، مارکرهای تست را برای هیچ فایل بازی که باز نیست نمی‌بینید. پس احتمالاً می‌خواهید از `<Space>ts` برای تاگل پنجرهٔ خلاصه استفاده کنید:

![خلاصهٔ تست در تم تیره](/images/book/chapter-18/summary-dark.png)

شکل ۱۰۲. خلاصهٔ تست

نمای خلاصه چند میان‌بر صفحه‌کلید مفید (`J` و `K` مفیدترین‌اند) دارد که می‌توانید با تایپ `?` وقتی فوکوس است ببینید:

![کلیدبندی‌های خلاصهٔ تست در تم تیره](/images/book/chapter-18/summary-mappings-dark.png)

شکل ۱۰۳. کلیدبندی‌های خلاصهٔ تست

دستور `m` برای «mark» یعنی علامت شایستهٔ اشاره است. اجازه می‌دهد تستی را «مورد علاقه» علامت بزنید، تا وقتی از دستور `R` یا `Run marked` استفاده می‌کنید فقط همان تست‌ها اجرا شوند. از `M` (بزرگ) برای پاک کردن همهٔ علامت‌ها یا `m` وقتی خطی علامت‌دار است برای تاگل خاموش تک‌علامت استفاده کنید.

### [۱۸.۴. حالت دیده‌بانی و دیباگ](#_watch_mode_and_debugging)

می‌توانید حالت «دیده‌بانی (watch)» را برای فایل فعلی با `<Space>tw` تاگل کنید. این هر بار که سورس‌کدتان تغییر می‌کند خودکار دستور تست را اجرا می‌کند. آیکون‌های خلاصه و فایل تست همه در زمان واقعی به‌روز می‌شوند.

اگر آداپتور دیباگ را چنان‌که در فصل ۱۸ توضیح داده شد فعال کرده باشید، حتی می‌توانید تست را با `<Space>td` اجرا کنید تا خودکار روی خطا بریک‌پوینت بگذارد. این می‌تواند برای بازرسی سریع لوکال‌ها یا افزودن واچ‌استیتمنت‌ها به‌جای افزودن کلی پرینت قبل از assertions مفید باشد.

### [۱۸.۵. نصب رانر تست](#_installing_a_test_runner)

اگر خوش‌شانس باشید، زبان‌تان اکسترای LazyVim دارد که از پیش برای کار با Neotest پیکربندی شده. مثلاً اکسترهای `lang.go` و `lang.python` هر دو پیکربندی برای راه‌اندازی Neotest با آن فریم‌ورک‌ها را شامل‌اند.

اما همهٔ زبان‌ها رانر تست پیش‌فرض واضحی ندارند. مثلاً اگر در تایپ‌اسکریپت کد می‌زنید، شاید `vitest` یا `jest` یا رانر تست `deno` را ترجیح دهید. هر سه این‌ها پشتیبانی Neotest دارند، اما هیچ‌کدام به‌طور پیش‌فرض با اکسترای تایپ‌اسکریپت فعال نیستند.

برای چنین زبان‌هایی، باید کمی پیکربندی دستی بکنید. بیایید به‌عنوان مثال سعی کنیم یکی برای `vitest` راه بیندازیم.

افزونه‌ای که لازم داریم [neotest-vitest](https://github.com/marilari88/neotest-vitest) است. باید دستورهای README آن ریپو را با مثال LazyVim در صفحهٔ [Neotest](https://www.lazyvim.org/extras/test/core) ترکیب کنیم.

فایل جدید `vitest.lua` در دایرکتوری افزونه‌هایم ساختم و پیکربندی زیر را به آن اضافه کردم:

فهرست ۶۷. پیکربندی Neotest-vitest

```
return {
  { "marilari88/neotest-vitest" },
  {
    "nvim-neotest/neotest",
    opts = { adapters = { "neotest-vitest" } },
  },
}
```

بعد نئوویم را ری‌استارت کردم و فایلی را باز کردم که تست `vitest` داشت. `<Space>tt` کار درست را کرد و افزونه پیکربندی شده است.

در ریپویی که تست می‌کردم، `vitest` با `npm` نصب شده بود، پس نصب اضافه‌ای لازم نبود. در بیشتر موارد انتظار دارم ابزارهایی که افزونه‌های Neotest به آن‌ها صدا می‌زنند وقتی به پروژه‌تان دسترسی دارند از قبل نصب شده باشند. اگر نه، شاید بتوانید از منوی `Mason` که از `<Space>cm` در دسترس است نصبش کنید.

### [۱۸.۶. نوشتن آداپتور تست خودتان](#_writing_your_own_test_adapter)

این کمی خارج از دامنهٔ این کتاب است، اما تصمیم گرفتم شاملش کنم چون الف) به هر حال لازم بود انجامش دهم، ب) این فصل به‌طرز غافلگیرکننده‌ای کوتاه است و ج) مثال خوبی برای نوشتن افزونهٔ ساده است.

نوشتن آداپتور Neotest خودتان فقط پیاده‌سازی پنج متد برای تطبیق با رابط `neotest.Adapter` لازم دارد. اما شیطان در جزئیات است.

برای این مثال، آداپتور تستی برای رانر تست [Bun](https://bun.sh) می‌نویسم. `Bun` را تا حدی انتخاب کردم چون آداپتور Neotest برایش وجود ندارد و خودم در پروژه‌هایم از `Bun` استفاده می‌کنم. اما انتخاب خوبی برای نمایش هم هست چون از قبل سه آداپتور Neotest تایپ‌اسکریپت/جاوااسکریپت هست که برای مثال و الهام از آن‌ها استفاده کنیم:

- [neotest-jest](https://github.com/haydenmeade/neotest-jest)

- [neotest-vitest](https://github.com/marilari88/neotest-vitest)

- [neotest-deno](https://github.com/MarkEmmons/neotest-deno)

همهٔ قابلیت‌های ممکن را پیاده نمی‌کنیم (مخصوصاً دیباگر جا می‌ماند)، اما مبانی اجرای تست‌های `Bun` و پارس خروجی را می‌گیریم.

اگر با `Bun` آشنا نیستید، ران‌تایم و کامپایلر جاوااسکریپت/تایپ‌اسکریپت است، کم‌وبیش جایگزینی برای `nodejs`. دستور تعبیه‌شدهٔ `bun test` سوئیت تستی شبیه `jest` اجرا می‌کند. همین دستوری است که به آن بایند می‌کنیم.

#### [۱۸.۶.۱. راه‌اندازی افزونهٔ محلی](#_initializing_a_local_plugin)

به‌طور پیش‌فرض، LazyVim افزونه‌ها را از ارائه‌دهنده‌ای مثل GitHub دانلود می‌کند. اما می‌توانید هر `git url` را به آن بدهید یا به دایرکتوری محلی اشاره‌اش کنید. ما دومی را انجام می‌دهیم.

اول، بیایید ساختار پایهٔ افزونه را در دایرکتوری جدیدی راه بیندازیم. باید سه دایرکتوری تودرتو بسازید:

فهرست ۶۸. ساختن دایرکتوری Neotest Bun

```
$ mkdir -p neotest-bun/lua/neotest-bun
```

`neotest-bun` اول واقعاً می‌تواند هر نامی باشد. `lua` لازم است تا LazyVim هر فایل داخلش را بردارد و `neotest-bun` آخر ماژول لوایی است که در پیکربندی‌مان ایمپورت می‌کنیم.

داخل این دایرکتوری، فایلی به نام `init.lua` بسازید. محتوای فایل فعلاً می‌تواند فقط کد لوای ساده‌ای باشد:

فهرست ۶۹. اسکریپت سادهٔ لوا

```
print("Hello, Lua!")
```

قدم بعدی وصل کردن این افزونهٔ محلی به پیکربندی LazyVim است. فایل جدیدی در دایرکتوری افزونه‌های LazyVim بسازید (مال خودم را `neotest-bun.lua` نامیدم). از همان قالبی که بالا برای `vitest` استفاده کردیم بهره می‌بریم، جز این‌که با کلید `dir` به افزونهٔ محلی‌مان اشاره می‌کنیم:

فهرست ۷۰. پیکربندی افزونهٔ محلی

```
return {
  { dir = "~/Desktop/Code/neotest-bun/" },
  {
    "nvim-neotest/neotest",
    opts = { adapters = { "neotest-bun" } },
  },
}
```

برای دیدن این‌که تا این‌جا کار می‌کند یا نه، هر فایلی را در نئوویم باز کنید و `<Space>tt` را اجرا کنید تا تلاش کنید رانر تست را راه بیندازید. شکست می‌خورد چون هنوز رابط آداپتور را درست پیاده نکردیم، اما باید نوتیفیکیشنی هم بالا بیاورد که می‌گوید «Hello, Lua!».

|  |  |
| --- | --- |
|  | نوتیفیکیشن سریع ناپدید می‌شود که خیلی ناراحت‌کننده است اگر شامل تریس‌بکی باشد که می‌خواهید بررسی کنید. همیشه می‌توانید از `<Space>sna` برای نشان دادن همهٔ پیام‌های اخیر در پنلی استفاده کنید. دستور `:messages` هم کار می‌کند. |

#### [۱۸.۶.۲. پیاده‌سازی آداپتور Neotest](#_implementing_the_neotest_adapter)

بیایید رابط آداپتور را کامل کنیم. فایل `neotest-bun/init.lua` را باز کنید و دستور `print` را با محتوای زیر جایگزین کنید:

فهرست ۷۱. رابط آداپتور Neotest

```
local BunNeotestAdapter = { name = "neotest-bun" }

function BunNeotestAdapter.root(dir) end

function BunNeotestAdapter.filter_dir(name, rel_path, root) end

function BunNeotestAdapter.is_test_file(file_path) end

function BunNeotestAdapter.discover_positions(file_path) end

function BunNeotestAdapter.build_spec(args) end

function BunNeotestAdapter.results(spec, result, tree) end

return BunNeotestAdapter
```

این رابتی است که باید پیاده کنیم. اگر می‌پرسید از کجا آوردمش، در [سورس‌کد Neotest](https://github.com/nvim-neotest/neotest/blob/master/lua/neotest/adapters/interface.lua) تعریف شده و از README پروژهٔ Neotest لینک شده. همچنین ریپوهای GitHub بسته‌های `neotest-jest` و `neotest-deno` را برای مرجع باز دارم.

|  |  |
| --- | --- |
|  | باید از نئوویم خارج شوید و ری‌استارتش کنید تا تغییرهایی که در فایل `init.lua` می‌دهید برداشته شوند. یادتان باشد می‌توانید از دستور `<Space>qq` برای خروج از نئوویم و بعد دستور `s` از داشبورد برای بازگردانی راه‌اندازی‌تان با حداقل دردسر استفاده کنید. |

اگر حالا سعی کنید تست‌ها را روی فایل تست `Bun` اجرا کنید، (احتمالاً) با پیام «No Tests Found» شکست می‌خورد. اگر نخورد، شاید رانر تست دیگری نصب است که فکر می‌کند این فایل تست معتبری است.

آداپتور ما الان درست گزارش می‌دهد که آداپتور Neotest است، اما بعد در ثبت پوشه یا فایل فعلی به‌عنوان فایل تست شکست می‌خورد. می‌توانیم با پیاده‌سازی سه متد اول در فایل درستش کنیم.

دایرکتوری `root` قرار است ریشهٔ پروژه را با گرفتن دایرکتوری فعلی پیدا کند. وقتی از `Bun` استفاده می‌کنیم، می‌توانیم از حضور یا غیاب فایل `bun.lock` به‌عنوان نشانگر ریشهٔ پروژهٔ فعلی استفاده کنیم. این فایل وقتی `bun install` را اجرا می‌کنید ساخته می‌شود و برای نگه‌داشتن وابستگی‌ها استفاده می‌شود.

پس بیایید متد `BunNeoTestAdapter.root` را این‌طور پیاده کنیم:

فهرست ۷۲. پیاده‌سازی دایرکتوری ریشه

```
local lib = require("neotest.lib")

local BunNeotestAdapter = { name = "neotest-bun" }

function BunNeotestAdapter.root(dir)
  return lib.files.match_root_pattern("bun.lock")(dir)
end
```

نکتهٔ کلیدی این‌جا تابع `match_root_pattern` از `neotest.lib` است. آن کتابخانه را ایمپورت می‌کنیم و به لوکالی تخصیصش می‌دهیم، بعد تابع `root` ما فقط باید کال‌بکی بسازد و صدایش بزند.

در همین حین، می‌توانیم تابع `filter_dir` را هم پیاده کنیم. این متد برای فیلتر کردن دایرکتوری‌هایی طراحی شده که نباید اسکن شوند. در پروژهٔ `Bun`، این شامل پوشهٔ `node_modules` می‌شود. قطعاً نمی‌خواهیم برای جست‌وجوی تست در آن پوشه وقت تلف کنیم!

فهرست ۷۳. پیاده‌سازی فیلتر دایرکتوری

```
function BunNeotestAdapter.filter_dir(name, rel_path, root)
  return name ~= "node_modules"
end
```

حالا اگر نئوویم را ری‌استارت کنید و سعی کنید تست‌ها را با `<Space>tT` اجرا کنید (یعنی بار دوم `T` بزرگ) پیام «No Tests found» را نشان نمی‌دهد. *کاری* نمی‌کند، اما دست‌کم خطا نمی‌دهد. اما `<Space>tt` خطا می‌دهد، چون نمی‌داند الان در فایل تستیم. می‌توانیم از متد `is_test_file` به آن بپردازیم.

در `Bun`، مثل بیشتر ران‌تایم‌های جاوااسکریپت، تست‌ها معمولاً در فایل `something.test.js` یا `somethingElse.test.ts` هستند. پس می‌توانیم از تابع لوای زیر برای بررسی این‌که در فایل تستیم استفاده کنیم:

فهرست ۷۴. پیاده‌سازی تشخیص فایل تست

```
function BunNeotestAdapter.is_test_file(file_path)
  return string.match(file_path, ".*.test.[tj]s$") ~= nil
end
```

اگر فایل `cohere.test.ts` را باز کنم و `<Space>tt` را اجرا کنم، هنوز `No Tests found` می‌گیرم. فایل را به‌عنوان فایل تست `Bun` تشخیص می‌دهد، اما نمی‌داند چگونه داخل فایل را برای پیدا کردن تستی نگاه کند.

#### [۱۸.۶.۳. کشف موقعیت‌های تست](#_discovering_test_positions)

حل این پیاده‌سازی تابع `discover_positions` لازم دارد و آن…​ پیچیده است. معمولاً کوئری‌های Treesitter می‌نوشتید که نیم‌فضاها (namespaces) و تست‌ها را در فایل تشخیص دهند. حدس می‌زنم می‌توانستید پارسر خودتان را هم بنویسید یا از `string.match` استفاده کنید، اما پارسر Treesitter احتمالاً بهتر از هر چیزی است که ما می‌توانیم بنویسیم.

من چیزی دربارهٔ نوشتن کوئری‌های Treesitter نمی‌دانم و خصوصاً نمی‌خواهم بدانم. پس فقط به این واقعیت تکیه می‌کنم که `Bun` از همان نحو `describe/test` که `Jest` استفاده می‌کند بهره می‌برد و کوئری‌ها را دربست از افزونهٔ [neotest-jest](https://github.com/nvim-neotest/neotest-jest/blob/main/lua/neotest-jest/init.lua#L162) کپی می‌کنم!

تکه‌کد نسبتاً طولانی است که احتمالاً در قالب کتاب خواندنش سخت باشد، اما برای کامل بودن این‌جا می‌آورمش:

فهرست ۷۵. کوئری‌های قرض‌گرفته‌شدهٔ کشف موقعیت

~~~
function BunNeotestAdapter.discover_positions(file_path)
  local query = [[
    ; -- Namespaces --
    ; Matches: `describe('context', () => {})`
    ((call_expression
      function: (identifier) @func_name (
        #eq? @func_name "describe"
      )
      arguments: (arguments (
        string (string_fragment) @namespace.name
      ) (arrow_function))
    )) @namespace.definition
    ; Matches: `describe('context', function() {})`
    ((call_expression
      function: (identifier) @func_name (
        #eq? @func_name "describe"
      )
      arguments: (arguments (
        string (string_fragment) @namespace.name
      ) (function_expression))
    )) @namespace.definition
    ; Matches: `describe.only('context', () => {})`
    ((call_expression
      function: (member_expression
        object: (identifier) @func_name (
          #any-of? @func_name "describe"
        )
      )
      arguments: (
        arguments (string (string_fragment) @namespace.name
      ) (arrow_function))
    )) @namespace.definition
    ; Matches: `describe.only('context', function() {})`
    ((call_expression
      function: (member_expression
        object: (identifier) @func_name (
          #any-of? @func_name "describe"
        )
      )
      arguments: (arguments (
        string (string_fragment) @namespace.name
      ) (function_expression))
    )) @namespace.definition
    ; Matches: `describe.each(['data'])('context', () => {})`
    ((call_expression
      function: (call_expression
        function: (member_expression
          object: (identifier) @func_name (
            #any-of? @func_name "describe"
          )
        )
      )
      arguments: (arguments (
        string (string_fragment) @namespace.name
      ) (arrow_function))
    )) @namespace.definition
    ; Matches: `describe.each(['data'])('context', function() {})`
    ((call_expression
      function: (call_expression
        function: (member_expression
          object: (identifier) @func_name (
            #any-of? @func_name "describe"
          )
        )
      )
      arguments: (arguments (
        string (string_fragment) @namespace.name
      ) (function_expression))
    )) @namespace.definition

    ; -- Tests --
    ; Matches: `test('test') / it('test')`
    ((call_expression
      function: (identifier) @func_name (
        #any-of? @func_name "it" "test"
      )
      arguments: (arguments (
        string (string_fragment) @test.name
      ) [(arrow_function) (function_expression)])
    )) @test.definition
    ; Matches: `test.only('test') / it.only('test')`
    ((call_expression
      function: (member_expression
        object: (identifier) @func_name (
          #any-of? @func_name "test" "it"
        )
      )
      arguments: (arguments (
        string (string_fragment) @test.name
      ) [(arrow_function) (function_expression)])
    )) @test.definition
    ; Matches: `test.each(['data'])('test')
    ((call_expression
      function: (call_expression
        function: (member_expression
          object: (identifier) @func_name (
            #any-of? @func_name "it" "test"
          )
          property: (property_identifier) @each_property (
            #eq? @each_property "each"
          )
        )
      )
      arguments: (arguments (
        string (string_fragment) @test.name
      ) [(arrow_function) (function_expression)])
    )) @test.definition
  ]]

  local positions = lib.treesitter.parse_positions(
    file_path, query, {
    nested_tests = false,
  })

  return positions
end
~~~

حالا می‌توانید نئوویم را ری‌استارت کنید و فایل تست `bun` را باز کنید تا خطای جدیدی بگیرید! خطاهای جدید پیشرفت‌اند، مگر نه؟

حالا متوجه می‌شوید که Neotest موقعیت‌های فراخوانی‌های `describe` و `test` را در گاتر تشخیص می‌دهد. به‌جای ضربدر قرمز یا چک سبزی که از اجرای موفق تست انتظار داریم، چشمِ خط‌خورده‌ای خواهد بود. حدس می‌زنم یعنی تست رد شده یا غیرقابل اجراست. خبر خوب این است که تست‌ها را پیدا می‌کند. خبر بد این است که تست‌ها را *اجرا* نمی‌کند.

#### [۱۸.۶.۴. ساختن اسپک](#_building_the_spec)

می‌توانیم با پیاده‌سازی تابع `build_spec` تست‌ها را اجرا کنیم. این تابع پارامترهای مختلفی برای تعیین این‌که کاربر تست‌ها را چگونه راه انداخته می‌پذیرد. اگر از `<Space>tr` استفاده کرده باشند در حالت «تک‌تست» است، اما اگر از `<Space>tt` استفاده کرده باشند در حالت «فایل» است و `<Space>tT` آن را در حالت «همهٔ تست‌ها» اجرا می‌کند.

مقدار برگشتی `build_spec` اساساً دستوری برای اجراست و زمینه‌ای برای خواندن نتایج.

کد واقعاً آن‌قدر طولانی نیست، پس این‌جا کاملش را می‌آورم و بعد بحث می‌کنم:

فهرست ۷۶. پیاده‌سازی ساختن اسپک

```
function BunNeotestAdapter.build_spec(args)
  local results_path = async.fn.tempname()
  local position = args.tree:data()
  local cwd = assert(
    BunNeotestAdapter.root(
      position.path
    ),
    "could not locate root directory of " .. position.path)
  local command = nil

  if position.type == "test" or position.type == "namespace" then
    command = "bun test " ..
      position.path ..
      " --test-name-pattern " ..
      position.name
  elseif position.type == "file" then
    command = "bun test " .. position.name
  elseif position.type == "dir" then
    command = "bun test"
  end

  return {
    command = command .. " 2>" .. results_path,
    context = {
      results_path = results_path,
    },
    cwd = cwd,
  }
end
```

با ساختن `results_path` موقتی با کتابخانهٔ `neotest.async` شروع می‌کنیم. (باید با `local async = require("neotest.async")` بالای فایل ایمپورتش کنید). `position` را لود می‌کنیم که ساختاری ساخته‌شده از مقدار برگشتی متد `discover_positions` است که تازه نوشتیم.

بلوک `if..elseif` اساساً بررسی می‌کند کاربر تست را چگونه راه انداخته و دستور مناسب `Bun` را اجرا می‌کند. اگر نام تست داده باشند، آرگومان `--test-name-pattern` را به دستور `bun test` پاس می‌دهیم. اگر به‌صورت فایل راهش انداخته باشند، `bun test filename` را اجرا می‌کنیم. و اگر بخواهند همهٔ تست‌ها را اجرا کنند، ساده همهٔ تست‌ها را با `bun test` اجرا می‌کنیم.

|  |  |
| --- | --- |
|  | رانر تست `Bun` آن‌قدر سریع است که انتظار دارم بیشتر فقط از فرم آخر با `<Space>tT` و نمای خلاصهٔ باز در نوار کناری چپ استفاده کنم. |

شیء برگشتی شامل زمینهٔ لازم است که وقتی نتایج را پارس می‌کنیم استفاده می‌شود. دستور `bun test` تا حدی غیرمعمول است که نتایج را به خطای استاندارد خروجی می‌دهد، پس ریدایرکت `2>` را پاس می‌دهیم تا نتایج در فایل موقتی که تعریف کردیم ذخیره شوند.

حالا فقط باید نتایج را از آن فایل استخراج کنیم.

#### [۱۸.۶.۵. پارس نتایج](#_parsing_results)

این ساده‌تر از انتظارم از آب درآمد، چون `bun test` نام‌ها را طوری جمع می‌کند که خیلی راحت به فرم موردانتظار Neotest نگاشت می‌شود. اما نصف روز ور رفتن برد تا کدی که واقعاً کار کند به دست آید!

متد `results` بیشتر فقط باید فایل `results_path` را که تابع `build_spec` ما ساخته بخواند و به جدول سادهٔ لوا تبدیلش کند. کلیدهای جدول نتایج نام‌های تست‌های موردنظرند و مقادیر فقط جدول دومی با `{status = "passed"}` یا `{status = "failed"}` هستند. دست‌کم، همهٔ چیزی است که می‌خواهیم داخلش بگذاریم. Neotest جزئیات دیگری هم این‌جا می‌پذیرد که می‌تواند در رابط کاربری رندرشان کند، اما آن را به‌عنوان «تمرینی برای خواننده» می‌گذارم.

|  |  |
| --- | --- |
|  | وقتی کتاب‌های آموزشی دیگر را می‌خوانید، «تمرینی برای خواننده» فقط تنبلی نویسنده‌هاست، یا (گاهی) ناشرها که سعی می‌کنند تعداد کلمات را کم کنند. حالا می‌دانید. |

بخش tricky «کلیدها نام‌های تست‌اند» است. هیچ مستنداتی روی این پیدا نکردم و کمی آزمون و خطا برد تا کشف کنم که نیم‌فضاهای تودرتو (فراخوانی‌های `describe`، در این مورد) در Neotest با `::` جدا می‌شوند. نام همچنین به مسیر مطلق فایل تست نیاز دارد. اگر آن را در قالب درست برگردانیم، Neotest با خوشحالی نتایج ما را به آیکون‌های مناسب تبدیل می‌کند!

این‌جا کدش:

فهرست ۷۷. پیاده‌سازی نتایج Neotest

```
function BunNeotestAdapter.results(spec, result, tree)
  local results = {}
  local file = assert(io.open(spec.context.results_path))
  local line = file:read("l")
  local test_suite = ""

  while line do
    local pass_match = string.match(line, "^%(pass%) (.*) %[.*%]$")
    if pass_match ~= nil then
      local test_name = pass_match.gsub(pass_match, " > ", "::")
      results[test_suite .. test_name] = { status = "passed" }
    end

    local fail_match = string.match(line, "^%(fail%) (.*) %[.*%]$")
    if fail_match ~= nil then
      local test_name = fail_match.gsub(fail_match, " > ", "::")
      results[test_suite .. test_name] = { status = "failed" }
    end

    local test_file = string.match(line, "^(.+.test.[tj]s):$")
    if test_file ~= nil then
      test_suite = spec.cwd .. "/" .. test_file .. "::"
    end

    line = file:read("l")
  end

  if file then
    file:close()
  end

  return results
end
```

برای زمینه، این تابع برای ترجمهٔ خروجی‌ای مثل این طراحی شده:

فهرست ۷۸. خروجی تست Bun

```
src/clients/stability/stability.test.ts:
(pass) Stability > generates a reference image [0.40ms]

src/clients/passage/passage.test.ts:
(pass) Passage > GetUserTier > Undefined [1.24ms]
(pass) Passage > GetUserTier > with tier free
(fail) Passage > GetUserTier > with tier hobby
```

به چیزی مثل این:

فهرست ۷۹. خروجی ترجمه‌شدهٔ تست Bun

```
{
  "/.../stability.test.ts::Stability::generates reference image" = {
    status = "passed"
  },
  "/.../passage.test.ts::Passage::GetUserTier::Undefined" = {
    status = "passed"
  },
  "/.../passage.test.ts::Passage::GetUserTier::with tier free" = {
    status = "passed"
  },
  "/.../passage.test.ts::Passage::GetUserTier::with tier hobby" = {
    status = "failed"
  },
}
```

متد اول نام فایل را از زمینه می‌گیرد (زمینه از متد `build_spec` برگشته بود). فایل را باز می‌کند و خط‌های آن فایل را یکی‌یکی می‌خواند. بعد از مچر استفاده می‌کند تا تعیین کند خط با `(passed)` یا `(failed)` شروع می‌شود که همان‌طور است که `Bun` نتیجهٔ تست را گزارش می‌کند. بقیهٔ خط تست نام تست نیم‌فضادارشدهٔ درست خواهد بود (منهای زمانی در کروشه)، جز این‌که نیم‌فضاها با `>` به‌جای `::` جدا شده‌اند. پس از `gsub` برای جایگزینی `>` با `::` استفاده می‌کنیم. این با مسیر مطلق نام فایل ترکیب می‌شود تا نام درست تست به دست آید.

اگر خطی نام تست نباشد، ممکن است نام فایل تست باشد که `Bun` لطف می‌کند به‌صورت مسیر نسبی و به دنبالش کولن مشخصش می‌کند. پس روی آن قالب مچ می‌کنیم و نام تست را به‌صورت مسیر مطلق ذخیره می‌کنیم (برای همین `spec.cwd` است) تا به نتایج تست‌های بعدی پیشوند شود.

و این مبانی پیاده‌سازی رانر تست خودمان است! چند قابلیتی کم دارد، مخصوصاً دیباگ تست‌ها و گرفتن خروجی، اما شروع خوبی است.

### [۱۸.۷. خلاصه](#_summary_18)

این فصل افزونهٔ Neotest را پوشش داد، از جمله راه‌های مختلف فراخوانی‌اش و نحوهٔ راه‌اندازی‌اش به روش آسان، سخت و فوق‌سخت.

همچنین کمی دربارهٔ نحوهٔ نوشتن افزونهٔ نئوویم یاد گرفتیم. در هسته‌اش، فقط مجموعه‌ای از فایل‌های لواست که LazyVim می‌تواند ایمپورتشان کند. در این مورد، فایل لوا آداپتور Neotest است و پیکربندی‌اش کردیم تا افزونه‌مان را در Neotest لود کند.

> **یادآوری:** این کتاب به‌صورت رایگان در دسترس است. محتوای آن به‌اندازهٔ یک کتاب درسی کامل است. اگر از این محتوا بهره می‌برید، از هر حمایتی که می‌توانید انجام دهید واقعاً سپاسگزارم — هم حمایت از خودم، هم از کسانی که توان مالی حمایت ندارند — به‌واسطهٔ خرید نسخه‌ای از کتاب یا کمک مالی. برای دیدن گزینه‌های مختلف خرید و حمایت، [اینجا](/course/purchase/) را کلیک کنید.
