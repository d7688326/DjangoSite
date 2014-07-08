# -*- coding: utf-8 -*-

"""
Django settings for mytravel project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p4d)y7th-!a#ya!^j+z2r%_r7q^s1i8e2rx3)rf5d&)s-tva97'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'south',
    'login',
    'article',
    'crispy_forms',
    'tastypie',
    'defusedxml',
    'coverage',
    'django.contrib.formtools',
    'userprofile',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF ='mytravel.urls'


WSGI_APPLICATION = 'mytravel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel',
        'USER':'d7688326',
        'PASSWORD':'7688326826',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

LOCALES =(
    ('zh-cn', u'简体中文'),
    ('zh-tw', u'繁體中文'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_PATH= os.path.join(PROJECT_PATH,'static')

STATIC_URL = '/static/'

MEDIA_ROOT= os.path.join(PROJECT_PATH,'media')

MEDIA_URL='/media/'

TEMPLATE_DIRS =(
    'polls/templates',
    'article/template',
    'mytravel/template',
    'userprofile/template'

)

# STATIC_ROOT=os.path.join(BASE_DIR, 'polls/')

STATICFILES_DIRS = (
    STATIC_PATH,
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOGIN_URL = '/accounts/login'