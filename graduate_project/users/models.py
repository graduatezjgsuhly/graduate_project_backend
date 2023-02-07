from django.db import models
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    phonenumber = models.CharField (max_length=200)
    passwd = models.CharField(max_length=200)
