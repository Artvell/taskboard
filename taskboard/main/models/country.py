"""Файл с моделью Country"""
from django.db import models

class Country(models.Model):
    """модель Country. Информация о стране. Поле: название страны"""
    objects = models.Manager()
    country = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
