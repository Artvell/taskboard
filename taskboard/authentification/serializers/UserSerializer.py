from rest_framework import serializers
from authentification.models.User import User
 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('username', 'email', 'password',"is_active")
        extra_kwargs = {'password': {'write_only': True}}