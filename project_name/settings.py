import os
import environ

ROOT = environ.Path(__file__) - 2
ENV = environ.Env(
    DEBUG=(bool, False), ALLOWED_HOSTS=(list, []), ENVIRONMENTS=(dict, {}))
environ.Env.read_env('%s/.env' % str(ROOT - 1))

DEBUG = ENV.bool('DEBUG')

BASE_DIR = ROOT()

SECRET_KEY = ENV('SECRET_KEY')

ALLOWED_HOSTS = ENV.list('ALLOWED_HOSTS', default=[])

DATABASES = {
    'default': ENV.db()
}

ENVIRONMENTS = ENV.json('ENVIRONMENTS')

EMAIL_CONFIG = ENV.email_url('EMAIL_URL', default='consolemail://localhost:25')
EMAIL_BACKEND = EMAIL_CONFIG.get('EMAIL_BACKEND')
EMAIL_HOST = EMAIL_CONFIG.get('EMAIL_HOST')
EMAIL_HOST_PASSWORD = EMAIL_CONFIG.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = EMAIL_CONFIG.get('EMAIL_PORT')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
]

OWN_APPS = ['log_viewer']  # fabutils, log-viewer

PROJECT_APPS = []

ENV_APPS = ENV.list('APPS', default=[])

INSTALLED_APPS = (
    DJANGO_APPS + THIRD_PARTY_APPS + OWN_APPS + PROJECT_APPS + ENV_APPS
)

MIDDLEWARE = [
    'common.middleware.not_found_url_middleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'

FRONTEND_DIR = '{{ project_name }}-frontend/dist'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, FRONTEND_DIR),
            os.path.join(BASE_DIR, 'templates')

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

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '../static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, FRONTEND_DIR),
    os.path.join(BASE_DIR, FRONTEND_DIR, 'static')
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}

LOGS_DIR = 'logs'

DB_BACKUP_DIR = os.path.join(BASE_DIR, '../backups/')
