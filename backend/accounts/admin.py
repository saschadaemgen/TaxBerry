from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'company', 'language', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'language', 'company')
    fieldsets = UserAdmin.fieldsets + (
        ('Zusätzliche Infos', {'fields': ('language', 'company')}),
    )