
from django.urls import path
from .views import LoginUserView,LogoutView,UserRegisterView,UserView,teamview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('api/teams/', teamview.as_view(), name = 'fifa_teams'),
    path('api/loginview/',LoginUserView.as_view()),
    path('api/register/',UserRegisterView.as_view()),
    path('api/userview/',UserView.as_view()),
    path('api/logout/',LogoutView.as_view())
]
