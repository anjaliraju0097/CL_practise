
from pkg_resources import require
from rest_framework import serializers,validators
from .models import UserRegister
from django.contrib.auth.hashers import make_password

class UserViewserializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = ('id','name','age','phone','email','password')        

        extra_kwargs  = {
            "password":{'write_only':True},
            "email":{'required':True,
            "allow_blank":False,
            "validators": [validators.UniqueValidator(UserRegister.objects.all(),"User with this email already exist")]
            }
            
            }
    def create(self, validated_data):
        name = validated_data.get('name')
        age = validated_data.get('age')
        phone = validated_data.get('phone')
        email = validated_data.get('email')
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserRegisterSerializer, self).create(validated_data)        
        