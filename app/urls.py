from django.urls import path

from .views import home , login_user , logout_user  , user_profile_home , sign_up

urlpatterns = [
    path('' , home , name='home'),
    path('signup/' , sign_up , name="signup"),
    path('login/', login_user ,name='login' ),
    path('logout/' , logout_user , name='logout'),
    path('user/' , user_profile_home , name='user-home')
]