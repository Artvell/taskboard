from django import forms
from authentification.models import User, TmpPass
from random import choice
from string import ascii_uppercase,ascii_lowercase , digits
from authentification.functions import Encoder,SendMail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from django.contrib import messages

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a role."""
    role = forms.CharField(label="Роль", max_length=20)
    available_roles = ["L1","L2","L3","admin"]
    def clean_role(self):
        data = self.cleaned_data['role']
        if data not in self.available_roles:
            raise ValidationError("Доступные роли: {}".format(",".join(self.available_roles)))
        return data


    class Meta:
        model = User
        fields = ('email', 'role')


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user_pass = ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(15))
        user.set_password(user_pass)
        username = "{}_{}".format(user.role,''.join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(12)))
        user.username = username
        user.is_active = False
        encoded_username = Encoder(username).encode()
        text = f'Перейдите по ссылке: {settings.DEFAULT_DOMAIN}api/auth/activateUser/{encoded_username}/ для активации вашего аккаунта'
        SendMail(text,[user.email]).send()
        TmpPass(username=username,password=user_pass).save()
        if commit:
            user.save()
        return user