from rest_framework import serializers
from main.models import Passport
from main.serializers.countrySerializer import CountrySerializer

class PassportSerializer(serializers.ModelSerializer):
    #person = PersonSerializer()
    #country = CountrySerializer()
    #comments = serializers.CharField()
    class Meta:
        model = Passport
        fields = "__all__"
        extra_kwargs = {'id': {"required":False}}
