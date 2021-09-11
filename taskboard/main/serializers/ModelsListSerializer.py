from rest_framework import serializers

class ModelsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()