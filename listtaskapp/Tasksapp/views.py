from django.shortcuts import render, redirect
from .forms import TaskForm, UserRegisterForm



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


# def register_user(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             UserRegisterForm()

