from django.contrib import admin
from tasks.models import Task, Entry

admin.site.register(Task)
admin.site.register(Entry)
