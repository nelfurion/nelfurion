"""
WSGI config for nelfurion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from nelfurion.settings import STATIC_ROOT

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nelfurion.settings")

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
