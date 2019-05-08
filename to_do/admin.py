from django.contrib import admin
from to_do.models import Task

class MyModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Task

admin.site.register(Task,MyModelAdmin)