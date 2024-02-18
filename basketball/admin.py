from django.contrib import admin

from .models import NewsModel, NoticeModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('context', 'created_at', 'updated_at')


@admin.register(NoticeModel)
class NoticeModelAdmin(admin.ModelAdmin):
    list_display = ('context', 'created_at', 'updated_at')


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('context', 'created_at', 'updated_at', 'image', 'notice', 'news')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
