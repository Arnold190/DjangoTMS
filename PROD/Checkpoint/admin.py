from django.contrib import admin
from .models import Attendance, Task, TaskStats, Uploads
from .models import Task, Meetings, Deadline


# Register your models here.
#admin.site.register(UserProfile)

admin.site.register(Task)
admin.site.register(Uploads)
admin.site.register(Meetings)
admin.site.register(Attendance)
admin.site.register(TaskStats)
class TaskStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'year', 'weekly_completed_tasks', 'monthly_completed_tasks', 'yearly_completed_tasks')
    list_filter = ('year', 'month', 'user')
admin.site.register(Deadline)