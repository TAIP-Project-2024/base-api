from pathlib import Path
from os import getenv
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
from datetime import timedelta

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY", "django-insecure-default-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'accounts',
    'drf_yasg',
    'corsheaders',
    'django_celery_beat'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middleware.auth_middleware.AuthMiddleware',
    'api.middleware.log_request_middleware.LogRequestMiddleware',
]

ROOT_URLCONF = 'BaseAPI.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':
            [
                BASE_DIR / 'BaseAPI' / 'propath',
                BASE_DIR / 'BaseAPI/',
                BASE_DIR / 'BaseAPI/resources/',
                BASE_DIR / 'api/ml_core/topic_modeling'
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'BaseAPI.wsgi.application'

# Database configuration (already customized)
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
        'OPTIONS': {
            'sslmode': 'require',  # Ensures SSL is used
        }
    }
}

# Custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# REST framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MONGODB_URI = os.getenv("MONGO_URI")
MONGODB_DB_NAME = os.getenv("MONGO_DB_NAME")

MONGODB_SETTINGS = {
    'URI': MONGODB_URI,
    'DB_NAME': MONGODB_DB_NAME
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_DEBUG = True

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
    "OPTIONS",
]

CELERY_BROKER_URL = 'redis://localhost:6379/0'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

CELERY_IMPORTS = [
    'api.tasks.graphs_tasks',
]

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'build_new_graphs': {
        'task': 'api.tasks.graphs_tasks.build_new_graphs',
        'schedule': crontab(minute='*')
    },
}

