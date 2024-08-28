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
        fields = ['task', 'due_date', 'status', 'description', 'uploads']
        widgets = {
            'task' : forms.TextInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Enter Task Title',
                'rows': 2
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Select date',
                'data-provider': 'flatpickr',
                'data-date-format': 'd M, Y',
                'type': 'datetime-local'
            }),
            'status': forms.Select(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Enter status'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Enter description',
                'rows': 10
            }),
        }

class DeadlineForm(forms.ModelForm):
    class Meta:
        model = Deadline
        fields = ['title', 'description', 'due_date']
        

class PhysMeetingForm(forms.ModelForm):
    class Meta:
        model = PhysMeeting
        fields = ['title', 'work_date', 'time', 'description']