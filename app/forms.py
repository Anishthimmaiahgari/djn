from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your CustomUser model
        fields = ('username', 'email')  # Add other fields as needed
