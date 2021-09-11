"""файл с классами EntitySerializer и FurtherInformationField"""
from datetime import datetime
from rest_framework import serializers
from main.models import Entity, EntityComments, L3Comment, Passport, BIO
from main.serializers import PersonSerializer, PassportSerializer
from main.serializers.entity_comments_serializer import EntityCommentsSerializer
from main.serializers.l3_comment_serializer import L3CommentSerializer
from main.functions import TextFormatter

class FurtherInformationField(serializers.Field):
    """класс, определяющий кастомное поле для сериалайзера"""
    def to_representation(self, value):
        return TextFormatter(value).text_to_json()

    def to_internal_value(self, data):
        return TextFormatter(data).json_to_text()

class EntitySerializer(serializers.ModelSerializer):
    """
    Класс, сериализирующий данные модели EntityComments
    Переопределены методы: create,update
    """
    person = PersonSerializer()
    passports = PassportSerializer(many=True)
    comments = serializers.SerializerMethodField()
    l3_comment = serializers.SerializerMethodField()
    further_information = FurtherInformationField()

    def get_comments(self,obj):
        """Возвращает данные для поля comments"""
        data = EntityComments.objects.filter(entity=obj)
        serializer = EntityCommentsSerializer(data,many=True)
        return serializer.data

    def get_l3_comment(self,obj):
        """Возвращает данные для поля l3_comment"""
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
        person, _ = BIO.objects.get_or_create(**person_data)
        Passport.objects.bulk_create(
                [Passport(person=person,**passport) for passport in passport_data]
            )

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
