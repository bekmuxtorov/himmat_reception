from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'full_name',
        'gender',
        'is_staff'
    )
    list_filter = ('gender', 'is_staff')
    ordering = ('created_at',)
    list_per_page = 50
    search_fields = ('phone_number', 'full_name', 'username', 'telegram_id')