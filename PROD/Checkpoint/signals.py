from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Attendance, TotalHoursWorked
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out

@receiver(post_save, sender=Attendance)
def update_total_hours(sender, instance, **kwargs):
    user = instance.user
    month_start = instance.work_date.replace(day=1)
    month_end = (month_start + timezone.timedelta(days=31)).replace(day=1) - timezone.timedelta(days=1)
    work_date = instance.work_date
    attendances = Attendance.objects.filter(user=user, work_date__range=(month_start, month_end))
    total_hours = sum(attendance.total_hours for attendance in attendances if attendance.total_hours is not None)
    #total_hours = sum(attendance.total_hours for attendance in attendances)

    total_hours_record, created = TotalHoursWorked.objects.get_or_create(user=user, month=month_start)
    total_hours_record.total_hours = total_hours
    total_hours_record.save()

@receiver(user_logged_in)
def clock_in(sender, request, user, **kwargs):
    work_date = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(user=user, work_date=work_date)
    if created or attendance.clock_in_time is None:
        attendance.clock_in_time = timezone.now()
        attendance.save()

@receiver(user_logged_out)
def clock_out(sender, request, user, **kwargs):
    work_date = timezone.now().date()
    try:
        attendance = Attendance.objects.get(user=user, work_date=work_date)
        attendance.clock_out_time = timezone.now()
        attendance.save()
    except Attendance.DoesNotExist:
        pass
