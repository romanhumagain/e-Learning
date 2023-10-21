from django.shortcuts import render, redirect
from django.http import HttpResponse
from App.forms import UserRegistrationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return HttpResponse("Welcome to the E-Learning Platform.")

class LoginUserView(View):
  def get(self, request):
    return render(request, 'app/login.html')
  def post(self,request):
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    
    if User.objects.filter(username = username).exists():
      user = authenticate(username = username, password = password)
      if user is not None:
        login(request, user)
        return redirect('/profile/')
      else:
        messages.error(request, "Invalid Password !!")
        return redirect('/login_user/')
    else:
      messages.error(request, "Invalid Username !!")
      return redirect('/login_user/')
      

class RegisterationView(View):
  def get(self, request):
    form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'app/register.html', context)
  
  def post(self, request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"your account has been created!")
      return redirect('/login/')
    else:
      return render(request, 'app/register.html', {'form':form})
    
class ProfileView(LoginRequiredMixin,View):
  def get(self, request):
    return render(request, 'app/profile.html')
  

def logout_user(request):
  logout(request)
  return redirect('/')
      
      