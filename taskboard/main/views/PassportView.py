from rest_framework.viewsets import ModelViewSet
from main.serializers import PassportSerializer
from main.models import Passport
from main.permissions import L1Permission, L3Permission

class PassportView(ModelViewSet):
    permission_classes = [L1Permission]
    serializer_class = PassportSerializer
    queryset = Passport.objects.all()
    def get_permissions(self):
        if self.action == 'delete':
            self.permission_classes = [L3Permission]
        else:
            self.permission_classes = [L1Permission]
        return super().get_permissions()