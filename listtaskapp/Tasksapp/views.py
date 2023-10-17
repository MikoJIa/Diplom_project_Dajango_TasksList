from django.contrib import auth
from django.shortcuts import render, redirect
from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseNotFound
from .models import User, Tasks


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            task = form.save(commit=False)
            user = User.objects.get(user=request.user) # Нужно обратить внимание, что мы
            # используем не id поле, а мы используем именно объект
            task.user = user
            task.save()
            return redirect('home_page.html')
    form = TaskForm()
    task_obj = Tasks.objects.all()
    context = {
        'form': form,
        'task_obj': task_obj
    }
    return render(request, 'Tasksapp/create_task.html', context)


def task_delete(request, id):
    try:
        task = Tasks.objects.get(id=id)
        task.delete()
        return redirect('create_task')
    except NameError:
        return HttpResponseNotFound(f'<h1>Такая задача не найдена!!!</h1>')


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

