# forms.py

from django import forms
from .models import Task, Uploads, Deadline, PhysMeeting
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.conf import settings
from .models import Event


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'email',
        'class': 'form-control form-input dark:bg-zink-600/50 border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200', 
        'placeholder': 'Enter Email'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
        'class': 'form-control form-input dark:bg-zink-600/50 border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200', 
        'placeholder': 'Enter Password'
    }))

    def clean_username(self):
        email = self.cleaned_data.get('username')
        return email




class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ['name', 'description','file']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Enter File Name',
                'rows': 2
            }),
        
            'description': forms.Textarea(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Enter description',
                'rows': 10
            }),
            
            'file' : forms.FileInput(attrs={
            #'class' : "text-white btn bg-custom-500 border-custom-500 hover:text-white hover:bg-custom-600 hover:border-custom-600 focus:text-white focus:bg-custom-600 focus:border-custom-600 focus:ring focus:ring-custom-100 active:text-white active:bg-custom-600 active:border-custom-600 active:ring active:ring-custom-100 dark:ring-custom-400/20"
            #'placeholder': 'Choose File',
            })
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due_date', 'status', 'description']
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
        fields = ['title', 'due_date', 'status', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Enter Task Title'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Select date',
                'data-provider': 'flatpickr',
                'data-date-format': 'd M, Y',
                'type': 'datetime-local'# Use 'text' for custom date pickers like flatpickr
            }),
            'status': forms.Select(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input border-slate-200 dark:border-zink-500 focus:outline-none focus:border-custom-500 disabled:bg-slate-100 dark:disabled:bg-zink-600 disabled:border-slate-300 dark:disabled:border-zink-500 dark:disabled:text-zink-200 disabled:text-slate-500 dark:text-zink-100 dark:bg-zink-700 dark:focus:border-custom-800 placeholder:text-slate-400 dark:placeholder:text-zink-200',
                'placeholder': 'Enter description',
                'rows': 10  # Applies only to Textarea
            }),
        }

        
class PhysMeetingForm(forms.ModelForm):
    class Meta:
        model = PhysMeeting
        fields = ['title', 'work_date', 'time', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input ...',
                'placeholder': 'Enter Meetup Title',
                'rows': 2
            }),
            'work_date': forms.DateInput(attrs={
                'class': 'form-input ...',
                'placeholder': 'Select date',
                'data-provider': 'flatpickr',
                'data-date-format': 'd M, Y',
                'type': 'date'  # Changed to 'date' instead of 'datetime-local'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-input ...',
                'type': 'time',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input ...',
                'placeholder': 'Enter description',
                'rows': 10
            }),
        }


###Event Form -- To be implemented later
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'end_time', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Title'}),
           
           # 'start_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            #'end_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
           
           # 'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }