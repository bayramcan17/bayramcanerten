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

## İçerik düzenleme

Sitedeki tüm metinler ve linkler `core/content.py` dosyasındadır. Şablonlarda sabit metin yoktur.

## Ortam değişkenleri

| Değişken | Açıklama |
|---|---|
| `SECRET_KEY` | Üretimde zorunlu. Vercel → Settings → Environment Variables |
| `DEBUG` | `True` yalnızca yerelde. Varsayılan `False` |

## Yayın

`main` dalına her push'ta Vercel otomatik olarak yayınlar. Diğer dallar önizleme (preview) adresi alır.
