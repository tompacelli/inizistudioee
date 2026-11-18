(() => {
  'use strict';
  /* Inizi 2027: motion layer (cursor, word reveals, progress) + the Tallinn map.
     Pure decoration / progressive enhancement. No network requests. The only thing stored is a sessionStorage flag
     so the intro plays once per visit. */
  const root = document.documentElement, body = document.body;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  const $ = (s, c = document) => [...c.querySelectorAll(s)];
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  try { if (sessionStorage.getItem('inizi_intro')) root.classList.add('seen'); else sessionStorage.setItem('inizi_intro', '1'); } catch (e) { root.classList.add('seen'); }

  /* ---- cursor: same ring + dot as the live inizi.studio page ---- */
  if (fine) {
    const ring = document.getElementById('cursor'), dot = document.getElementById('cursorDot');
    if (ring && dot) {
      body.classList.add('has-cursor');
      let mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my;
      addEventListener('pointermove', e => { mx = e.clientX; my = e.clientY; dot.style.left = mx + 'px'; dot.style.top = my + 'px'; ring.classList.add('on'); dot.classList.add('on'); }, { passive: true });
      document.addEventListener('mouseleave', () => { ring.classList.remove('on'); dot.classList.remove('on'); });
      (function loop() { rx += (mx - rx) * .35; ry += (my - ry) * .35; ring.style.left = rx + 'px'; ring.style.top = ry + 'px'; requestAnimationFrame(loop); })();
      const hov = 'a,button,[role="button"],.map__stage,.panel__media';
      document.addEventListener('pointerover', e => { if (e.target.closest && e.target.closest(hov)) ring.classList.add('hover'); });
      document.addEventListener('pointerout', e => { if (e.target.closest && e.target.closest(hov)) ring.classList.remove('hover'); });
    }
  }

  /* ---- headings reveal word by word ---- */
  const split = el => {
    let n = 0;
    const walk = (node, out) => node.childNodes.forEach(c => {
      if (c.nodeType === 3) {
        c.textContent.split(/(\s+)/).forEach(t => {
          if (!t) return;
          if (/^\s+$/.test(t)) { out.appendChild(document.createTextNode(' ')); return; }
          const w = document.createElement('span'); w.className = 'w';
          const i = document.createElement('span'); i.className = 'wi'; i.style.setProperty('--i', n++); i.textContent = t;
          w.appendChild(i); out.appendChild(w);
        });
      } else if (c.nodeType === 1) { const k = c.cloneNode(false); walk(c, k); out.appendChild(k); }
    });
    const frag = document.createElement('div'); walk(el, frag);
    el.textContent = ''; while (frag.firstChild) el.appendChild(frag.firstChild);
    el.classList.add('is-split');
  };
  if (!reduce) {
    const heads = $('h1.display,h2.display,h2.headline,.rule-list .title,.person .title');
    heads.forEach(split);
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { threshold: .2 });
    heads.forEach(h => io.observe(h));
  }

  /* ---- scroll layer: progress bar, nav hide/show (no parallax) ---- */
  const bar = document.querySelector('.progress i'), nav = document.querySelector('.nav');
  let lastY = scrollY, ticking = false, px = .5, py = .5;
  const frame = () => {
    ticking = false;
    const y = scrollY, max = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.transform = `scaleX(${max > 0 ? y / max : 0})`;
    if (nav) { nav.classList.toggle('is-hidden', y > lastY && y > 240 && !nav.classList.contains('is-open')); lastY = y; }
  };
  const req = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  addEventListener('scroll', req, { passive: true }); addEventListener('resize', req);
  frame();

  /* ---- journey: the section pins to the screen; scrolling inside it moves the journey 01 -> 03, both directions ---- */
  (() => {
    const sec = document.querySelector('.journey'), track = sec && sec.querySelector('.journey__track'); if (!track) return;
    const line = track.querySelector('.journey__line'), steps = $('.step', track);
    const small = () => matchMedia('(max-width:800px)').matches;
    let tick = false;
    const upd = () => {
      tick = false;
      if (reduce) { steps.forEach(el => el.classList.add('is-on')); line.style.setProperty('--p', 1); return; }
      const span = sec.offsetHeight - innerHeight;
      const p = span > 0 ? clamp(-sec.getBoundingClientRect().top / span, 0, 1) : 1;   /* 0 on arrival, 1 when the pin releases */
      const q = clamp((p - .04) / .8, 0, 1);
      line.style.setProperty('--p', q.toFixed(3));
      let n = p < .04 ? 0 : p < .36 ? 1 : p < .68 ? 2 : 3;                              /* how many steps are showing */
      steps.forEach((el, i) => {
        el.classList.toggle('is-on', small() ? i === Math.max(0, n - 1) && n > 0 : i < n);
        el.classList.toggle('is-past', small() && i < n - 1);
      });
    };
    const req2 = () => { if (!tick) { tick = true; requestAnimationFrame(upd); } };
    addEventListener('scroll', req2, { passive: true }); addEventListener('resize', req2); upd();
  })();

  /* ---- project results: numbers count up from 0 (ease-out) when they scroll into view ---- */
  (() => {
    const els = $('.proj__k b'); if (!els.length) return;
    const parse = t => { const m = String(t).trim().match(/^(\D*)(\d+(?:[.,]\d+)?)(.*)$/); if (!m) return null; const dec = (m[2].split(/[.,]/)[1] || '').length; return { pre: m[1], val: parseFloat(m[2].replace(',', '.')), dec, suf: m[3], sep: m[2].includes(',') ? ',' : '.' }; };
    const fmt = (d, v) => d.pre + v.toFixed(d.dec).replace('.', d.sep) + d.suf;
    const data = new Map(), raf = new Map();
    els.forEach(el => { const d = parse(el.textContent); if (d) { el.dataset.final = el.textContent; data.set(el, d); if (!reduce) el.textContent = fmt(d, 0); } });
    if (reduce || !('IntersectionObserver' in window)) { els.forEach(el => { if (el.dataset.final) el.textContent = el.dataset.final; }); return; }
    const run = el => {
      const d = data.get(el); if (!d) return; cancelAnimationFrame(raf.get(el));
      const dur = 2000, t0 = performance.now();
      const step = now => { const t = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - t, 4); el.textContent = fmt(d, d.val * e); if (t < 1) raf.set(el, requestAnimationFrame(step)); else el.textContent = el.dataset.final; };
      raf.set(el, requestAnimationFrame(step));
    };
    const io = new IntersectionObserver(es => es.forEach(en => {
      const el = en.target, d = data.get(el); if (!d) return;
      if (en.isIntersecting) { if (!el.dataset.on) { el.dataset.on = '1'; run(el); } }
      else { el.dataset.on = ''; cancelAnimationFrame(raf.get(el)); el.textContent = fmt(d, 0); }   /* leaves view or window closes: reset, replays next time */
    }), { threshold: .6 });
    els.forEach(el => io.observe(el));
  })();

  /* =========================== Tallinn map =========================== */
  const D = window.INIZI_MAP; if (!D) return;
  const NS = 'http://www.w3.org/2000/svg';
  const mk = (n, a, p) => { const e = document.createElementNS(NS, n); for (const k in a) e.setAttribute(k, a[k]); if (p) p.appendChild(e); return e; };

  $('[data-map]').forEach(map => {
    const stage = map.querySelector('.map__stage'), svg = map.querySelector('.map__svg'), tip = map.querySelector('.map__tip');
    const defs = mk('defs', {}, svg);
    const pat = mk('pattern', { id: 'dots' + Math.random().toString(36).slice(2, 6), width: 5, height: 5, patternUnits: 'userSpaceOnUse' }, defs);
    const dotR = mk('rect', { width: 1.3, height: 1.3, rx: .3, class: 'map__dotfill' }, pat);
    const world = mk('g', { class: 'map__world' }, svg);
    const grid = mk('g', { class: 'map__grid' }, world);
    for (let x = 0; x <= 1000; x += 100) mk('line', { x1: x, y1: 0, x2: x, y2: 520 }, grid);
    for (let y = 0; y <= 520; y += 100) mk('line', { x1: 0, y1: y, x2: 1000, y2: y }, grid);
    mk('path', { class: 'map__land', d: D.d, fill: `url(#${pat.id})` }, world);
    mk('path', { class: 'map__coast', d: D.d }, world);
    const P = D.pins.tallinn;
    const pin = mk('g', { class: 'map__pin', transform: `translate(${P[0]} ${P[1]})`, tabindex: 0, role: 'button', 'aria-label': map.dataset.name }, world);
    const sc = mk('g', { class: 'map__scale' }, pin);
    mk('rect', { class: 'map__pulse', x: -7, y: -7, width: 14, height: 14, rx: 5 }, sc);
    mk('rect', { class: 'map__pulse p2', x: -7, y: -7, width: 14, height: 14, rx: 5 }, sc);
    mk('rect', { class: 'map__mark', x: -3.5, y: -3.5, width: 7, height: 7, rx: 5 }, sc);
    mk('text', { class: 'map__label', x: 11, y: 4 }, sc).textContent = 'TALLINN';

    let v = { cx: 500, cy: 260, k: 1 }, anim = 0, open = false;
    const rect = () => stage.getBoundingClientRect();
    const apply = () => {
      const r = rect(), w = D.W / v.k, h = w * (r.height / r.width || .52);
      v.cx = clamp(v.cx, 0, D.W); v.cy = clamp(v.cy, 0, D.H);
      svg.setAttribute('viewBox', `${v.cx - w / 2} ${v.cy - h / 2} ${w} ${h}`);
      svg.style.setProperty('--k', String(v.k));
      const ds = clamp(5 / Math.pow(v.k, .62), 1.6, 5); pat.setAttribute('width', ds); pat.setAttribute('height', ds); dotR.setAttribute('width', ds * .26); dotR.setAttribute('height', ds * .26);
      placeTip();
    };
    const toScreen = p => { const pt = svg.createSVGPoint(); pt.x = p[0]; pt.y = p[1]; const m = svg.getScreenCTM(); if (!m) return null; const q = pt.matrixTransform(m), r = rect(); return [q.x - r.left, q.y - r.top]; };
    function placeTip() {
      if (!open) return; const s = toScreen(P); if (!s) return; const r = rect();
      const below = s[1] < 190;
      tip.style.left = clamp(s[0], 150, r.width - 150) + 'px'; tip.style.top = (s[1] + (below ? 26 : -26)) + 'px'; tip.classList.toggle('is-below', below);
    }
    const go = (to, ms) => {
      cancelAnimationFrame(anim);
      if (reduce) { v = { ...v, ...to }; apply(); return; }
      const from = { ...v }, t0 = performance.now(), ease = t => 1 - Math.pow(1 - t, 4);
      const step = now => { const t = clamp((now - t0) / ms, 0, 1), k = ease(t); v.cx = from.cx + (to.cx - from.cx) * k; v.cy = from.cy + (to.cy - from.cy) * k; v.k = from.k * Math.pow(to.k / from.k, k); apply(); if (t < 1) anim = requestAnimationFrame(step); };
      anim = requestAnimationFrame(step);
    };
    const show = () => {
      open = true; pin.classList.add('is-active');
      tip.replaceChildren();
      const a = document.createElement('p'); a.className = 'colhead'; a.textContent = map.dataset.tag;
      const h = document.createElement('h3'); h.className = 'title'; h.textContent = map.dataset.name;
      const d = document.createElement('p'); d.className = 'muted'; d.textContent = map.dataset.txt;
      tip.append(a, h, d); tip.classList.add('on'); placeTip();
      go({ cx: P[0], cy: P[1], k: 3.4 }, 1800);
    };
    const reset = () => { open = false; pin.classList.remove('is-active'); tip.classList.remove('on'); go({ cx: 500, cy: 260, k: 1 }, 1600); };
    const zoom = f => go({ cx: v.cx, cy: v.cy, k: clamp(v.k * f, 1, 9) }, 600);

    map.querySelector('[data-z="in"]').addEventListener('click', () => zoom(1.7));
    map.querySelector('[data-z="out"]').addEventListener('click', () => zoom(1 / 1.7));
    map.querySelector('[data-z="reset"]').addEventListener('click', reset);
    pin.addEventListener('click', e => { e.stopPropagation(); open ? reset() : show(); });
    pin.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open ? reset() : show(); } });

    const ptrs = new Map(); let last = null, pd = 0;
    stage.addEventListener('pointerdown', e => { if (e.target.closest('.map__ctrl')) return; stage.setPointerCapture(e.pointerId); ptrs.set(e.pointerId, [e.clientX, e.clientY]); last = [e.clientX, e.clientY]; stage.classList.add('is-drag'); cancelAnimationFrame(anim); });
    stage.addEventListener('pointermove', e => {
      if (!ptrs.has(e.pointerId)) return; ptrs.set(e.pointerId, [e.clientX, e.clientY]);
      const r = rect(), w = D.W / v.k;
      if (ptrs.size === 2) { const [a, b] = [...ptrs.values()], d = Math.hypot(a[0] - b[0], a[1] - b[1]); if (pd) { v.k = clamp(v.k * d / pd, 1, 9); apply(); } pd = d; return; }
      v.cx -= (e.clientX - last[0]) * (w / r.width); v.cy -= (e.clientY - last[1]) * (w / r.width); last = [e.clientX, e.clientY]; apply();
    });
    const up = e => { ptrs.delete(e.pointerId); pd = 0; if (!ptrs.size) stage.classList.remove('is-drag'); last = [...ptrs.values()][0] || null; };
    stage.addEventListener('pointerup', up); stage.addEventListener('pointercancel', up);
    stage.addEventListener('wheel', e => { if (!(e.ctrlKey || e.metaKey)) return; e.preventDefault(); zoom(e.deltaY < 0 ? 1.25 : .8); }, { passive: false });
    stage.addEventListener('dblclick', e => { if (!e.target.closest('.map__pin,.map__ctrl')) zoom(1.8); });
    stage.addEventListener('keydown', e => {
      const s = 60 / v.k, m = { ArrowLeft: [-s, 0], ArrowRight: [s, 0], ArrowUp: [0, -s], ArrowDown: [0, s] }[e.key];
      if (m) { e.preventDefault(); v.cx += m[0]; v.cy += m[1]; apply(); } else if (e.key === '+' || e.key === '=') zoom(1.5); else if (e.key === '-') zoom(1 / 1.5); else if (e.key === '0' || e.key === 'Escape') reset();
    });
    addEventListener('resize', apply);
    apply();
    new IntersectionObserver((es, o) => es.forEach(en => { if (en.isIntersecting) { map.classList.add('is-live'); setTimeout(show, reduce ? 0 : 1200); o.disconnect(); } }), { threshold: .35 }).observe(stage);
  });
})();
