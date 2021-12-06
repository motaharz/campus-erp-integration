import os
import django
from decouple import config
from mongoengine import connect, disconnect

DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = []
PAYMENT_LIB_DIR = BASE_DIR

mongodb_host = config('MONGODB_HOST')
mongodb_database = config('MONGODB_DATABASE')
mongodb_port = config('MONGODB_PORT')
mongodb_username = config('MONGODB_USERNAME')
mongodb_password = config('MONGODB_PASSWORD')
mongodb_auth_database = config('MONGODB_AUTH_DATABASE')

disconnect()
connect(mongodb_database, host=mongodb_host, port=int(mongodb_port), username=mongodb_username, password=mongodb_password, authentication_source=mongodb_auth_database)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'shared_models',
    'rest_framework',
    'rest_framework_api_key'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME', ''),
        'USER': config('DATABASE_USER', ''),
        'PASSWORD': config('DATABASE_PASSWORD', ''),
        'HOST': config('DATABASE_HOST', ''),
        'PORT': config('DATABASE_PORT', ''),
    }
}


def initialize_django():
    # Django stuff begins
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)
    django.setup()
