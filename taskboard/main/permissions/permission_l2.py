"""файл с классом L2Permission"""
from rest_framework import permissions

class L2Permission(permissions.BasePermission):
    """определяет, есть ли у пользователя права L2"""
    def has_permission(self,request,view):
        return (request.user and request.user.is_authenticated and
        (request.user.groups.filter(name='L2').exists() or request.user.is_superuser))
        