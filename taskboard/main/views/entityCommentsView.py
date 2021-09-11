from rest_framework.viewsets import ModelViewSet
from main.serializers import EntityCommentsSerializer
from main.models import EntityComments
from main.permissions import L2Permission

class EntityCommentsViewSet(ModelViewSet):
    permission_classes = [L2Permission]
    serializer_class = EntityCommentsSerializer
    queryset = EntityComments.objects.all()
