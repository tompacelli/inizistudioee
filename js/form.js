/* Contact form. Sends the fields as JSON to the mail-relay endpoint set on the form (data-endpoint / data-key) when, and only when, the visitor presses Send.
   Nothing is stored in the browser and no cookies are set. A hidden "botcheck" field and a minimum fill time act as a spam trap. */
(function () {
  'use strict';
  var form = document.getElementById('form'); if (!form) return;
  var status = form.querySelector('.cform__status'), btn = form.querySelector('button[type=submit]'), label = btn.querySelector('span');
  var idle = label.textContent, t0 = Date.now(), busy = false, d = form.dataset;
  var why = '';
  var mailLink = function () {                                  /* address assembled here, never written in the page source */
    var a = document.createElement('a'), addr = 'hello' + '@' + 'inizi.studio'; a.href = 'mailto:' + addr; a.textContent = addr; return a;
  };
  var say = function (msg, bad, withMail) {
    status.textContent = msg; status.classList.toggle('is-bad', !!bad);
    if (withMail) status.appendChild(mailLink());
    if (bad && why) status.appendChild(document.createTextNode(' (' + why + ')'));
  };
  var valid = function () {
    var ok = true;
    [].forEach.call(form.querySelectorAll('[required]'), function (el) {
      var bad = el.type === 'checkbox' ? !el.checked : !el.value.trim() || (el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim()));
      el.setAttribute('aria-invalid', bad ? 'true' : 'false'); if (bad) ok = false;
    });
    return ok;
  };
  form.addEventListener('input', function (e) { if (e.target.getAttribute('aria-invalid') === 'true') e.target.setAttribute('aria-invalid', 'false'); });
  form.addEventListener('submit', function (e) {
    e.preventDefault(); if (busy) return;
    if (!valid()) { say(d.req, true); var f = form.querySelector('[aria-invalid="true"]'); if (f) f.focus(); return; }
    var fd = new FormData(form);
    if (fd.get('botcheck') || Date.now() - t0 < 2500) { done(); return; }          /* bots: pretend it worked, send nothing */
    var data = {
      access_key: d.key, subject: 'Website enquiry: ' + String(fd.get('name')).slice(0, 80), from_name: 'Inizi website',
      name: fd.get('name'), email: fd.get('email'), company: fd.get('company') || '-', interest: fd.get('interest') || '-',
      timing: fd.get('timing') || '-', message: fd.get('message'), language: d.lang, botcheck: ''
    };
    busy = true; btn.disabled = true; label.textContent = d.sending; say('');
    var ctl = ('AbortController' in window) ? new AbortController() : null, to = setTimeout(function () { if (ctl) ctl.abort(); }, 15000);
    fetch(d.endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data), credentials: 'omit', referrerPolicy: 'no-referrer', signal: ctl ? ctl.signal : undefined })
      .then(function (r) { return r.json().then(function (j) { if (!(r.ok && j && j.success)) why = (r.status + ' ' + String((j && j.message) || '')).trim().slice(0, 90); return r.ok && j && j.success; }, function () { why = 'HTTP ' + r.status; return false; }); })
      .then(function (ok) { clearTimeout(to); if (ok) done(); else fail(); }, function (err) { clearTimeout(to); why = 'network: ' + String(err && err.name || 'blocked'); fail(); });
  });
  function fail() { busy = false; btn.disabled = false; label.textContent = idle; say(d.err, true, true); }
  function done() {
    var box = document.createElement('div'); box.className = 'cform__ok'; box.setAttribute('role', 'status'); box.tabIndex = -1;
    var h = document.createElement('p'); h.className = 'display'; h.textContent = d.okT; var p = document.createElement('p'); p.className = 'muted'; p.textContent = d.okP;
    box.appendChild(h); box.appendChild(p); form.replaceWith(box); box.focus({ preventScroll: true });
  }
})();
