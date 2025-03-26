from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField()
    email=
    password1=
    password2=