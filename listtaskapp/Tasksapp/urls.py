from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.create_task),
    path('register/', views.register_user, name='register'),
    path('home_page/', views.home_page, name='home_page'),
    path('auth_user/', views.auth_user, name='auth_user'),
    path('create_task/', views.create_task, name='create_task'),
    path('home_page/task_delete/<int:id>/', views.task_delete, name='task_delete'),
    path('status_task/<int:pk>/<str:status>/', views.status_task, name='status_task'),
    # path('home_page/add_favorite_task/<int:id>/', views.add_favorite_task),
    # path('favorite_task/', views.favorite_page),

]