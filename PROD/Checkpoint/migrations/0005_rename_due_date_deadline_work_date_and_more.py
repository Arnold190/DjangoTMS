# Generated by Django 5.0.6 on 2024-07-31 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkpoint', '0004_rename_date_physmeeting_work_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deadline',
            old_name='due_date',
            new_name='work_date',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='work_date',
        ),
    ]