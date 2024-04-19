from rest_framework import serializers

from .models import NewsModel, ClassModel, ImagesModel, StaffModel, BlogModel, AboutModel, LeagueModel, BossModel, \
    CommitteeModel, ClassDetailModel, ImageCategoryModel, LeagueTableModel, LeagueGroupModel, \
    RoleModel


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['id', 'image', 'description']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['id', 'image', 'description']


# for detail page
class ClassDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDetailModel
        fields = ['id', 'title', 'slug', 'status', 'deadline', 'capacity', 'city', 'location', 'gender',
                  'description', 'class_time', 'start_date']


# for main Card
class ClassMainCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDetailModel
        fields = ['id', 'title', 'slug', 'status', 'deadline', 'capacity', 'gender']


# for all classes page
class ClassSerializer(serializers.ModelSerializer):
    class_type = ClassMainCardSerializer(many=True)

    class Meta:
        model = ClassModel
        fields = ['class_name', 'class_type']


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


# for gallery all images
class ImageModelSerializer(serializers.ModelSerializer):
    image_category = serializers.StringRelatedField()

    class Meta:
        model = ImagesModel
        fields = ['image_category', 'image', 'description']


# for gallery all images
class ImageCategoryModelSerializer(serializers.ModelSerializer):
    image = ImageModelSerializer(many=True, read_only=True)

    class Meta:
        model = ImageCategoryModel
        fields = ['category_title', 'image']


# main mage of gallery to show recent image per each category
class RecentImageCategoryModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ImageCategoryModel
        fields = ['id', 'category_title', 'slug', 'image']

    def get_image(self, obj):
        images = obj.image.all()[:4]
        serializer = ImageModelSerializer(images, many=True)
        return serializer.data


class StaffModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields = '__all__'


class BossModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BossModel
        fields = '__all__'


class CommitteeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeModel
        fields = ['id', 'image', 'full_name', 'gender']


class RoleModelSerializer(serializers.ModelSerializer):
    role = CommitteeModelSerializer(many=True)

    class Meta:
        model = RoleModel
        fields = ['id', 'title', 'role']


# class AboutImageModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AboutImagesModel
#         fields = '__all__'


class AboutModelSerializer(serializers.ModelSerializer):
    # image = AboutImageModelSerializer(many=True, read_only=True)

    class Meta:
        model = AboutModel
        fields = ['description']


class LeagueTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueTableModel
        fields = ['id', 'team_name', 'gender', 'games', 'wins', 'fails', 'draws', 'goals', 'differences', 'scores']


class LeagueGroupSerializer(serializers.ModelSerializer):
    leaguetablemodel_set = LeagueTableSerializer(many=True)

    class Meta:
        model = LeagueGroupModel
        fields = ['id', 'group_name', 'league', 'is_playoff', 'leaguetablemodel_set']


class LeagueModelSerializer(serializers.ModelSerializer):
    leaguegroupmodel_set = LeagueGroupSerializer(many=True)

    class Meta:
        model = LeagueModel
        fields = ['id', 'league_name', 'leaguegroupmodel_set']
