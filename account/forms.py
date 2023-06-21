from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    profile_image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'profile_image']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User


class UserForgotPassword(PasswordResetForm):
    class Meta:
        model = User
