from django.shortcuts import render
from myapi.serializers import UserRegisterSerializer,UserViewserializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

@api_view(['GET'])
def UserView(request):
    obj = request.objects.all()
    serializer = UserViewserializer(obj,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def UserRegisterView(request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #result = {"result":"user successfully registered"}    
            return JsonResponse({"Status":"User successfully registered!", "Data : " : serializer.data},status=201)
        return JsonResponse(serializer.errors, status=400)  




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


