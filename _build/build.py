"""yusufdemir.com.tr sayfalarını üretir.

Metinler ve yapılandırılmış veri burada tek yerde durur; çalıştırınca kökteki
HTML dosyaları yeniden yazılır. Jekyll `_` ile başlayan klasörü yayına almaz.

    python3 _build/build.py
"""
import json
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://yusufdemir.com.tr'
PHONE = '+905511345360'
PHONE_TEXT = '+90 551 134 53 60'
EMAIL = 'yusufdemir4154@gmail.com'


def wa(text):
    from urllib.parse import quote
    return 'https://wa.me/905511345360?text=' + quote(text)


WA_GENEL = wa('Merhaba Yusuf Bey, bir proje hakkında görüşmek istiyorum.')
WA_ON_GORUSME = wa('Merhaba Yusuf Bey, 15 dakikalık ön görüşme için yazıyorum.')

NAV = [('/projeler/', 'Projeler'), ('/hizmetler/', 'Hizmetler'), ('/cozumler/', 'Çözümler'), ('/iletisim/', 'İletişim')]

# ---------------------------------------------------------------------------
# Yapılandırılmış veri (ziyaretçi görmez; Google ve yapay zeka araçları okur)
# ---------------------------------------------------------------------------
AREAS = [{"@type": "City", "name": "İzmit"}, {"@type": "AdministrativeArea", "name": "Kocaeli"},
         {"@type": "City", "name": "İstanbul"}, {"@type": "AdministrativeArea", "name": "Marmara Bölgesi"},
         {"@type": "Country", "name": "Türkiye"}]
SERVICES = ["Kurumsal web sitesi", "E-ticaret sitesi ve ürün kataloğu", "Mobil uygulama (iOS ve Android, Flutter)",
            "İşletmeye özel ERP / CRM yönetim sistemi", "Süreç otomasyonu ve entegrasyon",
            "Web sitesi onarımı ve hız iyileştirme"]
ADDRESS = {"@type": "PostalAddress", "addressLocality": "İzmit", "addressRegion": "Kocaeli", "addressCountry": "TR"}
DESCRIPTION = ("Freelance bilgisayar mühendisi. İşletmelere kurumsal web sitesi, e-ticaret, mobil uygulama ve "
               "işletmeye özel ERP/CRM sistemleri geliştirir; Türkiye'nin her yerine çevrim içi, Marmara "
               "Bölgesi'nde istenirse yüz yüze çalışır.")
BASE_LD = {"@context": "https://schema.org", "@graph": [
    {"@type": "Person", "@id": SITE + "/#kisi", "name": "Yusuf Demir",
     "jobTitle": "Bilgisayar Mühendisi, Freelance Yazılım Geliştirici", "url": SITE + "/",
     "image": SITE + "/assets/images/logo-yd.png", "telephone": PHONE, "email": "mailto:" + EMAIL,
     "address": ADDRESS,
     "knowsAbout": ["Web geliştirme", "Mobil uygulama geliştirme", "Flutter", "ERP", "CRM", "E-ticaret",
                    "Süreç otomasyonu", "SEO"],
     "sameAs": ["https://github.com/YusufDemir0"], "worksFor": {"@id": SITE + "/#hizmet"}},
    {"@type": "ProfessionalService", "@id": SITE + "/#hizmet", "name": "Yusuf Demir Yazılım",
     "url": SITE + "/", "image": SITE + "/assets/images/logo-yd.png", "logo": SITE + "/assets/images/logo-yd.png",
     "telephone": PHONE, "email": EMAIL, "description": DESCRIPTION,
     "founder": {"@id": SITE + "/#kisi"}, "address": ADDRESS, "areaServed": AREAS, "knowsLanguage": "tr",
     "contactPoint": {"@type": "ContactPoint", "telephone": PHONE, "contactType": "customer service",
                      "availableLanguage": "Turkish"},
     "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Hizmetler", "itemListElement": [
         {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s, "areaServed": AREAS}} for s in SERVICES]},
     "sameAs": ["https://github.com/YusufDemir0"]},
    {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "Yusuf Demir", "inLanguage": "tr-TR",
     "publisher": {"@id": SITE + "/#kisi"}}]}

PROJECTS_LD = {"@context": "https://schema.org", "@type": "ItemList", "name": "Yusuf Demir projeleri", "itemListElement": [
    {"@type": "ListItem", "position": 1, "item": {
        "@type": "MobileApplication", "name": "Kremi", "operatingSystem": "iOS, Android",
        "applicationCategory": "ShoppingApplication",
        "description": "Kremi Beauty'nin cilt bakım ve kozmetik ürünlerini sattığı resmi mobil alışveriş uygulaması.",
        "url": "https://apps.apple.com/tr/app/kremi/id6758256090",
        "sameAs": ["https://play.google.com/store/apps/details?id=com.kremibeauty.app"],
        "author": {"@id": SITE + "/#kisi"}, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "TRY"}}},
    {"@type": "ListItem", "position": 2, "item": {
        "@type": "CreativeWork", "name": "İmalat ve satış yönetim sistemi (ERP/CRM)",
        "url": SITE + "/projeler/#yonetim-sistemi", "creator": {"@id": SITE + "/#kisi"}}},
    {"@type": "ListItem", "position": 3, "item": {
        "@type": "WebSite", "name": "UBEI telefon aksesuarı e-ticaret sitesi", "url": "https://ubei.com.tr/",
        "creator": {"@id": SITE + "/#kisi"}}}]}

