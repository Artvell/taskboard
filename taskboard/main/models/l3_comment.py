"""файл с моделбю L3Comment"""
from django.db import models
from main.models.entity import Entity

class L3Comment(models.Model):
    """модель L3Comment. Содержит комментарий к Entity"""
    objects = models.Manager()
    entity = models.ForeignKey(Entity,on_delete=models.DO_NOTHING)
    comment = models.TextField()

    def __str__(self):
        return str(self.id)
    