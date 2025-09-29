from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from .models import Project,Task,TaskLog,Notification,Comments
from .serializers import ProjectSerializer,TaskSerializer,TaskLogSerializer,NotificationSerializer,CommentsSerializer
from .permissions import IsAdmin,IsManagerOrAdmin,IsDeveloperOfProject,CanCommentOnTask
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    permission_classes=[IsAuthenticated & (IsManagerOrAdmin | IsAdmin)] 

    def perform_create(self, serializer):  
        serializer.save(manager=self.request.user) 

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated & (IsAdmin | IsManagerOrAdmin | IsDeveloperOfProject)]

class TaskLogViewSet(viewsets.ModelViewSet):
    serializer_class=TaskLogSerializer
    queryset=TaskLog.objects.all()
    permission_classes=[IsAuthenticated, IsAdmin]

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class=NotificationSerializer
    queryset=Notification.objects.all()
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        #Each user only sees their notifications
        return self.queryset.filter(user=self.request.user) 
    
class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class=CommentsSerializer
    queryset=Comments.objects.all()
    permission_classes=[IsAuthenticated, CanCommentOnTask]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 





