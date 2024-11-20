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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .models import Event  # Assuming you have an Event model for storing events
from django.utils.timezone import localtime
from .models import PhysMeeting  
from datetime import datetime
from .models import TaskStats, TotalHoursWorked


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


# -------- USERDASH VIEW FILES --------------------

##dashboard Rendering

@login_required
def dashboard(request):
    context = {
        'username': request.user.username,
        
    }
    return render(request, 'Checkpoint/userdashboard.html', context)


##Passing deadlines, physical meets(appointments) and Virtual links to the dashboard


@login_required
def dashboard(request):
    # Fetch deadlines for the logged-in user
    deadlines = Deadline.objects.filter(created_by=request.user)

    # Fetch all virtual meetings
    meetings = Meetings.objects.all()

    # Fetching Physical Meets
    meetups = PhysMeeting.objects.filter(user=request.user)

    # Fetch Task Stats for the current month and year
    current_month = timezone.now().month
    current_year = timezone.now().year
    taskstats = TaskStats.objects.filter(user=request.user, month=current_month, year=current_year)

    #Hours Worked
    totalhoursworked = TotalHoursWorked.objects.filter(user=request.user)

    # Pass all the data to the template
    return render(request, 'Checkpoint/userdashboard.html', {
        'deadlines': deadlines,
        'meetings': meetings,  # Virtual meetings
        'meetups': meetups,  # Physical meetings
        'taskstats': taskstats,  # Task stats for the current month and year
        'totalhoursworked' : totalhoursworked #Total Hours Worked
    })


#-------- CALENDAR APP VIEW FILES ---------------

###Calendar

@login_required
def calendar(request):
    return render(request, 'Checkpoint/calendar.html')

##Calendar events served as JSON
def get_events(request):
    events = Event.objects.all()
    events_list = []
    for event in events:
        events_list.append({
            'title': event.title,
            'start': event.start_time,
            'end': event.end_time,
            'description': event.description,
            'category': event.category  # Add category field to the response
        })
    return JsonResponse(events_list, safe=False)


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



#----------CLOCK IN & OUT HANDLING-----------------------

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

####Attendance
@login_required
def attendance_status(request):
    user = request.user
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=user, work_date=today).first()
    return render(request, 'attendance_status.html', {'attendance': attendance})


#---------------- VIRTUAL MEETING LINKS ------------

@login_required
def meeting_links(request):
    meetings = Meetings.objects.all()
    return render(request, 'meetings.html', {'meetings': meetings})



##Task View
@login_required
def create_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        upload_form = UploadForm(request.POST, request.FILES)

        # Debug: Log POST data for troubleshooting
        print("POST data:", request.POST)

        if task_form.is_valid():
            task = task_form.save(commit=False)  # Don't save yet, to assign the user
            task.user = request.user  # Assign the logged-in user to the task

            # Handle file upload
            if upload_form.is_valid() and 'file' in request.FILES:  # Ensure file is present
                upload = upload_form.save(commit=False)
                upload.save()  # Save the uploaded file
                task.uploads = upload  # Link the uploaded file to the task

            task.save()  # Save the task after assigning user and uploads
            return redirect('create_task')  # Redirect after successful task creation
        else:
            # Debug: Log form errors to troubleshoot
            print("Task form errors:", task_form.errors)
            print("Upload form errors:", upload_form.errors)
    else:
        task_form = TaskForm()
        upload_form = UploadForm()

    # Fetch tasks for the current user
    tasks = Task.objects.filter(user=request.user)

    return render(request, 'Checkpoint/tasks.html', {
        'task_form': task_form,
        'upload_form': upload_form,
        'tasks': tasks
    })



#Deadline View
@login_required
def create_deadline(request):
    # Handle form submission
    if request.method == 'POST':
        deadline_form = DeadlineForm(request.POST)

        # Debug: Log POST data for troubleshooting
        print("POST data:", request.POST)

        if deadline_form.is_valid():
            deadline = deadline_form.save(commit=False)  # Delay saving to assign the user
            deadline.created_by = request.user  # Assign the logged-in user
            deadline.save()  # Save the deadline

            return redirect('create_deadline')  # Redirect after successful deadline creation
        else:
            # Debug: Log form errors to troubleshoot
            print("Deadline form errors:", deadline_form.errors)
    else:
        deadline_form = DeadlineForm()

    # Fetch all deadlines created by the logged-in user
    deadlines = Deadline.objects.filter(created_by=request.user)

    return render(request, 'Checkpoint/deadlines.html', {
        'deadline_form': deadline_form,  # Form for creating deadlines
        'deadlines': deadlines  # List of deadlines for the user
    })


@login_required
def deadline_list(request):
    deadlines = Deadline.objects.all()
    return render(request, 'Checkpoint/deadlines.html', {'deadlines': deadlines})

#Physical Meetups View
@login_required
def meetups(request):
    if request.method == 'POST':
        meetup_form = PhysMeetingForm(request.POST)

        # Debug: Check if request.POST contains all the necessary data
        print("POST data:", request.POST)

        if meetup_form.is_valid():
            meetup = meetup_form.save(commit=False)
            meetup.user = request.user  # Set the user to the currently logged-in user
            meetup.save()
            return redirect('meetups')  # Redirect after successful save
        else:
            # Debug: Log form errors to troubleshoot
            print("Form errors:", meetup_form.errors)
    else:
        meetup_form = PhysMeetingForm()

    # Fetch meetups for the current user
    meetups = PhysMeeting.objects.filter(user=request.user)

    return render(request, 'Checkpoint/meetups.html', {'meetup_form': meetup_form, 'meetups': meetups})


#@login_required
#def meetup_list(request):
#    deadlines = Deadline.objects.all()
#    return render(request, 'Checkpoint/deadlines.html', {'deadlines': deadlines})


@login_required
def uploads(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            upload = upload_form.save(commit=False)  # Save the form but don't commit yet
            upload.save()  # Save the upload to the database
            return redirect('uploads')  # Redirect to the same page after upload

        else:
            # Debug: Log form errors to troubleshoot
            print("Upload form errors:", upload_form.errors)

    else:
        upload_form = UploadForm()

    # Fetch uploads for the current user
    uploads = Uploads.objects.all()  # You can further filter this as needed

    return render(request, 'Checkpoint/uploads.html', {
        'upload_form': upload_form,
        'uploads': uploads  # Pass the uploads to the template
    })




#Total Employee View
@login_required
def total_employees(request):
    total = User.objects.count()
    context = {'total': total}
    return render(request, 'total_employees.html', context)


##Logout Handling View
@method_decorator(csrf_protect, name='dispatch')
class CustomLogoutView(LogoutView):
    template_name = 'Checkpoint/logout.html'  # You can create a custom logout template if needed

    def get_next_page(self):
        # Redirect to login page after logout
        return reverse_lazy('login')  # Redirect to your custom login view