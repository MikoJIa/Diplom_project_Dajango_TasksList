from django.urls import path
from . import views


urlpatterns = [
    path('create_task/', views.create_task),
    path('register/', views.register_user, name='register'),
    path('', views.home_page, name='home_page'),
    path('auth_user/', views.auth_user, name='auth_user'),
    path('create_task/', views.create_task, name='create_task'),
    path('home_page/task_delete/<int:id>/', views.task_delete, name='task_delete'),
    path('status_task/<int:pk>/<str:status>/', views.status_task, name='status_task'),
    path('priority_task/<int:pk>/<str:status>/', views.priority_task, name='priority_task'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('username/', views.username, name='username'),
    path('username/delete_user/<int:id>/', views.delete_user, name='delete_name'),
    path('username/update_user/<int:id>/', views.update_user, name='update_user'),
    # path('home_page/add_favorite_task/<int:id>/', views.add_favorite_task),
    # path('favorite_task/', views.favorite_page),

]