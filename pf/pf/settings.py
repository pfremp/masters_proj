"""
Django settings for pf project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oi!60kkg4)9^l+(81x_dl@07!j&dhvppljy+foks_19z#_3sx+'

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
    'part_finder',
    'bootstrap3',
    'bootstrap3_datetime',
    'datetimewidget',
    # 'django.contrib.formtools',
    'django.core.mail',
    'cities_light',
    'autocomplete_light',
    # 'django-formtools',
    'formtools',


    #allauth
    # The Django sites framework is required
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.angellist',
    # 'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.coinbase',
    # 'allauth.socialaccount.providers.dropbox',
    # 'allauth.socialaccount.providers.dropbox_oauth2',
    # 'allauth.socialaccount.providers.evernote',
    # # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.flickr',
    # 'allauth.socialaccount.providers.feedly',
    # 'allauth.socialaccount.providers.fxa',
    # 'allauth.socialaccount.providers.github',
     'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.hubic',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.spotify',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.weibo',
    # 'allauth.socialaccount.providers.xing',

)

SITE_ID = 1

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/part_finder/login_success/'


#all auth settings
ACCOUNT_ADAPTER ="allauth.account.adapter.DefaultAccountAdapter"
# ACCOUNT_ADAPTER = "part_finder.allauth.AccountAdapter"

ACCOUNT_AUTHENTICATION_METHOD ="username_email"

ACCOUNT_CONFIRM_EMAIL_ON_GET = False

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL =None

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "optional"

ACCOUNT_EMAIL_SUBJECT_PREFIX ="[Site] "

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

# ACCOUNT_FORMS ={}
  # Used to override forms, for example:
  # `{'login': 'myapp.forms.LoginForm'}`

ACCOUNT_LOGOUT_ON_GET =False

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE =False

ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

ACCOUNT_SIGNUP_FORM_CLASS = 'part_finder.forms.SignupForm'

ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

ACCOUNT_UNIQUE_EMAIL =True

ACCOUNT_USER_MODEL_USERNAME_FIELD ="username"
  # The name of the field containing the `username`, if any. See custom
  # user models.

ACCOUNT_USER_MODEL_EMAIL_FIELD ="email"
  # The name of the field containing the `email`, if any. See custom
  # user models.

# ACCOUNT_USER_DISPLAY (=a callable returning `user.username`)
  # A callable (or string of the form `'some.module.callable_name'`)
  # that takes a user as its only argument and returns the display name
  # of the user. The default implementation returns `user.username`.

ACCOUNT_USERNAME_MIN_LENGTH = 1

ACCOUNT_USERNAME_BLACKLIST =[]

ACCOUNT_USERNAME_REQUIRED =True

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE =False

ACCOUNT_PASSWORD_MIN_LENGTH =6

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True

ACCOUNT_SESSION_REMEMBER =None

ACCOUNT_SESSION_COOKIE_AGE =1814400

SOCIALACCOUNT_ADAPTER ="allauth.socialaccount.adapter.DefaultSocialAccountAdapter"

SOCIALACCOUNT_QUERY_EMAIL =ACCOUNT_EMAIL_REQUIRED

SOCIALACCOUNT_AUTO_SIGNUP =False

SOCIALACCOUNT_EMAIL_REQUIRED =ACCOUNT_EMAIL_REQUIRED

SOCIALACCOUNT_EMAIL_VERIFICATION =ACCOUNT_EMAIL_VERIFICATION

SOCIALACCOUNT_FORMS ={}

# SOCIALACCOUNT_PROVIDERS = dict

SOCIALACCOUNT_STORE_TOKENS =True

SOCIALACCOUNT_PROVIDERS = \
    { 'google':
        { 'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': { 'access_type': 'online' } }}

# When I sign up I run into connectivity errors (connection refused et al)
#https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'pf.urls'

WSGI_APPLICATION = 'pf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_LOADER = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.part_finder.Loader',
)

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

# TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates',),)


STATIC_PATH = os.path.join(BASE_DIR, 'static')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    STATIC_PATH,
)


#Not safe for deployment- chapter 5.5
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Absolute path to the media directory

#django all auth
TEMPLATE_CONTEXT_PROCESSORS = (

    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    # "django.contrib.messages.context_processors.messages",
    # Required by `allauth` template tags
    'django.core.context_processors.request',

    # `allauth` specific context processors
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',

    'django.contrib.auth.context_processors.auth',

)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

#Datetime picker

USE_L10N = True
USE_TZ = True
USE_I18N = True

#
# Django cities
CITIES_LIGHT_TRANSLATION_LANGUAGES = ['en']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['GB', 'FR']

SOUTH_MIGRATION_MODULES = {
    'cities_light': 'cities_light.south_migrations',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'cities_light': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
        # also use this one to see SQL queries
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}