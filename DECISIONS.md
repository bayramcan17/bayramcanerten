# Kararlar

## Faz 0 — 2026-09-26

| Konu | Karar | Not |
|---|---|---|
| Site dili | **A) Sadece Türkçe** | İngilizce ileride eklenebilir |
| Barındırma | **A) Django, Vercel Function olarak** | Sıfır yapılandırma; soğuk başlatma sorun olursa B'ye (statik dışa aktarma) geçilebilir |
| CSS | **A) Elle yazılmış sade CSS** | CSS değişkenleri, build adımı yok |
| İstatistik | **A) Yok** | Gerekirse Vercel Web Analytics sonradan eklenir |
| GitHub reposu | **A) Public** | Kişisel hesap: `bayramcan17` |
| Fotoğraf | **Yok** | Yerine şık bir "BCE" monogram/logo tasarlanacak |

## Doğrulanan bilgiler

- Ad soyad: **Bayram Can Erten**
- GitHub: https://github.com/bayramcan17
- Instagram: https://instagram.com/bayramcanerten
- Tenis Asistanı web: https://tenisasistani.com
- Tenis Asistanı App Store: https://apps.apple.com/us/app/tenis-asistan%C4%B1/id6791199819
- Tenis Asistanı logosu: `~/Desktop/TennisAssistantWeb/static/img/icon-512.png` (iOS: `AppIcon.appiconset/icon-1024.png`)
- Assos Kadırga Otel web: https://assoskadirgaotel.com — Instagram: `@assoskadirgaotel` (kullanıcı doğruladı)
- Assos Kadırga Otel logosu: `~/Desktop/otel-panel/public/logo.png`
- Erten Yapı Market: Google Maps — https://share.google/aZjqFMAuBJ10gNIUq
- otel-panel ekran görüntüleri: eklenecek (kullanıcıya göre yalnızca sayısal veri içeriyor; yine de yayından önce kişisel veri kontrolü yapılacak)

## Faz 1 — 2026-09-26

- Django **5.2 LTS** (6.1 güncel sürüm ama LTS değil). Bağımlılık yalnızca `requirements.txt`'teki Django.
- WhiteNoise eklenmedi: yerelde `DEBUG=True` ile Django statik dosyaları kendisi sunuyor, üretimde Vercel CDN sunuyor.
- CSRF middleware yok (formsuz, çerezsiz site); `security.W003` gerekçesiyle susturuldu.
- `SECURE_SSL_REDIRECT = not DEBUG`. HSTS Faz 6'da açılacak.
- otel-panel ekran görüntülerinde tutarlar, firma adları, açıklamalar ve panel adresi gizlendi.

## Faz 2 — 2026-09-26

- Görsel yön: **B) Ege esintili**. Deniz mavisi (`#24557a`, otel logosundaki ton) ve kum tonları, yumuşak köşeler, hero altında dalga motifi.
- Monogram: "BCE" harfleri, deniz mavisi daire içinde iki dalga çizgisiyle (satır içi SVG).
- Font: başlıklarda tek web fontu **Fraunces** (Google Fonts), gövde metni sistem fontu.
- Açık/koyu tema `prefers-color-scheme` ile; renkler `:root`'ta CSS değişkeni. Logolar koyu temada da açık renkli bir zeminde durur.
- İkonlar satır içi SVG (`core/templates/core/partials/icon.html`). Sayfada JavaScript yok.

## Faz 3 — 2026-09-26

- Metinler onaylandı. Kaynaklar: Tenis Asistanı kendi sitesi, otel bilgisi kullanıcı + assoskadirgaotel.com, otel-panel özellikleri ekran görüntüleri.
- Kullanıcı metin/içerik ifadelerinde karar yetkisini verdi; bundan sonra metin taslakları için ayrıca onay istenmeyecek (yalnızca verilen bilgilere dayanılacak).

## Faz 4 — 2026-09-26

- SEO: title, description, canonical, Open Graph + Twitter kartı, JSON-LD `Person`, `robots.txt`, `sitemap.xml`. 404 sayfası `noindex`.
- OG görseli `core/img/og.jpg` (1200×630, JPEG ~46 KB). Favicon seti: SVG, 32 px PNG, `.ico`, apple-touch-icon, 192/512 manifest ikonları. `/favicon.ico` statik dosyaya yönlenir.
- Performans: Google Fonts stili render'ı bloklamadan yüklenir (`media="print"` + `onload`, JS kapalıysa `<noscript>`). otel-panel ekran görüntülerinin 800 px küçük sürümleri `srcset` ile sunulur.
- Lighthouse (yerel, üretim ayarları): mobil ve masaüstü 100/100/100/100. Metin sıkıştırma ve uzun önbellek uyarıları yerel sunucudan; Vercel'de doğrulanacak (Faz 5).
- Google Fonts yerine fontu kendi sunucumuzda barındırmak ileride düşünülebilir (gizlilik: ziyaretçi IP'si Google'a gitmez).