FAQ = [
    ("Kocaeli ve İzmit'te freelance yazılımcı arıyorum, kime ulaşabilirim?",
     "Yusuf Demir, Kocaeli'de bulunan freelance bir bilgisayar mühendisidir; Kocaeli ve Marmara Bölgesi'ndeki "
     "işletmelerle istenirse yüz yüze de görüşür. Kurumsal web sitesi, e-ticaret, mobil uygulama ve ERP/CRM "
     "işlerini satışçı ya da ajans aracısı olmadan kendisi geliştirir. Telefon ve WhatsApp: " + PHONE_TEXT + "."),
    ("İstanbul'daki işletmelere hizmet veriyor musunuz?",
     "Evet. İstanbul dahil Marmara Bölgesi'ndeki işletmelerle yüz yüze ya da çevrim içi, Türkiye'nin her "
     "yerindeki işletmelerle çevrim içi çalışıyorum."),
    ("Web sitem mobilde bozuk, yavaş ya da formu çalışmıyor. Kim çözer?",
     "Siteye bakıp sorunun nerede olduğunu bulurum: mobil görünüm, hız, çalışmayan form, SSL, ödeme ya da "
     "WhatsApp düğmesi. İlk 15 dakikalık görüşme ücretsiz; ne yapılması gerektiğini açıkça söylerim."),
    ("Siparişlerimizi WhatsApp, Excel ve kâğıtla takip ediyoruz. Bunu nasıl toparlarız?",
     "İşletmenize göre bir yönetim sistemi kurarak siparişten üretime, sevkiyattan tahsilata her adımı tek "
     "ekranda görünür hâle getiririm. Bir üreticide kullanılan böyle bir sistem Projeler sayfasında anlatılıyor."),
    ("Mobil uygulama yapıp App Store ve Google Play'e yükleyebilir misiniz?",
     "Evet. Flutter ile iOS ve Android uygulaması geliştiriyor, mağaza başvurusunu da ben yürütüyorum. Kremi "
     "Beauty'nin alışveriş uygulaması iki mağazada da yayında."),
    ("Bir web sitesi ne kadar sürede yayına girer?",
     "İşin kapsamına bağlı. Ürün kataloğu ve WhatsApp sipariş düğmesi olan bir kurumsal site çoğu zaman birkaç iş "
     "gününde yayına girer; yönetim sistemi gibi büyük işler parça parça teslim edilir. Net süreyi ilk görüşmede "
     "veririm."),
    ("Bir proje hangi adımlarla ilerliyor?",
     "Önce 15 dakikalık ücretsiz görüşmede ne istediğinizi ve işlerinizin nasıl yürüdüğünü dinlerim. Ardından "
     "kapsamı, süreyi ve fiyatı yazılı olarak gönderirim. Onay verirseniz tasarımı hazırlayıp gösteririm; tasarım "
     "onaylanınca geliştirmeye geçerim ve ilerlemeyi bir önizleme bağlantısından siz de takip edersiniz. Son "
     "kontrollerden sonra alan adı, sunucu ya da mağaza başvurusuyla birlikte yayına alırım. Yayından sonra da "
     "soru ve değişiklik istekleriniz için doğrudan bana ulaşırsınız."),
    ("Fiyatı nasıl belirliyorsunuz?",
     "Fiyat, projenin kapsamına göre belirlenir: sayfa ya da ekran sayısı, ödeme, üyelik ve yönetim paneli gibi "
     "özellikler, muhasebe, kargo veya mevcut sistemlerle entegrasyon ihtiyacı ve metin ile görsellerin hazır "
     "olma durumu. İlk görüşmenin ardından kapsamı, teslim süresini ve fiyatı kalem kalem içeren yazılı bir "
     "teklif sunarım. Süreç içinde kapsam dışı bir talep doğarsa ek maliyeti önceden paylaşır, onayınız "
     "olmadan çalışmaya başlamam."),
    ("Ajans yerine freelance bir mühendisle çalışmanın farkı ne?",
     "Teklifi veren, kodu yazan ve sonradan destek veren aynı kişi. İstekleriniz aracıdan aracıya aktarılırken "
     "değişmez, bir değişiklik istediğinizde doğrudan işi yapanla konuşursunuz."),
]
FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}


def ld(obj):
    return '  <script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>\n'


def crumb(name, path, parents=()):
    trail = [("Ana sayfa", "/"), *parents, (name, path)]
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n, "item": SITE + p} for i, (n, p) in enumerate(trail, 1)]}


ICON_MENU = '<svg class="icon-open" width="24" height="24" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2.25" stroke-linecap="square"/></svg>'
ICON_CLOSE = '<svg class="icon-close" width="24" height="24" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19" stroke="currentColor" stroke-width="2.25" stroke-linecap="square"/></svg>'


def page(path, title, desc, main, crumb_name=None, extra_ld=(), noindex=False, hand_font=False, parents=()):
    items = ''.join(
        f'<li><a href="{h}" class="nav-link"{" aria-current=\"page\"" if h == path else ""}>{t}</a></li>'
        for h, t in NAV)
    # Fontlar site.css içinde, kendi sunucumuzdan; Caveat yalnız el yazısı kullanılan sayfada iner
    hand_preload = ('  <link rel="preload" href="/assets/fonts/caveat-latin-Wnz6HAc5.woff2" as="font" type="font/woff2" crossorigin />\n'
                    if hand_font else '')
    head_meta = '  <meta name="robots" content="noindex" />\n' if noindex else f'  <link rel="canonical" href="{SITE + path}" />\n'
    lds = '' if noindex else ld(BASE_LD) + (ld(crumb(crumb_name, path, parents)) if crumb_name else '') + ''.join(ld(x) for x in extra_ld)
    t, d = escape(title), escape(desc)
    return f'''<!DOCTYPE html>
<html lang="tr-TR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#f5e9d9" />
  <title>{t}</title>
  <meta name="description" content="{d}" />
  <meta name="author" content="Yusuf Demir" />
{head_meta}  <link rel="icon" href="/assets/images/logo-yd.png" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="tr_TR" />
  <meta property="og:title" content="{t}" />
  <meta property="og:description" content="{d}" />
  <meta property="og:url" content="{SITE + path}" />
  <meta property="og:site_name" content="Yusuf Demir" />
  <meta property="og:image" content="{SITE}/assets/images/og-kapak.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Yusuf Demir: defterde, Excel'de ve WhatsApp'ta dağılan işleri tek bir sisteme topluyorum." />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="geo.region" content="TR-41" />
  <meta name="geo.placename" content="İzmit, Kocaeli" />
  <link rel="alternate" type="text/plain" href="/llms.txt" title="LLM özeti" />
  <meta name="msvalidate.01" content="8C53056C7B7CA7FEEABC00C302D14538" />
  <link rel="preload" href="/assets/fonts/instrument-sans-latin-pxiTypc9.woff2" as="font" type="font/woff2" crossorigin />
{hand_preload}  <link rel="stylesheet" href="/assets/css/site.css" />
{lds}</head>

<body>
  <a class="skip-link" href="#icerik">İçeriğe geç</a>

  <header class="site-header">
    <div class="wrap header-inner">
      <a href="/" class="brand" aria-label="Yusuf Demir, ana sayfa">
        <img src="/assets/images/logo-yd.png" alt="" width="55" height="38" />
        <span>
          <span class="brand-name">Yusuf Demir</span>
          <span class="brand-role">Bilgisayar mühendisi · Freelance yazılım</span>
        </span>
      </a>

      <ul class="main-nav" id="ana-menu">{items}</ul>

      <div class="header-actions">
        <a href="{WA_GENEL}" target="_blank" rel="noopener" class="btn btn-primary btn-small">WhatsApp'tan yazın</a>
        <button class="nav-toggle" type="button" aria-controls="ana-menu" aria-expanded="false" aria-label="Menüyü aç">{ICON_MENU}{ICON_CLOSE}</button>
      </div>
    </div>
  </header>

  <main id="icerik">
{main}
  </main>

  <div class="mobile-bar">
    <a href="{WA_GENEL}" target="_blank" rel="noopener" class="btn btn-primary">WhatsApp</a>
    <a href="tel:{PHONE}" class="btn btn-secondary">Ara</a>
  </div>

  <footer class="site-footer">
    <div class="wrap footer-row">
      <div class="footer-brand">
        <img src="/assets/images/logo-yd.png" alt="" width="37" height="26" />
        <span><strong>Yusuf Demir</strong> · Bilgisayar mühendisi</span>
      </div>
      <div class="footer-links">
        <a href="tel:{PHONE}">{PHONE_TEXT}</a>
        <a href="mailto:{EMAIL}">E-posta</a>
        <a href="https://github.com/YusufDemir0" target="_blank" rel="noopener">GitHub</a>
        <a href="/site-kontrolu/">Ücretsiz site kontrolü</a>
        <a href="/gizlilik/">Gizlilik</a>
      </div>
    </div>
  </footer>

  <script src="/assets/js/site.js" defer></script>
  <!-- Cloudflare Web Analytics: çerezsiz ziyaret sayacı -->
  <script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "ade1c6e47aef44c1b42af82a34fc894d"}}'></script>
</body>
</html>
'''


