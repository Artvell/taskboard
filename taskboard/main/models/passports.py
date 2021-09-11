"""Файл с моделью Passport"""
from django.db import models
from main.models.bio import BIO
from main.models.country import Country

class Passport(models.Model):
    """
    модель Passport.
    Содержит информацию о паспорте.
    Поля: человек, номер паспорта, гражданство, страна
    """
    objects = models.Manager()
    entity = models.ForeignKey('Entity',
                                on_delete=models.DO_NOTHING,
                                related_name="passports",
                                blank=True,
                                null=True)
    person = models.ForeignKey(BIO,on_delete=models.CASCADE)
    pass_code = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.pass_code
