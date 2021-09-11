from rest_framework import serializers
from main.models import Keywords

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = "__all__"
        """extra_kwargs = {
            'keyword': {'validators': []},
        }"""