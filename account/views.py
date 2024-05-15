from django.contrib.auth import login, logout
from django.contrib import messages
from .models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm

from django.shortcuts import redirect
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully registered')
            return redirect('user_login')
        
    else:
        form = UserRegistrationForm()
        messages.error(request,'invalid')
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,'successfully logged in')
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request,'successfully logged out')
    return redirect('home')

