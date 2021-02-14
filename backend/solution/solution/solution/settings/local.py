from .base import *

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'solution.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'interview',
        'USER': 'interviewtest_SQLLogin_1',
        'PASSWORD': 'setsx7yjxe',
        'HOST': 'interview.mssql.somee.com',
        'PORT': '',

        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
        },
    },
}

DATABASE_CONNECTION_POOLING = False

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
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

