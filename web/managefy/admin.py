from .models import (
    TelegramGroups,
    Groups,
    Courses,
    Applications,
    AdminMessage,
    UserMessage
)
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "Himmat 700+ loyihasi"
admin.site.site_title = "Himmat 700+"
admin.site.index_title = "Himmat 700+ "

admin.site.unregister(Group)


@admin.register(TelegramGroups)
class TelegramGroupsAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'name', 'created_at')
    search_fields = ('name', 'telegram_id')
    list_per_page = 50


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'organiser',
        'course',
        'for_whom',
        'start_date',
        'end_date'
    )
    search_fields = (
        'name',
        'organiser',
        'course__name',
        'telegram_group__name'
    )
    list_filter = (
        'organiser',
        'course',
        'for_whom',
        'start_date',
        'end_date'
    )
    list_per_page = 50


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


class AdminMessageAdmin(admin.TabularInline):
    model = AdminMessage
    extra = 1


class UserMessageAdmin(admin.TabularInline):
    model = UserMessage
    fields = ['text', 'created_at']
    extra = 1


@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'group',
        'is_accepted',
        'is_enter_group',
        'created_at'
    )
    list_filter = ('is_accepted',)
    search_fields = ('user', 'group__name')
    list_per_page = 50
    inlines = [
        AdminMessageAdmin,
    ]
