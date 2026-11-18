# Builds the Inizi 2027 website (EN at /, ET at /et/) into /home/claude/inizi-2027
import os, html, json
OUT = "/home/claude/inizi-2027"
_d=lambda n: json.load(open(os.path.join(OUT,"data",n),encoding="utf8"))
PROJECTS=_d("projects.json")["projects"]; CLIENTS=_d("clients.json")["clients"]; REVIEWS=_d("reviews.json")["reviews"]
SITE = "https://www.inizi.studio"
DECK = "https://canva.link/mb2xid1qvzzn16g"
IG = "https://www.instagram.com/inizi.studio"

WM = '''<path d="M7.95,2.74v14.17c0,.53.03.91.08,1.15.05.24.21.39.47.45s.71.12,1.35.17c.02.18.02.35,0,.53-.39,0-.89,0-1.5-.03-.62-.02-1.1-.03-1.45-.03-.39,0-.88,0-1.48.03s-1.1.03-1.5.03c-.02-.18-.02-.35,0-.53.62-.05,1.06-.11,1.33-.16.27-.05.44-.18.5-.38.06-.2.09-.53.09-.99V2.98c0-.53-.04-.91-.11-1.14s-.24-.38-.5-.46-.7-.14-1.32-.17c-.02-.18-.02-.35,0-.53.26,0,.59,0,.96.01.38,0,.75.02,1.12.03.37,0,.68.01.92.01s.55,0,.91-.01c.36,0,.73-.02,1.1-.03.37,0,.68-.01.92-.01.02.18.02.35,0,.53-.62.05-1.06.11-1.32.16-.26.05-.43.18-.49.37-.06.19-.09.53-.09,1Z"/><path d="M40.04,19.67L27.5,3.43v13.36c0,.49.01.87.04,1.12.03.26.1.45.22.59.14.12.34.23.61.33.26.1.64.16,1.14.2.02.18.02.35,0,.53-.39,0-.81,0-1.28-.03s-.86-.03-1.17-.03-.71,0-1.17.03-.88.03-1.25.03c-.02-.18-.02-.35,0-.53.62-.07,1.06-.15,1.32-.24.26-.09.43-.26.49-.51.06-.26.09-.67.09-1.25V3.91c0-.69-.04-1.18-.11-1.49-.07-.31-.25-.52-.54-.62-.29-.11-.76-.19-1.41-.26-.02-.16-.02-.33,0-.5.4,0,.83,0,1.28.03s.89.03,1.33.03h.52c.29,0,.55,0,.78-.03l11.77,15.28V3.83c0-.48,0-.85-.03-1.12-.02-.27-.1-.47-.24-.59-.26-.3-.91-.48-1.95-.55-.02-.18-.02-.34,0-.5.37,0,.83,0,1.37.01.55,0,.98.01,1.29.01s.71,0,1.17-.01c.47,0,.89-.01,1.28-.01.02.16.02.33,0,.5-.62.07-1.06.15-1.33.25-.27.1-.44.27-.5.53-.06.26-.09.67-.09,1.25v15.97c-.12.04-.29.06-.52.08-.22.02-.41.03-.57.03Z"/><path d="M61.64,3.09v14.17c0,.53.03.91.08,1.15.05.24.21.39.47.45s.71.12,1.35.17c.02.18.02.35,0,.53-.39,0-.89,0-1.5-.03-.62-.02-1.1-.03-1.45-.03-.39,0-.88,0-1.48.03s-1.1.03-1.5.03c-.02-.18-.02-.35,0-.53.62-.05,1.06-.11,1.33-.16.27-.05.44-.18.5-.38.06-.2.09-.53.09-.99V3.33c0-.53-.04-.91-.11-1.14s-.24-.38-.5-.46-.7-.14-1.32-.17c-.02-.18-.02-.35,0-.53.26,0,.59,0,.96.01.38,0,.75.02,1.12.03.37,0,.68.01.92.01s.55,0,.91-.01c.36,0,.73-.02,1.1-.03.37,0,.68-.01.92-.01.02.18.02.35,0,.53-.62.05-1.06.11-1.32.16-.26.05-.43.18-.49.37-.06.19-.09.53-.09,1Z"/><path d="M92.25,1.45l-11.24,17.26h7.31c.72,0,1.27-.06,1.64-.17.37-.11.68-.33.92-.65.18-.23.36-.54.55-.92.19-.39.37-.85.53-1.37.16-.02.32-.02.48,0-.14.79-.27,1.53-.38,2.2-.11.68-.19,1.25-.22,1.73-.25,0-.99,0-2.22-.01-1.23,0-3.03-.01-5.38-.01-1.25,0-2.24,0-2.98.01-.74,0-1.32.02-1.76.03-.43,0-.82.01-1.17.01-.05-.14-.08-.27-.08-.4L89.48,1.87h-7.1c-.49,0-.92.04-1.28.11-.36.07-.66.23-.88.48-.18.19-.34.48-.5.87-.16.39-.3.83-.42,1.32-.18.02-.35.02-.53,0,.11-.63.2-1.26.28-1.87.08-.62.15-1.2.2-1.74,1.04.04,2.13.06,3.27.07,1.14,0,2.34.01,3.59.01s2.34,0,3.11-.01c.77,0,1.39-.02,1.85-.03.46,0,.83-.01,1.11-.01.02.05.03.11.05.17.02.06.03.14.03.22Z"/><path d="M111.19,3.09v14.17c0,.53.03.91.08,1.15.05.24.21.39.47.45s.71.12,1.35.17c.02.18.02.35,0,.53-.39,0-.89,0-1.5-.03-.62-.02-1.1-.03-1.45-.03-.39,0-.88,0-1.48.03s-1.1.03-1.5.03c-.02-.18-.02-.35,0-.53.62-.05,1.06-.11,1.33-.16.27-.05.44-.18.5-.38.06-.2.09-.53.09-.99V3.33c0-.53-.04-.91-.11-1.14s-.24-.38-.5-.46-.7-.14-1.32-.17c-.02-.18-.02-.35,0-.53.26,0,.59,0,.96.01.38,0,.75.02,1.12.03.37,0,.68.01.92.01s.55,0,.91-.01c.36,0,.73-.02,1.1-.03.37,0,.68-.01.92-.01.02.18.02.35,0,.53-.62.05-1.06.11-1.32.16-.26.05-.43.18-.49.37-.06.19-.09.53-.09,1Z"/>'''
SIG = '''<path d="M12.26,4.1v14.21c0,.53.03.91.08,1.15.05.24.21.39.48.45.26.06.71.12,1.35.17.02.18.02.35,0,.53-.39,0-.89,0-1.51-.03-.62-.02-1.1-.03-1.46-.03-.39,0-.88,0-1.48.03-.6.02-1.1.03-1.51.03-.02-.18-.02-.35,0-.53.62-.05,1.06-.11,1.34-.16.27-.05.44-.18.5-.38.06-.2.09-.53.09-.99V4.34c0-.53-.04-.91-.11-1.14-.07-.23-.24-.38-.5-.46-.26-.08-.7-.14-1.32-.17-.02-.18-.02-.35,0-.53.26,0,.59,0,.97.01.38,0,.75.02,1.12.03.37,0,.68.01.93.01s.55,0,.91-.01c.36,0,.73-.02,1.1-.03.37,0,.68-.01.93-.01.02.18.02.35,0,.53-.62.05-1.06.11-1.32.16s-.43.18-.49.37c-.06.19-.09.53-.09,1Z"/><path d="M27.22,19.39c0-.41.13-.74.4-1.02.26-.27.59-.41.98-.41.44,0,.79.15,1.05.44.26.29.38.62.38.99s-.13.72-.38,1.01c-.26.28-.6.42-1.05.42-.39,0-.71-.14-.98-.42-.26-.28-.4-.62-.4-1.01Z"/><path d="M47.1,4.1v14.21c0,.53.03.91.08,1.15.05.24.21.39.48.45.26.06.71.12,1.35.17.02.18.02.35,0,.53-.39,0-.89,0-1.51-.03-.62-.02-1.1-.03-1.46-.03-.39,0-.88,0-1.48.03-.6.02-1.1.03-1.51.03-.02-.18-.02-.35,0-.53.62-.05,1.06-.11,1.34-.16.27-.05.44-.18.5-.38.06-.2.09-.53.09-.99V4.34c0-.53-.04-.91-.11-1.14-.07-.23-.24-.38-.5-.46-.26-.08-.7-.14-1.32-.17-.02-.18-.02-.35,0-.53.26,0,.59,0,.97.01.38,0,.75.02,1.12.03.37,0,.68.01.93.01s.55,0,.91-.01c.36,0,.73-.02,1.1-.03.37,0,.68-.01.93-.01.02.18.02.35,0,.53-.62.05-1.06.11-1.32.16s-.43.18-.49.37c-.06.19-.09.53-.09,1Z"/><path d="M62.06,19.39c0-.41.13-.74.4-1.02.26-.27.59-.41.98-.41.44,0,.79.15,1.05.44.26.29.38.62.38.99s-.13.72-.38,1.01c-.26.28-.6.42-1.05.42-.39,0-.71-.14-.98-.42-.26-.28-.4-.62-.4-1.01Z"/><path d="M82.05,4.1v14.21c0,.53.03.91.08,1.15.05.24.21.39.48.45.26.06.71.12,1.35.17.02.18.02.35,0,.53-.39,0-.89,0-1.51-.03-.62-.02-1.1-.03-1.46-.03-.39,0-.88,0-1.48.03-.6.02-1.1.03-1.51.03-.02-.18-.02-.35,0-.53.62-.05,1.06-.11,1.34-.16.27-.05.44-.18.5-.38.06-.2.09-.53.09-.99V4.34c0-.53-.04-.91-.11-1.14-.07-.23-.24-.38-.5-.46-.26-.08-.7-.14-1.32-.17-.02-.18-.02-.35,0-.53.26,0,.59,0,.97.01.38,0,.75.02,1.12.03.37,0,.68.01.93.01s.55,0,.91-.01c.36,0,.73-.02,1.1-.03.37,0,.68-.01.93-.01.02.18.02.35,0,.53-.62.05-1.06.11-1.32.16s-.43.18-.49.37c-.06.19-.09.53-.09,1Z"/>'''

