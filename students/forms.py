#from .models import Myuser
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import User, UserCreationForm
from .models import Myuser

class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={
        'class':'form-class',
        'placeholder':('')
    }))
    last_name=forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':('')
        }))
    class Meta:
        model=Myuser
        fields=['username','first_name','last_name','password1','password2']