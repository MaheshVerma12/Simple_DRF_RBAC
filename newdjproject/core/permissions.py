from rest_framework import permissions
from .models import Task 

class IsAdmin(permissions.BasePermission):
    def has_permission(self,request,view):
        return request.user.role == 'ADMIN'
    
class IsManagerOrAdmin(permissions.BasePermission):
    def has_permission(self,request,view):
        return request.user.role in ['MANAGER', 'ADMIN']
    
class IsDeveloperOfProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):        
        # obj is the Task instance
        try:
            # First, check if the user is an Admin, the project manager, or on the project's developer team.
            is_project_manager = obj.project.manager == request.user
            is_project_developer = request.user in obj.project.developer.all()

            # An admin, the project manager, or a developer on the project can proceed.
            if not (request.user.role == 'ADMIN' or is_project_manager or is_project_developer):
                return False

            # For update methods, check if the user is the one assigned to the task.
            if request.method in ['PUT', 'PATCH']:
                # The assigned developer, the project manager, or an admin can update.
                return obj.assigned_to == request.user or is_project_manager or request.user.role == 'ADMIN'
            
            # For other methods like GET, being a project member is sufficient.
            return True
        except Exception as e:
            # Log the exception for debugging
            print(f"Error in IsDeveloperOfProject permission: {e}")
            return False
        
class CanCommentOnTask(permissions.BasePermission):
    """
    Custom permission class to only allow the assigned user, project manager or admin to comment on a task.
    """
    message="You do not have permission to comment on this task."
    def has_permission(self,request,view):
        if request.method=='GET': #If the request method is GET, we can allow the comments to be viewed.
            return True 
        
        try:
            task_id=request.data.get('task')
            if not task_id:
                self.message="A task_id must be sent to comment on that particular task."
                return False
            task=Task.objects.get(pk=task_id) #Fetch the task entry as an object on whom comment is to be made
            user=request.user

            is_admin=user.role == 'ADMIN'
            is_project_manager=task.project.manager==user
            is_project_developer=user in task.project.developer.all()

            if is_admin or is_project_manager or is_project_developer:
                return True
            else:
                return False
            
        except Exception as e:
            print(f"Error in CanCommentOnTask permission: {e}")
            return False
            



        

    
        

    