SPRITE = f'<svg class="sprite" width="0" height="0" aria-hidden="true" focusable="false"><symbol id="wm" viewBox="0 0 117.01 20.34">{WM}</symbol><symbol id="sig" viewBox="0 0 92.16 22.86">{SIG}</symbol></svg>'
LOCKUP = ('<div class="lockup"><svg viewBox="0 0 117.01 36" role="img" aria-label="Inizi. Here it begins.">'
          '<use href="#wm" width="117.01" height="20.34" class="logo"/>'
          '<text class="lt" x="0" y="33.3" font-size="11.5" textLength="54.8" lengthAdjust="spacing">HERE IT</text>'
  '<text class="lt la" x="61.8" y="33.3" font-size="13.16" textLength="55.2" lengthAdjust="spacing">BEGINS.</text>'
  '</svg></div>')


_wm_paths=WM.split('<path')[1:]
SIG_LETTERS=''.join(f'<path class="hl i{i}" d="{pp.split(chr(34))[1]}"/>' for i,pp in enumerate(SIG.split('<path')[1:]))
HERO_LETTERS=''.join(f'<path class="hl i{i}" d="{pp.split(chr(34))[1]}"/>' for i,pp in enumerate(_wm_paths))
HERO_LOCKUP=('<div class="lockup lockup--hero"><svg viewBox="0 0 117.01 36" role="img" aria-label="Inizi. Here it begins.">'
  f'<g class="logo">{HERO_LETTERS}</g>'
  '<text class="lt" x="0" y="33.3" font-size="11.5" textLength="54.8" lengthAdjust="spacing">HERE IT</text>'
  '<text class="lt la" x="61.8" y="33.3" font-size="13.16" textLength="55.2" lengthAdjust="spacing">BEGINS.</text></svg></div>')
MAPT={'en':dict(desc='Interactive black and white map. Inizi is based in Tallinn, Estonia.',zin='Zoom in',zout='Zoom out',reset='Reset map',hint='Drag to pan · Ctrl + scroll or + / − to zoom',tag='Based here',name='Tallinn, Estonia',txt='Where every Inizi project begins. We travel wherever the story is.'),
      'et':dict(desc='Interaktiivne mustvalge kaart. Inizi asub Tallinnas, Eestis.',zin='Suurenda',zout='Vähenda',reset='Lähtesta kaart',hint='Lohista · Ctrl + kerimine või + / − suurendab',tag='Asume siin',name='Tallinn, Eesti',txt='Siit algab iga Inizi projekt. Reisime sinna, kus lugu on.')}
def map_block(L,compact=False):
    t=MAPT[L]
    return (f'<div class="map{" map--compact" if compact else ""}" data-map data-name="{t["name"]}" data-tag="{t["tag"]}" data-txt="{t["txt"]}">'
      f'<div class="map__stage" tabindex="0" role="application" aria-label="{t["desc"]}">'
      '<svg class="map__svg" viewBox="0 0 1000 520" aria-hidden="true" focusable="false"></svg>'
      '<div class="map__tip" role="status" aria-live="polite"></div>'
      f'<div class="map__ctrl"><button type="button" class="map__btn" data-z="in" aria-label="{t["zin"]}">+</button><button type="button" class="map__btn" data-z="out" aria-label="{t["zout"]}">&minus;</button><button type="button" class="map__btn" data-z="reset" aria-label="{t["reset"]}">&#9678;</button></div>'
      f'<p class="map__hint">{t["hint"]}</p></div></div>')

def esc(s): return html.escape(s, quote=True)
def em(s): return s  # content already holds <em>

# ------------------------------------------------------------------ copy
C = {
 'en': dict(
  lang='en', htmllang='en', nav=[('work','Work'),('services','Services'),('about','About'),('contact','Contact')],
  menu='Menu', close='Close', to_day='Switch to day mode', to_night='Switch to night mode', skip='Skip to content', home_aria='Inizi — home',
  footer=dict(studio='Inizi OÜ', tag='Film production', loc='Tallinn, Estonia — Worldwide', pages='Pages', write='Write', else_='Elsewhere', insta='Instagram', deck='Introduction deck',
              legal='Legal', privacy='Privacy & cookies', cookies='Cookie settings', rights='© 2027 Inizi OÜ'),
  cta_start='Start a project', cta_deck='Explore our introduction deck', cta_subject='New project',
 ),
 'et': dict(
  lang='et', htmllang='et', nav=[('work','Tööd'),('services','Teenused'),('about','Meist'),('contact','Kontakt')],
  menu='Menüü', close='Sulge', to_day='Lülita päevarežiimile', to_night='Lülita öörežiimile', skip='Mine sisu juurde', home_aria='Inizi — avaleht',
  footer=dict(studio='Inizi OÜ', tag='Filmitootmine', loc='Tallinn, Eesti — üle maailma', pages='Lehed', write='Kirjuta', else_='Mujal', insta='Instagram', deck='Tutvustusdeck',
              legal='Õiguslik info', privacy='Privaatsus ja küpsised', cookies='Küpsiste seaded', rights='© 2027 Inizi OÜ'),
  cta_start='Alustame projekti', cta_deck='Tutvu meie tutvustusdeckiga', cta_subject='Uus projekt',
 ),
}

P = {}  # page content per language
P['en'] = {
 'index': dict(title='Inizi — Film production in Tallinn, Estonia', desc='Inizi is a film production company in Tallinn, Estonia, making travel and destination films, branded content, social video and music filmmaking for clients worldwide.'),
 'work': dict(title='Work — Inizi', desc='Selected travel films, branded content, social video and music work by Inizi, a film production company in Tallinn, Estonia.'),
 'services': dict(title='Services — Inizi', desc='Travel and destination films, branded content and marketing, social retainers, and music and events films from Inizi, Tallinn.'),
 'about': dict(title='About — Inizi', desc='Inizi means beginnings. Meet Johanna-Liisa Meema and Tom Pacelli, the filmmakers behind Inizi in Tallinn.'),
 'contact': dict(title='Contact — Inizi', desc='Start a project with Inizi. Write to hello@inizi.studio or find us on Instagram.'),
 'privacy': dict(title='Privacy & cookies — Inizi', desc='How Inizi OÜ handles personal data and cookies on this website.'),
 '404': dict(title='Page not found — Inizi', desc='This page could not be found.'),
}
P['et'] = {
 'index': dict(title='Inizi — Filmitootmine Tallinnas', desc='Inizi on Tallinnas tegutsev filmitootmisettevõte: reisi- ja sihtkohafilmid, brändisisu, sotsiaalmeedia video ja muusikafilmid klientidele üle maailma.'),
 'work': dict(title='Tööd — Inizi', desc='Valik Inizi reisifilme, brändisisu, sotsiaalmeedia videoid ja muusikatöid. Filmistuudio Tallinnas.'),
 'services': dict(title='Teenused — Inizi', desc='Reisi- ja sihtkohafilmid, brändisisu ja turundus, sotsiaalmeedia püsikoostöö ning muusika- ja eventfilmid Iniziga.'),
 'about': dict(title='Meist — Inizi', desc='Inizi tähendab algust. Tutvu Johanna-Liisa Meema ja Tom Pacelliga, Inizi taga olevate filmitegijatega Tallinnas.'),
 'contact': dict(title='Kontakt — Inizi', desc='Alustame projekti. Kirjuta hello@inizi.studio või leia meid Instagramist.'),
 'privacy': dict(title='Privaatsus ja küpsised — Inizi', desc='Kuidas Inizi OÜ käsitleb isikuandmeid ja küpsiseid sellel veebilehel.'),
 '404': dict(title='Lehte ei leitud — Inizi', desc='Seda lehte ei leitud.'),
}

