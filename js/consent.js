(() => {
  'use strict';
  /* Cookie / analytics consent.
     - Nothing from Google is requested until the visitor presses Accept.
     - Decline and Accept are the same size; the choice can be changed any time from the footer ("Cookie settings").
     - A browser privacy signal (Global Privacy Control / Do Not Track) counts as Decline: no banner, no analytics.
     - The only thing stored is the visitor's choice, in this browser's localStorage (not a cookie, never sent anywhere). */
  const GA_ID = 'G-9RKY3HS47H', KEY = 'inizi_consent_v1', MAX_AGE = 180 * 864e5;
  const me = document.currentScript, lang = (me && me.dataset.lang) === 'et' ? 'et' : 'en';
  const privacy = (me && me.dataset.privacy) || 'privacy.html';
  const T = {
    en: { title: 'Cookies', text: 'We would like to use one analytics cookie to see which pages are visited. It is off unless you accept. Nothing is sold or used for advertising. ', link: 'Privacy & cookies', no: 'Decline', yes: 'Accept' },
    et: { title: 'Küpsised', text: 'Soovime kasutada ühte analüütikaküpsist, et näha, milliseid lehti külastatakse. See on välja lülitatud, kui te ei nõustu. Midagi ei müüda ega kasutata reklaamiks. ', link: 'Privaatsus ja küpsised', no: 'Keeldun', yes: 'Nõustun' }
  }[lang];
  const signal = navigator.globalPrivacyControl === true || navigator.doNotTrack === '1' || window.doNotTrack === '1';

  const read = () => { try { const c = JSON.parse(localStorage.getItem(KEY)); if (c && c.v === 1 && Date.now() - c.ts < MAX_AGE) return c; } catch (e) {} return null; };
  const write = analytics => { try { localStorage.setItem(KEY, JSON.stringify({ v: 1, analytics, ts: Date.now() })); } catch (e) {} };

  let loaded = false;
  const loadGA = () => {
    if (loaded) return; loaded = true;
    window['ga-disable-' + GA_ID] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { allow_google_signals: false, allow_ad_personalization_signals: false, cookie_flags: 'SameSite=Lax;Secure' });
    const s = document.createElement('script'); s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    document.head.appendChild(s);
  };
  const stopGA = () => {
    window['ga-disable-' + GA_ID] = true;
    const parts = location.hostname.split('.'), domains = ['', location.hostname];
    for (let i = 0; i < parts.length - 1; i++) domains.push('.' + parts.slice(i).join('.'));
    document.cookie.split(';').map(c => c.split('=')[0].trim()).filter(n => n === '_ga' || n === '_gid' || n.indexOf('_ga_') === 0).forEach(n =>
      domains.forEach(d => { document.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + (d ? '; domain=' + d : ''); }));
  };

  let box, yesBtn, opener;
  const close = () => { box.hidden = true; if (opener && document.contains(opener)) opener.focus(); opener = null; };
  const build = () => {
    box = document.createElement('div'); box.className = 'consent'; box.hidden = true;
    box.setAttribute('role', 'dialog'); box.setAttribute('aria-labelledby', 'consent-title'); box.setAttribute('aria-describedby', 'consent-text');
    const h = document.createElement('h2'); h.id = 'consent-title'; h.className = 'colhead'; h.textContent = T.title;
    const p = document.createElement('p'); p.id = 'consent-text'; p.append(T.text);
    const a = document.createElement('a'); a.href = privacy; a.textContent = T.link; p.append(a, '.');
    const row = document.createElement('div'); row.className = 'btn-row';
    const no = document.createElement('button'); no.type = 'button'; no.className = 'btn btn--ghost'; no.textContent = T.no;
    yesBtn = document.createElement('button'); yesBtn.type = 'button'; yesBtn.className = 'btn'; yesBtn.textContent = T.yes;
    row.append(no, yesBtn); box.append(h, p, row); document.body.appendChild(box);
    no.addEventListener('click', () => { write(false); stopGA(); close(); });
    yesBtn.addEventListener('click', () => { write(true); loadGA(); close(); });
    box.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  };
  const open = from => { if (!box) build(); opener = from || null; box.hidden = false; if (from) yesBtn.focus(); };

  const saved = read();
  if (saved && saved.analytics) loadGA();
  else if (!saved && !signal) setTimeout(() => open(null), 1800);

  document.addEventListener('click', e => { const t = e.target.closest('[data-consent-open]'); if (t) open(t); });
})();
