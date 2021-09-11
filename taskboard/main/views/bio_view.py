"""файл с классом BIOView"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from main.serializers import PersonSerializer
from main.models import BIO
from main.permissions import L1Permission, L3Permission

class BIOView(ModelViewSet):
    """представление модели BIO, с выставленными правами доступа"""
    permission_classes = [L1Permission]
    serializer_class = PersonSerializer
    queryset = BIO.objects.all()
    def get_permissions(self):
        if self.action == 'update' or self.action == "create":
            self.permission_classes = [L1Permission,]
        elif self.action == "delete":
            self.permission_classes = [L3Permission,]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
