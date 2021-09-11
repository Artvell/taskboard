"""файл с моделью TmpPass для временного хранения паролей"""
from django.db import models

class TmpPass(models.Model):
    """Модель для временного хранения паролей"""
    objects=models.Manager()
    username = models.CharField(max_length=23,unique=True)
    password = models.CharField(max_length=15,unique=True)
