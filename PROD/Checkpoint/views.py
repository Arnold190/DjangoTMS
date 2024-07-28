from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Attendance, Meetings

from .forms import TaskForm, UploadForm, DeadlineForm
from .models import Task, Uploads, Deadline


@login_required
def dashboard(request):
    # Logic for the dashboard view
    return render(request, 'userdashboard.html') 


@login_required
def clock_in(request):
    user = request.user
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(user=user, date=today)
    if not attendance.clock_in_time:
        attendance.clock_in_time = timezone.now()
        attendance.save()
    return redirect('attendance_status')

@login_required
def clock_out(request):
    user = request.user
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=user, date=today).first()
    if attendance and not attendance.clock_out_time:
        attendance.clock_out_time = timezone.now()
        attendance.save()
    return redirect('attendance_status')

@login_required
def attendance_status(request):
    user = request.user
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=user, date=today).first()
    return render(request, 'attendance_status.html', {'attendance': attendance})

def meeting_links(request):
    meetings = Meetings.objects.all()
    return render(request, 'meetings.html', {'meetings': meetings})


def create_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        upload_form = UploadForm(request.POST, request.FILES)
        if task_form.is_valid() and upload_form.is_valid():
            upload = upload_form.save()
            task = task_form.save(commit=False)
            task.uploads = upload
            task.save()
            return redirect('task_list')  # Redirect to a task list or another page
    else:
        task_form = TaskForm()
        upload_form = UploadForm()
    return render(request, 'create_task.html', {'task_form': task_form, 'upload_form': upload_form})


@login_required
def create_deadline(request):
    if request.method == 'POST':
        form = DeadlineForm(request.POST)
        if form.is_valid():
            deadline = form.save(commit=False)
            deadline.created_by = request.user
            deadline.save()
            return redirect('deadline_list')  # Change this to the name of your deadline list view
    else:
        form = DeadlineForm()
    return render(request, 'create_deadline.html', {'form': form})

@login_required
def deadline_list(request):
    deadlines = Deadline.objects.all()
    return render(request, 'deadline_list.html', {'deadlines': deadlines})


@login_required
def total_employees(request):
    total = User.objects.count()
    context = {'total': total}
    return render(request, 'total_employees.html', context)