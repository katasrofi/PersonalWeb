from django.forms import ModelForm
from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model 
from .models import Products 

class ProfilesForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
