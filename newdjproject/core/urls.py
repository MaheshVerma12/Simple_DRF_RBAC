from rest_framework.routers import DefaultRouter 
from .views import ProjectViewSet,TaskViewSet,TaskLogViewSet,NotificationViewSet,CommentsViewSet

router=DefaultRouter()
router.register('projects',ProjectViewSet,basename='projects')
router.register('tasks',TaskViewSet,basename='tasks')
router.register('tasklogs',TaskLogViewSet,basename='tasklogs')
router.register('notifications',NotificationViewSet,basename='notifications')
router.register('comments',CommentsViewSet,basename='comments') 

urlpatterns=router.urls  