def cta_band(title, text):
    return f'''      <div class="cta-band">
        <div>
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <a href="/iletisim/" class="btn btn-primary">İletişime geçin</a>
      </div>'''


# ---------------------------------------------------------------------------
# Ana sayfa
# ---------------------------------------------------------------------------
# Yanma videosu varsa (Omni + _build/video/isle.sh) CSS animasyonunun yerine oynar; yoksa CSS animasyonu kalır
BURN_VIDEO = ('''
          <video class="burn-video" muted playsinline preload="none" poster="/assets/video/yanma-poster.jpg" aria-hidden="true">
            <source src="/assets/video/yanma.mp4" type="video/mp4" />
          </video>''' if os.path.exists(os.path.join(ROOT, 'assets/video/yanma.mp4')) else '')
HOME = f'''    <section class="wrap hero">
      <div>
        <h1>Defterde, Excel'de ve WhatsApp'ta dağılan işleri <em>tek bir sisteme</em> topluyorum.</h1>
        <p class="hero-lead">Ben Yusuf Demir, bilgisayar mühendisiyim. İşletmelerin isteklerine göre modern web siteleri, mobil uygulamalar ve işe özel yönetim sistemleri yapıyorum. Teklifi veren de, kodu yazan da, sonra destek veren de benim.</p>
        <div class="hero-ctas">
          <a href="{WA_GENEL}" target="_blank" rel="noopener" class="btn btn-primary">WhatsApp'tan yazın</a>
          <a href="/iletisim/" class="btn btn-secondary">Ücretsiz ön görüşme</a>
        </div>
        <p class="hero-area"><strong>Tüm Türkiye'ye çevrim içi</strong> · Marmara Bölgesi'ndeyseniz yüz yüze de görüşebiliriz. <a href="/hizmetler/">Hizmetler</a></p>
        <ul class="perks">
          <li><strong>Aracı yok.</strong> Ne istediğinizi doğrudan işi yapan kişiye anlatırsınız.</li>
          <li><strong>Yayına kadar ben takip ederim.</strong> Alan adı, sunucu, App Store ve Google Play başvurusu dahil.</li>
        </ul>
      </div>

      <figure class="burn-figure">
        <div class="burn-stage">
          <div class="digital" aria-label="Aynı işlerin yönetim sistemindeki görünümü">
            <div class="digital-top"><b>Bugün</b><span>● Güncel</span></div>
            <div class="digital-stats">
              <div><strong>12</strong><small>yeni sipariş</small></div>
              <div><strong>3</strong><small>sevkiyat yolda</small></div>
              <div><strong>₺18.400</strong><small>tahsilat bekliyor</small></div>
              <div><strong>0</strong><small>unutulan sipariş</small></div>
            </div>
            <ul class="digital-list">
              <li><span>#1042 Ahmet K.</span><em>Kapora alındı</em></li>
              <li><span>#1043 Kargoya verildi</span><em>Takip no iletildi</em></li>
              <li><span>#1044 Fatura</span><em>Kesildi</em></li>
              <li class="warn"><span>Masa ayağı · 4 adet kaldı</span><em>Stok uyarısı</em></li>
            </ul>
          </div>
          <div class="sheet" aria-hidden="true">
            <h3>Sipariş defteri · Ekim</h3>
            <ul>
              <li>12.10 Ahmet Bey, 2 masa. Kapora? <span class="red">sor!</span></li>
              <li>13.10 Kargo no WhatsApp'ta, kimdeydi?</li>
              <li>14.10 Stokta 4 mü kaldı, 14 mü? Excel'e bak</li>
              <li><span class="red">15.10 Fatura kesilmedi!!</span></li>
              <li>Geri aranacak: 3 müşteri</li>
              <li>Mehmet Bey ödedi mi?</li>
            </ul>
            <span class="stain"></span>
          </div>
          <div class="char" aria-hidden="true"></div>{BURN_VIDEO}
        </div>
        <figcaption class="burn-caption">
          <span>Kâğıtta kaybolan işler, sistemde tek ekranda.</span>
          <button type="button" class="replay">Tekrar oynat</button>
        </figcaption>
      </figure>
    </section>

    <section class="wrap" style="padding-top:4rem;">
      <div class="section-head">
        <h2>Yaptığım işlerden</h2>
        <span>Yayında ve kullanımda</span>
      </div>
      <div class="card-grid">
        <a class="card" href="/projeler/#kremi">
          <span class="tag">Mobil uygulama</span>
          <h3>Kremi</h3>
          <p>Kremi Beauty'nin cilt bakım ve kozmetik ürünlerini sattığı alışveriş uygulaması. App Store ve Google Play'de.</p>
          <span class="more">Ayrıntılar →</span>
        </a>
        <a class="card" href="/projeler/#yonetim-sistemi">
          <span class="tag">Yönetim sistemi</span>
          <h3>İmalat ve satış yönetimi</h3>
          <p>Bir üretici için siparişi, stoğu, sevkiyatı ve tahsilatı tek ekranda toplayan sistem.</p>
          <span class="more">Ayrıntılar →</span>
        </a>
        <a class="card" href="/projeler/#ubei">
          <span class="tag">E-ticaret</span>
          <h3>UBEI</h3>
          <p>Türkiye geneline satış yapan bir telefon aksesuarı mağazası için modern e-ticaret sitesi.</p>
          <span class="more">Ayrıntılar →</span>
        </a>
      </div>
      <p class="more-row"><a href="/projeler/" class="btn btn-secondary">Tüm projeler</a></p>

      <div class="strip">
        <div>
          <span class="eyebrow">Ücretsiz site kontrolü</span>
          <p>Siteniz var ama telefondan gelen müşteri azsa bağlantıyı gönderin. Mobil görünüme, hıza ve Google'daki durumuna bakıp kısa bir değerlendirme yollayayım.</p>
        </div>
        <a href="/site-kontrolu/" class="btn btn-secondary">Nasıl işliyor?</a>
      </div>

{cta_band("Aklınızdaki işi konuşalım.", "İlk görüşme 15 dakika ve ücretsiz. Ne gerektiğini ve ne kadar süreceğini açıkça söylerim.")}
    </section>'''

