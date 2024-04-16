from django.contrib import admin
from .models import Task, AppUser

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Task)