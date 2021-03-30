"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import sys

# import django_heroku 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&u=+3twv5cl(jw-uvtbeng=_58pa^wosv0(o27#=@u6s2q5m!s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Updated the installed apps (03/01/21)
    'django.contrib.sites',
    'crispy_forms',
    # 'exercise',
    # 'django_gamification',
    # 'pinax.badges',
    'exercise.apps.ExerciseConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# Added 03/22
# AUTH_USER_MODEL = 'exercise.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
## The following stack overflow post aided in writing this code
## https://stackoverflow.com/questions/47579644/django-configuring-different-databases
## https://docs.djangoproject.com/en/3.1/ref/settings/#databases
## https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django?fbclid=IwAR22uppxhHcUSnvO73roHVYH3qzRzmP3687S7krh1844c5N49h2l7VTKrrA 
## This site was critical in helping to debug an issue with Travis and automated testing: https://medium.com/analytics-vidhya/provisioning-a-test-postgresql-database-on-heroku-for-your-django-app-febb2b5d3b29
if 'test' in sys.argv:
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dcap1mcbmkirfo',
            'USER': 'rclnkmcxxugxnk',
            'PASSWORD': 'b0a9b9684c9f9e0f3985450566ee881c179f0e2b78956ce2609b39ba9fee27dd',
            'HOST': 'ec2-3-233-43-103.compute-1.amazonaws.com',
            'PORT': 5432,
            'TEST': {
                'NAME': 'dcap1mcbmkirfo', 
            }
        }
    }
else:
    DATABASES = { 
    'default': 
    {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcd2j05latd35a',
        'USER': 'kkkifpshjwhhue',
        'PASSWORD': '456391adf83d19807c430d193ccfe73c37ea28affa4933d4a9e2eb17913f5c8a',
        'HOST': 'ec2-54-198-73-79.compute-1.amazonaws.com',
        'PORT': '5432'
    },
}


SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Specified 'allauth' backend (03/01/21)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Added site id and also specified the redirect URL
# SITE_ID = 0
# Use 5 when deploying to Heroku
SITE_ID = 5
LOGIN_REDIRECT_URL = '/'

# Added 03/22
# ACCOUNT_EMAIL_VERIFICATION = "none"
# ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Way to get user's email addresses when they log in
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# Added 03/19/21
# AUTH_USER_MODEL = 'exercise.User'
# End

# Activate Django-Heroku.
try:
    # Configure Django App for Heroku.
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False

