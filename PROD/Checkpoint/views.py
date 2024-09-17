from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Attendance, Meetings
from django.contrib import messages
from .forms import TaskForm, UploadForm, DeadlineForm, PhysMeetingForm
from .models import Task, Uploads, Deadline
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect



@method_decorator(csrf_protect, name='dispatch')
class CustomLoginView(LoginView):
    template_name = 'Checkpoint/login.html'  # Replace with your actual template path
    form_class = CustomLoginForm 

    def get_success_url(self):
        return self.get_redirect_url() or reverse_lazy('dashboard')  
    
    def form_valid(self, form):
        # Override to use email instead of username
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid email or password')
            return self.form_invalid(form)



@login_required
def dashboard(request):
    context = {
        'username': request.user.username,
        
    }
    return render(request, 'Checkpoint/userdashboard.html', context)


#@login_required
#def dashboard(request):
 #context = {
      #  'username': request.user.username,
    #}

    #return render(request, 'Checkpoint/userdashboard.html') 


#def LoginView(request):
  # return render(request, 'Checkpoint/login.html')

#@csrf_protect
#def LoginView(request):
#    if request.method == 'POST':
#        form = CustomLoginForm(request.POST)
#        if form.is_valid():
#            email = form.cleaned_data.get('email')
#            password = form.cleaned_data.get('password')
#            user = authenticate(request, username=email, password=password)  # Authenticate by email
#            if user is not None:
#                login(request, user)
#                return redirect('dashboard')  # Redirect to a success page or dashboard
#            else:
#                messages.error(request, 'Invalid email or password.')
#        else:
#            messages.error(request, 'Invalid form submission.')
#    else:
#        form = CustomLoginForm()

#    return render(request, 'Checkpoint/login.html', {'form': form})


##########



@login_required
def clock_in(request):
    user = request.user
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(user=user, work_date=today)
    if not attendance.clock_in_time:
        attendance.clock_in_time = timezone.now()
        attendance.save()
    return redirect('attendance_status')

@login_required
def clock_out(request):
    user = request.user
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=user, work_date=today).first()
    if attendance and not attendance.clock_out_time:
        attendance.clock_out_time = timezone.now()
        attendance.save()
    return redirect('attendance_status')

@login_required
def attendance_status(request):
    user = request.user
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=user, work_date=today).first()
    return render(request, 'attendance_status.html', {'attendance': attendance})

@login_required
def meeting_links(request):
    meetings = Meetings.objects.all()
    return render(request, 'meetings.html', {'meetings': meetings})

@login_required
def create_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        upload_form = UploadForm(request.POST, request.FILES)

        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user

            # Check if a file was uploaded
            if upload_form.is_valid() and request.FILES.get('file'):  # 'file' should match the field name in UploadForm
                upload = upload_form.save()
                task.uploads = upload

            task.save()
            return redirect('Checkpoint/tasks.html')  # Redirect to a task list or another page

    else:
        task_form = TaskForm()
        upload_form = UploadForm()

    return render(request, 'Checkpoint/tasks.html', {'task_form': task_form, 'upload_form': upload_form})


@login_required
def create_deadline(request):
    if request.method == 'POST':
        deadline_form = DeadlineForm(request.POST)
        if deadline_form.is_valid():
            deadline = deadline_form.save(commit=False)
            deadline.created_by = request.user
            deadline.save()
            return redirect('Checkpoint/deadlines.html')  # Change this to the name of your deadline list view
    else:
        deadline_form = DeadlineForm()
    return render(request, 'Checkpoint/deadlines.html', {'deadline_form': deadline_form})


@login_required
def meetups(request):
    if request.method == 'POST':
        meetup_form = PhysMeetingForm(request.POST)
        if meetup_form.is_valid():
            meetup = meetup_form.save(commit=False)
            meetup.created_by = request.user
            meetup.save()
            return redirect('Checkpoint/meetups.html')
    else:
        meetup_form = PhysMeetingForm()
    return render(request, 'Checkpoint/meetups.html', {'meetup_form': meetup_form})

@login_required
def uploads(request):
    if request.method == 'POST':
        uploads_form = UploadForm(request.POST)
        if uploads_form.is_valid():
            upload = uploads_form.save(commit=False)
            upload.created_by = request.user 
            upload.save()
            return redirect('Checkpoint/uploads.html')
        
    else:
        uploads_form = UploadForm()
    return render(request, 'Checkpoint/uploads.html', {'uploads_form': uploads_form})



@login_required
def deadline_list(request):
    deadlines = Deadline.objects.all()
    return render(request, 'Checkpoint/deadlines.html', {'deadlines': deadlines})


@login_required
def total_employees(request):
    total = User.objects.count()
    context = {'total': total}
    return render(request, 'total_employees.html', context)