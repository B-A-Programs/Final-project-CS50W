# Generated by Django 4.0.4 on 2022-06-08 14:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobFinderApp', '0017_job_compensation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applicants',
            field=models.ManyToManyField(blank=True, related_name='applications', to=settings.AUTH_USER_MODEL),
        ),
    ]