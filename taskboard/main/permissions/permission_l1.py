"""файл с классом L1Permission"""
from rest_framework import permissions

class L1Permission(permissions.BasePermission):
    """определяет, имеет ли пользователь права L1"""
    def has_permission(self,request,view):
        return (request.user and request.user.is_authenticated and
            (request.user.groups.filter(name='L1').exists() or request.user.is_superuser))
