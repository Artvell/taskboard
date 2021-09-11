from rest_framework import serializers
from main.models import Category
from main.serializers.subcategorySerializer import SubcategorySerializer

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            'title': {'validators': []},
        }
