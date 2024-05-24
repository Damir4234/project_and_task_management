from django.contrib import admin
from tasks.models import Task, Project


admin.site.register(Task)

admin.site.register(Project)
