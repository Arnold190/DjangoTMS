# forms.py

from django import forms
from .models import Task, Uploads, Deadline, PhysMeeting

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
        fields = ['title', 'date', 'time', 'description']