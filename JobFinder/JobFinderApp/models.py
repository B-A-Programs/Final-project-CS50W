from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    description = models.CharField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    field = models.CharField(max_length=500, blank=True, null=True)
    is_company = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    link_to_location = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['-id']

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

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_posts")
    applicants = models.ManyToManyField(User, related_name="applications", blank=True)
    accepted = models.ManyToManyField(User, related_name="accepted", blank=True)
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    color = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=2000)
    requirements = models.TextField(max_length=1500)
    compensation = models.TextField(max_length=1500, default="None")
    field = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.title} at {self.user.username}"

class Message(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interviews")
    date = models.DateField(blank = True, null = True)
    time = models.CharField(max_length=20)
    location = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.company.username} interview for {self.person.first_name} {self.person.last_name}"