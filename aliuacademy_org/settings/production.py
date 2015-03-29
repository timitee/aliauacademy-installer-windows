# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
TESTING = get_env_variable_bool('TESTING')
THUMBNAIL_DEBUG = DEBUG

if get_env_variable_bool('SSL'):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# We are running this site on a LAN so will accept connections from anywhere.
# 'ALLOWED_HOSTS' will be set to '*' in the vassal when on a LAN
ALLOWED_HOSTS = [get_env_variable('ALLOWED_HOSTS'), ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{}_test'.format(SITE_NAME) if TESTING else SITE_NAME,
        'USER': SITE_NAME,
        'PASSWORD': get_env_variable('DB_PASS'),
        'HOST': get_env_variable('DB_IP'),
        'PORT': '',
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = get_env_variable("MEDIA_ROOT")

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = get_env_variable("SENDFILE_ROOT")
SENDFILE_URL = '/private'

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('87.115.141.255',)