def mail(u, label_hint, subject=None, keep=False, cls='', d='inizi.studio'):
    a = f'<a {"class=%s " % chr(34)+cls+chr(34) if False else ""}data-u="{u}" data-d="{d}"'
    if subject: a += f' data-s="{esc(subject)}"'
    if keep: a += ' data-keep="1"'
    if cls: a = a.replace('<a ', f'<a class="{cls}" ', 1)
    return a + f' href="#">{esc(label_hint)}</a>'

def label(n, text): return f'<p class="label"><b>{n}</b><span>{text}</span></p>'

def img(name, alt, lazy=True):
    return f'<img src="@A@img/still-{name}.jpg" alt="{esc(alt)}" width="768" height="432"{" loading=\"lazy\"" if lazy else ""} decoding="async">'

# ---------------- page bodies
def body_index(L):
    c = C[L]
    if L == 'en':
        s1_h = 'A film company for the stories that <em>begin something.</em>'
        s1_p = 'We are Johanna-Liisa and Tom, filmmakers based in Tallinn. Inizi means beginnings, and it is how we work: every film starts with a clear idea, natural light and people who care how it looks and moves.'
        s1_b = 'About us'
        s2_l = 'What we make'; s2 = [('Travel &amp; destination films','Hotels, resorts and destinations, shot to make people want to go.'),('Branded content &amp; marketing','Campaign films, brand stories and a steady rhythm of social video.'),('Music &amp; events','Music videos and festival aftermovies, when the room has the energy.')]
        all_s = 'All services'
        show = 'Your <em>partner</em> in crime when high-level visual storytelling is at <em>stake.</em>'
        s3_l = 'How we work'; s3 = [('Brief &amp; strategy','We listen first, then write the treatment: idea, look and structure.'),('Production','A small, fast crew shooting in natural light, wherever the story is.'),('Edit &amp; delivery','Pacing, sound and grade in our own hands, delivered in every format you need.')]
        cta_h = 'Have a story <em>to begin?</em>'
        marq=['Brand films','Festival aftermovies','Music filmmaking','Social &amp; retainers']; wl_='Where we work'; wh_='Based in Tallinn. <em>Working worldwide.</em>'; line = 'Brand films · Festival aftermovies · Music filmmaking'; foot_l = 'Estonia — Worldwide'; foot_r = 'Scroll'; studio_l='About'
    else:
        s1_h = 'Filmifirma lugudele, mis <em>midagi algatavad.</em>'
        s1_p = 'Meie oleme Johanna-Liisa ja Tom, Tallinnas tegutsevad filmitegijad. Inizi tähendab algust ja nii me töötamegi: iga film algab selgest ideest, loomulikust valgusest ja inimestest, kellele läheb korda, kuidas see välja näeb ja liigub.'
        s1_b = 'Meist'
        s2_l = 'Mida me teeme'; s2 = [('Reisi- ja sihtkohafilmid','Hotellid, kuurordid ja sihtkohad, filmitud nii, et inimesed tahavad minna.'),('Brändisisu ja turundus','Kampaaniafilmid, brändilood ja pidev sotsiaalmeedia videorütm.'),('Muusika ja eventid','Muusikavideod ja festivalide aftermovie’d, kui ruumis on energiat.')]
        all_s = 'Kõik teenused'
        show = 'Teie <em>kaasosaline</em>, kui kõrgetasemeline visuaalne jutustamine on <em>mängus.</em>'
        s3_l = 'Kuidas me töötame'; s3 = [('Brief ja strateegia','Kuulame kõigepealt, siis kirjutame treatmendi: idee, välimus ja struktuur.'),('Võtted','Väike ja kiire tiim, loomulik valgus, kus iganes lugu asub.'),('Montaaž ja üleandmine','Rütm, heli ja värv meie endi käes, üle antud kõigis vajalikes formaatides.')]
        cta_h = 'On teil lugu, <em>mida alustada?</em>'
        marq=['Brändifilmid','Festivalide aftermovie’d','Muusikafilmid','Sotsiaalmeedia']; wl_='Kus me töötame'; wh_='Kodu Tallinnas. <em>Töö üle maailma.</em>'; line = 'Brändifilmid · Festivalide aftermovie’d · Muusikafilmid'; foot_l = 'Eesti — üle maailma'; foot_r = 'Keri'; studio_l='Meist'
    rows = ''.join(f'<li class="reveal"><span class="numeral">{i+1:02d}</span><h3 class="title">{t}</h3><p class="muted">{d}</p></li>' for i,(t,d) in enumerate(s2))
    steps = ''.join(f'<div class="reveal"><p class="colhead">{i+1:02d} · {t}</p><p class="muted">{d}</p></div>' for i,(t,d) in enumerate(s3))
    HL = {'en':dict(trusted='Trusted by',logo='Client logo',recent='Recent projects',all_work='All work',kind='Kind words'),'et':dict(trusted='Meiega töötavad',logo='Kliendi logo',recent='Hiljutised projektid',all_work='Kõik tööd',kind='Head sõnad')}[L]
    trust = ''.join((f'<li class="reveal"><img src="@A@img/clients/{x["logo"]}" alt="{esc(x["name"])}" loading="lazy" decoding="async"></li>' if x.get('logo') else f'<li class="reveal trust__ph"><span>{HL["logo"]}</span></li>') for x in CLIENTS)
    feat = ''.join(project_cube(P, L, k+1, 'h3') for k,P in enumerate([P for P in PROJECTS if P.get('featured')][:3]))
    rev = ''.join(f'<figure class="rev reveal"><blockquote><p>{r[L]["quote"]}</p></blockquote><figcaption><b>{r[L]["name"]}</b><span>{r[L]["company"]}</span></figcaption></figure>' for r in REVIEWS)
    mapsec=f'<section class="section section--tight"><div class="wrap"><div class="reveal u-mb8">{label("04", wl_)}</div><h2 class="headline reveal u-mb7">{wh_}</h2>{map_block(L, True)}</div></section>'
    JH = 'From first idea to <em>final delivery.</em>' if L=='en' else 'Esimesest ideest <em>valmis tööni.</em>'
    JI = ['still-dawn','still-forest','still-coast']
    jsteps = ''.join(f'<li class="step"><p class="step__n" aria-hidden="true">{i+1:02d}</p><div class="step__img"><img src="@A@img/{JI[i]}.jpg" alt="" width="960" height="640" loading="lazy" decoding="async"></div><h3 class="title">{t}</h3><p class="muted">{d}</p></li>' for i,(t,d) in enumerate(s3))
    journey = f'''<section class="section journey" id="journey">
  <div class="journey__pin"><div class="wrap">
    <div class="reveal u-mb7">{label('03', s3_l)}</div>
    <h2 class="display journey__h reveal">{JH}</h2>
    <div class="journey__track"><div class="journey__line" aria-hidden="true"></div><ol class="journey__list">{jsteps}</ol></div>
  </div></div>
</section>'''
    return f'''<section class="reel hero" data-reel="0">
  <video class="reel__vid" muted playsinline preload="none" aria-hidden="true" tabindex="-1"></video>
  <video class="reel__vid" muted playsinline preload="none" aria-hidden="true" tabindex="-1"></video>
  <h1 class="sr">Inizi — Here it begins.</h1>
  {HERO_LOCKUP}
  <p class="hero__loc">{foot_l}</p>
  <div class="hero__foot" aria-hidden="true"><span>{foot_r}</span></div>
</section>

<section class="section" id="studio">
  <div class="wrap about-intro">
    {label('01', studio_l)}
    <div class="stack">
      <h2 class="display reveal">{s1_h}</h2>
      <p class="body-lg muted reveal">{s1_p}</p>
      <p class="reveal"><a class="btn btn--ghost" href="about.html">{s1_b}</a></p>
    </div>
  </div>
</section>

<section class="section section--tight trust">
  <div class="wrap">
    <p class="trust__l reveal">{HL['trusted']}</p>
    <ul class="trust__g">{trust}</ul>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="reveal u-mb8">{label('02', s2_l)}</div>
    <ol class="rule-list">{rows}</ol>
    <p class="reveal u-mt7"><a class="link" href="services.html">{all_s}</a></p>
    <div class="home-proj">
      <div class="home-proj__h reveal"><p class="colhead">{HL['recent']}</p><a class="link" href="work.html">{HL['all_work']}</a></div>
      <div class="cubes cubes--home">{feat}</div>
    </div>
  </div>
</section>

{journey}

{mapsec}

<section class="section section--tight">
  <div class="wrap">
    <div class="reveal u-mb8">{label('05', HL['kind'])}</div>
    <div class="revs">{rev}</div>
  </div>
</section>





<section class="section section--tight">
  <div class="wrap stack u-center">
    <h2 class="display reveal">{cta_h}</h2>
    <div class="btn-row reveal u-jc">{mail('hello', c['cta_start'], c['cta_subject'], keep=True, cls='btn')}<a class="btn btn--ghost" href="{DECK}" target="_blank" rel="noopener noreferrer">{c['cta_deck']}</a></div>
  </div>
</section>'''

