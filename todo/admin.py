from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)