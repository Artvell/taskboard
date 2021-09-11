"""Файл с классом L3CommentViewSet"""
from rest_framework.viewsets import ModelViewSet
from main.serializers import L3CommentSerializer
from main.models import L3Comment
from main.permissions import L3Permission

class L3CommentViewSet(ModelViewSet):
    """Вьюсет для реализации CRUD для модели L3Comment"""
    permission_classes = [L3Permission]
    serializer_class = L3CommentSerializer
    queryset = L3Comment.objects.all()
