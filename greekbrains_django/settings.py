"""
Django settings for greekbrains_django project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')d+f3au_oi)lww15a*wiba39hn)!66a+9ly!$v@h%p2@l=p*e@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',# Фреймворк аутентификации и моделей по умолчанию.
    'django.contrib.contenttypes',# Django контент-типовая система (даёт разрешения, связанные с моделями).
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'psycopg2',
    'main',
    'products',
    'products2',
    'account'
]

AUTH_USER_MODEL = 'account.AccountUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',# Управление сессиями между запросами
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',# Связывает пользователей, использующих сессии, запросами.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'greekbrains_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'main/templates'),
            os.path.join(BASE_DIR, 'products/templates'),
            os.path.join(BASE_DIR, 'account/templates'),
            os.path.join(BASE_DIR, 'greekbrains_django','templates'),
        ]
        ,
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

WSGI_APPLICATION = 'greekbrains_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.postgresql',
    # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db_default',  # Or path to database file if using sqlite3. #!Базу вписывать здесь!
        'USER': 'postgres',  # Not used with sqlite3.
        'PASSWORD': '12345',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',},
'products': {
        'ENGINE': 'django.db.backends.postgresql',
    # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db1',  # Or path to database file if using sqlite3. #!Базу вписывать здесь!
        'USER': 'postgres',  # Not used with sqlite3.
        'PASSWORD': '12345',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',
    },
    'products2': {
         'ENGINE': 'django.db.backends.postgresql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db2',           # Or path to database file if using sqlite3. #!Базу вписывать здесь!
        'USER': 'postgres',                        # Not used with sqlite3.
        'PASSWORD': '12345',                       # Not used with sqlite3.
        'HOST': '',                                # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [ #Кастомные файлы статики
    os.path.join(BASE_DIR, 'greekbrains_django', 'static'),
    #os.path.join(BASE_DIR, 'account', 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGIN_REDIRECT_URL="/"


DATABASE_ROUTERS = ['products.databaseRouter.ProductsDBRouter', 'products2.databaseRouter.Products2DBRouter']


