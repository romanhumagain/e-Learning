from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
  first_name = forms.CharField(required=True,
                               label="First Name",
                               widget=forms.TextInput(attrs={'class':'form-control'})
                               )
  
  last_name = forms.CharField(required=True,
                               label="Last Name",
                               widget=forms.TextInput(attrs={'class':'form-control'})
                               )
  
  email = forms.EmailField(required=True,
                           label="Email",
                           widget=forms.EmailInput(attrs={"placeholder":"example@gmail.com", 'class':'form-control'}))
  
  class Meta:
    model = User
    fields =['first_name','last_name','username', 'email', 'password1', 'password2']