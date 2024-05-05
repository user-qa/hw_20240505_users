from django.contrib import admin
from users.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'age', 'region']
    list_filter = ['full_name', 'phone_number', 'age', 'region']
    search_fields = ['full_name', 'phone_number', 'age', 'region']
