# bayramcanerten.com — Uygulama Planı (Claude Code için)

> **Bu dosyayı nasıl kullanmalı:** Proje klasörünün köküne `PLAN.md` olarak koy ve Claude Code'a şunu söyle:
> *"PLAN.md dosyasını baştan sona oku, kurallara uy ve Faz 0'dan başla."*

---

## 0. Claude Code için çalışma kuralları

1. **Faz faz ilerle.** Her fazın sonunda dur. Ne yaptığını 3–5 maddeyle özetle, "Kabul kriterleri"ni tek tek işaretle ve bir sonraki faza geçmek için kullanıcıdan onay al.
2. **🛑 DANIŞ işaretli noktalarda karar verme, sor.** Soruyu her zaman aşağıdaki biçimde sor, sonra cevap bekle:
   ```
   🛑 KARAR: <konu>
   A) ... — artısı / eksisi
   B) ... — artısı / eksisi
   C) ... — artısı / eksisi
   Önerim: X, çünkü ...
   ```
3. **Planın dışına bir teknoloji eklemek gerekirse** (yeni kütüphane, servis, build adımı) önce aynı biçimde seçenek sun. Django + Vercel dışına çıkmak kullanıcı onayı gerektirir.
4. **Bilgi uydurma.** Link, metin, tarih, logo gibi eksik bir şey varsa `TODO:` yer tutucusu koy, `TODO.md` dosyasına ekle ve faz sonunda kullanıcıya liste halinde sor.
5. **Basit tut.** Veritabanı yok, kullanıcı girişi yok, admin paneli yok. Site tek sayfa ve birkaç yardımcı dosyadan ibaret.
6. **Gizli bilgi commit etme.** `SECRET_KEY` gibi değerler ortam değişkeninden okunur; `.env*` dosyaları `.gitignore`'da olur.
7. **Kullanıcının yapması gereken işleri açıkça söyle.** GoDaddy ve Vercel hesaplarına Claude Code giriş yapamaz. Bu adımları numaralı, tıklanacak menü adlarıyla birlikte kullanıcıya ver.
8. Kod, değişken ve commit mesajları İngilizce; sitedeki metinler Türkçe (Faz 0'daki dil kararına göre).

---

## 1. Proje özeti

**Amaç:** Az içerikli, sade, hızlı, bakımı kolay bir kişisel kartvizit sitesi.

**Kişi:** Bayram Can Erten *(yazımı Faz 0'da doğrulanacak)*
- Bilgisayar Mühendisi
- Çanakkale Onsekiz Mart Üniversitesi mezunu
- Uzun bir "hakkımda" metni **olmayacak**. Kullanıcı kendini uzun uzun tanıtmak istemiyor.

**İçerik:**

| Bölüm | İçerik |
|---|---|
| Giriş (hero) | Ad soyad, "Bilgisayar Mühendisi", "Çanakkale Onsekiz Mart Üniversitesi" (küçük satır), GitHub ve Instagram ikonları |
| Projeler | **Tenis Asistanı**: tenis ekipmanlarını ve maçları takip eden uygulama. Rozetler: *Web* (kendi sitesine link), *App Store* (mağaza linki), *Google Play — Yakında*. <br>**otel-panel**: Assos Kadırga Otel için geliştirilmiş, canlıda aktif olarak kullanılan otel yönetim paneli. Rozet: *Canlıda · Dahili kullanım*. Dışarıya açık bir linki **yok**. |
| İşletmelerimiz | **Assos Kadırga Otel**: Behram, Ayvacık/Çanakkale; 1979'dan beri. Web: `https://assoskadirgaotel.com`, Instagram: `@assoskadirgaotel` *(kullanıcı doğrulayacak)*. <br>**Erten Yapı Market**: Ayvacık/Çanakkale. Link: `TODO` (web sitesi bulunamadı; Google Maps / Instagram linki kullanıcıdan alınacak). *Not: İstanbul'daki "ERT Yapı Market" farklı bir firma, onunla karıştırma.* |
| Alt bilgi | © yıl · ad soyad · sosyal ikonlar |

**Teknoloji:** Python + Django, Vercel (Hobby planı).

**Vercel Hobby notları** (Eylül 2026 itibarıyla, Vercel dokümantasyonuna göre):
- Hobby planında **200 proje** hakkı var; bu site bunlardan biri olur.
- Plan kişisel ve **ticari olmayan** kullanım içindir. Portfolyo sitesi olarak uygundur; sitede satış, reklam veya ödeme alma **olmamalı**. İşletmelere yalnızca tanıtım linki verilir.
- Hobby hesabı, GitHub **organizasyonuna** ait repolara bağlanamaz. Repo, kullanıcının **kişisel** GitHub hesabında olmalı.
- Vercel Django'yu sıfır yapılandırmayla destekliyor: `manage.py`'yi bulur, `WSGI_APPLICATION`'dan giriş noktasını okur, `STATIC_ROOT` tanımlıysa `collectstatic`'i kendisi çalıştırır ve statik dosyaları CDN'den sunar. Python varsayılanı 3.12. Kaynak: https://vercel.com/docs/frameworks/full-stack/django

---

## Faz 0 — Kararlar ve malzeme toplama

Kod yazmadan önce aşağıdakileri kullanıcıya sor. Hepsini **tek mesajda**, numaralı olarak sor.

**Bilgi soruları (açık uçlu):**
1. Ad soyadın sitede nasıl yazılsın? ("Bayram Can Erten" doğru mu?)
2. GitHub kullanıcı adı ve Instagram hesabı (kişisel olan).
3. Tenis Asistanı: web sitesinin adresi ve App Store linki. Uygulamanın logosu/ikonu (PNG/SVG) var mı?
4. otel-panel için 1–2 ekran görüntüsü eklensin mi? **Eklenecekse misafir adı, telefon, TC no gibi kişisel veri içermemeli (KVKK).** Gerekirse bulanıklaştırılmış hali kullanılır.
5. Assos Kadırga Otel linkleri doğru mu? Erten Yapı Market için hangi link verilsin (Google Maps, Instagram, Facebook)?
6. İşletme logoları var mı?
7. Sitede fotoğrafın olsun mu? (Varsayılan: hayır. Yerine baş harflerden oluşan bir monogram "BCE" kullanılır.)

**🛑 DANIŞ — Dil**
- A) Sadece Türkçe — en basit *(önerilen)*
- B) Türkçe + İngilizce (Django i18n, `/en/` yolu) — yurt dışından bakanlar için; bakım yükü ikiye katlanır

