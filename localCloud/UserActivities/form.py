from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import request
#from django.contrib.auth import get_user_model
from .models import User

#User = get_user_model()
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'username', 
            'password1', 
            'password2', 
            'email', 
            'date_of_birth'
        ]