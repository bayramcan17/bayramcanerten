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
