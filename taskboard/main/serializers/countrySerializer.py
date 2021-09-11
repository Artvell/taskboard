from rest_framework import serializers
from main.models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        """extra_kwargs = {
            'country': {'validators': []},
        }"""