"""All site content lives here. Edit this file to change text or links.

See README.md ("İçerik düzenleme") for field descriptions and examples.
Badge kinds: "web", "appstore", "googleplay" (linked), "soon", "live".
Icons: core/templates/core/partials/icon.html. Images: core/static/core/img/.
"""

SITE = {
    "name": "Bayram Can Erten",
    "title": "Bilgisayar Mühendisi",
    "school": "Çanakkale Onsekiz Mart Üniversitesi",
    "monogram": "BCE",
    "url": "https://bayramcanerten.com/",
    "description": (
        "Bayram Can Erten — Bilgisayar Mühendisi. Tenis Asistanı ve "
        "otel-panel projeleri; Assos Kadırga Otel ve Erten Yapı Market."
    ),
    "og_image": {"src": "core/img/og.jpg", "width": 1200, "height": 630},
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
    # Short interface labels (navigation, buttons, screen-reader text).
    "ui": {
        "nav_label": "Bölümler",
        "home": "Başa dön",
        "theme_to_dark": "Koyu temaya geç",
        "theme_to_light": "Açık temaya geç",
        "scroll_down": "Projelere in",
        "zoom": "Büyüt",
        "close": "Kapat",
    },
    "projects": [
        {
            "name": "Tenis Asistanı",
            "summary": (
                "Kortta canlı skor tutan, antrenmanları ve ekipman ömrünü "
                "takip eden tenis uygulaması. Apple Watch ile bilekten skor."
            ),
            "logo": {"src": "core/img/tenis-asistani.webp", "width": 168, "height": 168},
            "badges": [
                {"kind": "web", "icon": "web", "label": "Web", "url": "https://tenisasistani.com"},
                {
                    "kind": "appstore",
                    "icon": "appstore",
                    "label": "App Store",
                    "url": "https://apps.apple.com/us/app/tenis-asistan%C4%B1/id6791199819",
                },
                {"kind": "soon", "icon": "play", "label": "Google Play — Yakında", "url": None},
            ],
            "stack": ["SwiftUI", "SwiftData", "watchOS", "Jetpack Compose", "Django"],
            "screenshots": [],
        },
        {
            "name": "otel-panel",
            "summary": (
                "Assos Kadırga Otel için geliştirdiğim yönetim paneli: gelir-gider, "
                "firma bakiyeleri, personel ve denetim kaydı tek yerde. Otelde "
                "canlıda, aktif olarak kullanılıyor."
            ),
            "logo": None,
            "badges": [
                {"kind": "live", "icon": "live", "label": "Canlıda · Dahili kullanım", "url": None},
            ],
            "stack": ["Next.js", "TypeScript", "Prisma", "Tailwind CSS", "Recharts"],
            "screenshots": [
                {
                    "src": "core/img/otel-panel-dashboard.webp",
                    "thumb": "core/img/otel-panel-dashboard-800.webp",
                    "width": 1623,
                    "height": 1095,
                    "alt": "otel-panel ana paneli: gelir, gider ve ödeme yöntemi özetleri",
                },
                {
                    "src": "core/img/otel-panel-islemler.webp",
                    "thumb": "core/img/otel-panel-islemler-800.webp",
                    "width": 1968,
                    "height": 1081,
                    "alt": "otel-panel gelir ve gider işlemleri listesi",
                },
            ],
        },
    ],
    "businesses": [
        {
            "name": "Assos Kadırga Otel",
            "summary": (
                "Behram, Ayvacık/Çanakkale'de deniz kenarında, bahçe içinde "
                "butik bir aile işletmesi. 1979'dan beri."
            ),
            "logo": {"src": "core/img/assos-kadirga-otel.webp", "width": 480, "height": 268},
            "icon": None,
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
            "summary": "Ayvacık/Çanakkale'de temelden çatıya yapı malzemeleri.",
            "logo": None,
            "icon": "store",
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
