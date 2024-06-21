from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={"class": "form-input"}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={"class": "form-input"}))
    email = forms.EmailField(label="Почтовый ящик", widget=forms.EmailInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "input"}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={"class": "input"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


#     first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(
#         required=True,
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'placeholder': 'example@gmail.com'})
#     )
#     password1 = forms.CharField(label='Password',
#                                 strip=False,
#                                 widget=forms.PasswordInput(
#                                     attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
#
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#         }
