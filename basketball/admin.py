from django.contrib import admin
from django.utils.html import format_html

from .models import NewsModel, ClassModel, BlogModel, ImagesModel, StaffModel, AboutModel, LeagueModel, \
    LeagueTableModel, ClassDetailModel, BossModel, CommitteeModel, ImageCategoryModel, \
    LeagueGroupModel, RoleModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'short_description', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    sortable_by = ('created_at',)

    def short_description(self, obj):
        return ' '.join(obj.description.split()[:15]) + '...'

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>', obj.image.url)
        else:
            return "No image"


class ClassDetailModelInline(admin.TabularInline):
    model = ClassDetailModel
    extra = 0
    readonly_fields = ('slug',)


@admin.register(ClassModel)
class ClassModelAdmin(admin.ModelAdmin):
    inlines = (ClassDetailModelInline,)
    list_display = ('class_name',)


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')

    def short_description(self, obj):
        return ' '.join(obj.description.split()[:15]) + '...'


class ImageModelInline(admin.TabularInline):
    model = ImagesModel
    extra = 0
    fields = ('image_tag', 'image', 'description',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>', obj.image.url)
        else:
            return "No image"


@admin.register(ImageCategoryModel)
class ImageCategoryModelAdmin(admin.ModelAdmin):
    inlines = (ImageModelInline,)
    list_display = ('category_title', 'display_images')
    readonly_fields = ('slug',)

    def display_images(self, obj):
        images = obj.image.all()
        if images:
            return format_html(''.join(
                '<img src="{}" style="max-width:100px; max-height:100px"/>'.format(img.image.url) for img in images))
        else:
            return "No images"


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width:100px; max-height:100px"/>')
        else:
            return "No image"

    list_display = ('image_tag', 'full_name')
    search_fields = ('full_name',)


@admin.register(BossModel)
class BossModelAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width:100px; max-height:100px"/>')
        else:
            return "No image"

    list_display = ('image_tag', 'full_name', 'city')
    search_fields = ('full_name',)


@admin.register(RoleModel)
class RoleModelAdmin(admin.ModelAdmin):
    pass


@admin.register(CommitteeModel)
class CommitteeModelAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width:100px; max-height:100px"/>')
        else:
            return "No image"

    list_display = ('image_tag', 'full_name', 'gender')
    list_filter = ('gender',)
    search_fields = ('full_name',)


# class AboutImagesModelInline(admin.TabularInline):
#     model = AboutImagesModel
#     max_num = 3
#     fields = ('image_tag', 'image')
#     readonly_fields = ('image_tag',)
#
#     def image_tag(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>', obj.image.url)
#         else:
#             return "No image"


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    # inlines = (AboutImagesModelInline,)
    MAX_OBJECTS = 1
    list_display = ('short_description',)

    def short_description(self, obj):
        return ' '.join(obj.description.split()[:15]) + '...'

    # def display_images(self, obj):
    #     images = obj.image.all()
    #     if images:
    #         return format_html(''.join(
    #             '<img src="{}" style="max-width:100px; max-height:100px"/>'.format(img.image.url) for img in images))
    #     else:
    #         return "No images"

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


class LeagueTableModelInline(admin.StackedInline):
    model = LeagueTableModel
    extra = 0


@admin.register(LeagueGroupModel)
class LeagueGroupAdmin(admin.ModelAdmin):
    inlines = [LeagueTableModelInline]
    list_display = ('group_name', 'league', 'is_playoff')
    list_editable = ('league', 'is_playoff')
    search_fields = ['group_name', 'league__league_name']


@admin.register(LeagueModel)
class LeagueModelAdmin(admin.ModelAdmin):
    list_display = ('league_name', 'available')
    search_fields = ('league_name',)
