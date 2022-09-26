from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150)
    content= forms.CharField()
    is_publisher = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())