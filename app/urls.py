from django.urls import path

from .views import home , login_user , logout_user  , user_profile_home

urlpatterns = [
    path('' , home , name='home'),
    path('login/', login_user ,name='login' ),
    path('logout/' , logout_user , name='logout'),
    path('user/' , user_profile_home , name='user-home')
]