def panels(items):
    out = ''
    for it in items:
        lis = ''.join(f'<li>{b}</li>' for b in it['bullets'])
        out += f'''<article class="panel reveal">
  <div class="panel__media">{img(it['img'], it['alt'])}</div>
  <div class="panel__body"><p class="colhead">{it['n']}</p><h2 class="headline">{it['t']}</h2><p class="body-lg muted">{it['d']}</p><ul>{lis}</ul></div>
</article>'''
    return out

PROJ_T = {
 'en': dict(ph='Project', open='Open project', prev='Previous project', next='Next project', close='Close', film='Final film',
  meta_l=['Client','Year','Service','Role','Format'], l_over='The project', l_brief='The brief', l_deliv='Deliverables', l_loc='Shot on location', l_kpi='Results', l_gal='Frames &amp; behind the scenes', cta='Have a story <em>to begin?</em>'),
 'et': dict(ph='Projekt', open='Ava projekt', prev='Eelmine projekt', next='Järgmine projekt', close='Sulge', film='Valmisfilm',
  meta_l=['Klient','Aasta','Teenus','Roll','Formaat'], l_over='Projekt', l_brief='Briif', l_deliv='Tulemused', l_loc='Võttekohad', l_kpi='Tulemused ja mõõdikud', l_gal='Kaadrid ja kulisside taga', cta='Kas sul on lugu, <em>mida alustada?</em>'),
}

def project_cube(P, L, k, tag='h2'):
    p = P[L]; T = PROJ_T[L]
    return f'<a class="cube reveal" href="work.html#project-{P["id"]}" data-project="{P["id"]}" aria-label="{T["open"]} {k:02d}"><img src="@A@img/still-{P["image"]}.jpg" alt="" width="768" height="432" loading="lazy" decoding="async"><{tag} class="cube__t">{p["cube"]}</{tag}></a>'

def body_work(L):
    c = C[L]
    if L == 'en':
        h = 'Selected <em>work.</em>'; sf = 'Travel and destination films, branded content, social video and music work for hotels, destinations, brands and artists. Full case studies are shared on request.'
        items = [
         dict(n='01 · Branded content', img='dawn', alt='Clouds drifting over a mountain range at dawn', t='Branded <em>content</em>', d='Films that carry a brand’s story from first idea to final grade, for hospitality, travel and lifestyle brands.', bullets=['Campaign films','Brand stories','Hospitality and destination films']),
         dict(n='02 · Music &amp; festivals', img='flare', alt='A single warm light in the dark', t='Music &amp; <em>festivals</em>', d='Aftermovies, artist films and live coverage, shot and cut with the energy of the room.', bullets=['Festival aftermovies','Artist and music films','Live coverage']),
         dict(n='03 · Social &amp; retainers', img='ridge', alt='A line of hikers on a ridge above the clouds at sunrise', t='Social &amp; <em>retainers</em>', d='A steady rhythm of short-form video for brands that need to show up every week.', bullets=['Monthly content days','Edits for every platform','One consistent look']),
        ]
        rh = 'In <em>motion.</em>'; rl = 'Reel'; cap = ['Reel 01','Reel 02','Reel 03']
        ch = 'Want to see more?'; cb = 'Case studies and the full showreel are available on request.'; ask = 'Request case studies'; asks='Case studies'
    else:
        h = 'Valik <em>töid.</em>'; sf = 'Reisi- ja sihtkohafilmid, brändisisu, sotsiaalmeedia video ja muusikatööd hotellidele, sihtkohtadele, brändidele ja artistidele. Täielikud juhtumiuuringud jagame soovi korral.'
        items = [
         dict(n='01 · Brändisisu', img='dawn', alt='Pilved mäeaheliku kohal koidikul', t='Brändi<em>sisu</em>', d='Filmid, mis kannavad brändi lugu esimesest ideest lõppvärvikorrektsioonini: hospitality, reisi- ja elustiilibrändidele.', bullets=['Kampaaniafilmid','Brändilood','Hospitality ja sihtkohafilmid']),
         dict(n='02 · Muusika ja festivalid', img='flare', alt='Üks soe valgus pimeduses', t='Muusika ja <em>festivalid</em>', d='Aftermovie’d, artistifilmid ja otseülekanded, filmitud ja monteeritud ruumi energiaga.', bullets=['Festivalide aftermovie’d','Artisti- ja muusikafilmid','Live-kaardistus']),
         dict(n='03 · Sotsiaalmeedia ja püsikoostöö', img='ridge', alt='Matkajate rida mäeharjal pilvede kohal päikesetõusul', t='Sotsiaalmeedia ja <em>püsikoostöö</em>', d='Pidev lühivideote rütm brändidele, kes peavad end nädalast nädalasse näitama.', bullets=['Igakuised filmipäevad','Montaažid igale platvormile','Ühtne visuaalne keel']),
        ]
        rh = 'Liikumises<em>.</em>'; rl = 'Showreel'; cap = ['Reel 01','Reel 02','Reel 03']
        ch = 'Tahad rohkem näha?'; cb = 'Juhtumiuuringud ja täispikk showreel on soovi korral saadaval.'; ask = 'Küsi juhtumiuuringuid'; asks='Juhtumiuuringud'
    T = PROJ_T[L]; N = len(PROJECTS)
    cubes = ''.join(project_cube(P, L, k+1) for k,P in enumerate(PROJECTS))
    def proj(k,P):
        p = P[L]; i = P['id']
        g = ''.join(f'<figure class="proj__g"><img src="@A@img/{x}.jpg" alt="" loading="lazy" decoding="async"></figure>' for x in P['gallery'])
        meta = ''.join(f'<div><dt>{a_}</dt><dd>{b_}</dd></div>' for a_,b_ in zip(T['meta_l'],[p['client'],p['year'],p['service'],p['role'],p['format']]))
        dl = ''.join(f'<li><span class="numeral">{j+1:02d}</span><span class="proj__dn">{a_}</span><span class="proj__df">{b_}</span></li>' for j,(a_,b_) in enumerate(p['deliverables']))
        loc = ''.join(f'<li><i class="proj__pin" aria-hidden="true"></i>{x}</li>' for x in p['locations'])
        kpi = ''.join(f'<div class="proj__k"><b>{v}</b><span>{k_}</span></div>' for v,k_ in p['kpis'])
        prv = PROJECTS[(k-2)%N]['id']; nxt = PROJECTS[k%N]['id']
        return f"""<article class="proj" id="project-{i}" role="dialog" aria-modal="true" aria-labelledby="pt-{i}" tabindex="-1">
<div class="proj__bar"><span class="proj__count">{T["ph"]} {k:02d} / {N:02d}</span><div class="proj__nav"><a href="#project-{prv}" data-nav="prev" aria-label="{T["prev"]}">&larr;</a><a href="#project-{nxt}" data-nav="next" aria-label="{T["next"]}">&rarr;</a><button type="button" class="proj__close" data-close>{T["close"]}</button></div></div>
<div class="proj__in">
<div class="proj__hero"><img src="@A@img/still-{P['image']}.jpg" alt="" decoding="async"><span class="proj__play" aria-hidden="true"></span><span class="proj__cap">{T["film"]}</span></div>
<header class="proj__head"><div><p class="colhead">{T["ph"]} {k:02d}</p><h2 class="display" id="pt-{i}">{p["title"]}</h2></div><dl class="proj__meta">{meta}</dl></header>
<div class="proj__cols"><section><p class="colhead">{T["l_over"]}</p><p class="body-lg">{p["overview"]}</p></section><section><p class="colhead">{T["l_brief"]}</p><p class="body-lg muted">{p["brief"]}</p></section></div>
<section class="proj__sec"><p class="colhead">{T["l_deliv"]}</p><ul class="proj__dl">{dl}</ul></section>
<section class="proj__sec"><p class="colhead">{T["l_loc"]}</p><ul class="proj__loc">{loc}</ul></section>
<section class="proj__sec"><p class="colhead">{T["l_kpi"]}</p><div class="proj__kpis">{kpi}</div></section>
<section class="proj__sec"><p class="colhead">{T["l_gal"]}</p><div class="proj__gal">{g}</div></section>
<footer class="proj__foot"><p class="headline">{T["cta"]}</p><div class="btn-row">{mail('hello', c['cta_start'], c['cta_subject'], keep=True, cls='btn')}<a class="btn btn--ghost" href="#project-{nxt}" data-nav="next">{T["next"]} &rarr;</a></div></footer>
</div></article>"""
    layer = '<div class="proj-layer" aria-hidden="true">'+''.join(proj(k+1,P) for k,P in enumerate(PROJECTS))+'</div>'
    return f'''<header class="page-head wrap">{label('01', c['nav'][0][1])}<h1 class="display">{h}</h1><p class="standfirst">{sf}</p></header>
<section class="section section--tight"><div class="cubes" aria-label="{c['nav'][0][1]}">{cubes}</div></section>
{layer}
<section class="section"><div class="wrap split">{label('02', ch)}<div class="stack"><p class="body-lg muted reveal">{cb}</p><div class="btn-row reveal">{mail('hello', ask, asks, keep=True, cls='btn')}<a class="btn btn--ghost" href="{DECK}" target="_blank" rel="noopener noreferrer">{c['cta_deck']}</a></div></div></div></section>'''

