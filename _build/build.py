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
    ("Ajans yerine freelance bir mühendisle çalışmanın farkı ne?",
     "Teklifi veren, kodu yazan ve sonradan destek veren aynı kişi. İstekleriniz aracıdan aracıya aktarılırken "
     "değişmez, bir değişiklik istediğinizde doğrudan işi yapanla konuşursunuz."),
]
FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}


def ld(obj):
    return '  <script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>\n'


def crumb(name, path):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}


ICON_MENU = '<svg class="icon-open" width="24" height="24" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" stroke-width="2.25" stroke-linecap="square"/></svg>'
ICON_CLOSE = '<svg class="icon-close" width="24" height="24" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19" stroke="currentColor" stroke-width="2.25" stroke-linecap="square"/></svg>'


def page(path, title, desc, main, crumb_name=None, extra_ld=(), noindex=False, hand_font=False):
    items = ''.join(
        f'<li><a href="{h}" class="nav-link"{" aria-current=\"page\"" if h == path else ""}>{t}</a></li>'
        for h, t in NAV)
    fonts = 'family=Instrument+Sans:wght@400;600;700&family=JetBrains+Mono:wght@500;700'
    if hand_font:
        fonts += '&family=Caveat:wght@500;700'
    head_meta = '  <meta name="robots" content="noindex" />\n' if noindex else f'  <link rel="canonical" href="{SITE + path}" />\n'
    lds = '' if noindex else ld(BASE_LD) + (ld(crumb(crumb_name, path)) if crumb_name else '') + ''.join(ld(x) for x in extra_ld)
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
  <meta property="og:image" content="{SITE}/assets/images/logo-yd.png" />
  <meta name="geo.region" content="TR-41" />
  <meta name="geo.placename" content="İzmit, Kocaeli" />
  <link rel="alternate" type="text/plain" href="/llms.txt" title="LLM özeti" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap" />
  <link rel="stylesheet" href="/assets/css/site.css" />
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
      </div>
    </div>
  </footer>

  <script src="/assets/js/site.js" defer></script>
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
          <div class="char" aria-hidden="true"></div>
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
    ("Kurumsal web sitesi", "İşletmenizin kimliğine ve isteklerine göre tasarlanan, telefonda hızlı açılan, Google'da bulunan modern bir site."),
    ("E-ticaret ve ürün kataloğu", "Ürün kataloğu, filtreler, sepet ve sipariş adımıyla satışa hazır modern bir e-ticaret sitesi. Son işim: ubei.com.tr."),
    ("Mobil uygulama", "Flutter ile iOS ve Android uygulaması. App Store ve Google Play başvurusu dahil."),
    ("İşletmeye özel yönetim sistemi", "Sipariş, stok, üretim, sevkiyat ve tahsilatı tek ekranda toplayan, yetkiye göre çalışan sistem."),
    ("Süreç otomasyonu", "Excel'le ve kâğıtla yürüyen işleri otomatiğe bağlarım: Telegram/WhatsApp bildirimleri, PDF fiş ve raporlar."),
    ("Site onarımı ve hız", "Mobilde bozuk görünen, formu çalışmayan, SSL hatası veren ya da yavaş açılan siteleri onarırım."),
]
SERVICES_HTML = f'''    <section class="wrap">
      <div class="page-head">
        <p class="breadcrumb"><a href="/">Ana sayfa</a> / Hizmetler</p>
        <span class="eyebrow">Tüm Türkiye · Çevrim içi</span>
        <h1>Hizmetler</h1>
        <p>Türkiye'nin her yerindeki işletmelerle çevrim içi çalışıyorum. Marmara Bölgesi'ndeyseniz isterseniz yüz yüze de görüşebiliriz. Her işi aracı olmadan, baştan sona kendim geliştiriyorum.</p>
      </div>
      <div class="panel">
        <div class="card-grid">{''.join(f"""
          <div class="card"><h2 style="font-size:1.25rem;color:var(--ink);line-height:1.25">{t}</h2><p>{d}</p></div>""" for t, d in SERVICE_CARDS)}
        </div>
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
        </div>
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
    '404.html': page('/404.html', 'Sayfa bulunamadı | Yusuf Demir', 'Aradığınız sayfa bulunamadı.', NOT_FOUND, noindex=True),
}

for rel, html in PAGES.items():
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
print('yazıldı:', ', '.join(PAGES))
