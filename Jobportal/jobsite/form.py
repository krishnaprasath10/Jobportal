from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
  
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    conpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Your Password'}))

    class Meta:
        model=User
        fields=['email','password','conpassword']