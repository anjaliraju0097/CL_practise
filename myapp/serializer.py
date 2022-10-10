from rest_framework import serializers,validators
from rest_framework.exceptions import NotAuthenticated
from myapp.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'password')
        extra_kwargs = {
            "password": {"write_only":True},
        }

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4,write_only=True,required=True,style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'password')

        extra_kwargs = {
            "password": {"write_only":True},
            "username" : {"required":True,
            "allow_blank":False,
            "validators": [validators.UniqueValidator(User.objects.all(),"User with is username already exist")]
            }
        }
     
    def create(self, validated_data):
        username = validated_data.get('username')
        age = validated_data.get('age')
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(RegisterSerializer, self).create(validated_data)


        






