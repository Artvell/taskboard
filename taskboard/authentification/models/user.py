"""файл с моделью User"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Расширенная модель для хранения данных пользователя.
    Добавлено обязательное поле Роль.
    Поле email теперь обязательно и уникально
    """
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,verbose_name="Роль")
    REQUIRED_FIELDS = ['email','role']
    def __str__(self):
        return self.username
