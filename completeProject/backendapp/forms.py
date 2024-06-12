from .models import *
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms

class CustomUserForm(UserCreationForm):
   class Meta:
      model = Custom_user
      fields = UserCreationForm.Meta.fields + ('city','profile_pic','user_type','email','first_name')
      

      
class customAuthForm(AuthenticationForm):
   class Meta:
      model = Custom_user
      fields = ['username','password']


class createtaskform(forms.ModelForm):
   class Meta:
      model = TasknameModel
      fields = []


class jobAddform(forms.ModelForm):
   class Meta:
      model = JobModel
      fields = ('job_title', 'qualifications','deadline','salary','number_of_openings','category' ,'job_description','skills')
      widgets = {
         'deadline':forms.DateInput(attrs={'type':'date'}),
      }
      
class applyJobForm(forms.ModelForm):
   class Meta:
      model = jobApplyModel
      fields = ('skills','resume','seeker_profile_pic','qualifications','date_fix')

      widgets = {
         'resume':forms.DateInput(attrs={'type':'file'}),
         'seeker_profile_pic':forms.DateInput(attrs={'type':'file'}),
         'date_fix':forms.DateInput(attrs={'type':'date'}),
      }