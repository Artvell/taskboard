from rest_framework import serializers
from main.models import L3Comment

class L3CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = L3Comment
        fields = "__all__"