"""файл с классом KeywordSerializer"""
from rest_framework import serializers
from main.models import Keywords

class KeywordSerializer(serializers.ModelSerializer):
    """сериализирует данные из модели Keywords"""
    class Meta:
        model = Keywords
        fields = "__all__"
