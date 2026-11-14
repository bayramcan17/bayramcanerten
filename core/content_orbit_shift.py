"""Orbit Shift: Neon Rush pages (/orbit-shift, /orbit-shift/privacy, /orbit-shift/support).

Text comes from OrbitShift/docs/web/ (game-page.md, privacy.md, support.md) and must stay as
written there: the privacy policy has to match the one the game links to. The game is English
only, so these pages are too.

Inline markup in texts: **bold**, [label](url) and {email} (rendered as a mailto link).
"""

COMMON = {
    "name": "Orbit Shift: Neon Rush",
    "short_name": "Orbit Shift",
    "email": "bayrammcan17@gmail.com",
    # Set "live" and the id/url once the game is in each store; the badges then become links.
    "app_store": {"live": False, "id": None, "url": None},
    "google_play": {
        "live": False,
        "url": "https://play.google.com/store/apps/details?id=com.bayramcanerten.orbitshift",
    },
    # AdMob publisher ID ("pub-…", AdMob > Settings). While None, /app-ads.txt answers 404.
    "admob_publisher_id": None,
    "stack": ["Unity 6", "C#", "Google AdMob"],
    # Raw captures are 660×1434; WebP copies live in core/static/core/img/orbit-shift/screens/.
    "screen_size": {"width": 660, "height": 1434},
    "screens": [
        {"file": "gameplay-1", "label": "Tap to switch orbits and dodge the arcs"},
        {"file": "gameplay-2", "label": "Moving arcs and pulsing zones as you speed up"},
        {"file": "menu", "label": "Endless, Levels, Daily and Style"},
        {"file": "levels", "label": "30 levels, three stars each"},
        {"file": "daily-missions", "label": "Three new missions every day"},
        {"file": "style", "label": "Orbs, trails and themes"},
    ],
    "hero_screen": "gameplay-1",
}

UI = {
    "nav_label": "Orbit Shift pages",
    "back": "Projects",
    "theme_to_dark": "Switch to dark theme",
    "theme_to_light": "Switch to light theme",
    "close": "Close",
    "previous": "Previous",
    "next": "Next",
    "coming_soon": "Coming soon",
    "app_store": "App Store",
    "google_play": "Google Play",
    "download_on": "Download on the",
    "get_it_on": "Get it on",
    "contents": "Contents",
    "write_to_me": "Send an email",
    "faq_title": "Frequently asked questions",
    "screen_alt": "Orbit Shift screenshot:",
}

NAV = {"product": "Orbit Shift", "privacy": "Privacy", "support": "Support"}

PRODUCT = {
    "title": "Orbit Shift: Neon Rush — a one-tap arcade game for iPhone, iPad and Android",
    "description": (
        "Tap to switch orbits and dodge glowing arcs. Endless mode, 30 levels and a new "
        "Daily Challenge every day. Plays offline."
    ),
    "og_title": "Orbit Shift: Neon Rush",
    "og_description": "Two orbits. One tap. How long can you last?",
    "headline": "Two orbits. One tap. How long can you last?",
    "intro": (
        "Orbit Shift: Neon Rush is a fast, minimal arcade game. Your orb circles the center on "
        "one of two rings. Tap anywhere to jump to the other ring and slip past the glowing arcs "
        "before they light up."
    ),
    "coming_soon": "Coming soon to the App Store and Google Play.",
    "features_title": "Features",
    "features": [
        {"icon": "tap", "title": "One-touch controls.", "text": "Easy to learn, hard to master."},
        {
            "icon": "shield",
            "title": "Fair by design.",
            "text": "Every hazard is warned in advance, so each run comes down to your timing.",
        },
        {
            "icon": "infinity",
            "title": "Endless mode",
            "text": "that speeds up the longer you survive, with moving arcs and pulsing zones.",
        },
        {"icon": "star", "title": "30 handcrafted levels,", "text": "each with three stars to earn."},
        {
            "icon": "calendar",
            "title": "A new Daily Challenge",
            "text": "and three daily missions every day.",
        },
        {"icon": "bolt", "title": "Collect energy", "text": "to unlock orbs, trails and themes."},
        {
            "icon": "offline",
            "title": "Plays fully offline.",
            "text": "Ads are optional rewards only, never forced. No in-app purchases.",
        },
        {
            "icon": "sliders",
            "title": "Comfort options:",
            "text": "haptics, reduced motion and sound settings.",
        },
    ],
    "screens_title": "Screenshots",
    "details_title": "Details",
    "details": [
        ("Platforms", "iPhone, iPad (iOS 15+), Android (7.1+)"),
        ("Price", "Free, with optional rewarded ads"),
        ("Age", "13+"),
        ("Languages", "English"),
        ("Developer", "Bayram Can Erten"),
    ],
}

