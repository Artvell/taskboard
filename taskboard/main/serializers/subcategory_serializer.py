"""файл с классом SubcategorySerializer"""
from rest_framework import serializers
from main.models import Subcategory

class SubcategorySerializer(serializers.ModelSerializer):
    """класс для сериализации данных из модели Subcategory"""
    class Meta:
        model = Subcategory
        fields = "__all__"
