from rest_framework import serializers
from main.models import EntityComments
from collections import OrderedDict

class EntityCommentsSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        result = super(EntityCommentsSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if (result[key] is not None and result[key] !="" and bool(result[key]))])
    
    class Meta:
        model = EntityComments
        fields = "__all__"