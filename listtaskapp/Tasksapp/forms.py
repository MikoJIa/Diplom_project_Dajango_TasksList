from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Manager

from .models import User, Tasks
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'first_password', 'second_password']


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['name', 'password']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        obj_task = Manager()