PRIVACY = {
    "title": "Privacy Policy — Orbit Shift: Neon Rush",
    "heading": "Privacy Policy",
    "description": "How Orbit Shift: Neon Rush handles information: no accounts, no analytics, optional rewarded ads only.",
    "effective": "Effective date: November 16, 2026",
    "effective_iso": "2026-11-16",
    "intro": (
        'This policy explains how **Orbit Shift: Neon Rush** (the "Game"), a mobile game developed '
        'by Bayram Can Erten ("we"), handles information.'
    ),
    "sections": [
        {
            "id": "summary",
            "title": "Summary",
            "items": [
                "The Game itself does **not collect** personal data from you, does **not send** it to us or to any other server, and does **not sell** it.",
                "There are **no** accounts, sign-ins, purchases, leaderboards or analytics tools.",
                "The Game can be played offline. When you are online, Google's advertising service (Google AdMob) is used **only for optional rewarded ads**; the data described below is processed by that service.",
            ],
        },
        {
            "id": "on-device",
            "title": "Information stored on your device",
            "paragraphs": [
                "Your progress is stored only on your device, in the Game's own folder:",
            ],
            "items": [
                "game progress (energy, best score, unlocked and equipped looks, level stars, daily missions, tutorial completion),",
                "settings (sound, music, haptics, reduced motion),",
                "random run identifiers used so that an ad reward is not granted twice for the same run,",
                "a performance log (frame times and run statistics; no personal information).",
            ],
            "after": [
                "This information never leaves your device and we cannot access it. You can reset your progress in **Settings > Reset progress**, and deleting the Game removes all of it from your device.",
            ],
        },
        {
            "id": "advertising",
            "title": "Advertising (Google AdMob)",
            "paragraphs": [
                "The Game only shows rewarded ads that **you choose** to watch (for bonus energy after a run or to continue a run). There are no forced, banner or interstitial ads.",
                "To show ads, the Google Mobile Ads SDK may collect and process information such as:",
            ],
            "items": [
                "your device's advertising identifier (Android Advertising ID; on iOS the IDFA only if you allow it),",
                "IP address and approximate location derived from it,",
                "device and app information (model, operating system version, language, app version),",
                "ad interactions (impressions, clicks) and error/diagnostic information.",
            ],
            "after": [
                "Google uses this information to deliver and measure ads, prevent fraud and, with your consent, personalize ads. See how Google uses information from sites or apps that use its services — [https://policies.google.com/technologies/partner-sites](https://policies.google.com/technologies/partner-sites) — and the Google Privacy Policy — [https://policies.google.com/privacy](https://policies.google.com/privacy)",
            ],
        },
        {
            "id": "choices",
            "title": "Consent and your choices",
            "items": [
                "**European Economic Area, United Kingdom and Switzerland:** Google's consent form (User Messaging Platform) is shown before any ads load. You can change your choice later in **Settings > Privacy options**.",
                "**iOS:** The Game asks for permission to track you across other companies' apps and websites (App Tracking Transparency). If you decline, the IDFA is not shared; ads still work but are not personalized. You can change this in iOS Settings > Privacy & Security > Tracking.",
                "**Android:** You can reset or delete your advertising ID in Settings > Privacy > Ads.",
                "Watching ads is entirely optional; the whole Game can be played without them.",
            ],
        },
        {
            "id": "children",
            "title": "Children",
            "paragraphs": [
                "The Game is designed for users aged 13 and over and is not directed at children under 13. We do not knowingly collect personal data from children under 13.",
            ],
        },
        {
            "id": "security",
            "title": "Security and retention",
            "paragraphs": [
                "Because we do not collect data from you, no information about you is stored on our servers. Information on your device is removed when you delete the Game. Retention of data held by Google is governed by Google's policies.",
            ],
        },
        {
            "id": "changes",
            "title": "Changes",
            "paragraphs": [
                "If we update this policy, we will publish the new version on this page and change the effective date.",
            ],
        },
        {
            "id": "contact",
            "title": "Contact",
            "paragraphs": ["Questions: {email}"],
        },
    ],
}

SUPPORT = {
    "title": "Support — Orbit Shift: Neon Rush",
    "heading": "Support",
    "description": "Help, bug reports and answers to common questions about Orbit Shift: Neon Rush.",
    "intro": (
        "Need help, found a bug or have an idea? Email **{email}**. Please include your device "
        "model, its iOS or Android version and what happened. I usually reply within a few days."
    ),
    "faq": [
        (
            "How do I play?",
            "Your orb circles the center on one of two rings. Tap anywhere on the screen to jump to "
            "the other ring. Arcs are drawn as an outline first and light up red a moment later: be "
            "on the other ring when they do. Collect the gold energy dots on the way. You can replay "
            "the tutorial any time from **Settings > How to play**.",
        ),
        (
            "Do I need an internet connection?",
            "No. The whole game works offline. A connection is only used for optional rewarded ads.",
        ),
        (
            "Are there ads? Do I have to watch them?",
            "Ads are always optional. After a run you can watch one for bonus energy, and after a "
            "long run (40 seconds or more) one ad lets you continue once. There are no banners and "
            "no ads that interrupt play.",
        ),
        ("Are there in-app purchases?", "No."),
        (
            "Where is my progress saved? Can I move it to a new phone?",
            "Progress (energy, unlocked looks, best score, level stars, daily missions) is saved "
            "only on your device. There is no account or cloud save, so progress cannot be moved "
            "to another device, and deleting the game deletes it.",
        ),
        (
            "How do I reset my progress?",
            "**Settings > Reset progress.** Your settings are kept. This cannot be undone.",
        ),
        (
            "How do I change my ad privacy choices?",
            "In the European Economic Area, the UK and Switzerland: **Settings > Privacy options** "
            "in the game. On iOS you can also allow or deny tracking in iOS **Settings > Privacy & "
            "Security > Tracking**. On Android you can reset or delete your advertising ID in "
            "**Settings > Privacy > Ads**. See the [Privacy Policy](/orbit-shift/privacy).",
        ),
        (
            "Motion or sound is too much.",
            "**Settings** has switches for music, sound effects, haptics and **Reduce motion** (no "
            "pulsing, zooming or fading effects).",
        ),
        (
            "Which devices are supported?",
            "iPhone and iPad with iOS 15 or later, and Android phones and tablets with Android 7.1 "
            "or later (64-bit).",
        ),
    ],
}
