from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_seller', 'is_customer')
    list_filter = ('is_seller', 'is_customer')
