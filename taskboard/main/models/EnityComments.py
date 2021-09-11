from django.db import models
from main.models.Entity import Entity
import jsonfield

class EntityComments(models.Model):
    objects = models.Manager()
    entity = models.ForeignKey(Entity,on_delete = models.CASCADE)
    person = models.TextField(blank=True,null=True)
    passports = jsonfield.JSONField(blank=True,null=True,default=[])
    category = models.TextField(blank=True,null=True)
    keywords = jsonfield.JSONField(blank=True,null=True,default=[])
    countries = jsonfield.JSONField(blank=True,null=True,default=[])
    ssn = models.TextField(blank=True,null=True)
    io = models.TextField(blank=True,null=True)
    further_information = models.TextField(blank=True,null=True)
    external_sources = models.TextField(blank=True,null=True)
    entered = models.TextField(blank=True,null=True)
    age_date = models.TextField(blank=True,null=True)
    locations = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"