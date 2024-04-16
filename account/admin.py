from django.contrib import admin

from .models import RegisterFormModel


@admin.register(RegisterFormModel)
class RegisterFormModelAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
