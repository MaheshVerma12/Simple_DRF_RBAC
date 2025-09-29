from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, Task, TaskLog

# Custom User Admin to handle password hashing and custom fields
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskLog)