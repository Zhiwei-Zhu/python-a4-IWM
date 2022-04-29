from django.db import models

# Create your models here.
class Questions(models.Model):
    text = models.CharField(max_length=200)

