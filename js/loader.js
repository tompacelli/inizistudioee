/* Page loader (every page). The III fades in over 1.2s by CSS; the bar under it shows how much of the page has really loaded:
   DOM parsed, fonts ready, images in/near the first screen decoded, window load. Pure UI: no network requests, nothing stored. */
(function () {
  'use strict';
  var root = document.documentElement, loader = document.querySelector('.loader');
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ready = function () { root.classList.add('is-ready'); };
  /* between pages: no loader, only a fade out of the old page and a fade in of the new one */
  var go = function () {
    addEventListener('pageshow', function (e) { if (e.persisted) root.classList.remove('is-leaving'); });
    document.addEventListener('click', function (e) {
      if (e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      var a = e.target.closest && e.target.closest('a[href]'); if (!a || a.target === '_blank' || a.hasAttribute('download')) return;
      var u; try { u = new URL(a.href, location.href); } catch (x) { return; }
      if (u.origin !== location.origin || (u.pathname === location.pathname && u.search === location.search)) return;   /* external, mailto, same-page and #project links: untouched */
      if (reduce) return;
      e.preventDefault(); root.classList.add('is-leaving');
      setTimeout(function () { location.href = a.href; }, 260);
    });
  };
  go();
  if (root.classList.contains('no-intro')) { ready(); if (loader) loader.style.display = 'none'; return; }
  if (!loader) { ready(); return; }
  var bar = loader.querySelector('.loader__bar i');
  var MIN = reduce ? 0 : 1300;          /* let the III finish its 1.2s fade */
  var done = 0, total = 3, shown = 0, finished = false;                       /* DOM + fonts + window load */
  var tick = function () { done++; };

  var imgs = [].slice.call(document.images).filter(function (im) {
    if (im.closest('.proj-layer') || !im.getClientRects().length) return false;   /* hidden images (project windows) never load while lazy: don't wait for them */
    return im.loading !== 'lazy' || im.getBoundingClientRect().top < innerHeight * 1.2;
  });
  total += imgs.length;
  imgs.forEach(function (im) {
    if (im.complete) { tick(); return; }
    var once = false, f = function () { if (!once) { once = true; tick(); } };
    im.addEventListener('load', f); im.addEventListener('error', f);
  });
  if (document.readyState !== 'loading') tick(); else document.addEventListener('DOMContentLoaded', tick);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(tick, tick); else tick();
  if (document.readyState === 'complete') { tick(); done = total; } else addEventListener('load', function () { tick(); done = total; });   /* window load = everything that matters is in */

  var finish = function () {
    if (finished) return; finished = true;
    ready(); loader.classList.add('is-out');
    setTimeout(function () { loader.style.display = 'none'; }, 700);
  };
  var frame = function () {
    var target = Math.min(1, done / total);
    shown += (target - shown) * 0.18; if (target - shown < 0.002) shown = target;
    if (bar) bar.style.setProperty('--p', shown.toFixed(3));
    if (shown >= 1 && performance.now() >= MIN) { finish(); return; }
    requestAnimationFrame(frame);
  };
  requestAnimationFrame(frame);
  setTimeout(finish, 10000);            /* safety net: never trap a visitor behind the loader */
})();
