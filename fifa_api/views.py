from webbrowser import get
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from .serializers import UserRegisterSerializer,UserViewSerializer,TeamSerializer
from rest_framework.response import Response
from .models import User
from FIFA.settings import SECRET_KEY
from rest_framework import status
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
import re

# Create your views here.

class teamview(APIView):

    # authenticaton_classes = ( JWTAuthentication, )
    # permission_classes = ( IsAuthenticated, )

    def post (self, request):
        # print(request.data)
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
        # serializer.is_valid()
            # print ("\n\n", serializer.data, "\n\n")
            serializer.save()
            # print ("\n\n", serializer.data, "\n\n")
            return Response ({"Status" : "Success"})
        # print ("\n\n", serializer.data, "\n\n")
        return Response ({"Status" : "Team already exist"})


class UserRegisterView(APIView):
    def post(self,request):
            serializer = UserRegisterSerializer(data=request.data) 
            if serializer.is_valid():
                serializer.save()
                #result = {"result":"user successfully registered"}    
                return Response({"Result":"User successfully registered!", "Data : " : serializer.data},status=201) 
            print('\n\n',serializer.data,'\n\n')      
            return Response(serializer.errors, status=400) 



class LoginUserView(APIView):
    def get(self, request):

        token = request.META['HTTP_AUTHORIZATION']
        accesst = token.split(' ')[1]
        print('\n\n Access token = ',accesst,'\n\n')
        try:
           
            payload = jwt.decode(accesst, SECRET_KEY, algorithms=['HS256']) #decode the access token
            print('\n\n payload =', payload,'\n\n')
            user_data = User.objects.get(id=payload['user_id'])#Retrieve user data from DB with user id
            #print('\n\n',user_data.query,'\n\n')
            user = UserViewSerializer(user_data,many = False)
            print('\n\n ',user.data,'\n\n')
            return Response({'status': 'Successfully activated','data' : user.data}, status=201)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Activations link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)     


class UserView(APIView):
    def get(self,request,*args,**kwargs):
        try: 
            user_data =User.objects.all()
            print('\n\n',user_data.query,'\n\n')
            serializer = UserViewSerializer(user_data ,many=True)
            return Response(serializer.data,status=201)
        except:
            return Response({"detail":"No such users found "}, status=400)    

# class EmailVerification(APIView):
#     def post(self,request):
#         value = "@codelynks.com"
#         print(value)
#         try:
#             validate_email(value)
#         except ValidationError as e:
#             print("bad email, details:", e)
#         else:
#             print("good email")
 
#         return Response({'status':'sucess'})  

class LogoutView(APIView):
        def post(self,request):
            try:
                Refresh_token = request.data["refresh"]
                token = RefreshToken(Refresh_token)
                token.blacklist()
                return Response({"status":"Successfully Signed out"}, status=201)
            except:
                return Response({"code": "Token is blacklisted", "detail": "Invalid Token"}, status=40)
