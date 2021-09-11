"""обработчик для события создания нового юзера"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import Group
from authentification.models import TmpPass

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(instance, created,**kwargs):
    """добавляет юзера в группу по его роли"""
    if created and instance.role != "admin":
        group,created = Group.objects.get_or_create(name=instance.role)
        instance.groups.add(group)

@receiver(post_delete, sender=settings.AUTH_USER_MODEL)
def delete_user(instance,**kwargs):
    """при удалении User, стирает временные логин/пароль"""
    try:
        tmp_user = TmpPass.objects.get(username=instance.username)
        tmp_user.delete()
    except TmpPass.DoesNotExist:
        pass