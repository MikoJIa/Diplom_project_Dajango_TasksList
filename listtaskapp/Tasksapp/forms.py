from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Manager
from django.contrib.auth.models import User
from .models import User, Tasks
from django.forms import ModelForm


# class UserRegisterForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ['name', 'age', 'first_password', 'second_password']

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'age']

    def clean_password(self):  # для проверки совпадения первого пороля и второго
        cd = self.cleaned_data  # эта проверка происходит на этапе is_valid()
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Введите правильный пароль!')
        return cd['password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # class Meta:
    #     model = User
    #     fields = ['name', 'password']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'  # ['title', 'description', 'user', 'is_favorite']''
        obj_task = Manager()