from django.contrib import admin
from django.contrib.admin import register
from base.models import Task

@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'complete', 'created_time']
    list_filter = ['complete']


# admin.site.register(Task)