# ---------------------------------------------------------------------------
# Projeler
# ---------------------------------------------------------------------------
PROJECTS = f'''    <section class="wrap">
      <div class="page-head">
        <p class="breadcrumb"><a href="/">Ana sayfa</a> / Projeler</p>
        <h1>Projeler</h1>
        <p>Yayında olan ve kullanılan işlerden üçü. Her biri işletmenin isteklerine göre baştan sona tek elden geliştirildi.</p>
      </div>

      <div class="cases">
        <article id="kremi" class="case">
          <div class="case-body">
            <div class="case-meta"><span class="tag">Mobil uygulama · Flutter</span><span class="status">App Store ve Google Play'de</span></div>
            <h2>Kremi: mobil alışveriş uygulaması</h2>
            <p>Kremi Beauty'nin resmi mobil uygulaması. Markanın cilt bakım ve kozmetik ürünleri uygulamadan incelenip güvenli ödemeyle satın alınabiliyor. Amaç, web mağazasındaki alışverişi telefona taşımaktı.</p>
            <ul>
              <li>Kategori ve filtrelerle ürün arama</li>
              <li>İçerik bilgisi olan ayrıntılı ürün sayfaları</li>
              <li>Güvenli ödeme, sipariş oluşturma ve sipariş takibi</li>
              <li>Kampanya ve indirim duyuruları</li>
              <li>Uygulama yalnız hizmet için gereken kullanıcı bilgisini kullanıyor</li>
            </ul>
            <div class="case-links">
              <a href="https://apps.apple.com/tr/app/kremi/id6758256090" target="_blank" rel="noopener" class="btn btn-secondary btn-small">App Store ↗</a>
              <a href="https://play.google.com/store/apps/details?id=com.kremibeauty.app" target="_blank" rel="noopener" class="btn btn-secondary btn-small">Google Play ↗</a>
            </div>
          </div>
          <div class="case-media">
            <div class="logo-plate">
              <img src="/assets/images/kremi-logo.png" alt="Kremi logosu" width="240" height="73" />
              <p>iOS ve Android için tek kod tabanı</p>
            </div>
          </div>
        </article>

        <article id="yonetim-sistemi" class="case flip">
          <div class="case-body">
            <div class="case-meta"><span class="tag">ERP / CRM</span><span class="status">Bir üreticide kullanımda</span></div>
            <h2>İmalat ve satış yönetim sistemi</h2>
            <p>Hem üretim yapan hem de birden fazla mağazadan satan bir işletme için yazdım. Satış, depo, sevkiyat ve kasa aynı sistemde; herkes kendi işine ait ekranı görüyor.</p>
            <ul>
              <li>Yetkiye göre ekran: satıcı kendi satışlarını ve kârını, depo personeli adetleri, yönetim tüm tabloyu görür</li>
              <li>Reçeteli üretim ve kritik stok uyarıları</li>
              <li>Sevkiyat ve tahsilat takibi; teslimde paranın hangi hesaba girdiği kaydedilir</li>
              <li>Her satışta yöneticinin Telegram'ına PDF fiş düşer</li>
            </ul>
          </div>
          <div class="case-media">
            <div class="shot"><img src="/assets/images/erp-genel-bakis.webp" alt="Yönetim sisteminin genel bakış ekranı: hızlı işlemler, bekleyen işler ve günlük rakamlar" width="1440" height="900" loading="lazy" /></div>
          </div>
        </article>

        <article id="ubei" class="case">
          <div class="case-body">
            <div class="case-meta"><span class="tag">E-ticaret · Next.js</span><span class="status">Yayında</span></div>
            <h2>UBEI: telefon aksesuarı e-ticaret sitesi</h2>
            <p>Türkiye geneline gönderim yapan bir telefon aksesuarı mağazası için modern bir e-ticaret sistemi. Katalog, ürün sayfaları, sepet ve sipariş adımı işletmenin satış biçimine göre kurgulandı.</p>
            <ul>
              <li>Kategori, fiyat ve malzemeye göre filtreleme; hızlı önizleme ve favoriler</li>
              <li>Uyumlu model bilgili ürün sayfaları, "birlikte alınanlar" önerileri</li>
              <li>Kampanya bandı, indirimli ürünler ve sipariş alımını tek anahtarla açıp kapatma</li>
              <li>Telefonda rahat kullanılan, hızlı açılan sayfalar ve arama motoru verileri</li>
            </ul>
            <div class="case-links">
              <a href="https://ubei.com.tr/" target="_blank" rel="noopener" class="btn btn-secondary btn-small">Mağazayı gezin ↗</a>
            </div>
          </div>
          <div class="case-media">
            <div class="shot"><img src="/assets/images/ubei-vitrin.webp" alt="UBEI e-ticaret sitesinin ana sayfası" width="1440" height="864" loading="lazy" /></div>
          </div>
        </article>
      </div>

{cta_band("Sizin işiniz için de yapalım.", "Ne kurmak istediğinizi anlatın, 15 dakikada nasıl ilerleyeceğimizi konuşalım.")}
    </section>'''

# ---------------------------------------------------------------------------
# Hizmetler
# ---------------------------------------------------------------------------
SERVICE_CARDS = [
    ("Kurumsal web sitesi", "İşletmenizin kimliğine ve isteklerine göre tasarlanan, telefonda hızlı açılan, Google'da bulunan modern bir site.", "/hizmetler/kurumsal-web-sitesi/"),
    ("E-ticaret ve ürün kataloğu", "Ürün kataloğu, filtreler, sepet ve sipariş adımıyla satışa hazır modern bir e-ticaret sitesi. Son işim: ubei.com.tr.", "/hizmetler/e-ticaret/"),
    ("Mobil uygulama", "Flutter ile iOS ve Android uygulaması. App Store ve Google Play başvurusu dahil.", "/hizmetler/mobil-uygulama/"),
    ("İşletmeye özel yönetim sistemi", "Sipariş, stok, üretim, sevkiyat ve tahsilatı tek ekranda toplayan, yetkiye göre çalışan sistem.", "/hizmetler/yonetim-sistemi/"),
    ("Süreç otomasyonu", "Excel'le ve kâğıtla yürüyen işleri otomatiğe bağlarım: Telegram/WhatsApp bildirimleri, PDF fiş ve raporlar.", None),
    ("Site onarımı ve hız", "Mobilde bozuk görünen, formu çalışmayan, SSL hatası veren ya da yavaş açılan siteleri onarırım. Önce ücretsiz kontrol.", "/site-kontrolu/"),
]


def service_card(t, d, href):
    if not href:
        return f"""
          <div class="card"><h2 class="card-title">{t}</h2><p>{d}</p></div>"""
    return f"""
          <a class="card" href="{href}"><h2 class="card-title">{t}</h2><p>{d}</p><span class="more">Ayrıntılar →</span></a>"""
SERVICES_HTML = f'''    <section class="wrap">
      <div class="page-head">
        <p class="breadcrumb"><a href="/">Ana sayfa</a> / Hizmetler</p>
        <span class="eyebrow">Tüm Türkiye · Çevrim içi</span>
        <h1>Hizmetler</h1>
        <p>Türkiye'nin her yerindeki işletmelerle çevrim içi çalışıyorum. Marmara Bölgesi'ndeyseniz isterseniz yüz yüze de görüşebiliriz. Her işi aracı olmadan, baştan sona kendim geliştiriyorum.</p>
      </div>
      <div class="panel">
        <div class="card-grid">{''.join(service_card(*c) for c in SERVICE_CARDS)}
        </div>
      </div>

      <div class="section-head"><h2>Sektöre göre</h2></div>
      <div class="card-grid card-grid-2">
        <a class="card" href="/sektorler/uretici-ve-imalat/"><span class="tag">Üretim</span><h3>Üreticiler ve imalatçılar</h3><p>Sipariş, kapora, üretim sırası, stok ve sevkiyatın tek yerden takibi; ürünleri gösteren bir katalog sitesi.</p><span class="more">Ayrıntılar →</span></a>
        <a class="card" href="/sektorler/magaza-ve-markalar/"><span class="tag">Satış</span><h3>Mağazalar ve markalar</h3><p>Kendi e-ticaret siteniz ve müşterinin telefonunda duran bir mobil uygulama.</p><span class="more">Ayrıntılar →</span></a>
      </div>

      <div class="section-head"><h2>Sık sorulan sorular</h2></div>
      <div class="faq">{''.join(f"""
        <details>
          <summary>{escape(q)}</summary>
          <p>{escape(a)}</p>
        </details>""" for q, a in FAQ)}
      </div>

{cta_band("Sorunuzun cevabı burada yok mu?", "Doğrudan sorun. İlk 15 dakikalık görüşme ücretsiz.")}
    </section>'''

