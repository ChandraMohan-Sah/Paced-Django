
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from app9_async import models 
from django.contrib.auth.models import User
import datetime

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        self.send('{"type":"accept", "status":"accepted"}')
        # print(self.scope.get("url_route").get("kwargs").get("id"))
        self.person_id = self.scope.get("url_route").get("kwargs").get("id")

        try:
            user_channel = models.UserChannel.objects.get(user=self.scope.get("user"))
            user_channel.channel_name = self.channel_name
            user_channel.save()
        except:
            user_channel = models.UserChannel()
            user_channel.user = self.scope.get("user")
            user_channel.channel_name = self.channel_name
            user_channel.save()


    def receive(self, text_data):
            print(text_data)
            text_data = json.loads(text_data)
            print(text_data.get("type"))
            print(text_data.get("message"))

            # We received message from client side : 
            # Now we want to save this in database. Let's Create database and save emssage

            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
            time = now.strftime("%H:%M:%S")  # Format time as HH:MM:SS

            other_user = User.objects.get(id=self.person_id)
            new_message = models.Message()
            new_message.from_who = self.scope.get("user")
            new_message.to_whom = other_user
            new_message.message = text_data.get("message")
            new_message.date = date
            new_message.time = time
            new_message.as_been_seen = False
            new_message.save()



            try:
                user_channel_name = models.UserChannel.objects.get(user=other_user)

                #Creating data that can be sent to another client 
                data = {
                    "type":"receiver_function",
                    "type_of_data": "new_message",
                    "data" : text_data.get("message"),
                    "date": date,
                    "time": time
                }

                #Finally sending te data to specific channel
                async_to_sync(self.channel_layer.send)(user_channel_name.channel_name, data)
            except:
                print("Error")



    def receiver_function(self, the_data_that_wil_come_from_the_layer):
        # print(the_data_that_wil_come_from_the_layer)
        data = json.dumps(the_data_that_wil_come_from_the_layer)
        print(the_data_that_wil_come_from_the_layer)
        self.send(data)





