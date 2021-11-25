from django.contrib import admin
from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_no', 'is_active', 'is_staff', 'is_admin', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_admin')
    search_filter = ('id', 'full_name', 'email', 'phone_no')

admin.site.register(User, UserAdmin)
admin.site.register(Profile)