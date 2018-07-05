from .base import * 
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["django-project-miguelmargar.c9users.io", "miguel-django-project.herokuapp.com"]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')