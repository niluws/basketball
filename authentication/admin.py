from django.contrib import admin

from .models import User, LogUserModel, LogExceptionModel


class LogUserModelInline(admin.TabularInline):
    model = LogUserModel
    readonly_fields = ('created_at', 'event')
    extra = 0


@admin.register(LogExceptionModel)
class LogExceptionAdmin(admin.ModelAdmin):
    list_display = ('error', 'created_at')
    readonly_fields = ('error', 'created_at')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (LogUserModelInline,)

    list_display = ('phone_number', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
