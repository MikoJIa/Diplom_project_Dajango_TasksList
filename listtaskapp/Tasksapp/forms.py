from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Manager
from django.contrib.auth.models import User
from .models import User, Tasks
from django.forms import ModelForm


class ChangeUserNameForme(forms.Form):
    new_username = forms.CharField(max_length=50)
    new_age = forms.IntegerField()

    class Meta:
        model = User
        fields = ['new_username', 'new_age', ]


class UserRegisterForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите имя'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Возраст'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['name', 'age', 'password1', 'password2']

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
    class Meta:
        model = User
        fields = ['name', 'password']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'user']  # ['title', 'description', 'user']
        obj_task = Manager()