def body_services(L):
    c = C[L]
    if L == 'en':
        h = 'What we <em>make.</em>'; sf = 'Three ways to work with us, one standard of craft.'
        items = [
         dict(n='01', img='dawn', alt='Clouds drifting over a mountain range at dawn', t='Travel &amp; destination <em>films</em>', d='Films that make people want to go: hotels, resorts, tourism boards and destinations, shot in natural light with people mid-moment.', bullets=['Destination and tourism films','Hotel and resort films','Creator and press-trip coverage']),
         dict(n='02', img='ridge', alt='A line of hikers on a ridge above the clouds at sunrise', t='Branded content &amp; <em>marketing</em>', d='Films that carry a brand’s story from first idea to final grade, plus a steady rhythm of short-form video for brands that need to show up every week.', bullets=['Campaign films and brand stories','Social content and monthly retainers','Edits for every platform']),
         dict(n='03', img='flare', alt='A single warm light in the dark', t='Music &amp; <em>events</em>', d='Music videos and festival aftermovies, shot and cut with the energy of the room.', bullets=['Music videos and artist films','Festival aftermovies']),
        ]
        s2l = 'How we work'; steps = [('Brief &amp; strategy','We listen first, then write the treatment: idea, look and structure.'),('Production','A small, fast crew shooting in natural light, wherever the story is.'),('Edit &amp; delivery','Pacing, sound and grade in our own hands, delivered in every format you need.')]
        lh = 'Languages'; lp = 'We work in English, French and Estonian, and deliver in the language your audience speaks.'
        ch = 'Have a brief?'; cb = 'Tell us what you are making and when. We will take it from there.'
    else:
        h = 'Mida me <em>teeme.</em>'; sf = 'Kolm viisi meiega koostööd teha, üks käsitööstandard.'
        items = [
         dict(n='01', img='dawn', alt='Pilved mäeaheliku kohal koidikul', t='Reisi- ja sihtkoha<em>filmid</em>', d='Filmid, mis panevad inimesi minema tahtma: hotellid, kuurordid, turismiorganisatsioonid ja sihtkohad, filmitud loomulikus valguses, inimesed hetke sees.', bullets=['Sihtkoha- ja turismifilmid','Hotelli- ja kuurordifilmid','Loojate ja pressireiside kaardistus']),
         dict(n='02', img='ridge', alt='Matkajate rida mäeharjal pilvede kohal päikesetõusul', t='Brändisisu ja <em>turundus</em>', d='Filmid, mis kannavad brändi lugu esimesest ideest lõppvärvikorrektsioonini, ning pidev lühivideote rütm brändidele, kes peavad end iga nädal näitama.', bullets=['Kampaaniafilmid ja brändilood','Sotsiaalmeedia sisu ja igakuine püsikoostöö','Montaažid igale platvormile']),
         dict(n='03', img='flare', alt='Üks soe valgus pimeduses', t='Muusika ja <em>eventid</em>', d='Muusikavideod ja festivalide aftermovie’d, filmitud ja monteeritud ruumi energiaga.', bullets=['Muusikavideod ja artistifilmid','Festivalide aftermovie’d']),
        ]
        s2l = 'Kuidas me töötame'; steps = [('Brief ja strateegia','Kuulame kõigepealt, siis kirjutame treatmendi: idee, välimus ja struktuur.'),('Võtted','Väike ja kiire tiim, loomulik valgus, kus iganes lugu asub.'),('Montaaž ja üleandmine','Rütm, heli ja värv meie endi käes, üle antud kõigis vajalikes formaatides.')]
        lh = 'Keeled'; lp = 'Töötame inglise, prantsuse ja eesti keeles ning anname üle keeles, mida teie publik räägib.'
        ch = 'On teil brief?'; cb = 'Räägi, mida valmistad ja millal. Edasi võtame üle meie.'
    st = ''.join(f'<div class="reveal"><p class="colhead">{i+1:02d} · {t}</p><p class="muted">{d}</p></div>' for i,(t,d) in enumerate(steps))
    return f'''<header class="page-head wrap">{label('01', c['nav'][1][1])}<h1 class="display">{h}</h1><p class="standfirst">{sf}</p></header>
<section class="section section--tight"><div class="wrap">{panels(items)}</div></section>
<section class="section section--tight"><div class="wrap"><div class="reveal u-mb8">{label('02', s2l)}</div><div class="grid-3">{st}</div></div></section>
<section class="section section--tight"><div class="wrap split">{label('03', lh)}<p class="body-lg muted reveal">{lp}</p></div></section>
<section class="section"><div class="wrap split">{label('04', ch)}<div class="stack"><p class="body-lg muted reveal">{cb}</p><div class="btn-row reveal">{mail('hello', c['cta_start'], c['cta_subject'], keep=True, cls='btn')}<a class="btn btn--ghost" href="{DECK}" target="_blank" rel="noopener noreferrer">{c['cta_deck']}</a></div></div></div></section>'''

def person(name, role, bio, photo=None, alt=''):
    mark = f'<img src="@A@img/{photo}.jpg" alt="{esc(alt)}" width="960" height="1200" loading="lazy" decoding="async">' if photo else '<svg viewBox="0 0 92.16 22.86" class="logo" role="img" aria-label="I . I . I"><use href="#sig"/></svg>'
    return f'<article class="person reveal"><div class="person__mark">{mark}</div><h3 class="title">{name}</h3><p class="role">{role}</p><p class="muted">{bio}</p></article>'

