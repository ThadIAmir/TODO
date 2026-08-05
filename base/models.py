from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        (0, 'Very Urgent'),
        (1, 'Urgent'),
        (2, 'Whenever')
    ]
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['priority', 'complete', '-created_time']
        


