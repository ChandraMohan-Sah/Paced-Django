create :
    routing.py ---> similar to urls.py      [import namespace: from djnago.urls import path ]
    consumers.py ---> similar to views.py   [import namespace: from channels.generic.websocket import WebsocketConsumer]
    
    (
        We have created routing, consumers but how can we tell
        django that if there is a connection ; that will come using websocket
        protocol.[routing-->consumer].

        for that we have to tell django.lets configure:
            #----------------------------------------------------------------------
            1. asgi.py file [main project directory]

            '''
                #asgi config 
                from channels.routing import ProtocolTypeRouter, URLRouter 
                from app9_async.app9_api import routing

                # application = get_asgi_application() : initially this is the file

                application = ProtocolTypeRouter({
                    "http":get_asgi_application(),
                    "websocket":URLRouter(
                        routing.ASGI_urlpatterns
                    )
                })
            '''


            2. configure daphne server instead of development server
               :because of daphne server we can use asgi applications.
            '''
                -Keep 'channels', 'daphne' inside installed apps
                ###
                    Add this belows line in 'settings.py'
                    ASGI_APPLICATION = 'Paced_Django.asgi.application'
            '''

            3.Run the server now.


    )

    Step 2 : Simple code to check connection.
    <script>
        //connecting to the websocket 
        const url = `ws://127.0.0.1:8000/websocket`;
        const chat_websocket = new WebSocket(url);
    </script>

    Step 3: Simple code to connect websocket from client side  to django/backend/consumers.py.
    

