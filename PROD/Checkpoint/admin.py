from django.contrib import admin
from .models import Attendance, Task, TaskStats, Uploads, Employee, TotalHoursWorked
from .models import Task, Meetings, Deadline, PhysMeeting


# Register your models here.
#admin.site.register(UserProfile)

admin.site.register(Task)
admin.site.register(Uploads)
admin.site.register(Meetings)
#admin.site.register(Attendance)
admin.site.register(TaskStats)
class TaskStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'year', 'weekly_completed_tasks', 'monthly_completed_tasks', 'yearly_completed_tasks')
    list_filter = ('year', 'month', 'user')
admin.site.register(Deadline)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'work_date', 'clock_in_time', 'clock_out_time', 'status', 'total_hours')
    list_filter = ('work_date', 'user')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(PhysMeeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'time', 'created_at')
    list_filter = ('date', 'user')
    search_fields = ('title', 'user__username')


#@admin.register(Attendance)
#class AttendanceAdmin(admin.ModelAdmin):
   # list_display = ('user', 'date', 'clock_in_time', 'clock_out_time', 'status', 'total_hours')
    #list_filter = ('date', 'user')



@admin.register(TotalHoursWorked)
class TotalHoursWorkedAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'total_hours')
    list_filter = ('month', 'user')