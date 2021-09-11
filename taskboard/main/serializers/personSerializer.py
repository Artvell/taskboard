from rest_framework import serializers
from main.models import BIO

class PersonSerializer(serializers.ModelSerializer):
    #comments = serializers.CharField()
    class Meta:
        model = BIO
        fields = "__all__"
