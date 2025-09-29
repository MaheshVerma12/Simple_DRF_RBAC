from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Task,TaskLog,Notification
from django.core.mail import send_mail

#Signal to create a tasklog whenever a new Task is created 
@receiver(post_save,sender=Task)                
def create_task_log(sender,instance,created,**kwargs):
    if created:
        TaskLog.objects.create(task=instance,action=f'New Task Created -> {instance.title}')

    else:
        TaskLog.objects.create(task=instance,action=f'Task Updated -> {instance.title}')


@receiver(pre_save, sender=Task)  
def store_old_assigned_to(sender, instance, **kwargs):        
    try:
        if instance.pk:
            instance._old_assigned_to = Task.objects.get(pk=instance.pk).assigned_to
        else:
            instance._old_assigned_to = None        
    except Task.DoesNotExist:
        instance._old_assigned_to = None  

# Use post_save to send notification after the task is successfully saved
@receiver(post_save, sender=Task)
def create_assignment_notification(sender, instance, created, **kwargs):
    """
    Signal to create a notification when a task is assigned or reassigned.
    """
    try:
        new_assignee = instance.assigned_to 
        
        if created:
            # Case 1: A new task is created and assigned to someone.
            if new_assignee:
                message = f"You have been assigned a new task: '{instance.title}'"
                Notification.objects.create(user=new_assignee, message=message)

                #Send Email notification
                send_mail(
                    subject="New Task Assignment",
                    message=f"Hi, {instance.assigned_to.username},\n\n"
                            f"You have been assigned to a task: {instance.title} \n\n"
                            f"Project: {instance.project.name}\n\n"
                            f"Best Regards, \n RBAC system",
                    from_email="maheshcverma1223@gmail.com",
                    recipient_list=[instance.assigned_to.email],
                    fail_silently=True,

                )


        else:
            # Case 2: An existing task is updated.
            old_assignee = getattr(instance, '_old_assigned_to', None)
            # Check if the assignee has changed and there is a new assignee.
            if old_assignee != new_assignee and new_assignee:
                message = f"A task assigned to you has been updated: '{instance.title}'"
                Notification.objects.create(user=new_assignee, message=message)

                #Send notification email
                send_mail(
                    subject="Task Assignment Updated",
                    message=f"Hi, {instance.assigned_to.username}, \n"
                            f"Your task has been updated to {instance.title} \n"
                            f"The task belongs to the project {instance.project.name} \n"
                            f"Best Regards, \n RBAC system",
                    from_email="maheshcverma1223@gmail.com",
                    recipient_list=[instance.assigned_to.email],
                    fail_silently=True
                    
                )


    except Exception as e:        
        # Handle potential errors, e.g., logging
        print(f"Error in create_assignment_notification signal: {e}")
            