## Faz 5 — 2026-09-26

- Vercel projesi: `bayramcanerten` (hesap: bayramcan17s-projects), Vercel CLI 54.21 ile yayınlandı. Adres: https://bayramcanerten.vercel.app
- `SECRET_KEY` Vercel'de Production ve Preview için ayrı ayrı, "sensitive" olarak üretildi; hiçbir dosyada yok. `DEBUG` tanımlı değil (varsayılan `False`).
- Canlıda: brotli sıkıştırma açık, güvenlik başlıkları geliyor, http → https yönlendirmesi çalışıyor. Lighthouse (canlı): mobil ve masaüstü 100/100/100/100.
- Statik dosyalar `max-age=0, must-revalidate` ile sunuluyor (Vercel varsayılanı). Dosya adları hash'li olmadığı için uzun önbellek bilerek açılmadı.
- GitHub: https://github.com/bayramcan17/bayramcanerten (public), Vercel projesine bağlı; `main`'e her push production'a otomatik yayın (doğrulandı: 14bf9a7).
- Fonksiyon bölgesi `vercel.json` ile **fra1 (Frankfurt)**; varsayılan iad1 (ABD) Türkiye'ye uzaktı.
- Not: `~/.config` klasörü root'a aitti; `gh` giriş bilgisini yazamıyordu. Kullanıcı `sudo chown` ile düzeltti.

## Faz 6 — 2026-09-26

- DNS: **A) GoDaddy'de kalır**. Ana adres: **A) bayramcanerten.com**, `www` → 308 ile ana adrese.
- GoDaddy kayıtları: `A @ 216.198.79.1`, `CNAME www 26626799dda9cd4c.vercel-dns-017.com` (Vercel API'nin önerdiği değerler). Park sayfası A kaydı kaldırıldı. `_dmarc` ve `_domainconnect` GoDaddy varsayılanı olarak duruyor.
- SSL: Let's Encrypt, Vercel otomatik yeniliyor.
- HSTS: Vercel özel domainde zaten `max-age=63072000` gönderiyor; Django'da aynı değer. `includeSubDomains` ve `preload` yok.

## Faz 7 — atlandı

- Kişisel e-posta şimdilik kurulmadı (kullanıcı kararı). Kurulursa DNS GoDaddy'de olduğu için MX/TXT kayıtları oraya eklenir.

## Faz 8 — 2026-09-26

- README bakım kılavuzu: yerelde çalıştırma, proje/işletme ekleme (örnekli), görsel ekleme (boyutlar, WebP, KVKK), yayın akışı, Google Play rozeti güncelleme, DNS kayıtları.
- Yeni rozet türü `googleplay` (linkli rozetlerle aynı görünüm) Google Play yayınlanınca kullanılacak.

## Animasyonlar ve modern teknikler — 2026-09-30

Kullanıcı isteği: site "tek düze", daha canlı ve güncel teknikler. Harici kütüphane **eklenmedi**; yalnızca tarayıcıların yerleşik özellikleri:

- **Scroll-driven animations** (`animation-timeline: scroll()/view()`): kartların belirmesi, başlık çizgisi, teknoloji etiketleri, üstte ilerleme çubuğu, menünün cama dönüşmesi, hero'nun kaydırınca batması. Desteklemeyen tarayıcıda içerik olduğu gibi görünür.
- **View Transitions API**: tema değişiminde düğmeden yayılan daire; ekran görüntüsünün büyüyerek pencereye dönüşmesi.
- **`light-dark()` + `color-scheme`**: tüm renkler tek tanımda; tema düğmesi yalnızca `color-scheme`'i değiştirir. Seçim `localStorage`'da (kişisel tercih).
- **`@property`**: isim üzerinde gezen ışık parlaması. **`@starting-style`** + `<dialog>`: pencere açılış animasyonu.
- Diğer: hareketli dalgalar (SVG, `translate`), su üstünde parıltılar, güneş/ay, imleci takip eden ışık ve kartlarda hafif 3B eğim (yalnızca fareli cihazlarda), `text-wrap: balance/pretty`, `color-mix()`.
- Proje kartlarına **teknoloji etiketleri** eklendi (projelerin kendi kodundan doğrulandı).
- Erişilebilirlik: tüm hareketler `prefers-reduced-motion: no-preference` içinde; JS kapalıyken site eksiksiz (tema düğmesi gizli kalır, ekran görüntüsü linki yeni sekmede açılır).
- `@view-transition { navigation: auto }` denendi ve **kaldırıldı**: Chrome'da ilk boyamayı geciktirip mobil Lighthouse performansını 87'ye düşürüyordu; sitede tek sayfa geçişi (404 → ana sayfa) olduğu için değmez.
- Hero girişi opacity 0'dan başlamaz (monogram küçükten büyür, isim bulanıktan netleşir); aksi halde en büyük öğe (LCP) geç sayılıyordu.
- Lighthouse (yerel, üretim ayarları): mobil ve masaüstü 100/100/100/100, CLS 0.
