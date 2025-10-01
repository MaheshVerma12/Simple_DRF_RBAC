from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProjectViewSet, TaskViewSet, TaskLogViewSet, NotificationViewSet, CommentsViewSet, CurrentUserView

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('tasks', TaskViewSet, basename='tasks')
router.register('tasklogs', TaskLogViewSet, basename='tasklogs')
router.register('notifications', NotificationViewSet, basename='notifications')
router.register('comments', CommentsViewSet, basename='comments')

urlpatterns = router.urls + [
    path('user/', CurrentUserView.as_view(), name='current-user'),
]

