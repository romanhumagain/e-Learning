from django.shortcuts import render, redirect
from django.http import HttpResponse
from App.forms import UserRegistrationForm
from django.views import View
from django.contrib import messages

# Create your views here.
def index(request):
  return HttpResponse("Welcome to the E-Learning Platform.")

def login(request):
  return render(request, 'app/login.html')

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
      
      