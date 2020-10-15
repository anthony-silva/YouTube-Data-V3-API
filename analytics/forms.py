from django.db import models
from django import forms
from analytics.models import Search

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))