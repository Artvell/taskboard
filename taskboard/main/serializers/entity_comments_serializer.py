"""файл с классом EntityCommentsSerializer"""
from collections import OrderedDict
from rest_framework import serializers
from main.models import EntityComments

class EntityCommentsSerializer(serializers.ModelSerializer):
    """класс для сериализации данных из модели EntityComments"""
    def to_representation(self, instance):
        """переопределенный возврат данных из класса"""
        result = super(EntityCommentsSerializer, self).to_representation(instance)
        return OrderedDict(
                [
                (key, result[key]) for key in result if
                (result[key] is not None and result[key] !="" and bool(result[key]))
                ]
            )

    class Meta:
        model = EntityComments
        fields = "__all__"