# ---------------------------------------------------------------------------
# Çözümler
# ---------------------------------------------------------------------------
PROBLEMS = [
    ("Web sitesi", "Telefonda yavaş açılan site",
     "Ziyaretçilerin çoğu siteye telefondan giriyor. Sayfa geç açılıyorsa, form çalışmıyorsa ya da arama düğmesi yoksa birkaç saniye içinde rakibe geçiyorlar; reklama verilen para da boşa gidiyor.",
     "İşletmenizin isteklerine göre tasarlanan, telefonda hızlı açılan ve ziyaretçiyi müşteriye dönüştüren modern bir web sitesi."),
    ("Mobil", "Müşterinin telefonunda olmamak",
     "Sipariş ya da randevu için her seferinde aramak zorunda kalan müşteri bir süre sonra vazgeçiyor. Kendi uygulaması olan işletmeyi ise müşteri cebinde taşıyor; kampanya ve yenilikler doğrudan ona ulaşıyor.",
     "İşletmenize özel, App Store ve Google Play'de yayınlanan bir mobil uygulama: sipariş, randevu ya da sadakat programı, neye ihtiyacınız varsa."),
    ("İş takibi", "Defterde, Excel'de ve WhatsApp'ta kaybolan siparişler",
     "Sipariş bir yerde, kapora başka yerde, kargo numarası bir sohbette kalıyor. Kime ne teslim edileceğini öğrenmek için her seferinde birinin aranması gerekiyor.",
     "Siparişten teslimata her adımı tek ekranda gösteren, işletmenize özel bir yönetim sistemi."),
]
SOLUTIONS = f'''    <section class="wrap">
      <div class="page-head">
        <p class="breadcrumb"><a href="/">Ana sayfa</a> / Çözümler</p>
        <h1>İşletmeler müşteriyi en çok nerede kaçırıyor?</h1>
        <p>Çalıştığım işletmelerde sorun çoğu zaman reklam bütçesinde değil; müşteriyi karşılayan sitede ya da işlerin takip edilme biçiminde çıkıyor. En sık gördüğüm üç durum:</p>
      </div>
      <div class="panel">
        <div class="card-grid">{''.join(f"""
          <div class="card">
            <span class="tag">{tag}</span>
            <h2 style="font-size:1.25rem;color:var(--ink);line-height:1.25">{t}</h2>
            <p>{body}</p>
            <p class="fix"><b>Ne yapıyorum:</b> {fix}</p>
          </div>""" for tag, t, body, fix in PROBLEMS)}
        </div>
      </div>
{cta_band("Bunlardan biri sizde de var mı?", "Kısa bir görüşmede birlikte bakalım.")}
    </section>'''

# ---------------------------------------------------------------------------
# İletişim
# ---------------------------------------------------------------------------
CONTACT = f'''    <section class="wrap">
      <div class="page-head">
        <p class="breadcrumb"><a href="/">Ana sayfa</a> / İletişim</p>
        <h1>İletişim</h1>
        <p>Telefon, WhatsApp ya da e-posta; hangisi kolayınıza gelirse. Doğrudan bana ulaşırsınız.</p>
      </div>
      <div class="contact-box">
        <div>
          <span class="eyebrow">Ücretsiz ön görüşme</span>
          <h2>15 dakikada işinize bakalım</h2>
          <p>Sitenizi, uygulamanızı ya da işleri nasıl takip ettiğinizi anlatın. Nerede aksadığını ve ne gerektiğini açıkça söylerim; sonrasında benimle çalışmak zorunda değilsiniz.</p>
        </div>
        <div class="contact-actions">
          <a href="{WA_ON_GORUSME}" target="_blank" rel="noopener" class="btn btn-primary">WhatsApp'tan yazın</a>
          <a href="tel:{PHONE}" class="btn btn-secondary">Arayın: {PHONE_TEXT}</a>
          <a href="mailto:{EMAIL}" class="btn btn-secondary"><span class="email">{EMAIL}</span></a>
          <a href="/yusuf-demir.vcf" download class="btn btn-secondary">Rehbere ekle</a>
        </div>
      </div>
    </section>'''

# ---------------------------------------------------------------------------
# Hizmet ve sektör ayrıntı sayfaları
# ---------------------------------------------------------------------------
WA_SITE_KONTROL = wa('Merhaba Yusuf Bey, ücretsiz site kontrolü istiyorum. Sitemin adresi: ')