**🛑 DANIŞ — Barındırma yöntemi**
- A) **Django, Vercel Function olarak çalışır** (sıfır yapılandırma) — en az iş, resmi destekli. Az ziyaret alan sitede ilk açılışta kısa bir "soğuk başlatma" gecikmesi olabilir. *(önerilen)*
- B) **Django ile yazılır, build sırasında statik HTML'e dönüştürülür** (ör. `django-distill`) ve Vercel'e statik site olarak yüklenir — soğuk başlatma yok, en hızlısı; ama build adımı biraz daha karmaşık.
- C) Django'yu bırakıp tamamen statik HTML/CSS — en basiti ama kullanıcı Django istedi.

**🛑 DANIŞ — CSS yaklaşımı**
- A) Elle yazılmış sade CSS (CSS değişkenleri, build adımı yok) *(önerilen)*
- B) Tailwind (standalone CLI ile, build adımı gerektirir)
- C) Pico.css gibi hazır, sınıfsız hafif bir kütüphane

**🛑 DANIŞ — Ziyaretçi istatistikleri**
- A) Hiç yok *(önerilen başlangıç)*
- B) Vercel Web Analytics (Hobby'de aylık 50.000 olay ücretsiz, çerezsiz)
- C) Başka bir araç (Plausible, Google Analytics vb.) — GA çerez bildirimi gerektirir

**🛑 DANIŞ — GitHub reposu**
- A) Public (portfolyonun bir parçası olarak görünür)
- B) Private

**Kabul kriterleri**
- [ ] Tüm kararlar `DECISIONS.md` dosyasına yazıldı
- [ ] Eksik kalan bilgiler `TODO.md`'de listelendi
- [ ] Kullanıcı Faz 1'e geçişi onayladı

---

## Faz 1 — Proje iskeleti

Aşağıdaki yapı Faz 0'da **A) Vercel Function** seçildiği varsayılarak yazıldı. B seçildiyse aynı yapıya statik dışa aktarma adımını ekle.

