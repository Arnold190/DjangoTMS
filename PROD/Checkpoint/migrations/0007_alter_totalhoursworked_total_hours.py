# Generated by Django 5.0.6 on 2024-08-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checkpoint', '0006_rename_work_date_deadline_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalhoursworked',
            name='total_hours',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