DETAIL_PAGES = [
    {"path": "/hizmetler/kurumsal-web-sitesi/", "parent": ("Hizmetler", "/hizmetler/"), "crumb": "Kurumsal web sitesi",
     "title": "Kurumsal Web Sitesi | Yusuf Demir · Freelance Yazılımcı",
     "desc": "İşletmenizi doğru anlatan, telefonda hızlı açılan ve Google'da bulunan kurumsal web sitesi. Tasarım, yayına alma ve Search Console kaydı dahil.",
     "eyebrow": "Hizmet", "h1": "Kurumsal web sitesi",
     "lead": "İşletmenizi doğru anlatan, telefonda hızlı açılan ve Google'da bulunan bir site. Tasarım işletmenizin kimliğine göre hazırlanır; metin düzeni, müşterinin aradığını ilk bakışta bulacağı şekilde kurulur.",
     "includes": ["İşletmenize özel tasarım ve sayfa düzeni",
                  "Telefon, tablet ve bilgisayarda düzgün görünüm",
                  "WhatsApp, arama ve e-posta düğmeleri",
                  "Sayfa başlıkları, açıklamalar, site haritası ve Google Search Console kaydı",
                  "Alan adı, SSL sertifikası ve yayına alma",
                  "İsterseniz ürün kataloğu ya da teklif isteme bölümü"],
     "fit": ["Henüz sitesi olmayan ya da sitesi eskimiş işletmeler",
             "Müşterisine gönderebileceği derli toplu bir bağlantı isteyenler",
             "Reklam verdiği hâlde siteden dönüş alamayanlar"],
     "related": None,
     "faq": [("Sitemi sonradan kendim güncelleyebilir miyim?",
              "İhtiyaca göre. Ürün, duyuru ya da fiyat gibi sık değişen içerikler için yönetim paneli eklenebilir. Nadiren değişen sitelerde güncellemeleri ben yaparım."),
             ("Bir kurumsal site ne kadar sürede yayına girer?",
              "Kapsama bağlı. Ürün kataloğu ve WhatsApp düğmesi olan bir kurumsal site çoğu zaman birkaç iş gününde yayına girer. Net süreyi ilk görüşmede veririm.")]},
    {"path": "/hizmetler/e-ticaret/", "parent": ("Hizmetler", "/hizmetler/"), "crumb": "E-ticaret sitesi",
     "title": "E-ticaret Sitesi ve Ürün Kataloğu | Yusuf Demir · Freelance Yazılımcı",
     "desc": "Kategori, filtre, ürün sayfası, sepet ve sipariş adımıyla işletmenize özel e-ticaret sitesi. Online ödeme ya da sipariş talebiyle çalışabilir.",
     "eyebrow": "Hizmet", "h1": "E-ticaret sitesi",
     "lead": "Ürünlerinizi kategorilere ayıran, aramayı ve filtrelemeyi kolaylaştıran, sepetten siparişe kadar sorunsuz ilerleyen bir mağaza. Satış biçiminize göre kurulur: kartla ödeme, havale ya da sipariş talebi.",
     "includes": ["Kategori, arama ve filtreler",
                  "Görselli, seçenekli ve stok bilgili ürün sayfaları",
                  "Sepet ve sipariş adımı; kartla ödeme için sanal POS bağlantısı ya da sipariş talebi",
                  "Kampanya bandı ve indirimli ürünler",
                  "Sipariş alımını tek anahtarla açıp kapatma",
                  "Google'ın ürünleri doğru okuması için yapılandırılmış veri"],
     "fit": ["Instagram ya da WhatsApp'tan satış yapıp düzene geçmek isteyenler",
             "Pazaryeri komisyonu yerine kendi mağazasını isteyenler",
             "Ürünlerini katalog olarak gösterip sipariş talebi toplamak isteyen üreticiler"],
     "related": ("UBEI", "Telefon aksesuarı mağazası için kurduğum e-ticaret sitesi.", "/projeler/#ubei"),
     "faq": [("Online ödeme almak zorunda mıyım?",
              "Hayır. Bazı işletmeler için sipariş talebi toplayıp ödemeyi havale ya da teslimatta almak daha uygundur. İki yol da kurulabilir, sonradan biri diğerine çevrilebilir."),
             ("Ürünleri kim yükler?",
              "İlk ürünleri birlikte yükleriz; sonrasında yönetim panelinden siz ekleyip güncelleyebilirsiniz.")]},
    {"path": "/hizmetler/mobil-uygulama/", "parent": ("Hizmetler", "/hizmetler/"), "crumb": "Mobil uygulama",
     "title": "Mobil Uygulama Geliştirme (iOS ve Android) | Yusuf Demir · Freelance Yazılımcı",
     "desc": "Flutter ile tek kod tabanından iOS ve Android uygulaması. App Store ve Google Play başvurusu ve yayın süreci dahil.",
     "eyebrow": "Hizmet", "h1": "Mobil uygulama",
     "lead": "Flutter ile tek kod tabanından iOS ve Android uygulaması. Uygulamanın tasarımından mağaza başvurusuna ve yayından sonraki güncellemelere kadar süreci ben yürütürüm.",
     "includes": ["iOS ve Android için tek kod tabanı",
                  "Kullanıcı girişi, sipariş, randevu ya da sadakat programı; ihtiyaca göre",
                  "Kampanya ve sipariş bildirimleri",
                  "Mevcut web sitenizle ya da sisteminizle bağlantı",
                  "App Store ve Google Play başvurusu, inceleme sürecinin takibi"],
     "fit": ["Müşterisinin telefonunda yer almak isteyen markalar",
             "Web mağazasındaki alışverişi uygulamaya taşımak isteyenler",
             "Sipariş ya da randevuyu telefonla almaktan yorulan işletmeler"],
     "related": ("Kremi", "Kremi Beauty'nin App Store ve Google Play'de yayında olan alışveriş uygulaması.", "/projeler/#kremi"),
     "faq": [("Uygulama mağazalarda ne kadar sürede yayınlanır?",
              "Apple ve Google'ın incelemesi genelde birkaç gün sürer. İnceleme sırasında bir düzeltme istenirse yapıp yeniden gönderirim."),
             ("Hem iOS hem Android için ayrı ayrı mı yapılıyor?",
              "Hayır. Flutter ile tek bir kod yazılır ve iki platformda da çalışır; bu, hem süreyi hem bakım maliyetini düşürür.")]},
    {"path": "/hizmetler/yonetim-sistemi/", "parent": ("Hizmetler", "/hizmetler/"), "crumb": "Yönetim sistemi (ERP / CRM)",
     "title": "İşletmeye Özel Yönetim Sistemi (ERP / CRM) | Yusuf Demir · Freelance Yazılımcı",
     "desc": "Sipariş, stok, üretim, sevkiyat ve tahsilatı tek ekranda toplayan, yetkiye göre çalışan işletmeye özel ERP / CRM sistemi.",
     "eyebrow": "Hizmet", "h1": "İşletmeye özel yönetim sistemi",
     "lead": "Siparişi, stoğu, üretimi, sevkiyatı ve tahsilatı tek ekranda toplayan; herkesin yalnız kendi işini gördüğü bir sistem. Hazır bir programa uymaya çalışmak yerine sistem sizin iş akışınıza göre kurulur.",
     "includes": ["Yetkiye göre ekranlar: satış, depo, sevkiyat ve yönetim ayrı ayrı",
                  "Sipariş, kapora ve müşteri kaydı",
                  "Stok, reçeteli üretim ve kritik stok uyarıları",
                  "Sevkiyat ve tahsilat takibi",
                  "PDF fiş ve irsaliye; Telegram ya da WhatsApp bildirimi",
                  "Web sitenizden gelen siparişlerin sisteme düşmesi"],
     "fit": ["Siparişini defterde, Excel'de ya da WhatsApp'ta takip eden işletmeler",
             "Hem üretip hem satan imalatçılar",
             "Birden fazla mağazası ya da deposu olanlar"],
     "related": ("İmalat ve satış yönetim sistemi", "Bir üreticide kullanılan, satıştan tahsilata her adımı tek ekranda toplayan sistem.", "/projeler/#yonetim-sistemi"),
     "faq": [("Hazır bir ERP programı yerine neden özel sistem?",
              "Hazır programlar herkese göre yapılır; işletme ya programa uyar ya da yalnız bir kısmını kullanır. Özel sistem sizin iş akışınıza göre kurulur ve yalnız gereken ekranları içerir. Küçük başlayıp ihtiyaç oldukça büyütülebilir."),
             ("Sistem bir anda mı devreye giriyor?",
              "Hayır, parça parça teslim edilir. Genelde önce sipariş ve müşteri kaydıyla başlanır; stok, üretim ve tahsilat sonraki aşamalarda eklenir.")]},
    {"path": "/sektorler/uretici-ve-imalat/", "parent": ("Hizmetler", "/hizmetler/"), "crumb": "Üreticiler ve imalatçılar",
     "title": "Üreticiler İçin Sipariş, Üretim ve Stok Takibi | Yusuf Demir",
     "desc": "Üretici ve imalatçılar için sipariş, kapora, üretim sırası, stok ve sevkiyatı tek yerden takip eden sistem ve ürün kataloğu sitesi.",
     "eyebrow": "Sektör", "h1": "Üreticiler ve imalatçılar için",
     "lead": "Üretim yapan işletmelerde iş çoğu zaman siparişin kendisinde değil, takibinde aksar: kapora bir yerde yazılı, üretim sırası ustanın aklında, sevkiyat tarihi bir WhatsApp sohbetinde. Bunu tek bir sistemde topluyorum.",
     "includes": ["Siparişin kapora, üretim ve teslim durumuyla birlikte kaydı",
                  "Reçeteye göre malzeme ihtiyacı ve kritik stok uyarısı",
                  "Sevkiyat planı ve teslimde tahsilat kaydı",
                  "Bayi ya da mağaza satışlarının aynı sistemde toplanması",
                  "Ürünleri gösteren, sipariş talebi toplayan bir katalog sitesi"],
     "fit": ["Mobilya, ahşap, metal ve benzeri sipariş üzerine üretim yapanlar",
             "Birden fazla satış noktası ya da bayisi olan üreticiler",
             "Toptan ve perakendeyi birlikte yürütenler"],
     "related": ("İmalat ve satış yönetim sistemi", "Hem üreten hem birden fazla mağazadan satan bir işletmede kullanılıyor.", "/projeler/#yonetim-sistemi"),
     "faq": [("Ustalarımız bilgisayar kullanmıyor, sistem işe yarar mı?",
              "Ekranlar herkesin yalnız kendi işini göreceği şekilde sade tutulur; depo ya da atölye için telefondan kullanılabilen kısa ekranlar yapılabilir.")]},
    {"path": "/sektorler/magaza-ve-markalar/", "parent": ("Hizmetler", "/hizmetler/"), "crumb": "Mağazalar ve markalar",
     "title": "Mağazalar ve Markalar İçin E-ticaret ve Mobil Uygulama | Yusuf Demir",
     "desc": "Mağazalar ve markalar için kendi e-ticaret sitesi ve App Store ile Google Play'de yayınlanan mobil alışveriş uygulaması.",
     "eyebrow": "Sektör", "h1": "Mağazalar ve markalar için",
     "lead": "Satışın bir kısmı pazaryerinde, bir kısmı Instagram mesajlarında, bir kısmı da telefonda yürüyorsa müşteri de siz de zorlanırsınız. Kendi mağazanız ve isterseniz kendi uygulamanızla satış tek bir yere toplanır.",
     "includes": ["Markanıza özel e-ticaret sitesi: katalog, filtre, sepet ve sipariş",
                  "iOS ve Android alışveriş uygulaması",
                  "Kampanya, indirim ve duyuru alanları",
                  "Sipariş takibi ve müşteriye durum bilgisi",
                  "Google'da ürünlerin doğru görünmesi için yapılandırılmış veri"],
     "fit": ["Kozmetik, giyim, aksesuar ve benzeri ürün satan markalar",
             "Pazaryeri komisyonunu azaltmak isteyen mağazalar",
             "Sadık müşterisine doğrudan ulaşmak isteyen işletmeler"],
     "related": ("Kremi ve UBEI", "Bir kozmetik markasının mobil uygulaması ve bir aksesuar mağazasının e-ticaret sitesi.", "/projeler/"),
     "faq": [("Önce site mi, uygulama mı?",
              "Çoğu işletme için önce site. Müşteri ilk olarak Google'dan ya da paylaşılan bir bağlantıdan gelir; uygulama, düzenli alışveriş yapan müşteri kitlesi oluştuğunda daha çok işe yarar.")]},
]


