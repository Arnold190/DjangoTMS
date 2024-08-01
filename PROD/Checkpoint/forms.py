# forms.py

from django import forms
from .models import Task, Uploads, Deadline, PhysMeeting
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ['file']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'task', 'due_date', 'status', 'description', 'uploads']


class DeadlineForm(forms.ModelForm):
    class Meta:
        model = Deadline
        fields = ['title', 'description', 'due_date']
        

class PhysMeetingForm(forms.ModelForm):
    class Meta:
        model = PhysMeeting
        fields = ['title', 'work_date', 'time', 'description']