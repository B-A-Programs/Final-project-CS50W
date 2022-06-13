from django.contrib import admin
from .models import User, Job_experiences, Education, Languages, Courses, Job, Message

class JobAdmin(admin.ModelAdmin):
    filter_horizontal = ("applicants", "accepted",)

# Register your models here.
admin.site.register(User)
admin.site.register(Job_experiences)
admin.site.register(Education)
admin.site.register(Languages)
admin.site.register(Courses)
admin.site.register(Job, JobAdmin)
admin.site.register(Message)