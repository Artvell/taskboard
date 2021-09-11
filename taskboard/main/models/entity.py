"""файл с моделью Entity"""
import uuid
from datetime import datetime
from django.db import models
import jsonfield
from authentification.models import User
from .bio import BIO
from .category import Category
from .keywords import Keywords
from .country import Country


class Entity(models.Model):
    """Модель Entity. Основная модель проекта"""
    choices = [
        (1,"Updated"), #замечания исправлены
        (2,"Pending"), #создано, на проверке
        (3,"Declined"), #возвращено с замечаниями L2
        (4,"Proceeded"), #одобрено L2
        (5,"Approved"), #одобрено L3
        (6,"Declined L3") #возвращено с замечаниями L3
    ]
    objects = models.Manager()
    UUID = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    status = models.IntegerField(choices=choices,default=2)
    person = models.ForeignKey(BIO,on_delete=models.PROTECT)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    keywords = models.ManyToManyField(Keywords)
    countries = models.ManyToManyField(Country)
    ssn = models.CharField(max_length=28)
    io = models.TextField()
    further_information = models.TextField(default="<p>[bio]</p><p>[info]</p><p>[desc]</p>")
    external_sources = jsonfield.JSONField(blank=True,null=True)
    entered = models.DateTimeField()
    editor = models.ForeignKey(User,on_delete=models.PROTECT)
    updated = models.DateTimeField(default=datetime.now(),blank=True,null=True)
    age_date = models.CharField(max_length=100)
    locations = jsonfield.JSONField(blank=True,null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Entity"
        verbose_name_plural = "Entities"
