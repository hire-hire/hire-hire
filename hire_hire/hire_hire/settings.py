import os
from dataclasses import dataclass, field
from datetime import timedelta
from pathlib import Path

from django.urls import reverse_lazy
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('D_KEY', default='share-like-repost')

DEBUG = os.getenv('DEBUG_MODE', default='ON').lower() in ('on', 'yes', 'true')

ALLOWED_HOSTS = [
    '*'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'sorl.thumbnail',
    'corsheaders',

    'contributors.apps.StaticInfoConfig',
    'duel.apps.DuelsConfig',
    'interview.apps.InterviewConfig',
    'homepage.apps.HomepageConfig',
    'users.apps.UsersConfig',
    'add_question.apps.AddquestionConfig',
    'api.apps.ApiConfig',
    'api_interview.apps.ApiInterviewConfig',
    'api_add_question.apps.ApiAddQuestionConfig',
    'api_donation.apps.ApiDonationConfig',
    'api_duel.apps.ApiDuelConfig',
    'api_users.apps.ApiUsersConfig',
]

if DEBUG:
    INSTALLED_APPS += ['drf_spectacular']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'hire_hire.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.get_login_and_signup_forms',
            ],
            'environment': 'hire_hire.jinja2.environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.get_login_and_signup_forms',
            ],
        },
    },
]

WSGI_APPLICATION = 'hire_hire.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': os.getenv('DB_NAME', default=BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('POSTGRES_USER', default='postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='password'),
        'HOST': os.getenv('DB_HOST', default='localhost'),
        'PORT': os.getenv('DB_PORT', default='5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'users.validators.PasswordMaxLengthValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static_files/'
STATIC_ROOT = BASE_DIR / 'static_files'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    '127.0.0.1',
]

AUTH_USER_MODEL = 'users.User'

DEFAULT_QUESTIONS_COUNT = 10
MAX_QUESTIONS_COUNT_BY_ONE_SESSION = 30
QUESTION_COUNT_CHOICE = (
    (10, '10 вопросов'),
    (20, '20 вопросов'),
    (30, '30 вопросов'),
)

LIMIT_ADD_QUESTIONS_PER_DAY = 1000

ADMIN_PANEL_ADDED_QUESTION_PER_PAGE = 8

LOGIN_URL = reverse_lazy('users:login')
LOGIN_REDIRECT_URL = reverse_lazy('users:profile')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'BLACKLIST_AFTER_ROTATION': False,
}

CSRF_TRUSTED_ORIGINS = [
    'https://hire-hire.proninteam.ru',
    'https://test-hire-hire.proninteam.ru'
]

USERNAME_MIN_LENGTH = 2
USERNAME_MAX_LENGTH = 25
PASSWORD_MAX_LENGTH = 40

LIMIT_CONTRIBUTORS_CONTACTS = 3
THUMBNAIL_SIZE = '1000x1000'

SPECTACULAR_SETTINGS = {
    'TITLE': 'HireHire API',
    'DESCRIPTION': 'Interview service',
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
}

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [
        "https://test-hire-hire.proninteam.ru",
        "https://hire-hire.proninteam.ru",
    ]

CORS_ALLOW_CREDENTIALS = True

DJOSER = {
    'SERIALIZERS': {
        'current_user': 'api_users.serializers.CustomUserSerializer',
    },
}


@dataclass(frozen=True)
class Donation:
    default_currency: str = 'RUB'
    default_description: str = 'Пронину на пиво'
    is_auto_capture_on: bool = True
    currencies: list[tuple[str, str]] = field(
        default_factory=lambda: [('RUB', 'Рубли')],
    )
    api_key: str = 'some_kassa_key'
    shop_id: str = 'some_shop_id'
    return_url: str = 'https://test-hire-hire/donation/callback/'
    api_url: str = 'https://api.yookassa.ru/v3/payments'


DONATION = Donation(
    'RUB',
    'Пронину на пиво',
    True,
    [('RUB', 'Рубли')],
    os.getenv('YOOKASSA_KEY', default='some_kassa_key'),
    os.getenv('YOOKASSA_SHOP_ID', default='some_shop_id'),
    os.getenv(
        'DONATE_CALLBACK',
        default='https://test-hire-hire.proninteam.ru/donation/callback/',
    ),
    os.getenv('YOKASSA_URL', default='https://api.yookassa.ru/v3/payments'),
)
