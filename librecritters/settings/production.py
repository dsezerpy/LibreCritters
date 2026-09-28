import os
import dj_database_url
from .base import *

# Explicitly disable debug mode
DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Domain security
ALLOWED_HOSTS = [
    'librecritters.org',
    'www.librecritters.org',
    '127.0.0.1',
    'localhost',
]

CSRF_TRUSTED_ORIGINS = [
    'https://librecritters.org',
    'https://www.librecritters.org',
]

# Static files storage (WhiteNoise compressed manifest)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}