def body_about(L):
    c = C[L]
    if L == 'en':
        h = 'Two filmmakers, <em>one mission.</em>'
        p1 = 'Inizi was founded by Tom Pacelli and Johanna-Liisa Meema, brought together by a shared love for storytelling and the belief that every brand has a story worth telling. Our passion lies in capturing the beauty, emotion, and details that make an experience truly memorable.'
        p2 = 'Our journey has taken us across the world, capturing moments that reflect the elegance and authenticity of some of the world’s most remarkable destinations.'
        tl = 'The team'
        jr, tr_ = 'Co-founder &amp; Creative Director', 'Co-founder &amp; Director / DP'
        jb = 'Johanna’s background in marketing adds a deeper dimension to her emotion-driven storytelling, where the focus is not only on visuals, but also on authenticity, brand alignment, and meaningful connection. Her approach combines strategic thinking with high-quality visuals to create content that genuinely resonates with audiences.'
        tb = 'Tom is a multiple award-winning creative with extensive international experience. He combines technical mastery with an instinctive sense for atmosphere and emotion. At the core of his work is authenticity and the moments that unfold naturally, transforming into compelling visuals that leave a lasting impression.'
        wl = 'Where we work'; wh = 'Based in Tallinn. <em>Working worldwide.</em>'; wp = 'Based in Tallinn, Estonia. Working worldwide, in English, French and Estonian.'
        ch = 'Say hello'; cb = 'Tell us what you are making.'
        bl = 'Behind the scenes'; bal = ['Filming a skyline at golden hour from a rooftop','Interview set-up with soft light in a hotel suite','Crew on location in the mountains at dusk','Shooting from a moving car at night in the city','Silhouettes of the crew at a monitor on a studio set','Johanna-Liisa checking the monitor on location','Operating a camera at a festival with a crowd at the stage','Reviewing a shot in a park in the morning light']
        pa = ['Portrait of Johanna-Liisa Meema with a camera','Portrait of Tom Pacelli with a camera']
        t1 = 'Supported by a world-class team of creatives, we craft visuals that feel natural while remaining intentionally refined.'; t2 = 'Our mission is to create campaigns that reflect the essence of your brand through elegant and immersive visual experiences.'
    else:
        h = 'Kaks filmitegijat, <em>üks missioon.</em>'
        p1 = 'Inizi asutasid Tom Pacelli ja Johanna-Liisa Meema, keda ühendab armastus jutustamise vastu ja veendumus, et igal brändil on lugu, mida väärib rääkida. Meie kirg on tabada ilu, emotsioone ja detaile, mis teevad kogemuse tõeliselt meeldejäävaks.'
        p2 = 'Meie teekond on viinud meid üle maailma, jäädvustama hetki, mis peegeldavad mõne maailma tähelepanuväärseima sihtkoha elegantsi ja ehtsust.'
        tl = 'Tiim'
        jr, tr_ = 'Kaasasutaja ja loovjuht', 'Kaasasutaja ja režissöör / DP'
        jb = 'Johanna turundustaust annab tema emotsioonidest lähtuvale jutustamisele sügavama mõõtme: fookuses pole ainult visuaal, vaid ka ehtsus, brändiga kooskõla ja sisuline side. Tema lähenemine ühendab strateegilise mõtlemise kvaliteetse pildikeelega, luues sisu, mis publikuga päriselt resoneerub.'
        tb = 'Tom on mitmekordselt auhinnatud loovinimene, kellel on lai rahvusvaheline kogemus. Ta ühendab tehnilise meisterlikkuse instinktiivse tunnetusega atmosfääri ja emotsiooni vastu. Tema töö tuumaks on ehtsus ja hetked, mis kulgevad loomulikult ning muutuvad mõjuvaks pildiks, mis jätab püsiva mulje.'
        wl = 'Kus me töötame'; wh = 'Kodu Tallinnas. <em>Töö üle maailma.</em>'; wp = 'Asume Tallinnas, Eestis. Töötame üle maailma, inglise, prantsuse ja eesti keeles.'
        ch = 'Ütle tere'; cb = 'Räägi, mida sa valmistad.'
        bl = 'Kulisside taga'; bal = ['Kaadri filmimine katuselt kuldsel tunnil','Intervjuu seadistus pehme valgusega hotellisviidis','Meeskond mägedes õhtuhämaruses','Filmimine liikuvast autost öises linnas','Meeskonna siluetid monitori taga stuudiovõttel','Johanna-Liisa kontrollib monitori võttekohal','Kaameraga tööd festivalil, rahvas laval ees','Kaadri ülevaatus pargis hommikuses valguses']
        pa = ['Johanna-Liisa Meema portree kaameraga','Tom Paceli portree kaameraga']
        t1 = 'Maailmatasemel loovmeeskonna toel loome visuaali, mis tundub loomulik, kuid on kavatsuslikult viimistletud.'; t2 = 'Meie missioon on luua kampaaniaid, mis peegeldavad sinu brändi olemust elegantsete ja kaasahaaravate visuaalsete elamuste kaudu.'
    cls_ = ['p','l','l','p','l','l','p','l']
    def fig(i): return f'<figure class="bts__i {cls_[i]} reveal"><img src="@A@img/bts-{i+1}.jpg" alt="{esc(bal[i])}" loading="lazy" decoding="async"></figure>'
    gal = '<div class="bts__row r1">'+''.join(fig(i) for i in range(4))+'</div><div class="bts__row r2">'+''.join(fig(i) for i in range(4,8))+'</div>'
    return f'''<section class="reel banner" data-reel="1" data-clip="2">
  <img class="banner__img" src="@A@img/still-ridge.jpg" alt="" decoding="async">
  <video class="reel__vid" muted playsinline preload="none" aria-hidden="true" tabindex="-1"></video>
  <video class="reel__vid" muted playsinline preload="none" aria-hidden="true" tabindex="-1"></video>
  <h1 class="display banner__t">{h}</h1>
</section>
<section class="section section--tight"><div class="wrap grid-2"><p class="body-lg reveal">{p1}</p><p class="body-lg muted reveal">{p2}</p></div></section>
<section class="section section--tight"><div class="wrap"><div class="reveal u-mb8">{label('02', tl)}</div><div class="grid-2">{person('Johanna-Liisa Meema', jr, jb, 'portrait-johanna', pa[0])}{person('Tom Pacelli', tr_, tb, 'portrait-tom', pa[1])}</div><div class="grid-2 u-mt7"><p class="body-lg reveal">{t1}</p><p class="body-lg muted reveal">{t2}</p></div></div></section>
<section class="section section--tight"><div class="wrap"><div class="reveal u-mb8">{label('03', bl)}</div><div class="bts">{gal}</div></div></section>
<section class="section section--tight"><div class="wrap"><div class="reveal u-mb8">{label('04', wl)}</div><div class="split u-mb7"><h2 class="headline reveal">{wh}</h2><p class="body-lg muted reveal">{wp}</p></div>{map_block(L)}</div></section>
<section class="section"><div class="wrap split">{label('05', ch)}<div class="stack"><p class="body-lg muted reveal">{cb}</p><div class="btn-row reveal">{mail('hello', c['cta_start'], c['cta_subject'], keep=True, cls='btn')}<a class="btn btn--ghost" href="{DECK}" target="_blank" rel="noopener noreferrer">{c['cta_deck']}</a></div></div></div></section>'''

def body_contact(L):
    c = C[L]
    if L == 'en':
        h = 'Let’s <em>begin.</em>'; sf = 'Tell us what you are making and when, and we will come back to you.'
        dts = dict(studio='General', people='People', social='Social', deck='Introduction deck', where='Where')
        deck_l = 'Open the deck'; where = 'Tallinn, Estonia — Worldwide'; ig = 'Instagram: @inizi.studio'; jl='Johanna-Liisa Meema'; tl_='Tom Pacelli'
    else:
        h = 'Alustame <em>sealt, kust algab.</em>'; sf = 'Räägi, mida sa valmistad ja millal, ning me võtame sinuga ühendust.'
        dts = dict(studio='Üldine', people='Inimesed', social='Sotsiaalmeedia', deck='Tutvustusdeck', where='Asukoht')
        deck_l = 'Ava deck'; where = 'Tallinn, Eesti — üle maailma'; ig = 'Instagram: @inizi.studio'; jl='Johanna-Liisa Meema'; tl_='Tom Pacelli'
    if L == 'en':
        F = dict(name='Name', email='Email', company='Company or project (optional)', interest='I am interested in', i0='Choose one', i1='A travel or destination film', i2='Branded content', i3='Social content or a retainer', i4='Music or festival film', i5='Something else',
                 when='When do you need it? (optional)', msg='Tell us about it', ph='What are you making, for whom, and what should it feel like?', consent='I agree that Inizi OÜ may use these details to reply to me. <a href="privacy.html">Privacy notice</a>.',
                 send='Send message', sending='Sending…', ok_t='Thank you.', ok_p='Your message is on its way to us. We will come back to you soon.', err='We could not send your message. Please try again in a moment, or write to us at ', req='Please complete the required fields.', ns='The form needs JavaScript. Please enable it, or email us at ')
    else:
        F = dict(name='Nimi', email='E-post', company='Ettevõte või projekt (valikuline)', interest='Mind huvitab', i0='Vali', i1='Reisi- või sihtkohafilm', i2='Brändisisu', i3='Sotsiaalmeedia sisu või püsikoostöö', i4='Muusika- või festivalifilm', i5='Midagi muud',
                 when='Millal sul seda vaja on? (valikuline)', msg='Räägi meile', ph='Mida sa valmistad, kellele ja mis tunde see peaks looma?', consent='Nõustun, et Inizi OÜ kasutab neid andmeid minule vastamiseks. <a href="privacy.html">Privaatsusteave</a>.',
                 send='Saada sõnum', sending='Saadan…', ok_t='Aitäh.', ok_p='Sinu sõnum on meile teel. Võtame varsti sinuga ühendust.', err='Sõnumi saatmine ei õnnestunud. Proovi hetke pärast uuesti või kirjuta meile aadressil ', req='Palun täida kohustuslikud väljad.', ns='Vorm vajab JavaScripti. Lülita see sisse või kirjuta meile aadressil ')
    form = f'''<form class="cform" id="form" method="post" action="#" novalidate data-endpoint="{FORM_ENDPOINT}" data-key="{FORM_KEY}" data-lang="{L}" data-ok-t="{F['ok_t']}" data-ok-p="{F['ok_p']}" data-err="{F['err']}" data-req="{F['req']}" data-sending="{F['sending']}">
  <div class="cform__row">
    <p class="field"><label for="f-name">{F['name']} <abbr title="required">*</abbr></label><input id="f-name" name="name" type="text" autocomplete="name" maxlength="120" required></p>
    <p class="field"><label for="f-email">{F['email']} <abbr title="required">*</abbr></label><input id="f-email" name="email" type="email" autocomplete="email" maxlength="160" required></p>
  </div>
  <div class="cform__row">
    <p class="field"><label for="f-co">{F['company']}</label><input id="f-co" name="company" type="text" autocomplete="organization" maxlength="160"></p>
    <p class="field field--sel"><label for="f-int">{F['interest']}</label><select id="f-int" name="interest"><option value="">{F['i0']}</option><option>{F['i1']}</option><option>{F['i2']}</option><option>{F['i3']}</option><option>{F['i4']}</option><option>{F['i5']}</option></select></p>
  </div>
  <p class="field"><label for="f-when">{F['when']}</label><input id="f-when" name="timing" type="text" maxlength="120"></p>
  <p class="field"><label for="f-msg">{F['msg']} <abbr title="required">*</abbr></label><textarea id="f-msg" name="message" rows="6" maxlength="4000" placeholder="{F['ph']}" required></textarea></p>
  <p class="field field--hp" aria-hidden="true"><label for="f-site">Leave this empty</label><input id="f-site" name="botcheck" type="text" tabindex="-1" autocomplete="off"></p>
  <p class="field field--check"><input id="f-ok" name="consent" type="checkbox" required><label for="f-ok">{F['consent']} <abbr title="required">*</abbr></label></p>
  <div class="cform__foot"><button class="btn" type="submit"><span>{F['send']}</span></button><p class="cform__status" role="status" aria-live="polite"></p></div>
  <noscript><p class="muted">{F['ns']}{mail('hello','hello [at] inizi.studio')}</p></noscript>
</form>'''
    return f'''<header class="page-head wrap">{label('01', c['nav'][3][1])}<h1 class="display">{h}</h1><p class="standfirst">{sf}</p></header>
<section class="section section--tight"><div class="wrap contact-grid">
  <div class="contact-grid__form">{form}</div>
  <dl class="contact-list u-start">
    <div><dt>{dts['social']}</dt><dd><a href="{IG}" target="_blank" rel="noopener noreferrer">{ig}</a></dd></div>
    <div><dt>{dts['deck']}</dt><dd><a href="{DECK}" target="_blank" rel="noopener noreferrer">{deck_l}</a></dd></div>
    <div><dt>{dts['where']}</dt><dd><span>{where}</span></dd></div>
  </dl>
</div></section>'''

