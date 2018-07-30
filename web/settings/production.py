from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'webapp',
        'PASSWORD': 'UI7s!YgVI6QtUMdpIhtf&zyJ#f0G',
        'HOST': 'leaguebit.cttompnysgnr.us-west-1.rds.amazonaws.com',   
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
