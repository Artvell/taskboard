from rest_framework import serializers
from main.models import *
from main.serializers import (
                            PersonSerializer, 
                            PassportSerializer,
                            CategorySerializer,
                            CountrySerializer,
                            KeywordSerializer,
)
from main.serializers.entityCommentsSerializer import EntityCommentsSerializer
from main.serializers.L3CommentSerializer import L3CommentSerializer
from authentification.serializers import UserSerializer
from authentification.models import User
from main.functions import TextFormatter
from datetime import datetime

class FurtherInformationField(serializers.Field):
    def to_representation(self, value):
        return TextFormatter(value).textToJson()

    def to_internal_value(self, data):
        return TextFormatter(data).jsonToText()

class EntitySerializer(serializers.ModelSerializer):

    person = PersonSerializer()
    passports = PassportSerializer(many=True)
    comments = serializers.SerializerMethodField()
    l3_comment = serializers.SerializerMethodField()
    further_information = FurtherInformationField()

    def get_comments(self,obj):
        data = EntityComments.objects.filter(entity=obj)
        serializer = EntityCommentsSerializer(data,many=True)
        return serializer.data
    
    def get_l3_comment(self,obj):
        data = L3Comment.objects.filter(entity=obj)
        serializer = L3CommentSerializer(data,many=True)
        return serializer.data

    def create(self, validated_data):
        
        person_data = validated_data.pop("person")
        passport_data = validated_data.pop("passports")
        category_data = validated_data.pop("category")
        keywords_data = validated_data.pop("keywords")
        countries_data = validated_data.pop("countries")
        editor_id = validated_data.pop("editor")
        further_data = validated_data.pop("further_information")
        person, p = BIO.objects.get_or_create(**person_data)
        Passport.objects.bulk_create([Passport(person=person,**passport) for passport in passport_data])
        
        entity = Entity.objects.create(
                person=person, 
                category=category_data, 
                editor=editor_id,
                further_information = further_data,
                **validated_data
            )
        entity.entered = datetime.now()
        entity.countries.add(*countries_data)
        entity.keywords.add(*keywords_data)
        entity.save()

        return entity
    
    def update(self,instance, validated_data):
        if "keywords" in validated_data:
            keywords_data = validated_data.pop("keywords")
            instance.keywords.clear()
            instance.keywords.add(*keywords_data)

        if "countries" in validated_data:
            countries_data = validated_data.pop("countries")
            instance.countries.clear()
            instance.countries.add(*countries_data)
        
        if "further_information" in validated_data:
            further_data = validated_data.pop("further_information")
            instance.further_information = further_data

        for attr, value in validated_data.items():
            if attr == "person" or attr == "passports":
                raise serializers.ValidationError(f'Invalid field for update:"{attr}"')
            setattr(instance, attr, value)
        instance.updated = datetime.now()
        instance.status = 1
        instance.save()
        return instance
        
    class Meta:
        model = Entity
        fields = (
             'id',
             'status',
             'person',
             'passports',
             'category',
             'keywords',
             'countries',
             'ssn',
             'io',
             'external_sources',
             'age_date',
             'entered',
             'editor',
             'updated',
             'locations',
             'further_information',
             'comments',
             'l3_comment'
         )
