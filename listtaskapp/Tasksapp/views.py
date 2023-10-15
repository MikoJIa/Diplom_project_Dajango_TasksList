from django.contrib import auth
from django.shortcuts import render, redirect
from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import User


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.user = request.user
            return redirect('home.html')
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'Tasksapp/create_task', context)


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Tasksapp/register_done.html')
    form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'Tasksapp/register.html', context)


def auth_user(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(request, name=name, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponse('Пользователь вошёл в систему')
    context = {
        'form': form
    }
    return render(request, 'Tasksapp/auth_user.html', context)


def home_page(request):
    user = User.objects.all()
    context = {
        'user': user
    }
    return render(request, 'Tasksapp/home_page.html', context)

