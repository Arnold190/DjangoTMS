from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Attendance, TotalHoursWorked
from django.contrib.auth.models import User

@receiver(post_save, sender=Attendance)
def update_total_hours(sender, instance, **kwargs):
    user = instance.user
    month_start = instance.date.replace(day=1)
    month_end = (month_start + timezone.timedelta(days=31)).replace(day=1) - timezone.timedelta(days=1)

    attendances = Attendance.objects.filter(user=user, date__range=(month_start, month_end))
    total_hours = sum(attendance.total_hours for attendance in attendances)

    total_hours_record, created = TotalHoursWorked.objects.get_or_create(user=user, month=month_start)
    total_hours_record.total_hours = total_hours
    total_hours_record.save()
