"""
Django settings for ecommerce project.
"""

from pathlib import Path

from decouple import config

import dj_database_url



BASE_DIR = Path(__file__).resolve().parent.parent





# ======================
# SECURITY
# ======================

SECRET_KEY = config(
    "SECRET_KEY"
)


DEBUG = config(
    "DEBUG",
    default=False,
    cast=bool
)



ALLOWED_HOSTS = [

    "localhost",

    "127.0.0.1",

    ".onrender.com",

]







# ======================
# APPLICATIONS
# ======================

INSTALLED_APPS = [

    "cloudinary_storage",


    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",



    "store",
    "cart",
    "orders",
    "accounts",



    "rest_framework",
    "rest_framework.authtoken",

    "django_filters",

    "drf_spectacular",



    "cloudinary",

]







# ======================
# MIDDLEWARE
# ======================


MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",


    "whitenoise.middleware.WhiteNoiseMiddleware",


    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]







ROOT_URLCONF = "ecommerce.urls"



WSGI_APPLICATION = "ecommerce.wsgi.application"








# ======================
# TEMPLATES
# ======================


TEMPLATES = [

    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",


        "DIRS": [

            BASE_DIR / "templates"

        ],


        "APP_DIRS": True,


        "OPTIONS": {


            "context_processors": [


                "django.template.context_processors.request",


                "django.contrib.auth.context_processors.auth",


                "django.contrib.messages.context_processors.messages",


            ],

        },

    },

]









# ======================
# DATABASE - NEON
# ======================


DATABASES = {


    "default": dj_database_url.config(


        default=config(

            "DATABASE_URL"

        )

    )

}








# ======================
# PASSWORD VALIDATION
# ======================


AUTH_PASSWORD_VALIDATORS = [

    {

        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",

    },


    {

        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",

    },


    {

        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",

    },


    {

        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",

    },


]








# ======================
# INTERNATIONALIZATION
# ======================


LANGUAGE_CODE = "en-us"


TIME_ZONE = "UTC"


USE_I18N = True


USE_TZ = True








# ======================
# STATIC FILES
# ======================


STATIC_URL = "/static/"


STATIC_ROOT = BASE_DIR / "staticfiles"
WHITENOISE_USE_FINDERS = True


STATICFILES_DIRS = [

    BASE_DIR / "static"

]



# for django-cloudinary-storage compatibility

STATICFILES_STORAGE = (

    "whitenoise.storage.StaticFilesStorage"

)









# ======================
# CLOUDINARY MEDIA
# ======================


MEDIA_URL = "/media/"



CLOUDINARY_STORAGE = {


    "CLOUD_NAME": config(

        "CLOUD_NAME"

    ),



    "API_KEY": config(

        "API_KEY"

    ),



    "API_SECRET": config(

        "API_SECRET"

    ),

}








# Django 6 storage system

STORAGES = {


    "default": {


        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",

    },



    "staticfiles": {


        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",

    },


}










# ======================
# AUTH
# ======================


LOGIN_REDIRECT_URL = "/"


LOGOUT_REDIRECT_URL = "/"


LOGIN_URL = "/accounts/login/"









# ======================
# DJANGO REST FRAMEWORK
# ======================


REST_FRAMEWORK = {


    "DEFAULT_AUTHENTICATION_CLASSES": [

        "rest_framework.authentication.TokenAuthentication",

    ],




    "DEFAULT_PERMISSION_CLASSES": [

        "rest_framework.permissions.IsAuthenticatedOrReadOnly",

    ],





    "DEFAULT_PAGINATION_CLASS":

        "rest_framework.pagination.PageNumberPagination",




    "PAGE_SIZE":

        5,






    "DEFAULT_FILTER_BACKENDS": [


        "django_filters.rest_framework.DjangoFilterBackend",


        "rest_framework.filters.SearchFilter",


        "rest_framework.filters.OrderingFilter",


    ],






    "DEFAULT_SCHEMA_CLASS":

        "drf_spectacular.openapi.AutoSchema",


}