# bayramcanerten.com

Kişisel kartvizit sitesi. Django 5.2 LTS; Vercel'de (Hobby) Vercel Function olarak çalışır. Veritabanı yoktur.

Canlı: https://bayramcanerten.com

## Kurulum

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Yerelde çalıştırma

```bash
DEBUG=True python manage.py runserver
```

Tarayıcıda http://127.0.0.1:8000 adresini aç. `DEBUG` ayarlanmazsa site üretim modunda çalışır ve HTTPS'e yönlendirir.

## Test

```bash
python manage.py test
python manage.py check --deploy
```

Testler; ana sayfayı, 404'ü, SEO etiketlerini, `robots.txt`/`sitemap.xml`'i ve `content.py`'de adı geçen **her görselin gerçekten var olduğunu** kontrol eder. Bir görsel eklerken yolu yanlış yazarsan test bunu yakalar.

## İçerik düzenleme

Sitedeki **tüm** metinler ve linkler `core/content.py` dosyasındadır. Şablonlarda sabit metin yoktur; çoğu değişiklik için yalnızca bu dosyayı düzenlemek yeterlidir.

### Yeni proje ekleme

`SITE["projects"]` listesine yeni bir sözlük ekle. Sıra, sitedeki sırayı belirler.

```python
{
    "name": "Proje Adı",
    "summary": "1–2 cümlelik açıklama.",
    # Logo yoksa: "logo": None,
    "logo": {"src": "core/img/proje-adi.webp", "width": 168, "height": 168},
    "badges": [
        {"kind": "web", "icon": "web", "label": "Web", "url": "https://..."},
        {"kind": "appstore", "icon": "appstore", "label": "App Store", "url": "https://apps.apple.com/..."},
        {"kind": "soon", "icon": "play", "label": "Google Play — Yakında", "url": None},
        {"kind": "live", "icon": "live", "label": "Canlıda", "url": None},
    ],
    # Ekran görüntüsü yoksa: "screenshots": [],
    "screenshots": [
        {
            "src": "core/img/proje-adi-1.webp",        # tam boy (tıklanınca açılır)
            "thumb": "core/img/proje-adi-1-800.webp",  # 800 px genişlik (kartta görünen)
            "width": 1600,   # tam boy görselin gerçek genişliği
            "height": 1000,  # tam boy görselin gerçek yüksekliği
            "alt": "Görselde ne olduğunu anlatan kısa cümle",
        },
    ],
},
```

**Alanlar**

| Alan | Açıklama |
|---|---|
| `name` | Kart başlığı |
| `summary` | Kısa açıklama |
| `logo` | Kare logo; kartta 56 px görünür. `None` ise logo alanı hiç çıkmaz |
| `badges` | Rozetler. `url` varsa tıklanabilir (mavi dolgulu), `None` ise düz etiket |
| `screenshots` | İsteğe bağlı ekran görüntüleri; masaüstünde yan yana 2 sütun |

**Rozet türleri (`kind`)**: `web`, `appstore`, `googleplay` → linkli rozetler (aynı görünüm) · `soon` → kesik çizgili, soluk ("Yakında") · `live` → yeşil noktalı ("Canlıda").

**İkonlar (`icon`)**: `web`, `appstore`, `play`, `live`, `github`, `instagram`, `map`, `store`. Yeni ikon gerekirse `core/templates/core/partials/icon.html` dosyasına eklenir.

### Yeni işletme ekleme

`SITE["businesses"]` listesine ekle:

```python
{
    "name": "İşletme Adı",
    "summary": "Kısa açıklama.",
    # Logo varsa "icon": None; yoksa "logo": None ve bir ikon (ör. "store")
    "logo": {"src": "core/img/isletme.webp", "width": 480, "height": 268},
    "icon": None,
    "links": [
        {"label": "Web", "icon": "web", "url": "https://..."},
        {"label": "Instagram", "icon": "instagram", "url": "https://instagram.com/..."},
        {"label": "Haritada gör", "icon": "map", "url": "https://maps.google.com/..."},
    ],
},
```

### Google Play yayınlanınca (Tenis Asistanı)

`core/content.py` içinde Tenis Asistanı'nın rozetlerinde şu satırı:

```python
{"kind": "soon", "icon": "play", "label": "Google Play — Yakında", "url": None},
```

şununla değiştir (linki Play Console'daki mağaza adresinden al):

```python
{"kind": "googleplay", "icon": "play", "label": "Google Play", "url": "https://play.google.com/store/apps/details?id=..."},
```

Commit + push; site birkaç saniye içinde güncellenir.

## Görsel ekleme

- **Klasör:** `core/static/core/img/`
- **Biçim:** WebP (paylaşım görseli `og.jpg` hariç). Dosya adı küçük harf, Türkçe karakter ve boşluk yok: `proje-adi.webp`.
- **Boyutlar:**

| Görsel | Önerilen boyut |
|---|---|
| Proje logosu (kare) | 168 × 168 px |
| İşletme logosu | En fazla 480 px genişlik, **şeffaf arka plan** (koyu temada açık zeminde durur) |
| Ekran görüntüsü, tam boy | Olduğu gibi (≈1600–2000 px genişlik) |
| Ekran görüntüsü, küçük (`thumb`) | 800 px genişlik |

- **WebP'ye çevirme:** Kurulum gerektirmeyen en kolay yol https://squoosh.app — görseli sürükle, sağda **WebP** seç, gerekirse **Resize** ile genişliği ayarla, indir. Kalite 80 civarı yeterli.
- **Kişisel veri:** Ekran görüntülerinde müşteri/personel adı, telefon, TC no, tutar gibi bilgiler bulanıklaştırılmalı (KVKK). Tarayıcı adres çubuğu ve dahili panel adresleri kırpılmalı.
- `width`/`height` değerlerini görselin **gerçek** piksel boyutlarıyla yaz (Finder'da görsel → Bilgi Al). Sayfa yüklenirken kaymayı bu değerler önler.

## Yayın

`main` dalına her push'ta Vercel otomatik olarak **production**'a yayınlar (~20 sn). Diğer dallar önizleme (preview) adresi alır.

```bash
python manage.py test   # önce testler
git add -A
git commit -m "Add new project"
git push
```

- Vercel projesi: `bayramcanerten` (bayramcan17s-projects), bölge: Frankfurt (`vercel.json`).
- Domain: GoDaddy'de kayıtlı; DNS GoDaddy'de. Kayıtlar: `A @ 216.198.79.1`, `CNAME www 26626799dda9cd4c.vercel-dns-017.com`. SSL'i Vercel otomatik yeniler.

## Ortam değişkenleri

| Değişken | Açıklama |
|---|---|
| `SECRET_KEY` | Üretimde zorunlu. Vercel → Project → Settings → Environment Variables (Production ve Preview'da tanımlı) |
| `DEBUG` | `True` yalnızca yerelde. Varsayılan `False` |

## Proje yapısı

```
config/            Django ayarları, URL kökü, WSGI
core/content.py    TÜM site içeriği
core/templates/    base, index, 404 ve bölüm parçaları (partials/)
core/static/core/  css/site.css, img/, favicon/
DECISIONS.md       Alınan kararlar ve gerekçeleri
PLAN.md            İlk uygulama planı
```
