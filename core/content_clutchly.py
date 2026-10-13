"""Clutchly pages (/clutchly, /clutchly/privacy, /clutchly/support).

Text comes from Clutchly/docs/web/clutchly-site.md and must stay as written there:
the privacy policy has to match the in-app policy. Both languages share one structure.
"""

LANGUAGES = ("tr", "en")
DEFAULT_LANGUAGE = "en"

COMMON = {
    "name": "Clutchly",
    "email": "bayrammcan17@gmail.com",
    "controller": "Bayram Can Erten",
    # Set "live": True once the App Store page exists; the badge then links to it.
    "app_store": {"live": False, "url": "https://apps.apple.com/app/id6821973888"},
    "stack": ["SwiftUI", "AlarmKit", "ActivityKit", "WidgetKit", "Supabase", "RevenueCat"],
    # Raw captures are 1320×2868; WebP copies live in core/static/core/img/clutchly/<lang>/.
    "screen_size": {"width": 1320, "height": 2868},
    "screens": [
        {"file": "1-tonight", "label": {"tr": "Bu Gece", "en": "Tonight"}},
        {"file": "2-game", "label": {"tr": "Maç sayfası", "en": "Game page"}},
        {"file": "4-morning", "label": {"tr": "Sabah özeti", "en": "Morning brief"}},
        {"file": "5-player", "label": {"tr": "Şut haritası", "en": "Shot chart"}},
        {"file": "7-player-milestones", "label": {"tr": "Dönüm noktaları", "en": "Milestones"}},
        {"file": "8-player-top", "label": {"tr": "Oyuncum", "en": "My Player"}},
        {"file": "3-rules", "label": {"tr": "Uyarı kuralları", "en": "Alert rules"}},
    ],
    "hero_screen": "1-tonight",
}

