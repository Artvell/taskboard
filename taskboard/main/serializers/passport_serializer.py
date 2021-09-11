"""файл с классом PassportSerializer"""
from rest_framework import serializers
from main.models import Passport

class PassportSerializer(serializers.ModelSerializer):
    """сериализирует данные из модели Passport"""
    class Meta:
        model = Passport
        fields = "__all__"
        extra_kwargs = {'id': {"required":False}}
