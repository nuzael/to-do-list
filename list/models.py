from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    task = models.CharField(max_length=255, verbose_name='Task')
    completed = models.BooleanField(default=False, verbose_name='Completed')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    
    def __str__(self):
        return self.task
    