# Generated by Django 5.0.6 on 2024-07-31 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkpoint', '0003_employee_physmeeting_totalhoursworked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='physmeeting',
            old_name='date',
            new_name='work_date',
        ),
    ]