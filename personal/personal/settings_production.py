from .settings_general import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'personal',
        'USER': 'personal_db',
        'PASSWORD': 'personal_db',
	    'HOST': 'localhost',
        'PORT': '',
    }
}

