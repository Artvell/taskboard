"""файл с моделью BIO"""
from django.db import models
import jsonfield

class BIO(models.Model):
    """Модель BIO. Базовая информация о человеке/организации"""
    ei_choices = [
        (1,"Мужской"),
        (2,"Женский"),
        (3,"Не определен"),
        (4, "Нет")
    ]
    status_choices = [
        (1,"Физическое лицо"),
        (2,"Юридическое лицо")
    ]
    objects = models.Manager()
    first_name = models.CharField(max_length=92,null=True,blank=True)
    last_name = models.CharField(max_length=230,null=True,blank=True)
    place_of_birth = models.CharField(max_length=255)
    birth_date = models.DateField()
    deceased_date = models.DateField()
    aliases = jsonfield.JSONField(null=True,blank=True)
    low_quality_aliases = jsonfield.JSONField(null=True,blank=True)
    alternative_spelling = jsonfield.JSONField(null=True,blank=True)
    ei = models.IntegerField(choices=ei_choices,default=3)
    status = models.IntegerField(choices=status_choices,default=1)
    def __str__(self):
        return self.first_name