def body_privacy(L):
    c = C[L]
    if L == 'en':
        return f'''<header class="page-head wrap">{label('', 'Legal')}<h1 class="display">Privacy &amp; <em>cookies.</em></h1><p class="standfirst">Last updated 17 November 2026.</p></header>
<section class="section section--tight"><div class="wrap legal prose">
<h2>Who we are</h2>
<p>This website is run by Inizi OÜ, a film production company based in Tallinn, Estonia (“Inizi”, “we”). We are the controller of the personal data described below. You can reach us at {mail('hello','hello [at] inizi.studio')}.</p>
<h2>What we collect, and why</h2>
<ul>
<li><span class="strong">Messages you send us.</span> If you use the contact form we receive what you type into it (name, email, optional company, interest and timing, and your message); if you email us we receive your address, your message and anything you attach. The form is delivered to our inbox by Web3Forms, which processes it on our behalf and does not use it for its own purposes. We use it to reply and to run the project you ask about (legal basis: your request, or our legitimate interest in answering enquiries). We keep it for as long as the conversation or project needs, then as long as the law requires.</li>
<li><span class="strong">Server logs.</span> Our hosting provider records technical data such as IP address, time and requested page, to deliver and secure the site (legitimate interest). These logs are kept for a short period.</li>
<li><span class="strong">Analytics, only if you accept.</span> If you press Accept in the cookie banner we load Google Analytics 4, which sets cookies and reports which pages are visited, roughly where from and on what kind of device. We have switched off advertising features and Google signals. Legal basis: your consent. If you decline, or your browser sends a Global Privacy Control or Do Not Track signal, nothing is loaded from Google.</li>
</ul>
<p>We do not run advertising, we do not sell personal data and the only form on this site is the contact form, which sends nothing until you press Send.</p>
<h2>Cookies and similar storage</h2>
<div class="tablewrap"><table><thead><tr><th>Name</th><th>What it does</th><th>When</th><th>Lasts</th></tr></thead><tbody>
<tr><td>inizi_consent_v1</td><td>Remembers your cookie choice. Stored in your browser’s local storage, not sent to us.</td><td>Always (strictly necessary)</td><td>180 days</td></tr>
<tr><td>inizi_theme</td><td>Remembers whether you chose day or night mode. Stored in your browser’s local storage, not sent to us.</td><td>Only if you use the day/night switch</td><td>Until you clear it</td></tr>
<tr><td>_ga</td><td>Google Analytics: tells visitors apart.</td><td>Only after Accept</td><td>2 years</td></tr>
<tr><td>_ga_G-9RKY3HS47H</td><td>Google Analytics: keeps session state.</td><td>Only after Accept</td><td>2 years</td></tr>
</tbody></table></div>
<p>You can change your choice at any time with <button class="link linkbtn" type="button" data-consent-open>Cookie settings</button>. Declining after accepting removes the analytics cookies.</p>
<h2>Who receives data</h2>
<p>Google Ireland Limited and Google LLC receive analytics data, only if you accept. Our hosting and email providers process data on our behalf. When you follow a link to Instagram (Meta) or Canva you leave this site and their own privacy policies apply; we embed nothing from them.</p>
<h2>Your rights</h2>
<p>Under the GDPR you may ask us for access to your data, correction, deletion, restriction or a portable copy, and you may object to processing based on legitimate interest or withdraw consent at any time. Write to {mail('hello','hello [at] inizi.studio')}. You may also complain to the Estonian Data Protection Inspectorate (Andmekaitse Inspektsioon, aki.ee) or to your local supervisory authority.</p>
<h2>Security</h2>
<p>The site is served over HTTPS, loads no third-party fonts or scripts except analytics you accept, and its only form (contact) is sent over HTTPS with a spam trap and no tracking. Contact addresses are not written into the page source, to reduce spam.</p>
<h2>Changes</h2>
<p>If we change this notice the date at the top changes too.</p>
</div></section>'''
    return f'''<header class="page-head wrap">{label('', 'Õiguslik info')}<h1 class="display">Privaatsus ja <em>küpsised.</em></h1><p class="standfirst">Viimati uuendatud 17. novembril 2026.</p></header>
<section class="section section--tight"><div class="wrap legal prose">
<h2>Kes me oleme</h2>
<p>Seda veebilehte haldab Inizi OÜ, Tallinnas tegutsev filmitootmisettevõte (“Inizi”, “me”). Me oleme allpool kirjeldatud isikuandmete vastutav töötleja. Meiega saab ühendust võtta aadressil {mail('hello','hello [at] inizi.studio')}.</p>
<h2>Mida me kogume ja miks</h2>
<ul>
<li><span class="strong">Sõnumid, mida meile saadad.</span> Kui kasutad kontaktivormi, saame selle, mille sisestad (nimi, e-post, valikuline ettevõte, huvi ja ajastus ning sõnum); kui kirjutad meile e-kirja, saame sinu aadressi, sõnumi ja manused. Vormi toimetab meie postkasti Web3Forms, kes töötleb seda meie nimel ega kasuta seda enda eesmärkidel. Kasutame neid vastamiseks ja projekti läbiviimiseks (õiguslik alus: sinu päring või meie õigustatud huvi päringutele vastata). Hoiame neid nii kaua, kui vestlus või projekt seda vajab, seejärel nii kaua, kui seadus nõuab.</li>
<li><span class="strong">Serverilogid.</span> Meie veebimajutaja salvestab tehnilisi andmeid, nagu IP-aadress, aeg ja külastatud leht, et leht töötaks ja oleks turvaline (õigustatud huvi). Logisid hoitakse lühikest aega.</li>
<li><span class="strong">Analüütika, ainult nõusolekul.</span> Kui vajutad küpsisebänneril “Nõustun”, laadime Google Analytics 4, mis paneb paika küpsised ja annab aru, milliseid lehti külastatakse, ligikaudu kust ja millise seadmega. Reklaamifunktsioonid ja Google signals on välja lülitatud. Õiguslik alus: sinu nõusolek. Kui keeldud või sinu brauser saadab Global Privacy Control või Do Not Track signaali, Google’ilt midagi ei laeta.</li>
</ul>
<p>Me ei tee reklaami, ei müü isikuandmeid ning lehe ainus vorm on kontaktivorm, mis ei saada midagi enne, kui vajutad “Saada”.</p>
<h2>Küpsised ja sarnane salvestus</h2>
<div class="tablewrap"><table><thead><tr><th>Nimi</th><th>Mida teeb</th><th>Millal</th><th>Kestus</th></tr></thead><tbody>
<tr><td>inizi_consent_v1</td><td>Jätab meelde sinu küpsisevaliku. Salvestatud brauseri kohalikus mälus, meile ei saadeta.</td><td>Alati (hädavajalik)</td><td>180 päeva</td></tr>
<tr><td>inizi_theme</td><td>Jätab meelde, kas valisid päeva- või öörežiimi. Salvestatud brauseri kohalikus mälus, meile ei saadeta.</td><td>Ainult siis, kui kasutad päeva/öö lülitit</td><td>Kuni sa selle kustutad</td></tr>
<tr><td>_ga</td><td>Google Analytics: eristab külastajaid.</td><td>Ainult pärast nõustumist</td><td>2 aastat</td></tr>
<tr><td>_ga_G-9RKY3HS47H</td><td>Google Analytics: hoiab seansi olekut.</td><td>Ainult pärast nõustumist</td><td>2 aastat</td></tr>
</tbody></table></div>
<p>Saad oma valikut igal ajal muuta nupust <button class="link linkbtn" type="button" data-consent-open>Küpsiste seaded</button>. Keeldumine pärast nõustumist eemaldab analüütikaküpsised.</p>
<h2>Kes andmeid saab</h2>
<p>Google Ireland Limited ja Google LLC saavad analüütikaandmeid, ainult kui nõustud. Meie majutus- ja e-posti teenusepakkujad töötlevad andmeid meie nimel. Kui järgid linki Instagrami (Meta) või Canva juurde, lahkud sellelt lehelt ja kehtivad nende enda privaatsuspoliitikad; me ei põimi nende sisu.</p>
<h2>Sinu õigused</h2>
<p>IKÜM-i alusel võid küsida juurdepääsu oma andmetele, parandamist, kustutamist, piiramist või ülekantavat koopiat, ning võid esitada vastuväite õigustatud huvil põhinevale töötlemisele või nõusoleku igal ajal tagasi võtta. Kirjuta aadressil {mail('hello','hello [at] inizi.studio')}. Võid esitada kaebuse ka Andmekaitse Inspektsioonile (aki.ee) või oma asukoha järelevalveasutusele.</p>
<h2>Turvalisus</h2>
<p>Leht serveeritakse HTTPS-iga, ei lae kolmanda osapoole fonte ega skripte, välja arvatud analüütika, millega nõustud, ning ainus vorm (kontakt) saadetakse HTTPS-iga, rämpsupüüdjaga ja ilma jälgimiseta. Kontaktaadresse ei ole lehe lähtekoodi kirjutatud, et vähendada spämmi.</p>
<h2>Muudatused</h2>
<p>Kui muudame seda teadet, muutub ka ülaltoodud kuupäev.</p>
</div></section>'''

