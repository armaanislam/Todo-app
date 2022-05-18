from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    class Meta: #Meta class provides extra attributes
        model = Task #For which model are we trying to create form
        fields = ['title']

class TaskUpdateForm(forms.ModelForm):
    class Meta: #Meta class provides extra attributes
        model = Task #For which model are we trying to create form
        fields = '__all__'