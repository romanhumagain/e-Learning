from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('',index, name='index' ),
  path('login_user/', LoginUserView.as_view(), name='login_user'),
  path('register/', RegisterationView.as_view(), name='register'),
  path('profile/', ProfileView.as_view(), name='profile'),
  # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('logout/', logout_user, name='logout'),
  
  
]