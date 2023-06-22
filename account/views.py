from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, UserForgotPassword
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password1')
            email = request.POST.get('email')
            f_name = request.POST.get('first_name')
            l_name = request.POST.get('last_name')
            user_obj = User.objects.filter(username=email)
            if user_obj.exists():
                messages.warning(request, 'Email is already taken')
                return HttpResponseRedirect(request.path_info)
            else:
                user_obj = User.objects.create(first_name=f_name, last_name=l_name, email=email, username=email)
                user_obj.set_password(password)
                user_obj.save()
                messages.success(request, 'An email has been sent on your mail')
                return redirect('account:login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username)
        if not user_obj.exists():
            messages.warning(request, 'Account not found')
            return HttpResponseRedirect(request.path_info)
        else:
            print(user_obj.first().profile.is_email_verified)
            if not user_obj.first().profile.is_email_verified:
                messages.warning(request, 'Your account is not verified!')
                return HttpResponseRedirect(request.path_info)
            else:
                user_obj = authenticate(username=username, password=password)
                if user_obj:
                    login(request, user_obj)
                    return redirect('/')
                else:
                    messages.warning(request, 'Invalid credentials')
                    return HttpResponseRedirect(request.path_info)
    return render(request, 'account/login.html', {'form': form})


def user_forgot_password(request):
    form = UserForgotPassword()
    return render(request, 'account/forgot_password.html', {'form': form})


def user_logout(request):
    return render(request, 'account/logout.html')


def activate_email(request, email_token):
    print(email_token)
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        print(e)
        return HttpResponse('Invalid Email token')
