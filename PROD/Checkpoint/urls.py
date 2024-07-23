# urls.py

from django.urls import path
from .views import clock_in, clock_out, attendance_status, dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard' ),
    path('clock-in/', clock_in, name='clock_in'),
    path('clock-out/', clock_out, name='clock_out'),
    path('attendance-status/', attendance_status, name='attendance_status'),
]

