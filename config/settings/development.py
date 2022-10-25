
from datetime import timedelta
from .base import *

DEBUG = True

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware',)


SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(hours=2)

ENODE_CLIENT_ID = os.environ.get('ENODE_CLIENT_ID_SANDBOX', default=None)
ENODE_CLIENT_SECRET = os.environ.get(
    'ENODE_CLIENT_SECRET_SANDBOX', default=None)
