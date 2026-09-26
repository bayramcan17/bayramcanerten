import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Local-only fallback; production reads SECRET_KEY from the environment.
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-insecure-key-do-not-use-in-production")

DEBUG = os.environ.get("DEBUG", "False").lower() in ("1", "true", "yes")

ALLOWED_HOSTS = [
    "bayramcanerten.com",
    "www.bayramcanerten.com",
    ".vercel.app",
    "localhost",
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# No database: the site is static content rendered from core/content.py.
DATABASES = {}

LANGUAGE_CODE = "tr"
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# Vercel terminates TLS and forwards X-Forwarded-Proto.
SECURE_SSL_REDIRECT = not DEBUG
# Matches the HSTS header Vercel already sends on the custom domain (2 years).
# Subdomains and preload are intentionally left out.
SECURE_HSTS_SECONDS = 0 if DEBUG else 63072000

# The site has no forms or cookies, so CSRF middleware is intentionally omitted.
SILENCED_SYSTEM_CHECKS = ["security.W003"]
