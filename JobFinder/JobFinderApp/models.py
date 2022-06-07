from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    description = models.CharField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    field = models.CharField(max_length=500, blank=True, null=True)
    is_company = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    link_to_location = models.CharField(max_length=200, blank=True, null=True)

class Job_experiences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    company_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Languages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="languages")
    language = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education")
    institution = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)