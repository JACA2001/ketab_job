# Generated by Django 4.2.16 on 2024-11-26 02:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_company_job_staf'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]