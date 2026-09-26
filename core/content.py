"""All site content lives here. Edit this file to change text or links.

Badge kinds: "live", "web", "appstore", "soon", "internal".
"""

SITE = {
    "name": "Bayram Can Erten",
    "title": "Bilgisayar Mühendisi",
    "school": "Çanakkale Onsekiz Mart Üniversitesi",
    "monogram": "BCE",
    "url": "https://bayramcanerten.com/",
    "description": (
        "Bayram Can Erten — Bilgisayar Mühendisi. "
        "Projeler ve işletmeler."
    ),
    "socials": [
        {
            "label": "GitHub",
            "icon": "github",
            "url": "https://github.com/bayramcan17",
        },
        {
            "label": "Instagram",
            "icon": "instagram",
            "url": "https://instagram.com/bayramcanerten",
        },
    ],
    "sections": {
        "projects": "Projeler",
        "businesses": "İşletmelerimiz",
    },
    "projects": [
        {
            "name": "Tenis Asistanı",
            "summary": (
                "Tenis ekipmanlarını ve maçları takip eden uygulama."
            ),
            "logo": "core/img/tenis-asistani.webp",
            "badges": [
                {"kind": "web", "label": "Web", "url": "https://tenisasistani.com"},
                {
                    "kind": "appstore",
                    "label": "App Store",
                    "url": "https://apps.apple.com/us/app/tenis-asistan%C4%B1/id6791199819",
                },
                {"kind": "soon", "label": "Google Play — Yakında", "url": None},
            ],
            "screenshots": [],
        },
        {
            "name": "otel-panel",
            "summary": (
                "Assos Kadırga Otel için geliştirilmiş, canlıda aktif olarak "
                "kullanılan otel yönetim paneli."
            ),
            "logo": None,
            "badges": [
                {"kind": "live", "label": "Canlıda · Dahili kullanım", "url": None},
            ],
            "screenshots": [
                {
                    "src": "core/img/otel-panel-dashboard.webp",
                    "alt": "otel-panel ana paneli: gelir, gider ve ödeme yöntemi özetleri",
                },
                {
                    "src": "core/img/otel-panel-islemler.webp",
                    "alt": "otel-panel gelir ve gider işlemleri listesi",
                },
            ],
        },
    ],
    "businesses": [
        {
            "name": "Assos Kadırga Otel",
            "summary": "Behram, Ayvacık/Çanakkale. 1979'dan beri.",
            "logo": "core/img/assos-kadirga-otel.webp",
            "links": [
                {"label": "Web", "icon": "web", "url": "https://assoskadirgaotel.com"},
                {
                    "label": "Instagram",
                    "icon": "instagram",
                    "url": "https://instagram.com/assoskadirgaotel",
                },
            ],
        },
        {
            "name": "Erten Yapı Market",
            "summary": "Ayvacık/Çanakkale.",
            "logo": None,
            "links": [
                {
                    "label": "Haritada gör",
                    "icon": "map",
                    "url": "https://share.google/aZjqFMAuBJ10gNIUq",
                },
            ],
        },
    ],
}
