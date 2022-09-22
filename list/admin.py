from django.contrib import admin
from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'completed')
    list_display_links = ('id', 'task')
    list_editable = ('completed',)
    

admin.site.register(ToDo, ToDoAdmin)