```
bayramcanerten/
├── manage.py
├── pyproject.toml          # veya requirements.txt
├── .python-version         # 3.12
├── .gitignore
├── README.md
├── PLAN.md  DECISIONS.md  TODO.md
├── config/                 # Django proje paketi
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/                   # tek uygulama
    ├── content.py          # TÜM site içeriği burada (Python dict/list)
    ├── views.py
    ├── urls.py
    ├── tests.py
    ├── templates/core/
    │   ├── base.html
    │   ├── index.html
    │   ├── partials/…      # hero, project_card, business_card, footer
    │   └── 404.html
    └── static/core/
        ├── css/site.css
        ├── img/…
        └── favicon/…
```

**Ayarlar (settings.py):**
- Django'nun güncel **LTS** sürümünü kullan (kurmadan önce güncel sürümü kontrol et, ör. 5.2 LTS).
- `INSTALLED_APPS`: yalnızca `django.contrib.staticfiles` ve `core`. `admin`, `auth`, `sessions`, `contenttypes`, `messages` **yok**.
- `DATABASES = {}` (veritabanı kullanılmıyor). Veritabanı gerektiren middleware ve context processor'ları çıkar.
- `SECRET_KEY` ortam değişkeninden; yoksa yalnızca yerelde kullanılan bir geliştirme anahtarı.
- `DEBUG` ortam değişkeninden, varsayılan `False`.
- `ALLOWED_HOSTS = ["bayramcanerten.com", "www.bayramcanerten.com", ".vercel.app", "localhost", "127.0.0.1"]`
- `STATIC_URL = "/static/"`, `STATIC_ROOT = BASE_DIR / "staticfiles"` (Vercel `collectstatic`'i kendisi çalıştırır).
- `WSGI_APPLICATION = "config.wsgi.application"`
- `LANGUAGE_CODE = "tr"`, `TIME_ZONE = "Europe/Istanbul"`
- Güvenlik: `SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")`, `SECURE_CONTENT_TYPE_NOSNIFF = True`, `X_FRAME_OPTIONS = "DENY"`, `SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"`. HSTS'yi Faz 6'da, domain çalıştıktan sonra aç.
- Yerel geliştirmede statik dosyalar için WhiteNoise kullanılabilir (Vercel ile uyumlu; üretimde statik dosyaları CDN sunar).

**İçerik yönetimi:** Metinlerin ve linklerin hepsi `core/content.py` içinde tutulur. Kullanıcı yeni bir proje eklemek istediğinde yalnızca bu dosyayı düzenler. Şablonlarda sabit metin olmamalı.

**Kabul kriterleri**
- [ ] `python manage.py runserver` ile ana sayfa açılıyor (henüz tasarımsız olabilir)
- [ ] `python manage.py check --deploy` ciddi bir uyarı vermiyor (HSTS hariç)
- [ ] `python manage.py test` geçiyor (ana sayfa 200, olmayan sayfa 404)
- [ ] README'de kurulum ve çalıştırma adımları var
- [ ] İlk commit atıldı

---

## Faz 2 — Tasarım

**🛑 DANIŞ — Görsel yön.** Önce 2–3 yön öner, her biri için ana sayfanın kaba bir önizlemesini hazırla (ekran görüntüsü veya yerel sayfa), kullanıcı seçsin:
- A) **Minimal tipografik**: bol boşluk, tek aksan rengi, büyük isim
- B) **Ege esintili**: deniz mavisi/kum tonları, yumuşak köşeler (Assos'a gönderme)
- C) **Geliştirici havası**: monospace detaylar, koyu tema öncelikli

**Her yönde geçerli olanlar:**
- Mobil öncelikli; 360 px genişlikte yatay kaydırma olmamalı.
- Açık/koyu tema (`prefers-color-scheme`); renkler `:root`'ta CSS değişkeni olarak tanımlanır.
- Sistem fontları veya en fazla bir web fontu (Google Fonts ya da yerelde barındırılan).
- İkonlar satır içi SVG (GitHub, Instagram, App Store, web, harita). Harici ikon kütüphanesi yok.
- Sayfa JavaScript olmadan tam çalışmalı. JS yalnızca küçük süslemeler için, isteğe bağlı.
- Erişilebilirlik: yeterli kontrast, odak halkaları, anlamlı `alt` metinleri, `lang="tr"`.

