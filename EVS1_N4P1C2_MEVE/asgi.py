"""
ASGI config for EVS1_N4P1C2_MEVE project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EVS1_N4P1C2_MEVE.settings')

application = get_asgi_application()
