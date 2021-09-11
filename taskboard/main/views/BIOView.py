from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from main.serializers import PersonSerializer
from main.models import BIO
from main.permissions import L1Permission

class BIOView(ModelViewSet):
    permission_classes = [L1Permission]
    serializer_class = PersonSerializer
    queryset = BIO.objects.all()
    def get_permissions(self):
        if self.action == 'update' or self.action == "create":
            self.permission_classes = [AllowAny,]
        else:
            self.permission_classes = [AllowAny,]
        return super().get_permissions()