**Kabul kriterleri**
- [ ] Kullanıcı bir yön seçti ve `DECISIONS.md`'ye yazıldı
- [ ] `base.html` ve CSS temel sistemi (renk, boşluk, tipografi değişkenleri) hazır

---

## Faz 3 — İçerik ve bölümler

1. `content.py`'yi Bölüm 1'deki tabloya göre doldur. Eksik olanlar `TODO` olarak kalsın.
2. Bölümleri şablon parçaları (partial) halinde yaz: hero, projeler, işletmeler, footer.
3. Proje kartı bileşeni: başlık, 1–2 cümle açıklama, rozetler, linkler, isteğe bağlı görsel.
4. Rozetler: "Canlıda", "App Store", "Google Play — Yakında", "Dahili kullanım".
5. Dış linkler `target="_blank" rel="noopener"` ile açılır.
6. Görseller WebP'ye çevrilir, `width`/`height` belirtilir, `loading="lazy"` kullanılır.
7. Özel 404 sayfası (siteyle aynı tasarımda, ana sayfaya dönüş linkiyle).

**🛑 DANIŞ:** Proje ve işletme açıklama metinlerini taslak olarak yaz ve kullanıcıya **tek liste halinde** onaya sun. Onaylanmadan yayına alma.

**Kabul kriterleri**
- [ ] Tüm bölümler mobilde ve masaüstünde düzgün görünüyor (her ikisinin de ekran görüntüsünü al ve kullanıcıya göster)
- [ ] Metinler kullanıcı tarafından onaylandı
- [ ] `TODO.md`'de yalnızca kullanıcının henüz vermediği bilgiler kaldı

---

## Faz 4 — SEO, performans ve son rötuşlar

- `<title>`, `meta description`, canonical link (`https://bayramcanerten.com/`)
- Open Graph ve Twitter kart etiketleri; 1200×630 bir **OG görseli** (isim + unvan, seçilen tasarımla uyumlu)
- Favicon seti (SVG + PNG + apple-touch-icon)
- `robots.txt` ve `sitemap.xml` (basit bir view/template ile)
- JSON-LD `Person` şeması: ad, unvan, `alumniOf` (Çanakkale Onsekiz Mart Üniversitesi), `sameAs` (GitHub, Instagram)
- Lighthouse hedefi: dört kategoride de **95+**. Sonuçları kullanıcıya göster.
- Linklerin hepsinin çalıştığını kontrol et (kırık link olmamalı).

**Kabul kriterleri**
- [ ] Lighthouse raporu hedefe ulaştı
- [ ] OG önizlemesi doğru görünüyor
- [ ] Testler geçiyor

---

## Faz 5 — GitHub ve Vercel'e yayın

**Kullanıcının yapacakları (Claude Code adım adım anlatır):**
1. Kişisel GitHub hesabında repo oluşturmak (Faz 0'daki public/private kararına göre) ya da Claude Code'un `gh` ile oluşturmasına izin vermek.
2. vercel.com'da Hobby hesabı açmak (yoksa) ve GitHub ile bağlamak.
3. Vercel'de **Add New → Project → repo'yu seç → Deploy**.
4. **Settings → Environment Variables**'a `SECRET_KEY` (Claude Code güçlü bir değer üretip verir) ve `DEBUG=False` eklemek.

**Claude Code'un yapacakları:**
- Push öncesi son kontroller (testler, `check --deploy`, `.gitignore`).
- Alternatif olarak kullanıcı `vercel login` yaparsa, Vercel CLI (`vercel`, `vercel deploy`) ile yayın. Vercel dokümanı Django için **CLI 50.38.0 veya üzeri** gerektiğini belirtiyor.
- Yayın sonrası `*.vercel.app` adresini kontrol etmek: ana sayfa, statik dosyalar, 404, `robots.txt`, `sitemap.xml`.

**Kabul kriterleri**
- [ ] `https://<proje>.vercel.app` sorunsuz açılıyor
- [ ] `main` dalına her push'ta otomatik yayın çalışıyor

---

## Faz 6 — Domain bağlama (GoDaddy → Vercel)

**🛑 DANIŞ — DNS yönetimi**
- A) **DNS GoDaddy'de kalır**, yalnızca Vercel'in istediği kayıtlar eklenir *(önerilen: en az değişiklik, e-posta kayıtları da GoDaddy'de kalır)*
- B) Nameserver'lar Vercel'e taşınır (DNS'i Vercel yönetir)

**🛑 DANIŞ — Ana adres**
- A) `bayramcanerten.com` ana adres, `www` buraya yönlenir *(önerilen)*
- B) `www.bayramcanerten.com` ana adres

