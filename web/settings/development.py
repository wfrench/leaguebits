from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': 'db',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

#INSTALLED_APPS += [
#    'debug_toolbar',
#]
#
#MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
#
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
#DEBUG_TOOLBAR_CONFIG = {
#    'JQUERY_URL': '',
#}
