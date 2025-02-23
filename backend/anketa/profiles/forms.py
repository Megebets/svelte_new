from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserProfileCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True)
    
    class Meta:
        model = UserProfile
        fields = ['phone', 'last_name', 'first_name', 'middle_name', 'password1', 'password2']
