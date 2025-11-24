from .base import *
import dj_database_url
import os

# Production mode
DEBUG = False     # Always false for prod

CSRF_TRUSTED_ORIGINS = [
    'http://13.220.92.71',
    'https://13.220.92.71',
]

# Hosts allowed
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "13.220.92.71").split(",")

# Security settings
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Database (Postgres in Docker)
DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("DATABASE_URL"),   # must be in .env
        conn_max_age=600
    )
}

# DRF Global Settings (optional but recommended)
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
        # "rest_framework.permissions.IsAuthenticated",

    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}

# AWS S3 (optional—only used if env vars are set)
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

if AWS_STORAGE_BUCKET_NAME:
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_QUERYSTRING_AUTH = False
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# Static files settings
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
