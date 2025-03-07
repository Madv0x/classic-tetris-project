"""
Django settings for classic_tetris_project_django project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import environ
ENV = environ.Env(
    SECRET_KEY=(str, 'd0$j=wune9kn70srt1lt!g3a8fim7ug#j@x8+zmy0gi_mv7&dk'),
    DEBUG=(bool, True),
    DATABASE_URL=(str, 'sqlite:///db.sqlite3'),
    CACHE_URL=(str, 'rediscache://'),
    BASE_URL=(str, 'http://dev.monthlytetris.info:8000'),
    DISCORD_USER_ID_WHITELIST=(list, []),
    DISCORD_CHANNEL_MESSAGES=(bool, False),
    ROLLBAR_ENABLED=(bool, False),
    ROLLBAR_TOKEN=(str, ''),
)
environ.Env.read_env('.env')

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = ENV('BASE_URL')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV('DEBUG')

ALLOWED_HOSTS = [
    'ctm.gg',
    'monthlytetris.info',
    'monthlytetris.com',
]
if DEBUG:
    ALLOWED_HOSTS.append('*')


# Application definition

INSTALLED_APPS = [
    'classic_tetris_project.apps.ClassicTetrisProjectConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django_extensions',
    'django_object_actions',
    'markdownx',
    'webpack_loader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'classic_tetris_project_django.urls'

LOGIN_URL = '/oauth/login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "classic_tetris_project", "templates"),
            os.path.join(BASE_DIR, "classic_tetris_project", "private", "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': [
                'classic_tetris_project.private.templatetags',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'classic_tetris_project.private.context_processors.session_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'classic_tetris_project_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        **ENV.db(),
        "ATOMIC_REQUESTS": True,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SITE_ID = 1

SHELL_PLUS_PRINT_SQL = True


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Expires after 180 days
SESSION_COOKIE_AGE = 180 * 24 * 60 * 60

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
]

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/tetris/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

ROLLBAR = {
    'access_token': ENV('ROLLBAR_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
    'enabled': ENV('ROLLBAR_ENABLED'),
}
import rollbar
rollbar.init(**ROLLBAR)


CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1',
