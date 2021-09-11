"""файл с классом L3CommentSerializer"""
from rest_framework import serializers
from main.models import L3Comment

class L3CommentSerializer(serializers.ModelSerializer):
    """сериализирует данные из модели L3Comment"""
    class Meta:
        model = L3Comment
        fields = "__all__"
