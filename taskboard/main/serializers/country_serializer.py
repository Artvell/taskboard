"""файл с классом CountrySerializer"""
from rest_framework import serializers
from main.models import Country

class CountrySerializer(serializers.ModelSerializer):
    """класс для сериализации данных из модели Country"""
    class Meta:
        model = Country
        fields = "__all__"
