from django.urls import path
from .views import *
urlpatterns = [
  path('',index, name='index' ),
  path('login/', login, name='login'),
  path('register/', RegisterationView.as_view(), name='register')
  
]