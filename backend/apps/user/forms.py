from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, SetPasswordForm

from backend.apps.user.models import User


class CustomUserCreationForm(BaseUserCreationForm):



    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'address']
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Введите email'}),
            "first_name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите имя'}),
            "last_name": forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Введите фамилию'}),
            "address":forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Введите адрес'}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Введите пароль'}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Повторите пароль'}),
        }



class UserPasswordChangeForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]