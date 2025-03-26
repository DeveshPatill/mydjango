from django import forms


class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField()
    email=
    password1=
    password2=