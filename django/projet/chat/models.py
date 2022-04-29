from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
     name = models.CharField(max_length=200)

class Message(models.Model):
    room = models.CharField(max_length=255)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)


