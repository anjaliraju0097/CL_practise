
from ast import Expression
from dataclasses import field
from lib2to3.pgen2.tokenize import TokenError
from operator import attrgetter
from os import defpath
from pkg_resources import require
from rest_framework import serializers,validators
from .models import UserRegister
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

class UserViewserializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = ('id','name','age','phone','email','password') 
        # deapth = 1
        extra_kwargs  = {
            "password":{'write_only':True},
                } 
   

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


# #Logout not needed for now
# class LogoutSerializer(serializers.ModelSerializer):
#     refresh = serializers.CharField()

#     default_error_messages = {
#         'bad_token': ('Token is invalid or expired')
#     }

#     def validate(self,attrs):
        
#         self.token = attrs['refresh']   
#         return attrs

#     def save(self,**kwargs):
#         try:
#             RefreshToken(self.token).blacklist()
#         except TokenError:
#             self.fail('Bad Token')

                
        