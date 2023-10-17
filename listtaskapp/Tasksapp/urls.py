from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.create_task),
    path('register/', views.register_user, name='register'),
    path('', views.home_page, name='home_page'),
    path('auth_user/', views.auth_user, name='auth_user'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_task/task_delete/<int:id>/', views.task_delete, name='task_delete'),
]