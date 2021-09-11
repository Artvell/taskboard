"""файл c классом EntityViewSet"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from main.serializers import EntitySerializer
from main.models import Entity
from main.permissions import L1Permission,L3Permission

class EntityViewSet(ModelViewSet):
    """Вьюсет для реализации CRUD для модели Entity"""
    #permission_classes = [L1Permission]
    serializer_class = EntitySerializer
    queryset = Entity.objects.all()

    def get_permissions(self):
        if self.action == 'update' or self.action == "create":
            self.permission_classes = [L1Permission]
        elif self.action == "delete":
            self.permission_classes = [L3Permission]
        else:
            self.permission_classes = [IsAuthenticated,]
        return super().get_permissions()
