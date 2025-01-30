from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        self.send('{"type":"accept", "status":"accepted"}')

        # print(self.scope)
        print(self.scope.get("user"))
        print(self.scope.get("user").id)
        print(self.scope.get("session"))
        print(self.scope.get("session").get("get_me_from_the_consumer"))
        print(self.scope.get("url_route")) #Its like dynamic segment in urls.py


        '''about layers'''
        # print(self.channel_layer)
        # print(type(self.channel_layer))
        print(self.channel_name)
        print(self.channel_layer.channels)
        print("Channel Groups is given Below :")
        print(self.channel_layer.groups)


        '''Creating a Group asynchronously'''
        async_to_sync(self.channel_layer.group_add)("momo_group", self.channel_name)
        print("After creating Channel Groups dict is given Below :")
        print(self.channel_layer.groups)

        '''Sending data to different channels'''
        data = {
            "type":"receiver_function", #search for this function
            "message":"Hi, my name is cms",
            "my last name":"Sah"
        }
        async_to_sync(self.channel_layer.send)(self.channel_name, data)


        '''Sending data to a group'''
        async_to_sync(self.channel_layer.group_add)("group_channels", self.channel_name)
        data = {
            "type":"receiver_function", #search for this function
            "message":"Message sent in a group.",
        }
        async_to_sync(self.channel_layer.group_send)("group_channels", data)
        

    def receive(self, text_data):
        print(text_data)

        #this sends a message to the client that message has been arrived
        self.send('{"type":"message_arrived", "status":"arrived"}')


    def disconnect(self, code):
        print(code)
        print("Hello, The connection is disconnected or stoped.")

    
    def receiver_function(self, the_data_that_wil_come_from_the_layer):
        print(the_data_that_wil_come_from_the_layer)





