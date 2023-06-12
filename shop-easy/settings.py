"""
Django settings for shop-easy project.

Generated by 'django-admin startproject' using Django 3.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

from decouple import Csv, config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE = os.path.join(BASE_DIR, '.env')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


def get_env(variable, cast, default_value=None, source_cast=None):
    """
    This function is to remove the unnecessary calls for fetching the variables either
    from the environment or the .env file. This would also keep the consistency to
    always fetch the variables in the same manner

    :param variable: The variable to fetch from the environment or .env
    :param cast: Type cast to str, bool, int etc
    :param default_value: If no variable is found, use this value
    :param source_cast: If the variable is in another type, then specify it to be
                                            changed into `cast` type
    :return: The value to be expected from the variable
    """

    if source_cast:
        return cast(source_cast(os.environ.get(key=variable, default=default_value))) \
            if not os.path.exists(ENV_FILE) else config(variable, cast=cast, default=default_value)
    return cast(os.environ.get(key=variable, default=default_value)) \
        if not os.path.exists(ENV_FILE) else config(variable, cast=cast, default=default_value)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env('SECRET', str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env('DEBUG', bool, 0, int)
ENABLE_TEST = get_env('ENABLE_TEST', bool, 0, int)
TEST_TOKEN = get_env('TEST_TOKEN', str, '12345')

# Django global log level
DJANGO_LOG_LEVEL = get_env('DJANGO_LOG_LEVEL', str, 'INFO')

ALLOWED_HOSTS = get_env('ALLOWED_HOSTS', Csv(), [])

# Twilio Tokens
TWILIO_ACCOUNT_SID = get_env('TWILIO_ACCOUNT_SID', str)
TWILIO_AUTH_TOKEN = get_env('TWILIO_AUTH_TOKEN', str)
TWILIO_MOBILE_NUMBER = get_env('TWILIO_MOBILE_NUMBER', str)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps
    'products',
    'accounts',

    # Other apps
    'phonenumber_field',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

ROOT_URLCONF = 'shop-easy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'shop-easy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': get_env('DB_ENGINE', str),
        'HOST': get_env('DB_HOST', str),
        'PORT': get_env('DB_PORT', int),
        'NAME': get_env('DB_NAME', str),
        'USER': get_env('DB_USERNAME', str),
        'PASSWORD': get_env('DB_PASSWORD', str),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIR = {
    os.path.join(BASE_DIR, 'public/static')
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/static')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
