from django.contrib import admin

#Register your models here.
from .models import Message, UserChannel
admin.site.register(Message)
admin.site.register(UserChannel)
