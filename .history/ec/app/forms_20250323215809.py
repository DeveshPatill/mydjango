from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':"form-control"}))
    email=
    password1=
    password2=