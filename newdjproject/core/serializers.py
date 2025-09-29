from rest_framework import serializers 
from .models import User,Project,Task,TaskLog,Notification,Comments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','role']

class ProjectSerializer(serializers.ModelSerializer):
    manager = UserSerializer(read_only=True)
    developer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='DEVELOPER'),
        many=True,
    )

    class Meta:
        model = Project
        fields = ('id', 'name', 'manager', 'developer')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'project', 'assigned_to', 'created_at')
        read_only_fields = ('created_at',)

class TaskLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskLog
        fields='__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__' 

class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comments
        fields = ['id', 'task', 'user', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']