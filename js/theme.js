/* Day / night mode. Loaded in <head> so the saved choice is applied before first paint (no flash).
   Stores only "day" or "night" under inizi_theme in this browser's local storage; nothing is sent anywhere. */
(function () {
  var KEY = 'inizi_theme', root = document.documentElement;
  /* The saved choice is read from every place that may hold it (local storage, session storage, window.name), because embedded
     previews and some privacy modes block or isolate storage per page. It is only the word "day" or "night"; nothing is sent anywhere. */
  var ok = function (v) { return v === 'day' || v === 'night' ? v : null; };
  var store = (function () { try { var k = '__t'; localStorage.setItem(k, '1'); localStorage.removeItem(k); return true; } catch (e) { return false; } })();
  var fromName = function () { try { var m = (window.name || '').match(/(?:^|;)inizi_theme=(day|night)(?:;|$)/); return m ? m[1] : null; } catch (e) { return null; } };
  var toName = function (v) { try { window.name = (window.name || '').replace(/(?:^|;)inizi_theme=[a-z]*/g, '') + ';' + KEY + '=' + v; } catch (e) {} };
  /* One source of truth: the browser's saved choice. Only when storage is blocked (some embedded previews) does the tab's window.name carry it. */
  var get = function () {
    if (store) { try { return ok(localStorage.getItem(KEY)); } catch (e) { return null; } }
    return ok(fromName());
  };
  var save = function (v) {
    if (store) { try { localStorage.setItem(KEY, v); } catch (e) {} } else toName(v);
  };
  var apply = function (t) {
    if (t === 'day') root.setAttribute('data-theme', 'light'); else root.removeAttribute('data-theme');
    var m = document.querySelector('meta[name="theme-color"]'); if (m) m.setAttribute('content', t === 'day' ? '#f6f0e8' : '#0a0503');
    var b = document.querySelector('.theme');
    if (b) { b.setAttribute('aria-pressed', String(t === 'day')); b.setAttribute('aria-label', t === 'day' ? b.dataset.toNight : b.dataset.toDay); }
  };
  /* Intro (the III loader) plays once per visit: on the first page of a session. Later pages only fade. */
  (function () {
    var seen = false;
    try { seen = sessionStorage.getItem('inizi_seen') === '1'; } catch (e) {}
    if (!seen) seen = /(?:^|;)inizi_seen=1(?:;|$)/.test(window.name || '');
    if (!seen) { try { seen = !!document.referrer && new URL(document.referrer).host === location.host; } catch (e) {} }   /* arrived from another page of this site: works even where storage is blocked */
    if (seen) root.classList.add('no-intro');
    else { try { sessionStorage.setItem('inizi_seen', '1'); } catch (e) {} try { window.name = (window.name || '') + ';inizi_seen=1'; } catch (e) {} }
  })();
  var cur = get() === 'day' ? 'day' : 'night';
  apply(cur);
  document.addEventListener('DOMContentLoaded', function () { apply(cur); });
  addEventListener('pageshow', function () { cur = get() === 'day' ? 'day' : 'night'; apply(cur); });   /* back/forward cache: re-read the saved choice */
  addEventListener('storage', function (e) { if (e.key === KEY) { cur = ok(e.newValue) || 'night'; apply(cur); } });   /* another tab changed it: follow */
  document.addEventListener('click', function (e) {
    if (e.isTrusted === false) return;   /* only a real click/tap on the toggle changes the theme */
    var b = e.target.closest && e.target.closest('.theme'); if (!b) return;
    cur = cur === 'day' ? 'night' : 'day'; apply(cur);
    save(cur);
  });
})();
