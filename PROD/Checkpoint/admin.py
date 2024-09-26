from django.contrib import admin
from .models import Attendance, Task, TaskStats, Uploads, Employee, TotalHoursWorked
from .models import Task, Meetings, Deadline, PhysMeeting

from .models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

# Register your models here.
#admin.site.register(UserProfile)
#admin.site.unregister(User)
#admin.site.unregister(Group)


#@admin.register(User)
#class UserAdmin(BaseUserAdmin, ModelAdmin):
#   pass


#@admin.register(Group)
#class GroupAdmin(BaseGroupAdmin, ModelAdmin):
  #  pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'custom_user_id')
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'status', 'due_date', 'user') 



@admin.register(Uploads)
class UploadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'description', 'uploaded_at')


@admin.register(Meetings)
class MeetingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
#admin.site.register(Attendance)

@admin.register(TaskStats)
class TaskStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'year', 'weekly_completed_tasks', 'monthly_completed_tasks', 'yearly_completed_tasks')
    list_filter = ('year', 'month', 'user')


@admin.register(Deadline)
class DeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'created_by')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'work_date', 'clock_in_time', 'clock_out_time', 'status', 'total_hours')
    list_filter = ('work_date', 'user')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(PhysMeeting)
class PhysMeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'work_date', 'time', 'created_at')
    #list_filter = ('work_date', 'user')
    #search_fields = ('title', 'user__username')


#@admin.register(Attendance)
#class AttendanceAdmin(admin.ModelAdmin):
   # list_display = ('user', 'date', 'clock_in_time', 'clock_out_time', 'status', 'total_hours')
    #list_filter = ('date', 'user')


@admin.register(TotalHoursWorked)
class TotalHoursWorkedAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'total_hours')
    #list_filter = ('month', 'user')