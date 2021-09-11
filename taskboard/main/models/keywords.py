"""файл с моделью Keywords"""
from django.db import models

class Keywords(models.Model):
    """модель Keywords. Содержит теги. Поле - название тега"""
    objects = models.Manager()
    keyword = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"
