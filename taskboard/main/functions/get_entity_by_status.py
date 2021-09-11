"""Файл с функцией для получения списка Entity  с указанным статусом"""
from main.models import Entity
from django.db.models import Q

def get_entity_by_status(status,group,user=None):
    """Функция для получения списка Entity  с указанным статуслм"""
    allowed_status = {
        "L1":[1, 2, 3],
        "L2":[1, 3, 4],
        "L3":[4, 5, 6],
        "superuser":[1, 2, 3, 4, 5, 6]
    }
    if status in allowed_status[group] and user is not None:
        queryset = Entity.objects.filter(Q(status=status)&Q(editor=user))
    elif status in allowed_status[group]:
        queryset = Entity.objects.filter(status=status)
    else:
        queryset = ""
    return queryset
