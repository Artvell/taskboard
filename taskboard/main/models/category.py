"""файл с моделью Category"""
from django.db import models

class Category(models.Model):
    """модель Category. Поля: название категории и ее описание"""
    objects = models.Manager()
    title = models.CharField(max_length=34,unique=True)
    description = models.CharField(max_length=50)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
