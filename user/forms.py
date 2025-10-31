from django import forms
from django.contrib.auth import get_user_model

# NOT NEEDED NOW!
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]
