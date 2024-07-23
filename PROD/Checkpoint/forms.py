# forms.py

from django import forms
from .models import Task, Uploads

class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ['file']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'task', 'due_date', 'status', 'description', 'uploads']
