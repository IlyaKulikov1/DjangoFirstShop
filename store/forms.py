from django import forms
from django.forms.widgets import (
    DateTimeInput,
    Textarea,
)
from .models import Category


class CreateProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(Category.objects.all())
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=1)
    created = forms.DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"})
    )
    available = forms.BooleanField(required=True)
    image = forms.ImageField()
    description = forms.CharField(max_length=500, required=False, widget=Textarea())
