import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Paced_Django.settings')



#asgi config 
from channels.routing import ProtocolTypeRouter, URLRouter 
from app9_async.app9_api import routing

'''adding user and session in asgi application'''
# from channels.sessions import SessionMiddlewareStack  #only Session Acceptance
# from channels.auth import AuthMiddleware              #only User Acceptance
from channels.auth import AuthMiddlewareStack           #both user and session


# Wrap the WebSocket connection in both session and auth middleware
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(            # Adds user ,authentication both
            URLRouter(routing.ASGI_urlpatterns)
        )
})