def detail_page(d):
    items = ''.join(f"\n            <li>{escape(x)}</li>" for x in d["includes"])
    fit = ''.join(f"\n            <li>{escape(x)}</li>" for x in d["fit"])
    faq = ''.join(f"""
        <details>
          <summary>{escape(q)}</summary>
          <p>{escape(a)}</p>
        </details>""" for q, a in d["faq"])
    related = ''
    if d["related"]:
        n, t, h = d["related"]
        related = f'''
          <a class="card" href="{h}"><span class="tag">İlgili iş</span><h3>{escape(n)}</h3><p>{escape(t)}</p><span class="more">Ayrıntılar →</span></a>'''
    pn, pp = d["parent"]
    return f'''    <section class="wrap">
      <div class="page-head">
        <p class="breadcrumb"><a href="/">Ana sayfa</a> / <a href="{pp}">{pn}</a> / {escape(d["crumb"])}</p>
        <span class="eyebrow">{d["eyebrow"]}</span>
        <h1>{escape(d["h1"])}</h1>
        <p>{escape(d["lead"])}</p>
      </div>
      <div class="svc">
        <div class="panel">
          <h2 class="svc-h">Neler dahil</h2>
          <ul class="checklist">{items}
          </ul>
          <h2 class="svc-h">Kimler için</h2>
          <ul class="checklist">{fit}
          </ul>
        </div>
        <aside class="svc-side">{related}
          <div class="card">
            <h3>15 dakikalık ön görüşme</h3>
            <p>Ne istediğinizi anlatın; nasıl ilerleyeceğimizi, süreyi ve yaklaşık kapsamı açıkça söyleyeyim.</p>
            <a href="{WA_ON_GORUSME}" target="_blank" rel="noopener" class="btn btn-primary">WhatsApp'tan yazın</a>
          </div>
        </aside>
      </div>

      <div class="section-head"><h2>Sık sorulan sorular</h2></div>
      <div class="faq">{faq}
      </div>

{cta_band("Fiyatı ve süreci merak ediyor musunuz?", 'Nasıl çalıştığımı ve fiyatın nasıl belirlendiğini <a href="/hizmetler/">Hizmetler</a> sayfasındaki sorularda anlattım.')}
    </section>'''


def detail_ld(d):
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
    svc = {"@context": "https://schema.org", "@type": "Service", "name": d["h1"], "description": d["desc"],
           "url": SITE + d["path"], "provider": {"@id": SITE + "/#hizmet"}, "areaServed": AREAS}
    return [svc, faq]


SITE_CHECK = f'''    <section class="wrap">
      <div class="page-head">
        <p class="breadcrumb"><a href="/">Ana sayfa</a> / Ücretsiz site kontrolü</p>
        <span class="eyebrow">Site onarımı ve hız</span>
        <h1>Ücretsiz site kontrolü</h1>
        <p>Sitenizin bağlantısını gönderin. Telefonda nasıl göründüğüne, ne kadar hızlı açıldığına ve Google'da nasıl çıktığına bakıp kısa ve anlaşılır bir değerlendirme yollayayım.</p>
      </div>
      <div class="svc">
        <div class="panel">
          <h2 class="svc-h">Neye bakıyorum</h2>
          <ul class="checklist">
            <li>Telefonda görünüm: taşan bölümler, okunmayan yazılar, küçük kalan düğmeler</li>
            <li>Açılış hızı ve hızı düşüren görseller ya da kodlar</li>
            <li>WhatsApp, arama ve form düğmeleri gerçekten çalışıyor mu</li>
            <li>SSL sertifikası ve tarayıcının verdiği güvenlik uyarıları</li>
            <li>Google'da görünürlük: sayfa başlıkları, açıklamalar ve dizine eklenme</li>
            <li>Yapay zeka asistanlarının sitenizi okuyup önerebilmesi için gereken temel ayarlar</li>
          </ul>
          <h2 class="svc-h">Nasıl ilerliyor</h2>
          <ul class="checklist">
            <li>Site adresinizi WhatsApp'tan ya da e-postayla gönderirsiniz.</li>
            <li>Siteyi telefonda ve bilgisayarda inceler, bulduklarımı önem sırasıyla yazarım.</li>
            <li>Ne yapılması gerektiğini açıkça söylerim. Benimle çalışmak zorunda değilsiniz; listeyi kendi ekibinize de verebilirsiniz.</li>
          </ul>
        </div>
        <aside class="svc-side">
          <div class="card">
            <h3>Site adresinizi gönderin</h3>
            <p>Mesajınıza sitenizin adresini eklemeniz yeterli.</p>
            <a href="{WA_SITE_KONTROL}" target="_blank" rel="noopener" class="btn btn-primary">WhatsApp'tan gönderin</a>
            <a href="mailto:{EMAIL}?subject=%C3%9Ccretsiz%20site%20kontrol%C3%BC" class="btn btn-secondary">E-postayla gönderin</a>
          </div>
        </aside>
      </div>
    </section>'''