TEXT = {
    "tr": {
        "locale": "tr_TR",
        "language_name": "Türkçe",
        "ui": {
            "nav_label": "Clutchly sayfaları",
            "home": "Bayram Can Erten — ana sayfa",
            "theme_to_dark": "Koyu temaya geç",
            "theme_to_light": "Açık temaya geç",
            "language_label": "Dil",
            "zoom": "Büyüt",
            "close": "Kapat",
            "previous": "Önceki",
            "next": "Sonraki",
            "coming_soon": "Yakında",
            "app_store": "App Store",
            "google_play": "Google Play",
            "download_on": "App Store'dan indir",
            "contents": "İçindekiler",
            "write_to_me": "E-posta gönder",
            "faq_title": "Sık sorulanlar",
            "privacy_link": "Gizlilik politikası",
            "screen_alt": "Clutchly ekran görüntüsü:",
        },
        "nav": {"product": "Clutchly", "privacy": "Gizlilik", "support": "Destek"},
        "not_affiliated": "Clutchly, NBA ile bağlantılı değildir.",
        "product": {
            "title": "Clutchly: Basketbol Maç Takibi",
            "description": (
                "NBA'i uykundan olmadan takip et. Gece maçlarını Türkiye saatiyle gösterir, "
                "maç çekişmeli bitecekse seni uyandırır, sabah skoru söylemeden hangi maçın "
                "izlemeye değer olduğunu anlatır."
            ),
            "headline": "NBA'i uykundan olmadan takip et.",
            "subhead": (
                "Gece maçları, Türkiye saatiyle. Son dakikalar çekişirse seni uyandırırız; "
                "sabah skoru söylemeden hangi maçın izlemeye değer olduğunu anlatırız."
            ),
            "features_title": "Özellikler",
            "features": [
                {
                    "icon": "moon",
                    "title": "Uyanmaya değer mi?",
                    "text": (
                        "Her maça önceden puan veririz; gece 03:00'teki maç için alarm kurmaya "
                        "değer mi, tek bakışta görürsün."
                    ),
                },
                {
                    "icon": "bell",
                    "title": "Clutch uyarısı",
                    "text": (
                        "Maç son dakikalara çekişmeli girince haber veririz. Çekişmeli değilse "
                        "hiç rahatsız etmeyiz."
                    ),
                },
                {
                    "icon": "alarm",
                    "title": "Nöbet alarmı",
                    "text": (
                        "Clutch anı gece gelirse sessiz modu ve Odak'ı delen gerçek bir alarm "
                        "çalar; \"İzle\"ye bas, maç açılsın."
                    ),
                },
                {
                    "icon": "shield",
                    "title": "Spoiler kalkanı",
                    "text": (
                        "Liste, bildirimler ve sabah özeti skoru ve kazananı göstermez; sen "
                        "istemedikçe."
                    ),
                },
                {
                    "icon": "sunrise",
                    "title": "Sabah özeti",
                    "text": "Dün gecenin maçları, kazananı söylemeden izlenebilirliğe göre sıralanır.",
                },
                {
                    "icon": "player",
                    "title": "Oyuncum",
                    "text": "Favori oyuncunun sezonu, şut haritası ve yaklaşan kariyer eşikleri.",
                },
            ],
            "screens_title": "Ekranlar",
            "plans_title": "Ücretsiz / Pro",
            "plans": [
                {
                    "name": "Ücretsiz",
                    "items": [
                        "favori oyuncunun maçlarında clutch uyarısı",
                        "takvim ve maç öncesi puan",
                        "skorsuz sabah listesi",
                        "temel istatistikler",
                        "widget'lar",
                    ],
                    "note": None,
                },
                {
                    "name": "Clutchly Pro",
                    "items": [
                        "her maç için uyarı (takip ettiklerin, izlemeye değer maçlar, tüm maçlar, seçtiklerin)",
                        "Nöbet alarmı",
                        "kendi clutch tanımın",
                        "kilit ekranında canlı maç",
                        "sabah raporu (puan ve gerekçeler)",
                        "şut haritası ve dönüm noktaları",
                        "10 oyuncu takibi",
                    ],
                    "note": "Aylık veya yıllık; yıllıkta 1 hafta ücretsiz deneme.",
                },
            ],
        },
        "privacy": {
            "title": "Clutchly Gizlilik Politikası",
            "description": "Clutchly'nin hangi verileri sakladığı, neleri toplamadığı ve verilerinle ilgili hakların.",
            "updated": "Son güncelleme: 12 Ekim 2026",
            "sections": [
                {
                    "id": "kisaca",
                    "title": "Kısaca",
                    "paragraphs": [
                        "Clutchly'yi kullanmak için hesap açman, e-posta ya da adını vermen gerekmez. "
                        "Uygulama yalnızca sana maç uyarısı göndermek ve tercihlerini hatırlamak için "
                        "gereken verileri saklar. Konumunu almayız, reklam ya da takip yapmayız, verini satmayız."
                    ],
                },
                {
                    "id": "sakladiklarimiz",
                    "title": "Hangi verileri saklıyoruz",
                    "items": [
                        ("Anonim kullanıcı kimliği", "ilk açılışta otomatik oluşturulan rastgele bir kimlik. Seni tanımlayan bir bilgi içermez."),
                        ("Bildirim jetonları", "Apple'ın bu cihaza bildirim ve Live Activity göndermek için verdiği jetonlar."),
                        ("Tercihlerin", "favori ve takip ettiğin oyuncular, uyarı, nöbet alarmı ve sabah özeti ayarların, spoiler kalkanı, uyarı açtığın ve skorunu gösterdiğin maçlar."),
                        ("Dil ve saat dilimi", "bildirim metinlerini ve alarm/sabah özeti saatlerini senin saatine göre ayarlamak için."),
                        ("Gönderim kayıtları", "aynı uyarıyı iki kez göndermemek için hangi maç uyarısının sana gittiği."),
                        ("Abonelik durumun", "Clutchly Pro'nun açık olup olmadığı, hangi plan olduğu ve ne zaman biteceği."),
                    ],
                },
                {
                    "id": "toplamadiklarimiz",
                    "title": "Neleri toplamıyoruz",
                    "paragraphs": [
                        "Konum, rehber, fotoğraf, reklam kimliği, kullanım analizi ya da çökme raporu "
                        "toplanmaz. Uygulamada üçüncü taraf analiz veya reklam aracı yoktur."
                    ],
                },
                {
                    "id": "paylasim",
                    "title": "Veriler nerede ve kimlerle",
                    "items": [
                        ("Supabase", "verilerin Avrupa Birliği'ndeki (Frankfurt) sunucularda saklanır."),
                        ("Apple Push Notification service", "bildirimler Apple üzerinden iletilir."),
                        ("RevenueCat (ABD)", "Clutchly Pro satın alımları RevenueCat üzerinden doğrulanır. Anonim kullanıcı kimliğin ve satın alma geçmişin (ürün, tarih, fiyat) paylaşılır; ödeme bilgilerin Apple'da kalır, bize ya da RevenueCat'e gelmez."),
                        (None, "Maç ve oyuncu istatistikleri bir spor veri sağlayıcısından alınır; bu sağlayıcıya senin hakkında hiçbir veri gönderilmez."),
                    ],
                },
                {
                    "id": "sure",
                    "title": "Ne kadar süre",
                    "paragraphs": [
                        "Veriler hesabın durduğu sürece saklanır. Hesabını sildiğinde tamamı, RevenueCat'teki "
                        "kaydınla birlikte kalıcı olarak silinir. Aboneliğin Apple'da sürer; iptal etmek için "
                        "App Store hesap ayarlarını kullan."
                    ],
                },
                {
                    "id": "haklarin",
                    "title": "Hakların",
                    "paragraphs": [
                        "KVKK (6698 sayılı Kanun, md. 11) ve GDPR kapsamında verilerine erişme, düzeltme ve "
                        "silinmesini isteme hakkın var. Tüm verilerini uygulama içinden silebilirsin: "
                        "Ayarlar → Hesabımı ve verilerimi sil. Diğer talepler için: {email}"
                    ],
                },
                {
                    "id": "cocuklar",
                    "title": "Çocuklar",
                    "paragraphs": [
                        "Clutchly 13 yaşın altındaki çocuklara yönelik değildir ve bilerek onlardan veri toplamaz."
                    ],
                },
                {
                    "id": "degisiklikler",
                    "title": "Değişiklikler",
                    "paragraphs": [
                        "Bu politikayı güncellersek bu sayfadaki tarihi değiştiririz; önemli değişiklikleri "
                        "uygulamada da duyururuz."
                    ],
                },
                {
                    "id": "veri-sorumlusu",
                    "title": "Veri sorumlusu",
                    "paragraphs": ["Bayram Can Erten · {email}"],
                },
            ],
        },
        "support": {
            "title": "Clutchly Destek",
            "description": "Clutchly için iletişim ve sık sorulan sorular.",
            # "{email}" is rendered as a bold mailto link.
            "intro": (
                "Bir sorun mu var ya da önerin mi? Yaz: {email} (genellikle 1–2 gün içinde dönüyorum). "
                "Yazarken iPhone modelini, iOS sürümünü ve hangi maçta ne olduğunu eklersen hızlı çözerim."
            ),
            "faq": [
                (
                    "Uyarı neden gelmedi?",
                    "Uyarı yalnızca maç son dakikalara çekişmeli girince gelir (varsayılan: son 5 dakika, "
                    "fark 5 sayı veya daha az). Bildirim izni kapalıysa Clutchly Ayarlar'ın en üstünde uyarı "
                    "görürsün. Ücretsiz sürümde yalnızca favori oyuncunun maçları uyarı alır.",
                ),
                (
                    "Uyarı ne kadar hızlı gelir?",
                    "Canlı veri sahadan ortalama yarım dakika gecikmeyle gelir; uyarı \"son dakikalar "
                    "başlıyor\" der, anlık skor servisi değildir.",
                ),
                (
                    "Nöbet alarmı çalmadı.",
                    "Alarm iznini (iPhone Ayarlar → Clutchly) ve Clutchly'deki alarm saat aralığını kontrol et. "
                    "Alarm her maçta bir kez ve yalnız clutch anı bu aralığa denk gelirse çalar. Uygulamayı "
                    "uygulama değiştiriciden kaydırıp kapatmak bildirimi engellemez.",
                ),
                (
                    "Skoru nasıl görürüm?",
                    "Spoiler kalkanı açıkken maç sayfasında \"Skoru göster\"e dokun; kalkanı Ayarlar'dan "
                    "tamamen kapatabilirsin.",
                ),
                (
                    "Aboneliğimi nasıl iptal ederim?",
                    "iPhone Ayarlar → adın → Abonelikler → Clutchly Pro. İptal edersen dönem sonuna kadar "
                    "Pro açık kalır.",
                ),
                (
                    "Yeni telefonda Pro'm görünmüyor.",
                    "Clutchly → Ayarlar → Clutchly Pro → \"Satın alımları geri yükle\".",
                ),
                (
                    "Verilerimi nasıl silerim?",
                    "Clutchly → Ayarlar → Hesabımı ve verilerimi sil. Her şey sunucudan kalıcı olarak silinir.",
                ),
            ],
        },
    },
    "en": {
        "locale": "en_US",
        "language_name": "English",
        "ui": {
            "nav_label": "Clutchly pages",
            "home": "Bayram Can Erten — home",
            "theme_to_dark": "Switch to dark theme",
            "theme_to_light": "Switch to light theme",
            "language_label": "Language",
            "zoom": "Enlarge",
            "close": "Close",
            "previous": "Previous",
            "next": "Next",
            "coming_soon": "Coming soon",
            "app_store": "App Store",
            "google_play": "Google Play",
            "download_on": "Download on the App Store",
            "contents": "Contents",
            "write_to_me": "Send an email",
            "faq_title": "FAQ",
            "privacy_link": "Privacy policy",
            "screen_alt": "Clutchly screenshot:",
        },
        "nav": {"product": "Clutchly", "privacy": "Privacy", "support": "Support"},
        "not_affiliated": "Clutchly is not affiliated with the NBA.",
        "product": {
            "title": "Clutchly: Basketball Alerts",
            "description": (
                "Follow the NBA without losing sleep. Clutchly shows late games in your time zone, "
                "wakes you up when a game is heading into a close finish, and tells you in the morning "
                "which games are worth watching — without the score."
            ),
            "headline": "Follow the NBA without losing sleep.",
            "subhead": (
                "Late games, in your time zone. If the finish gets close, we wake you up; in the morning "
                "we tell you what's worth watching, without the score."
            ),
            "features_title": "Features",
            "features": [
                {
                    "icon": "moon",
                    "title": "Worth waking up for?",
                    "text": (
                        "Every game gets a score in advance, so you know at a glance whether a 3 AM "
                        "tip-off deserves an alarm."
                    ),
                },
                {
                    "icon": "bell",
                    "title": "Clutch alerts",
                    "text": (
                        "We let you know when a game heads into a close finish. If it isn't close, "
                        "we won't bother you."
                    ),
                },
                {
                    "icon": "alarm",
                    "title": "Night Watch alarm",
                    "text": (
                        "If the clutch moment comes at night, a real alarm breaks through silent mode "
                        "and Focus. Tap \"Watch\" and the game opens."
                    ),
                },
                {
                    "icon": "shield",
                    "title": "Spoiler shield",
                    "text": (
                        "The list, notifications and morning brief never show the score or the winner, "
                        "unless you ask."
                    ),
                },
                {
                    "icon": "sunrise",
                    "title": "Morning brief",
                    "text": "Last night's games ranked by watchability, without naming the winner.",
                },
                {
                    "icon": "player",
                    "title": "My Player",
                    "text": "Your favorite player's season, shot chart and upcoming career milestones.",
                },
            ],
            "screens_title": "Screens",
            "plans_title": "Free / Pro",
            "plans": [
                {
                    "name": "Free",
                    "items": [
                        "clutch alerts for your favorite player's games",
                        "schedule and pre-game scores",
                        "a spoiler-free morning list",
                        "basic stats",
                        "widgets",
                    ],
                    "note": None,
                },
                {
                    "name": "Clutchly Pro",
                    "items": [
                        "alerts for any game (players you follow, games worth watching, every game, or games you pick)",
                        "Night Watch alarm",
                        "your own clutch definition",
                        "live games on your Lock Screen",
                        "the morning report (scores and reasons)",
                        "shot charts and milestones",
                        "follow 10 players",
                    ],
                    "note": "Monthly or yearly; the yearly plan starts with a 1-week free trial.",
                },
            ],
        },
        "privacy": {
            "title": "Clutchly Privacy Policy",
            "description": "What Clutchly stores, what it doesn't collect, and your rights over your data.",
            "updated": "Last updated: October 12, 2026",
            "sections": [
                {
                    "id": "in-short",
                    "title": "In short",
                    "paragraphs": [
                        "You don't need an account, email or name to use Clutchly. The app only stores what it "
                        "needs to send you game alerts and remember your preferences. We don't collect your "
                        "location, show ads, track you, or sell your data."
                    ],
                },
                {
                    "id": "what-we-store",
                    "title": "What we store",
                    "items": [
                        ("Anonymous user ID", "a random ID created automatically on first launch. It contains nothing that identifies you."),
                        ("Notification tokens", "the tokens Apple issues to send notifications and Live Activities to this device."),
                        ("Your preferences", "favorite and followed players, alert, Night Watch alarm and morning brief settings, the spoiler shield, and the games you turned alerts on for or revealed scores of."),
                        ("Language and time zone", "to write notifications in your language and time alarms and the morning brief to your clock."),
                        ("Delivery log", "which game alerts were sent to you, so the same alert never goes out twice."),
                        ("Your subscription status", "whether Clutchly Pro is on, which plan, and when it ends."),
                    ],
                },
                {
                    "id": "what-we-dont-collect",
                    "title": "What we don't collect",
                    "paragraphs": [
                        "No location, contacts, photos, advertising ID, usage analytics or crash reports are "
                        "collected. The app contains no third-party analytics or ad tools."
                    ],
                },
                {
                    "id": "where-your-data-goes",
                    "title": "Where your data goes",
                    "items": [
                        ("Supabase", "your data is stored on servers in the European Union (Frankfurt)."),
                        ("Apple Push Notification service", "notifications are delivered through Apple."),
                        ("RevenueCat (USA)", "Clutchly Pro purchases are verified through RevenueCat. Your anonymous user ID and purchase history (product, date, price) are shared; your payment details stay with Apple and never reach us or RevenueCat."),
                        (None, "Game and player stats come from a sports data provider; nothing about you is sent to that provider."),
                    ],
                },
                {
                    "id": "how-long",
                    "title": "How long",
                    "paragraphs": [
                        "Data is kept for as long as your account exists. When you delete your account, all of "
                        "it is deleted for good, including your RevenueCat record. Your subscription stays with "
                        "Apple; cancel it in your App Store account settings."
                    ],
                },
                {
                    "id": "your-rights",
                    "title": "Your rights",
                    "paragraphs": [
                        "Under GDPR and Turkey's KVKK (Law No. 6698, Art. 11) you have the right to access, "
                        "correct and request deletion of your data. You can delete all your data in the app: "
                        "Settings → Delete my account and data. For other requests: {email}"
                    ],
                },
                {
                    "id": "children",
                    "title": "Children",
                    "paragraphs": [
                        "Clutchly is not directed at children under 13 and does not knowingly collect their data."
                    ],
                },
                {
                    "id": "changes",
                    "title": "Changes",
                    "paragraphs": [
                        "If we update this policy, we change the date on this page and announce significant "
                        "changes in the app."
                    ],
                },
                {
                    "id": "data-controller",
                    "title": "Data controller",
                    "paragraphs": ["Bayram Can Erten · {email}"],
                },
            ],
        },
        "support": {
            "title": "Clutchly Support",
            "description": "Contact and frequently asked questions for Clutchly.",
            "intro": (
                "Found a problem or have an idea? Write to {email} (I usually reply within 1–2 days). "
                "Including your iPhone model, iOS version and which game it was helps me fix things fast."
            ),
            "faq": [
                (
                    "Why didn't I get an alert?",
                    "Alerts only come when a game heads into a close finish (by default: last 5 minutes, margin "
                    "of 5 or less). If notifications are off, Clutchly shows a warning at the top of Settings. "
                    "On the free plan, only your favorite player's games send alerts.",
                ),
                (
                    "How fast are alerts?",
                    "Live data arrives about half a minute behind the court; an alert means \"the final minutes "
                    "are starting\", not a play-by-play feed.",
                ),
                (
                    "The Night Watch alarm didn't ring.",
                    "Check the alarm permission (iPhone Settings → Clutchly) and the alarm hours in Clutchly. It "
                    "rings once per game, and only if the clutch moment falls within those hours. Swiping the "
                    "app away doesn't block it.",
                ),
                (
                    "How do I see the score?",
                    "With the spoiler shield on, tap \"Show score\" on the game page; you can turn the shield off "
                    "entirely in Settings.",
                ),
                (
                    "How do I cancel my subscription?",
                    "iPhone Settings → your name → Subscriptions → Clutchly Pro. After canceling, Pro stays on "
                    "until the end of the period.",
                ),
                (
                    "Pro doesn't show on my new phone.",
                    "Clutchly → Settings → Clutchly Pro → \"Restore purchases\".",
                ),
                (
                    "How do I delete my data?",
                    "Clutchly → Settings → Delete my account and data. Everything is permanently deleted from "
                    "the server.",
                ),
            ],
        },
    },
}
