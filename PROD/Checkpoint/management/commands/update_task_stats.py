# update_task_stats.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from Checkpoint.models import Task, TaskStats

class Command(BaseCommand):
    help = 'Update task statistics'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        start_of_week = now - timedelta(days=now.weekday())
        start_of_month = now.replace(day=1)
        start_of_year = now.replace(month=1, day=1)

        for user in User.objects.all():
            weekly_completed = Task.objects.filter(
                user=user, status='Completed', created_at__gte=start_of_week
            ).count()
            monthly_completed = Task.objects.filter(
                user=user, status='Completed', created_at__gte=start_of_month
            ).count()
            yearly_completed = Task.objects.filter(
                user=user, status='Completed', created_at__gte=start_of_year
            ).count()

            task_stats, created = TaskStats.objects.get_or_create(
                user=user, month=now.month, year=now.year
            )
            task_stats.weekly_completed_tasks = weekly_completed
            task_stats.monthly_completed_tasks = monthly_completed
            task_stats.yearly_completed_tasks = yearly_completed
            task_stats.save()

        self.stdout.write(self.style.SUCCESS('Task statistics updated successfully'))
