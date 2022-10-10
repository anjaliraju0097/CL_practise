from rest_framework.response import Response
from myapp import models
from myapp.models import User
from django.http import HttpResponse, JsonResponse
from .serializer import UserSerializer,RegisterSerializer

from rest_framework.decorators import api_view


# Create your views here.
# serializers in django do the below steps manualy.
# so we dont need to write all these codes.
#  instead we can use serializers.
# def userRegister(request):
#     U_R= User.objects.all()
#     userReg = list(U_R.values())
#     return JsonResponse(
#         {
#             'U_R' : userReg
#         }
#     )
@api_view(['GET'])
def UserView(request):
        obj = models.User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def UserRegister(request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        #     result = {"result":"user successfully registered"}    
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)  






      
















            






        