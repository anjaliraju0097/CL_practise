from dataclasses import field
from logging import exception
from wsgiref import validate
from rest_framework import serializers,validators
from django.contrib.auth.hashers import make_password
from .models import User,Teams

class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs  = {
            "password":{'write_only':True},
           }



# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         extra_kwargs  = {
#             "password":{'write_only':True},
#            }
    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["codelynks.com"]
        if domain not in domain_list:
            raise exception.ValidationError("Please enter an Email Address with a valid domain")
        print(data) 
        return data   
               



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'        
        extra_kwargs  = {
            "password":{'write_only':True},
            "email":{'required':True,
            "allow_blank":False,
            "validators": [validators.UniqueValidator(User.objects.all(),"User with this email already exist")]
            }
            
            }
    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        fav_team = validated_data.get('fav_team')
        points = validated_data.get('points')
        email = validated_data.get('email')
        password = validated_data.get('password')
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserRegisterSerializer, self).create(validated_data)  


    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        return super().validate(attrs)          

class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teams
        fields = ('team_id', 'group', 'name', 'coach', 'status') 



      