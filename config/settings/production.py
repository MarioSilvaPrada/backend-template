
from .base import *

DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
CORS_ORIGIN_WHITELIST = os.environ.get("CORS").split(" ")

ENODE_CLIENT_ID = os.environ.get('ENODE_CLIENT_ID', default=None)
ENODE_CLIENT_SECRET = os.environ.get('ENODE_CLIENT_SECRET', default=None)
