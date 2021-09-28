from django.db import models

# Create your models here.

class Home(models.Model):
    user = models.CharField(max_length=25)