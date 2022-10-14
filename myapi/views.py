from distutils.command.config import config
from myapi.serializers import UserRegisterSerializer,UserViewserializer
from rest_framework.response import Response
from myapi.models import UserRegister
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from userLOgin.settings import SECRET_KEY
# Create your views here.

class UserView(APIView):
    def get(self,request,*args ,**kwargs):
        try: 
            user_data =UserRegister.objects.all()
            serializer = UserViewserializer(user_data ,many=True)
            return Response(serializer.data,status=201)
        except:
            return Response({"detail":"No such users found with this user id"}, status=400)     


class UserRegisterView(APIView):
    def post(self,request):
            serializer = UserRegisterSerializer(data=request.data) 
            if serializer.is_valid():
                serializer.save()
                #result = {"result":"user successfully registered"}    
                return Response({"Status":"User successfully registered!", "Data : " : serializer.data},status=201)       
            return Response(serializer.errors, status=400)  

#Blacklist the refresh token: extract token from the header  during logout request user and refresh token is provided
class UserLogoutView(APIView):
        def post(self,request):
            try:
                Refresh_token = request.data["refresh"]
                token = RefreshToken(Refresh_token)
                token.blacklist()
                return Response("Successful Logout", status=201)
            except:
                return Response({"code": "Token is blacklisted", "detail": "Invalid Token"}, status=401)  


class LoginUserView(APIView):
    def get(self, request):

        token = request.META['HTTP_AUTHORIZATION']
        accesst = token.split(' ')[1]
        print('\n\n Access token = ',accesst,'\n\n')
        try:
            #decode the access token
            payload = jwt.decode(accesst, SECRET_KEY, algorithms=['HS256'])
            print('\n\n payload =', payload,'\n\n')
            #Retrieve user data from DB with user id
            user_data = UserRegister.objects.get(id=payload['user_id'])
            user = UserViewserializer(user_data,many = False)
            print('\n\n ',user.data,'\n\n')
            return Response({'status': 'Successfully activated','data' : user.data}, status=201)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Activations link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)            


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['name'] = user.name
#         # ...

#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer        


