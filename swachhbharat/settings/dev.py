import sys
import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm2@z#2sq(v!6*6@c3r&4x)c0k-=qbu^im7f2gooc$7y@_347#m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if sys.platform == 'darwin':
    # Setting for spatialite on OS X
    SPATIALITE_LIBRARY_PATH = '/usr/local/lib/mod_spatialite.dylib'

if os.path.exists('/usr/lib/x86_64-linux-gnu/mod_spatialite.so'):
    # Setting for GNU/Linux systems with spatialite 4.2+
    SPATIALITE_LIBRARY_PATH = 'mod_spatialite'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3.dev'),
    }
}
