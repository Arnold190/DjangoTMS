from django.db import models
from django.contrib.auth.models import User 
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django import forms
from django.contrib.auth.forms import AuthenticationForm
import uuid
from datetime import timedelta
from django.conf import settings

# Create your models here.

def generate_user_id(prefix):
    unique_id = uuid.uuid4().hex[:4].upper()
    return f"{prefix}{unique_id}"


class UserProfile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     custom_user_id = models.CharField(max_length=20, unique=True, blank=True)



     def save(self, *args, **kwargs):
        if not self.custom_user_id:
            prefix = "SCOW/ADMIN/" if self.user.is_staff else "SCOW/STAFF/"
            self.custom_user_id = generate_user_id(prefix)
        super(UserProfile, self).save(*args, **kwargs)


     def __str__(self):
        return self.user.username


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter your Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter your Password'
    }))

    def clean_username(self):
        email = self.cleaned_data.get('username')
        return email


class Task(models.Model):
    STATUS_CHOICES = [
     ('Pending', 'Pending'),
     ('Processing', 'Processing'),
     ('Completed', 'Completed'),
     ('Cancelled', 'Cancelled')

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    uploads = models.FileField(upload_to='uploads/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Task: {self.task} | Due: {self.due_date.strftime('%Y-%m-%d %H:%M')} | Status: {self.status} | Assigned to: {self.user.username}"


class TaskStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    weekly_completed_tasks = models.PositiveIntegerField(default=0)
    monthly_completed_tasks = models.PositiveIntegerField(default=0)
    yearly_completed_tasks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.user.username} - {self.year}/{self.month}"


class Uploads(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.file.name


class Meetings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_date = models.DateTimeField(auto_now_add=True)
    clock_in_time = models.DateTimeField(null=True, blank=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)

    @property
    def status(self):
        if self.clock_in_time and self.clock_out_time:
            return 'Present'
        elif self.clock_in_time and not self.clock_out_time:
            return 'Still Present'
        else:
            return 'Absent'

    @property
    def total_hours(self):
        if self.clock_in_time and self.clock_out_time:
            time_diff = self.clock_out_time - self.clock_in_time
            return time_diff.total_seconds() / 3600  # convert to hours
        return 0

    def __str__(self):
        return f"{self.user.username} - {self.work_date} - {self.status}"



class Deadline(models.Model):
    STATUS_CHOICES = [
     ('Pending', 'Pending'),
     ('Processing', 'Processing'),
     ('Completed', 'Completed'),
     ('Cancelled', 'Cancelled')

    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    due_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username
    
#Physical meetings model
class PhysMeeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #meeting_link = models.URLField(max_length=200)
    work_date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username} on {self.work_date} at {self.time}"

class TotalHoursWorked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    total_hours = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)


    def __str__(self):
        return f"{self.user.username} - {self.month.strftime('%B %Y')} - {self.total_hours} hours"
