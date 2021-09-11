from django.db import models
from .User import User

class TmpPass(models.Model):
    objects=models.Manager()
    username = models.CharField(max_length=23,unique=True)
    password = models.CharField(max_length=15,unique=True)