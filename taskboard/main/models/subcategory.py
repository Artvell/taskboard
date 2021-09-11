"""файл с моделью Subcategory"""
from django.db import models
from main.models.category import Category

class Subcategory(models.Model):
    """модель Subcategory. Связана с Category.
    Поля: категория, название, описание.
    """
    objects = models.Manager()
    category = models.ForeignKey(Category,
                                related_name="subcategories",
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    title = models.CharField(max_length=34)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
