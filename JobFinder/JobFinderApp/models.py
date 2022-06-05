from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    description = models.CharField(max_length=500, blank=True)

class job_experiences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    company_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

class languages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="languages")
    language = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

class education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education")
    institution = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
