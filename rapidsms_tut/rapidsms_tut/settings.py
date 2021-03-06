# Django settings for rapidsms_tut project.

import os

# The top directory for this project. Contains requirements/, manage.py,
# and README.rst, a rapidsms_tut directory with settings etc (see
# PROJECT_PATH), as well as a directory for each Django app added to this
# project.
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# The directory with this project's templates, settings, urls, static dir,
# wsgi.py, fixtures, etc.
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'rapidsms_tut')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rapidsms_tut_db',
        'USER': 'root',
        'PASSWORD': 'qwikpass421',
        'HOST': '',#empty string indicates localhost
        'PORT': '',#empty string indicates default port
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Kampala'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/public/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/public/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files to collect
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm5zq(e%*e5x&r7g-aq1pap8+r6g15abo4p)&s20ph0&h%azt37'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    #Added for sign-in and out functionality
    "account.context_processors.account",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    #Added for sign-in and out functionality
    "account.middleware.LocaleMiddleware",
    "account.middleware.TimezoneMiddleware",
)

ROOT_URLCONF = 'rapidsms_tut.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'rapidsms_tut.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

# A sample logging configuration.
# This logs all rapidsms messages to the file `rapidsms.log`
# in the project directory.  It also sends an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'basic',
            'filename': os.path.join(PROJECT_PATH, 'rapidsms.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'rapidsms': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',

    # External apps
    "django_tables2",
    "selectable",
    "account",
    # RapidSMS
    #"voting",
    # "tut",
    "webSMS",
    "borehole",
    "rapidsms", 
    "rapidsms.backends.kannel",
    "rapidsms.backends.database",
    #"rapidsms.contrib.locations",
    #"djtables",
    "rapidsms.contrib.handlers",
    "rapidsms.contrib.httptester",
    "rapidsms.contrib.messagelog",
    "rapidsms.contrib.messaging",
    "rapidsms.contrib.registration",
    "rapidsms.contrib.echo", #commented out as instructed by rapidsms tutorial 1
    "rapidsms.contrib.default",  # Must be last
)
#Test: Not sure this is where DEFAULT_RESPONSE goes, but i'm going to try it:
DEFAULT_RESPONSE = "%(project_name)s cannot understand your message"

INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.database.DatabaseBackend",
    },
    "kannel-fake-smsc" : {
        "ENGINE":  "rapidsms.backends.kannel.KannelBackend",
        "sendsms_url": "http://127.0.0.1:13013/cgi-bin/sendsms",
        "sendsms_params": {"smsc": "FAKE",
                           "from": "123", # not set automatically by SMSC
                           "username": "rapidsms",
                           "password": "CHANGE-ME"}, # or set in localsettings.py
        "coding": 0,
        "charset": "ascii",
        "encode_errors": "ignore", # strip out unknown (unicode) characters
        "delivery_report_url": "http://192.168.7.133:8000", #127.168.7.133:8000",
    },
#    "kannel-usb0-smsc" : {
#        "ENGINE":  "rapidsms.backends.kannel.KannelBackend",
#        #"sendsms_url": "http://127.0.0.1:13013/cgi-bin/sendsms",
#        "sendsms_url": "http://192.168.7.133:13013/cgi-bin/sendsms",
#        "sendsms_params": {"smsc": "usb0-modem",
#                           "from": "+2560792138686", # not set automatically by SMSC
#                           "username": "rapidsms",
#                           "password": "CHANGE-ME"}, # or set in localsettings.py
#        "coding": 0,
#        "charset": "ascii",
#        "encode_errors": "ignore", # strip out unknown (unicode) characters
#        "delivery_report_url": "http://192.168.7.133:8000",
#    },
}


LOGIN_REDIRECT_URL = '/'

RAPIDSMS_HANDLERS = (
    "voting.handlers.ResultsHandler",
    "voting.handlers.VoteHandler", 
    "voting.handle.Test",
    "borehole.handlers.UpdateHandler",
    "rapidsms.contrib.echo.handlers.echo.EchoHandler", #commented out for rapidsmsTUT
    "rapidsms.contrib.echo.handlers.ping.PingHandler", #commented out for rapidsmsTUT
)
