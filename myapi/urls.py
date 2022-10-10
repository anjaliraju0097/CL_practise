import imp
from django.urls import path
from myapi.views import UserRegisterView, UserView
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserView),
    path('api/register/', UserRegisterView),
    
    
]
