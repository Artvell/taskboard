"""файл с классом CategorySerializer"""
from rest_framework import serializers
from main.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """класс для сериализации данных из модели Category"""
    subcategories = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
