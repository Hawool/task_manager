from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'stat', 'text', 'date_planned']
        labels = {'name': ''}