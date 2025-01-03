# urls.py

from django.urls import path, include
from .views import clock_in, clock_out, attendance_status, dashboard, create_deadline, deadline_list, calendar
from django.contrib.auth import views as auth_views 
from . import views
from Checkpoint.views import CustomLoginView, CustomLogoutView

#app_name = 'Checkpoint'

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('allauth.urls')),
    path('login/', CustomLoginView.as_view(template_name='Checkpoint/login.html'), name='login'),
    #path('', CustomLoginView.as_view(template_name='Checkpoint/login.html'), name='login'),
    path('dashboard/', dashboard, name='dashboard' ),
    path('tasks/', views.create_task, name='create_task' ),
    #path('tasks/', views.create_task, name='create_task' ),
    path('meetups/', views.meetups, name='meetups'),
    path('uploads/', views.uploads, name='uploads'),
    #path('clock-in/', clock_in, name='clock_in'),
    #path('clock-out/', clock_out, name='clock_out'),
    path('attendance-status/', views.attendance_status, name='attendance_status'),
    path('create_deadline/', views.create_deadline, name='create_deadline'),
    path('deadlines/', views.deadline_list, name='deadline_list'),
    path('calendar/', views.calendar, name='calendar'),
    path('logout/', CustomLogoutView.as_view(template_name='Checkpoint/logout.html'), name='logout' )
 
]

