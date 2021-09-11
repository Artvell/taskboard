from rest_framework import permissions

class L3Permission(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.user and request.user.is_authenticated and (request.user.groups.filter(name='L3').exists() or request.user.is_superuser):
            return True
        else:
            return False
        