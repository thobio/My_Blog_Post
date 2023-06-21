from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, UserForgotPassword
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_register(request):
    form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


def user_login(request):
    form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_forgot_password(request):
    form = UserForgotPassword()
    return render(request, 'account/forgot_password.html', {'form': form})


def user_logout(request):
    return render(request, 'account/logout.html')
