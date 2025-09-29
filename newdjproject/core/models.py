from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Extend User model to add field
class User(AbstractUser):
    ROLE_CHOICES=[
        ('ADMIN','admin'),
        ('MANAGER','manager'),
        ('DEVELOPER','developer')
    ]
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default='developer')

    def __str__(self):      
        return self.username
    
class Project(models.Model):
    name=models.CharField(max_length=100)
    manager=models.ForeignKey(User,on_delete=models.CASCADE,related_name='managed_projects')
    developer=models.ManyToManyField(User,related_name='projects',blank=True) 

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks')
    assigned_to=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='tasks',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# A log model for signals
class TaskLog(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    action=models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.task.title} - {self.action}" 
    
class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}" 
    
class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at}" 