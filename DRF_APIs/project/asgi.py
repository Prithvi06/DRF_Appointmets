"""
ASGI config for dwyloapp_API project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
# import patient.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.dev')

application = get_asgi_application()

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             patient.routing.websocket_urlpatterns
#         )
#     ),
# })