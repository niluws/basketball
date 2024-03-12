from django.contrib import admin
from django.utils.html import format_html

from .models import NewsModel, ClassModel, BlogModel, ImagesModel, StaffMemberModel, AboutModel, LeagueModel, \
    LeagueTableModel, ClassDetailModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    sortable_by = ('created_at',)


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(ImagesModel)
class ImagesModelAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width:100px; max-height:100px"/>')
        else:
            return "No image"

    list_display = ('image_tag', 'description')


@admin.register(StaffMemberModel)
class StaffMemberModelAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width:100px; max-height:100px"/>')
        else:
            return "No image"

    list_display = ('image_tag', 'full_name', 'gender')
    list_filter = ('gender',)
    search_fields = ('full_name',)


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    pass


class LeagueTableModelInline(admin.TabularInline):
    model = LeagueTableModel
    extra = 0


@admin.register(LeagueModel)
class LeagueModelAdmin(admin.ModelAdmin):
    inlines = (LeagueTableModelInline,)
    list_display = ('league_name',)


class ClassDetailModelInline(admin.TabularInline):
    model = ClassDetailModel
    extra = 0


@admin.register(ClassModel)
class ClassModelAdmin(admin.ModelAdmin):
    inlines = (ClassDetailModelInline,)
    list_display = ('class_name',)
