from django import forms
from django.contrib.auth import get_user_model

# NOT NEEDED NOW!
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'id': 'password-field'})
    )