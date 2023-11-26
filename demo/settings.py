import logging
import os

from os import path

logger = logging.getLogger(__name__)

DEBUG = True
TEMPLATE_DEBUG = True
USE_TZ = True
USE_L10N = True

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "demo.db"}}

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # -------------------- BEGIN Microsoft Auth -----------------------
    "django.contrib.sites",
    "microsoft_auth",
    # -------------------- END Microsoft Auth -------------------------
    "django_extensions",
    "my_app",
)

MIDDLEWARE = [
    # default django middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

PROJECT_DIR = path.abspath(path.join(path.dirname(__file__)))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                # -------------------- BEGIN Microsoft Auth -----------------------
                "microsoft_auth.context_processors.microsoft",
                # -------------------- END Microsoft Auth -------------------------
            ]
        },
    }
]

STATIC_URL = "/static/"

SECRET_KEY = "secret"  # noqa: S105

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(levelname)s %(message)s"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
    "loggers": {
        "": {"handlers": ["console"], "propagate": True, "level": "DEBUG"},
        # 'django': {
        #     'handlers': ['console'],
        #     'propagate': True,
        #     'level': 'WARNING',
        # },
    },
}

ROOT_URLCONF = "demo.urls"

# -------------------- BEGIN Microsoft Auth -----------------------
AUTHENTICATION_BACKENDS = [
    "microsoft_auth.backends.MicrosoftAuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]

SITE_ID = 1

MICROSOFT_AUTH_CLIENT_ID = os.getenv("MSAUTH_CLIENT_ID")
MICROSOFT_AUTH_CLIENT_SECRET = os.getenv("MSAUTH_CLIENT_SECRET")
MICROSOFT_AUTH_TENANT_ID = os.getenv("MSAUTH_TENANT_ID")
if all([MICROSOFT_AUTH_CLIENT_ID, MICROSOFT_AUTH_CLIENT_SECRET, MICROSOFT_AUTH_TENANT_ID]):
    MICROSOFT_AUTH_LOGIN_ENABLED = True
else:
    logger.warning("Disabling Microsoft authentication backend because not all environment variables "
                   "(MSAUTH_CLIENT_ID, MSAUTH_CLIENT_SECRET, MSAUTH_TENANT_ID) are set!")

    MICROSOFT_AUTH_LOGIN_ENABLED = False

MICROSOFT_AUTH_LOGIN_TYPE = "ma"
MICROSOFT_AUTH_AUTHENTICATE_HOOK = "my_app.auth.on_user_login"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# -------------------- END Microsoft Auth -------------------------

if not DEBUG:
    raise Exception("This settings file can only be used with DEBUG=True")
