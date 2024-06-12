
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import secondCustomUser

class CreateuserForm(forms.ModelForm):
   class Meta:
      
      model = secondCustomUser
      fields = ['username','email','password']



