# urls.py

from django.urls import path
from .views import clock_in, clock_out, attendance_status, dashboard, create_deadline, deadline_list
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard' ),
    path('clock-in/', clock_in, name='clock_in'),
    path('clock-out/', clock_out, name='clock_out'),
    path('attendance-status/', attendance_status, name='attendance_status'),
    path('create_deadline/', create_deadline, name='create_deadline'),
    path('deadlines/', deadline_list, name='deadline_list'),
   
]