def body_404(L):
    if L == 'en':
        return '<section class="lost"><div class="stack"><p class="label u-jc"><b>404</b></p><h1 class="display">This page has <em>not begun.</em></h1><p class="body-lg muted">It may have moved, or never existed.</p><p><a class="btn" href="index.html">Back to Inizi</a></p></div></section>'
    return '<section class="lost"><div class="stack"><p class="label u-jc"><b>404</b></p><h1 class="display">Seda lehte <em>pole veel alanud.</em></h1><p class="body-lg muted">See võib olla ümber kolinud või pole kunagi olemas olnud.</p><p><a class="btn" href="index.html">Tagasi Inizi lehele</a></p></div></section>'

BODIES = dict(index=body_index, work=body_work, services=body_services, about=body_about, contact=body_contact, privacy=body_privacy, **{'404': body_404})
ORDER = ['index','work','services','about','contact']
FORM_ENDPOINT = 'https://api.web3forms.com/submit'
FORM_KEY = '2980827f-ba3e-4159-9117-a90e197b2ec4'   # public by design; the receiving address (hello@inizi.studio) is set in the Web3Forms dashboard, never in this code
CSP = ("default-src 'self'; script-src 'self' https://www.googletagmanager.com; style-src 'self'; font-src 'self'; "
       "img-src 'self' data: https://*.google-analytics.com https://*.googletagmanager.com; media-src 'self'; "
       "connect-src 'self' https://api.web3forms.com https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com; "
       "object-src 'none'; base-uri 'none'; form-action 'none'")

def build(L, key):
    c = C[L]; pre = '' if L == 'en' else '../'; other = 'et' if L == 'en' else 'en'
    fn = f'{key}.html'
    meta = P[L][key]
    here = f'{SITE}/{"" if L=="en" else "et/"}{fn}'
    alt_en, alt_et = f'{SITE}/{fn}', f'{SITE}/et/{fn}'
    sw = (f'et/{fn}' if L == 'en' else f'../{fn}')
    navl = ''.join(f'<a href="{k}.html"{" aria-current=\"page\"" if k == key else ""}>{t}</a>' for k, t in c['nav'])
    lang = (f'<a href="{pre}{fn}" lang="en" hreflang="en"{" aria-current=\"true\"" if L=="en" else ""}>EN</a>' if L=='en' else f'<a href="../{fn}" lang="en" hreflang="en">EN</a>') + \
           (f'<a href="et/{fn}" lang="et" hreflang="et">EE</a>' if L=='en' else f'<a href="{fn}" lang="et" hreflang="et" aria-current="true">EE</a>')
    if key == '404':
        robots = '<meta name="robots" content="noindex">'
    else: robots = ''
    f = c['footer']
    cnt = f'{ORDER.index(key)+1:02d} / {len(ORDER):02d}' if key in ORDER else ''
    body = BODIES[key](L).replace('@A@', pre + 'assets/')
    ld = ''
    if key == 'index':
        ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Inizi OÜ","alternateName":"Inizi","url":"' + SITE + '/","description":"Film production company in Tallinn, Estonia.","address":{"@type":"PostalAddress","addressLocality":"Tallinn","addressCountry":"EE"},"sameAs":["' + IG + '"]}</script>')
    og_loc = 'et_EE' if L == 'et' else 'en_GB'
    page = f'''<!doctype html>
<html lang="{c['htmllang']}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(meta['title'])}</title>
<meta name="description" content="{esc(meta['desc'])}">
{robots}
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#0a0503">
<meta name="color-scheme" content="dark">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="et" href="{alt_et}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:site_name" content="Inizi">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(meta['title'])}">
<meta property="og:description" content="{esc(meta['desc'])}">
<meta property="og:url" content="{here}">
<meta property="og:locale" content="{og_loc}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{pre}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{pre}assets/img/apple-touch-icon.png">
<link rel="preload" href="{pre}fonts/geologica-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>
<script src="{pre}js/theme.js"></script>
<link rel="stylesheet" href="{pre}css/site.css">
<link rel="stylesheet" href="{pre}css/motion.css">
{ld}
</head>
<body class="{'is-home' if key=='index' else ''}" data-assets="{pre}assets/">
{SPRITE}
{('<div class="loader" aria-hidden="true"><svg viewBox="0 0 92.16 22.86" class="logo">'+SIG_LETTERS+'</svg><span class="loader__bar"><i></i></span></div>')}
<div class="progress" aria-hidden="true"><i></i></div>
<div class="cursor" id="cursor" aria-hidden="true"></div><div class="cursor-dot" id="cursorDot" aria-hidden="true"></div>
<a class="skip" href="#main">{c['skip']}</a>
<header class="nav">
  <a class="nav__logo" href="index.html" aria-label="{c['home_aria']}"><svg viewBox="0 0 92.16 22.86" class="logo" role="img" aria-label="Inizi"><use href="#sig"/></svg></a>
  <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="menu" data-open="{c['menu']}" data-close="{c['close']}" aria-label="{c['menu']}"><span class="nav__bars" aria-hidden="true"><i></i><i></i><i></i></span></button>
  <div class="nav__menu" id="menu"><nav class="nav__links" aria-label="Main">{navl}</nav><div class="lang" aria-label="Language">{lang}</div><button class="theme" type="button" aria-pressed="false" data-to-day="{c['to_day']}" data-to-night="{c['to_night']}" aria-label="{c['to_day']}"><svg class="theme__i theme__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.6M12 18.9v2.6M2.5 12h2.6M18.9 12h2.6M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/></svg><svg class="theme__i theme__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg></button></div>
</header>
<main id="main">
{body}
</main>
<footer class="footer">
  <div class="footer__cols">
    <div><p class="colhead">{f['studio']}</p><ul><li>{f['tag']}</li><li>{f['loc']}</li></ul></div>
    <div><p class="colhead">{f['pages']}</p><ul>{''.join(f'<li><a href="{k}.html">{t}</a></li>' for k,t in c['nav'])}</ul></div>
    <div><p class="colhead">{f['write']}</p><ul><li>{mail('hello','hello [at] inizi.studio')}</li><li>{mail('tom','tom [at] inizi.studio')}</li><li>{mail('johannaliisa','johannaliisa [at] inizi.studio')}</li></ul></div>
    <div><p class="colhead">{f['else_']}</p><ul><li><a href="{IG}" target="_blank" rel="noopener noreferrer">{f['insta']}</a></li><li><a href="{DECK}" target="_blank" rel="noopener noreferrer">{f['deck']}</a></li><li><a href="privacy.html">{f['privacy']}</a></li><li><button class="linklike" type="button" data-consent-open>{f['cookies']}</button></li></ul></div>
  </div>
  <div class="footer__base"><span class="footer__mark">I N I Z I</span><span>{f['rights']}</span><span class="counter">{cnt}</span></div>
</footer>
<script src="{pre}js/map-data.js" defer></script>
<script src="{pre}js/loader.js" defer></script>
<script src="{pre}js/main.js" defer></script>
<script src="{pre}js/fx.js" defer></script>
{"<script src=" + chr(34) + pre + "js/form.js" + chr(34) + " defer></script>" if key == "contact" else ""}
<script src="{pre}js/consent.js" defer data-lang="{L}" data-privacy="{('privacy.html')}"></script>
</body>
</html>
'''
    outdir = OUT if L == 'en' else os.path.join(OUT, 'et')
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, fn), 'w').write(page)

for L in ('en', 'et'):
    for key in BODIES: build(L, key)
print('built', len(BODIES) * 2, 'pages')
