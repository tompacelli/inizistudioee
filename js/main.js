(() => {
  'use strict';
  const root = document.documentElement;
  root.classList.remove('no-js');

  // ---- header: solid after scroll, mobile menu ----
  const nav = document.querySelector('.nav');
  const toggle = document.querySelector('.nav__toggle');
  const openLabel = toggle && toggle.dataset.open, closeLabel = toggle && toggle.dataset.close;
  const onScroll = () => nav.classList.toggle('is-solid', window.scrollY > 40);
  onScroll(); addEventListener('scroll', onScroll, { passive: true });
  const setMenu = open => {
    nav.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? closeLabel : openLabel);
    document.body.style.overflow = open ? 'hidden' : '';
  };
  if (toggle) {
    toggle.addEventListener('click', () => setMenu(!nav.classList.contains('is-open')));
    addEventListener('keydown', e => { if (e.key === 'Escape' && nav.classList.contains('is-open')) { setMenu(false); toggle.focus(); } });
    nav.querySelectorAll('.nav__menu a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  }

  // ---- reveal on scroll ----
  const items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { threshold: .12 });
    items.forEach(i => io.observe(i));
  } else items.forEach(i => i.classList.add('is-in'));

  // ---- contact emails are assembled here, never written in the HTML (stops address harvesters) ----
  document.querySelectorAll('a[data-u]').forEach(a => {
    const addr = a.dataset.u + '@' + a.dataset.d;
    a.href = 'mailto:' + addr + (a.dataset.s ? '?subject=' + encodeURIComponent(a.dataset.s) : '');
    if (!a.dataset.keep) a.textContent = addr;
  });

  // ---- project showcase window (Work page): hash-linked, Esc / back button close, focus kept inside ----
  const layer = document.querySelector('.proj-layer');
  if (layer) {
    document.body.appendChild(layer);   // outside <main>, so it sits above the site nav
    const root = document.documentElement;
    const projs = [...layer.querySelectorAll('.proj')];
    let current = null, opener = null, hideTimer = 0;
    const focusables = p => [...p.querySelectorAll('a[href],button')].filter(x => !x.disabled && x.offsetParent !== null);
    const show = (id, from) => {
      const p = layer.querySelector('#' + id);
      if (!p) return false;
      clearTimeout(hideTimer);   // a pending close must never switch off a window that is being (re)opened
      layer.querySelectorAll('.proj.is-open,.proj.is-closing').forEach(x => { if (x !== p) x.classList.remove('is-open', 'is-closing'); });
      if (!current) opener = from || document.activeElement;
      current = p; p.classList.remove('is-closing'); p.classList.add('is-open'); p.scrollTop = 0;
      layer.removeAttribute('aria-hidden'); root.classList.add('proj-open');
      p.focus({ preventScroll: true });
      return true;
    };
    const hide = () => {
      if (!current) return;
      const p = current; current = null;
      p.classList.add('is-closing');
      clearTimeout(hideTimer);
      hideTimer = setTimeout(() => { if (current) return; p.classList.remove('is-open', 'is-closing'); layer.setAttribute('aria-hidden', 'true'); root.classList.remove('proj-open'); if (opener && opener.focus) opener.focus({ preventScroll: true }); opener = null; }, 420);
    };
    const go = h => { history.replaceState(null, document.title, location.pathname + location.search + h); sync(); };
    const sync = () => { const id = location.hash.slice(1); if (/^project-\d+$/.test(id)) show(id); else hide(); };
    window.addEventListener('hashchange', sync);
    document.addEventListener('click', e => {
      const t = e.target.closest && e.target.closest('[data-close]');
      if (t && current) { e.preventDefault(); history.replaceState(null, document.title, location.pathname + location.search); hide(); return; }
      const n = e.target.closest && e.target.closest('[data-nav]');
      if (n && current) { e.preventDefault(); go(n.getAttribute('href')); return; }
      const c = e.target.closest && e.target.closest('a.cube');
      if (c) { opener = c; }
    });
    document.addEventListener('keydown', e => {
      if (!current) return;
      if (e.key === 'Escape') { history.replaceState(null, document.title, location.pathname + location.search); hide(); }
      else if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        const a = current.querySelector('[data-nav="' + (e.key === 'ArrowRight' ? 'next' : 'prev') + '"]'); if (a) go(a.getAttribute('href'));
      } else if (e.key === 'Tab') {
        const f = focusables(current); if (!f.length) return;
        const first = f[0], last = f[f.length - 1];
        if (e.shiftKey && (document.activeElement === first || document.activeElement === current)) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
    sync();
  }

  // ---- mailto safety: inside an embedded preview (iframe), a mailto navigation can blank the whole page.
  // There we never navigate: the address is copied instead. On the live site (top-level) mail links work normally.
  const embedded = (() => { try { return window.self !== window.top; } catch (e) { return true; } })();
  const T = document.documentElement.lang === 'et'
    ? { copied: 'E-posti aadress kopeeritud: ' }
    : { copied: 'Email address copied: ' };
  let toastEl, toastT;
  const toast = msg => {
    if (!toastEl) { toastEl = document.createElement('div'); toastEl.className = 'toast'; toastEl.setAttribute('role', 'status'); toastEl.setAttribute('aria-live', 'polite'); document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add('is-on'); clearTimeout(toastT);
    toastT = setTimeout(() => toastEl.classList.remove('is-on'), 3200);
  };
  document.addEventListener('click', e => {
    const a = e.target.closest && e.target.closest('a');
    if (!a) return;
    const href = a.getAttribute('href') || '';
    if (href === '#') { e.preventDefault(); return; }                 // never jump/blank on an empty link
    if (!embedded || href.slice(0, 7) !== 'mailto:') return;
    e.preventDefault();
    const addr = decodeURIComponent(href.slice(7).split('?')[0]);
    const done = () => toast(T.copied + addr);
    try { navigator.clipboard.writeText(addr).then(done, done); } catch (err) { done(); }
  });

  // ---- footage: only when motion is welcome and data is not being saved ----
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const conn = navigator.connection || {};
  const motionOK = !reduce && !conn.saveData && !/(^|-)2g$/.test(conn.effectiveType || '');
  if (!motionOK) return;

  const clips = ['video/showreel-1.mp4', 'video/showreel-2.mp4', 'video/showreel-3.mp4'].map(p => (document.body.dataset.assets || 'assets/') + p);

  // crossfading reel (hero + showcase): two stacked <video> elements per .reel[data-reel]
  document.querySelectorAll('.reel[data-reel]').forEach(reel => {
    const vids = [...reel.querySelectorAll('.reel__vid')];
    if (reel.dataset.clip !== undefined && vids[0]) {            // one fixed clip, looping
      const v = vids[0]; vids.slice(1).forEach(x => x.remove()); v.loop = true;
      new IntersectionObserver(es => es.forEach(e => {
        if (e.isIntersecting) { if (!v.src) { v.src = clips[+reel.dataset.clip % clips.length]; v.load(); v.addEventListener('playing', () => v.classList.add('on'), { once: true }); } v.play().catch(() => {}); } else v.pause();
      }), { threshold: .05 }).observe(reel);
      return;
    }
    if (vids.length < 2) return;
    let cur = 0, idx = +reel.dataset.reel || 0, fading = false, started = false;
    const load = (v, i) => { v.src = clips[i % clips.length]; v.load(); };
    const swap = () => {
      if (fading) return; fading = true;
      const next = 1 - cur, nv = vids[next];
      nv.currentTime = 0; nv.play().catch(() => {});
      nv.classList.add('on'); vids[cur].classList.remove('on');
      const old = cur; cur = next; idx = (idx + 1) % clips.length;
      setTimeout(() => { vids[old].pause(); load(vids[old], idx + 1); fading = false; }, 1300);
    };
    vids.forEach((v, i) => v.addEventListener('timeupdate', () => { if (i === cur && v.duration && v.duration - v.currentTime < 1.1) swap(); }));
    const start = () => {
      if (started) return; started = true;
      load(vids[0], idx); load(vids[1], idx + 1);
      vids[0].addEventListener('playing', () => vids[0].classList.add('on'), { once: true });
      vids[0].play().catch(() => {});
    };
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(es => es.forEach(e => {
        if (e.isIntersecting) { start(); if (vids[cur].paused && started) vids[cur].play().catch(() => {}); }
        else vids[cur].pause();
      }), { threshold: .05 }).observe(reel);
    } else start();
  });

  // single looping clips (work page): play only while visible
  document.querySelectorAll('video[data-loop]').forEach(v => {
    const src = clips[+v.dataset.loop % clips.length];
    new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { if (!v.src) v.src = src; v.play().catch(() => {}); } else v.pause();
    }), { threshold: .25 }).observe(v);
  });

})();
