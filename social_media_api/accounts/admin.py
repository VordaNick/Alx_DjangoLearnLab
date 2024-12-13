from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'username', 'is_superuser']
    
admin.site.register(CustomUser, UserAdmin)