**Adımlar (A/A seçildiyse):**
1. Vercel → Proje → **Settings → Domains** → `bayramcanerten.com` ve `www.bayramcanerten.com` ekle, www için yönlendirmeyi seç.
2. Vercel'in **o anda gösterdiği** DNS kayıtlarını not et (genellikle kök domain için bir `A` kaydı, `www` için bir `CNAME`). **Değerleri ezberden yazma, Vercel ekranında ne yazıyorsa onu kullan.**
3. GoDaddy → **Domain Portfolio → bayramcanerten.com → DNS**:
   - GoDaddy'nin varsayılan **"Parked"** `A` kaydını ve varsa `www` CNAME'ini sil/düzenle.
   - Domain **Forwarding** açıksa kapat.
   - Vercel'in verdiği kayıtları ekle.
4. Yayılmayı `dig bayramcanerten.com +short` ve `dig www.bayramcanerten.com +short` ile kontrol et. Vercel ekranında domain "Valid Configuration" olana kadar bekle (dakikalar–birkaç saat).
5. SSL sertifikası Vercel tarafından otomatik verilir; `https://` ile açıldığını doğrula.
6. Her şey çalıştıktan sonra settings'e HSTS ekle (`SECURE_HSTS_SECONDS`, önce kısa bir süreyle başla) ve yeniden yayınla.

**Kabul kriterleri**
- [ ] `https://bayramcanerten.com` açılıyor, geçerli sertifika var
- [ ] `www` ve `http` istekleri ana adrese yönleniyor

---

## Faz 7 (isteğe bağlı) — Kişisel e-posta adresi

Kullanıcı isterse `bayram@bayramcanerten.com` gibi bir adres kurulur.

**🛑 DANIŞ — E-posta çözümü** (her birinin güncel fiyat/koşullarını kontrol edip öyle sun):
- A) **Ücretsiz yönlendirme servisi** (ör. ImprovMX): gelen postalar mevcut Gmail'e iletilir; GoDaddy DNS'ine birkaç MX/TXT kaydı eklenir. Gönderim için ek ayar gerekir.
- B) **Cloudflare Email Routing**: ücretsiz yönlendirme; ancak DNS'in Cloudflare'e taşınmasını gerektirir (Faz 6 kararını değiştirir).
- C) **Tam posta kutusu** (Google Workspace, Zoho Mail vb.): gönderme ve alma tam çalışır; çoğunlukla ücretlidir.
- D) Şimdilik e-posta yok; iletişim yalnızca sosyal hesaplar üzerinden.

Hangi seçenek seçilirse seçilsin: MX kayıtları Vercel'in A/CNAME kayıtlarıyla çakışmaz. SPF/DKIM/DMARC kayıtlarını da eklemeyi unutma.

---

## Faz 8 — Teslim ve bakım

- `README.md`'ye ekle:
  - Yerelde çalıştırma
  - **Yeni proje ekleme**: `content.py`'de hangi alan nasıl doldurulur (örnekle)
  - Görsel ekleme (hangi klasör, hangi boyut, WebP'ye çevirme)
  - Yayın akışı (push → otomatik deploy)
  - Google Play yayınlanınca Tenis Asistanı rozetinin nasıl güncelleneceği
- `TODO.md`'de kalan maddeleri kullanıcıyla birlikte gözden geçir.

**İleride eklenebilecekler (şimdi yapılmayacak):** blog/notlar sayfası, İngilizce sürüm, Tenis Asistanı için ayrı tanıtım sayfası, "şu an ne yapıyorum" (/now) sayfası.

---

## Genel "bitti" tanımı

- [ ] `https://bayramcanerten.com` mobilde ve masaüstünde düzgün, hızlı açılıyor
- [ ] Tüm linkler çalışıyor, uydurma bilgi yok
- [ ] Kişisel veri içeren ekran görüntüsü yok
- [ ] İçerik tek dosyadan (`content.py`) güncellenebiliyor
- [ ] Aylık maliyet: yalnızca domain yenilemesi (Vercel Hobby ücretsiz)
