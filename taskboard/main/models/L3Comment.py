from django.db import models
from main.models.Entity import Entity

class L3Comment(models.Model):
    objects = models.Manager()
    entity = models.ForeignKey(Entity,on_delete=models.DO_NOTHING)
    comment = models.TextField()

    def __str__(self):
        return str(self.id)
    