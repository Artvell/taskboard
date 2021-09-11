"""файл с классом EntityCommentsViewSet"""
from rest_framework.viewsets import ModelViewSet
from main.serializers import EntityCommentsSerializer
from main.models import EntityComments
from main.permissions import L2Permission

class EntityCommentsViewSet(ModelViewSet):
    """Вьюсет для реализации CRUD для модели EntityComments"""
    permission_classes = [L2Permission]
    serializer_class = EntityCommentsSerializer
    queryset = EntityComments.objects.all()
