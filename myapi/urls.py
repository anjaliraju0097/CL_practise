from myapi.views import UserRegisterView, LoginUserView,UserLogoutView,UserView
from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/logout1/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/user/', LoginUserView.as_view()),
    path('api/register/', UserRegisterView.as_view()),
    path('api/viewusers/', UserView.as_view()),
    path('api/logout/', UserLogoutView.as_view()),
    
]
