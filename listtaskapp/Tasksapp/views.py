from django.contrib import auth, messages
from django.core.mail import message
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import TaskForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseNotFound
from .models import User, Tasks, FavoriteTask
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            task = form.save(commit=False)
            user = User.objects.get(user=request.user.id) # Нужно обратить внимание, что мы
            # используем не id поле, а мы используем именно объект
            task.user = user.save()
            return redirect('home_page')
    form = TaskForm()
    task_obj = Tasks.objects.all()
    context = {
        'form': form,
        'task_obj': task_obj
    }
    return render(request, 'Tasksapp/create_task.html', context)


def status_task(request, pk, status):
    task = Tasks.objects.get(pk=pk)
    task.finished_task = status
    task.save()
    return redirect('home_page')


def priority_task(request, pk, status):
    task = Tasks.objects.get(pk=pk)
    task.is_favorite = status
    task.save()
    return redirect('home_page')


def task_delete(request, id):
    try:
        task = Tasks.objects.get(id=id)
        task.delete()
        return redirect('home_page')
    except NameError:
        return HttpResponseNotFound(f'<h1>Такая задача не найдена!!!</h1>')


# def add_favorite_task(request, task_id, user_id):
#     task = Tasks.objects.get(id=task_id)  # Находим нужную задачу
#     favorite_task = FavoriteTask.objects.create(user=user_id, task=task.user.id)
#     favorite_task.save()
#     task = FavoriteTask.objects.get(id=task_id)
#
#
# def favorite_page(request):
#     task = FavoriteTask.objects.filter(user=request.user)
#     context = {
#         'task': task
#     }
#     return render(request, 'Tasksapp/favorite_task', context)


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('name')
            messages.success(request, f'Аккаунт - {user} создан')
            return render(request, 'Tasksapp/register_done.html')
    form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'Tasksapp/register.html', context)


def profile_view(request):
    return render(request, 'Tasksapp/profile.html')


def auth_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            # name = request.POST.get('username')
            # password = request.POST.get('password')
            # user = authenticate(request, name=name, password=password)
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
            # if user is not None:
            #     login(request, user)
            #     return HttpResponse('Пользователь вошёл в систему')
            # else:
            #     return HttpResponseNotFound('Введены не верные данные')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'Tasksapp/auth_user.html', context)


def home_page(request):
    task_obj = Tasks.objects.all()
    context = {
        'task_obj': task_obj
    }
    return render(request, 'Tasksapp/home_page.html', context)

