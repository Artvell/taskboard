"""файл с классом UserCreationForm, переопределенной формой для создания юзеров"""
from random import choice
from string import ascii_uppercase,ascii_lowercase , digits
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from authentification.models import User, TmpPass
from authentification.functions import Encoder,SendMail

class UserCreationForm(forms.ModelForm):
    """Форма для создания новых юзеров. Сордержит поля стандартной формы и поле Роль"""
    role = forms.CharField(label="Роль", max_length=20)
    available_roles = ["L1","L2","L3","admin"]
    def clean_role(self):
        """"Валидирует данные из поля Роль"""
        data = self.cleaned_data['role']
        if data not in self.available_roles:
            raise ValidationError("Доступные роли: {}".format(",".join(self.available_roles)))
        return data

    class Meta:
        model = User
        fields = ('email', 'role')

    def save(self, commit=True):
        """Переопределенный метод сохранения
        Генерирует случайный пароль и хэширует его
        Генерирует случайный логи
        Отправляет письмо на указанный мэйл"""
        user = super().save(commit=False)
        user_pass = ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(15))
        user.set_password(user_pass)
        username = "{}_{}".format(user.role,
                                ''.join(choice(ascii_uppercase + ascii_lowercase + digits)
                                    for _ in range(12))
                                )
        user.username = username
        user.is_active = False
        encoded_username = Encoder(username).encode()
        pattern = "Перейдите по ссылке: {}api/auth/activateUser/{}/ для активации вашего аккаунта"
        text = pattern.format(settings.DEFAULT_DOMAIN,encoded_username)
        SendMail(text,[user.email]).send()
        TmpPass(username=username,password=user_pass).save()
        if commit:
            user.save()
        return user
