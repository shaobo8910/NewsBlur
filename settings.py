import sys
import logging
import os

# Route all 'print' statements to Apache
sys.stdout = sys.stderr

# ===========================
# = Directory Declaractions =
# ===========================

CURRENT_DIR = os.path.dirname(__file__)
NEWSBLUR_DIR = CURRENT_DIR
TEMPLATE_DIRS = (''.join([CURRENT_DIR, '/templates']),)
MEDIA_ROOT = ''.join([CURRENT_DIR, '/media'])
UTILS_ROOT = ''.join([CURRENT_DIR, '/utils'])
LOG_FILE = ''.join([CURRENT_DIR, '/logs/newsblur.log'])

# ==============
# = PYTHONPATH =
# ==============

COMPRESS_DIR = ''.join([CURRENT_DIR, '/utils/django-compress'])
if 'django-compress' not in ' '.join(sys.path):
    sys.path.append(COMPRESS_DIR)

# ===================
# = Global Settings =
# ===================

DEBUG = False
ADMINS = (
    ('Robert Samuel Clay', 'samuel@ofbrooklyn.com'),
)
MANAGERS = ADMINS

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
LOGIN_REDIRECT_URL = '/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'
SECRET_KEY = '6yx-@2u@v$)-=fqm&tc8lhk3$6d68+c7gd%p$q2@o7b4o8-*fz'

# ===============
# = Enviornment =
# ===============

PRODUCTION = __file__.find('/home/conesus/newsblur') == 0
STAGING = __file__.find('/home/conesus/stg-newsblur') == 0
DEV_SERVER1 = __file__.find('/Users/conesus/Projects/newsblur') == 0
DEV_SERVER2 = __file__.find('/Users/conesus/newsblur') == 0
DEVELOPMENT = DEV_SERVER1 or DEV_SERVER2

if PRODUCTION:
    DATABASE_ENGINE = 'mysql'
    DATABASE_NAME = 'newsblur'
    DATABASE_USER = 'newsblur'
    DATABASE_PASSWORD = ''
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = ''
    # Absolute path to the directory that holds media.
    # Example: "/Users/media/media.lawrence.com/"
    MEDIA_URL = 'http://www.newsblur.com/media/'
    DEBUG = False
    CACHE_BACKEND = 'file:///var/tmp/django_cache'
    logging.basicConfig(level=logging.WARN,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOG_FILE,
                    filemode='w')
elif STAGING:
    DATABASE_ENGINE = 'mysql'
    DATABASE_NAME = 'newsblur'
    DATABASE_USER = 'newsblur'
    DATABASE_PASSWORD = ''    
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = ''         

    # Absolute path to the directory that holds media.
    # Example: "/Users/media/media.lawrence.com/"
    MEDIA_URL = '/media/'
    DEBUG = True
    CACHE_BACKEND = 'file:///var/tmp/django_cache'
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOG_FILE,
                    filemode='w')
elif DEV_SERVER1:
    DATABASE_ENGINE = 'mysql'
    DATABASE_NAME = 'newsblur'
    DATABASE_USER = 'newsblur'
    DATABASE_PASSWORD = ''    
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = ''         

    # Absolute path to the directory that holds media.
    # Example: "/Users/media/media.lawrence.com/"
    MEDIA_URL = '/media/'
    DEBUG = True
    CACHE_BACKEND = 'dummy:///'
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOG_FILE,
                    filemode='w')
elif DEV_SERVER2:
    DATABASE_ENGINE = 'mysql'
    DATABASE_NAME = 'newsblur'
    DATABASE_USER = 'newsblur'
    DATABASE_PASSWORD = ''    
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = ''         

    # Absolute path to the directory that holds media.
    # Example: "/Users/media/media.lawrence.com/"
    MEDIA_URL = '/media/'
    DEBUG = True
    CACHE_BACKEND = 'dummy:///'
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOG_FILE,
                    filemode='w')

TEMPLATE_DEBUG = DEBUG

# ===========================
# = Django-specific Modules =
# ===========================

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'djangologging.middleware.LoggingMiddleware',
)


# =====================
# = Media Compression =
# =====================

COMPRESS_JS = {
    'all': {
        'source_filenames': (
            'js/jquery-1.3.2.js',
            'js/jquery.easing.js',
            'js/jquery.newsblur.js',
            'js/jquery.scrollTo.js',
            'js/jquery.timers.js',
            'js/jquery.corners.js',
            'js/jquery.hotkeys.js',
            'js/jquery.dropshadow.js',
            'js/jquery.ajaxupload.js',
            'js/jquery.simplemodal-1.3.js',
            'js/jquery.color.js',
            'js/jquery-ui-1.7.2.custom.min.js',
            'js/jquery.layout.js',
            
            'js/newsblur/assetmodel.js',
            'js/newsblur/reader.js'
        ),
        'output_filename': 'js/all-compressed-?.js'
    }
}

COMPRESS_CSS = {
    'all': {
        'source_filenames': (
            'css/reader.css',
        ),
        'output_filename': 'css/all-compressed-?.css'
    }
}

# COMPRESS = True
COMPRESS_AUTO = True
COMPRESS_VERSION = True
COMPRESS_JS_FILTERS = ['compress.filters.yui.YUICompressorFilter']
COMPRESS_CSS_FILTERS = []

YUI_DIR = ''.join([UTILS_ROOT, '/yuicompressor-2.4.2/build/yuicompressor-2.4.2.jar'])
COMPRESS_YUI_BINARY = 'java -jar ' + YUI_DIR
# COMPRESS_YUI_JS_ARGUMENTS = '--preserve-semi --nomunge --disable-optimizations'

# ==========================
# = Miscellaneous Settings =
# ==========================

AUTH_PROFILE_MODULE = 'newsblur.UserProfile'
TEST_DATABASE_COLLATION = 'utf8_general_ci'
ROOT_URLCONF = 'urls'
INTERNAL_IPS = ('127.0.0.1',)
LOGGING_LOG_SQL = True

# ===============
# = Django Apps =
# ===============

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'utils.django_extensions',
    'compress',
    'apps.rss_feeds',
    'apps.reader',
    'apps.analyzer',
    'apps.registration',
    'apps.opml_import',
    'apps.profile',
)
