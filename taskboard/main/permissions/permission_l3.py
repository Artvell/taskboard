"""файл с классом L3Permission"""
from rest_framework import permissions

class L3Permission(permissions.BasePermission):
    """проверяет, есть ли у юзера права L3"""
    def has_permission(self,request,view):
        return(
            request.user and request.user.is_authenticated and
            (request.user.groups.filter(name='L3').exists() or request.user.is_superuser)
            )
