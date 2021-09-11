"""файл с классом PersonSerializer"""
from rest_framework import serializers
from main.models import BIO

class PersonSerializer(serializers.ModelSerializer):
    """сериализует данные из модели BIO"""
    class Meta:
        model = BIO
        fields = "__all__"
