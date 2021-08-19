import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)28zqq*$sb26ae=4&#k$2l_s50&bz=3p3k=*z@+sn&c)hn*loc'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "buildcareer.herokuapp.com", "localhost"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'crispy_forms',

    'company.apps.CompanyConfig',
    'job.apps.JobConfig',
    'user.apps.UserConfig',

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

ROOT_URLCONF = 'build_career.urls'

TEMPLATE_DIR1 = os.path.join(BASE_DIR, "Templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR1, ],
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

WSGI_APPLICATION = 'build_career.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd4abf5hmiikjf4',
        'HOST': 'ec2-52-1-115-6.compute-1.amazonaws.com',
        'USER': 'oaixfjvttbxqwy',
        'PASSWORD': 'b1df6f3cffca7d34cefc6aa5b55bab9ead8f32bfe9f3aaaebd767bd956a69e0e'
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_dir")
STATIC_DIR1 = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [STATIC_DIR1, ]

MEDIA_ROOT = os.path.join(BASE_DIR, "static/images")
MEDIA_URL = "/images/"

CRISPY_TEMPLATE_PACK = "bootstrap4"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
