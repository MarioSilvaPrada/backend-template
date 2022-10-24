
from .base import *

DEBUG = True

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware',)


ACCESS_TOKEN_LIFETIME = 1000

ENODE_CLIENT_ID = os.environ.get('ENODE_CLIENT_ID_SANDBOX', default=None)
ENODE_CLIENT_SECRET = os.environ.get(
    'ENODE_CLIENT_SECRET_SANDBOX', default=None)
