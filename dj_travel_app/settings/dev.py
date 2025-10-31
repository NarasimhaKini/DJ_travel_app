from .base import *
import dj_database_url

DEBUG = True

# Local DB (Postgres via docker-compose)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'travel'),
        'USER': os.getenv('POSTGRES_USER', 'traveluser'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'travelpass'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# DATABASE_URL=postgres://traveluser:travelpass@rds-endpoint:5432/travel

# Media and static from local filesystem
STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
