// Sidebar toggle, TOC search, scroll-spy, copy buttons — no dependencies.
(function () {
  "use strict";

  // Mobile sidebar toggle
  var btn = document.getElementById("hamburger");
  var nav = document.getElementById("sidebar");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      nav.classList.toggle("open");
    });
  }

  // TOC live filter
  var search = document.getElementById("toc-search");
  if (search && nav) {
    search.addEventListener("input", function () {
      var q = search.value.trim();
      var items = nav.querySelectorAll("li[data-title]");
      items.forEach(function (li) {
        var t = li.getAttribute("data-title") || "";
        li.style.display = !q || t.indexOf(q) !== -1 ? "" : "none";
      });
    });
  }

  // Scroll-spy: highlight current chapter in sidebar
  try {
    var path = location.pathname.replace(/\/$/, "");
    var links = document.querySelectorAll("nav.sidebar a[href]");
    links.forEach(function (a) {
      var href = a.getAttribute("href") || "";
      // resolve relative href against current location
      var u;
      try {
        u = new URL(href, location.href).pathname.replace(/\/$/, "");
      } catch (e) {
        return;
      }
      if (u === path) {
        a.classList.add("active");
      }
    });
  } catch (e) {
    /* ignore */
  }

  // Copy buttons for code blocks (code stays LTR/English)
  document.querySelectorAll(".prose pre").forEach(function (pre) {
    if (pre.querySelector(".copy-btn")) return;
    var b = document.createElement("button");
    b.className = "copy-btn";
    b.type = "button";
    b.textContent = "کپی";
    b.addEventListener("click", function () {
      var code = pre.querySelector("code");
      var text = code ? code.innerText : pre.innerText;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          b.textContent = "کپی شد ✓";
          setTimeout(function () { b.textContent = "کپی"; }, 1500);
        });
      }
    });
    pre.appendChild(b);
  });
})();
