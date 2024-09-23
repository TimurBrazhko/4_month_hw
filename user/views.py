from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', context={'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/register.html', context={'form': form})
        form.cleaned_data.pop('password_confirm')
        User.objects.create_user(**form.cleaned_data)
        return redirect('main_page')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', context={'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', context={'form': form})
        user = authenticate(**form.cleaned_data)
        if user is None:
            form.add_error(None, f'Wrong username or password.')
            return render(request, 'user/login.html', context={'form': form})
        login(request, user)
        return redirect('main_page')


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('main_page')