PRIVACY = f'''    <section class="wrap">
      <div class="page-head">
        <p class="breadcrumb"><a href="/">Ana sayfa</a> / Gizlilik</p>
        <h1>Gizlilik</h1>
        <p>Bu sitede üyelik, form ya da çerez yok. Hangi bilgilerin nerede işlendiğini aşağıda kısaca anlattım.</p>
      </div>
      <div class="panel prose">
        <h2 class="svc-h">Ziyaret istatistikleri</h2>
        <p>Kaç kişinin hangi sayfayı ziyaret ettiğini görmek için Cloudflare Web Analytics kullanıyorum. Bu araç çerez kullanmaz ve ziyaretçiyi tanımlamaz; yalnız sayfa adresi, geldiğiniz site, tarayıcı türü ve ülke gibi toplu bilgiler tutulur.</p>
        <h2 class="svc-h">Barındırma</h2>
        <p>Site GitHub Pages üzerinde yayınlanıyor. GitHub, güvenlik ve hizmetin işleyişi için ziyaretçilerin IP adresi gibi teknik kayıtları tutabilir. Fontlar ve görseller bu sitenin kendi sunucusundan yüklenir; üçüncü taraf bir font ya da reklam servisi kullanılmaz.</p>
        <h2 class="svc-h">Benimle iletişime geçtiğinizde</h2>
        <p>WhatsApp, telefon ya da e-postayla paylaştığınız bilgileri yalnız talebinizi yanıtlamak ve teklif hazırlamak için kullanırım; üçüncü kişilerle paylaşmam.</p>
        <h2 class="svc-h">Haklarınız</h2>
        <p>6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında bilgilerinize erişmek, düzeltilmesini ya da silinmesini istemek için <a href="mailto:{EMAIL}">{EMAIL}</a> adresine yazabilirsiniz.</p>
        <p class="muted">Son güncelleme: 27 Ekim 2026</p>
      </div>
    </section>'''

NOT_FOUND = '''    <section class="wrap">
      <div class="page-head">
        <span class="eyebrow">404</span>
        <h1>Bu sayfa bulunamadı</h1>
        <p>Adres değişmiş ya da yanlış yazılmış olabilir.</p>
        <p style="margin-top:1.5rem"><a href="/" class="btn btn-primary">Ana sayfaya dönün</a></p>
      </div>
    </section>'''

PAGES = {
    'index.html': page('/', 'Yusuf Demir | Freelance Yazılımcı · Türkiye, İstanbul, Kocaeli',
                       "Freelance bilgisayar mühendisi: kurumsal web sitesi, e-ticaret, mobil uygulama ve işletmeye özel yönetim sistemleri. Türkiye'nin her yerine çevrim içi, Marmara Bölgesi'nde istenirse yüz yüze.",
                       HOME, hand_font=True),
    'projeler/index.html': page('/projeler/', 'Projeler | Yusuf Demir · Freelance Yazılımcı',
                                "Kremi Beauty mobil alışveriş uygulaması, bir üreticinin imalat ve satış yönetim sistemi ve UBEI telefon aksesuarı e-ticaret sitesi.",
                                PROJECTS, 'Projeler', [PROJECTS_LD]),
    'hizmetler/index.html': page('/hizmetler/', 'Hizmetler | Freelance Web, Mobil ve Yönetim Sistemi · Yusuf Demir',
                                 "Kurumsal web sitesi, e-ticaret, mobil uygulama, işletmeye özel yönetim sistemi, süreç otomasyonu ve site onarımı. Türkiye'nin her yerine çevrim içi; Kocaeli, İstanbul ve Marmara'da yüz yüze.",
                                 SERVICES_HTML, 'Hizmetler', [FAQ_LD]),
    'cozumler/index.html': page('/cozumler/', 'Çözümler | İşletmeler Müşteriyi Nerede Kaçırıyor? · Yusuf Demir',
                                "Telefonda yavaş açılan siteler, mobil uygulama eksikliği ve defterle Excel arasında kaybolan siparişler: üç yaygın sorun ve çözümleri.",
                                SOLUTIONS, 'Çözümler'),
    'iletisim/index.html': page('/iletisim/', 'İletişim | Yusuf Demir · Freelance Yazılımcı',
                                f"Yusuf Demir ile 15 dakikalık ücretsiz ön görüşme. Telefon ve WhatsApp: {PHONE_TEXT}. Türkiye'nin her yerine çevrim içi; Marmara'da istenirse yüz yüze.",
                                CONTACT, 'İletişim'),
    'site-kontrolu/index.html': page('/site-kontrolu/', 'Ücretsiz Site Kontrolü | Yusuf Demir · Freelance Yazılımcı',
                                     "Sitenizin bağlantısını gönderin; mobil görünüm, hız, çalışmayan düğmeler, SSL ve Google görünürlüğü için ücretsiz ve bağlayıcı olmayan bir değerlendirme alın.",
                                     SITE_CHECK, 'Ücretsiz site kontrolü'),
    'gizlilik/index.html': page('/gizlilik/', 'Gizlilik | Yusuf Demir', 'Bu sitede hangi bilgilerin nerede işlendiği: çerezsiz ziyaret istatistikleri, barındırma ve iletişim.',
                                PRIVACY, 'Gizlilik'),
    '404.html': page('/404.html', 'Sayfa bulunamadı | Yusuf Demir', 'Aradığınız sayfa bulunamadı.', NOT_FOUND, noindex=True),
}
for d in DETAIL_PAGES:
    PAGES[d["path"].strip('/') + '/index.html'] = page(d["path"], d["title"], d["desc"], detail_page(d), d["crumb"],
                                                      detail_ld(d), parents=[d["parent"]])

for rel, html in PAGES.items():
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

# Site haritası: 404 dışındaki bütün sayfalar
from datetime import date
urls = ['/' if r == 'index.html' else '/' + r[:-len('index.html')] for r in PAGES if r != '404.html']
with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    f.write(''.join(f'  <url><loc>{SITE}{u}</loc><lastmod>{date.today().isoformat()}</lastmod></url>\n' for u in urls))
    f.write('</urlset>\n')
print('yazıldı:', ', '.join(PAGES))
