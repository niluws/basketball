from rest_framework import serializers

from .models import NewsModel, ClassModel, ImagesModel, StaffModel, BlogModel, AboutModel, LeagueModel, BossModel, \
    CommitteeModel, ClassDetailModel, ImageCategoryModel, LeagueTableModel, LeagueGroupModel, \
    RoleModel


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


class ClassDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDetailModel
        fields = '__all__'


class ClassModelSerializer(serializers.ModelSerializer):
    class_type = ClassDetailModelSerializer(many=True, read_only=True)

    class Meta:
        model = ClassModel
        fields = ['class_name', 'slug', 'class_type']


class RecentClassSerializer(serializers.ModelSerializer):
    class_types = serializers.SerializerMethodField()

    class Meta:
        model = ClassModel
        fields = ['class_name', 'slug', 'class_types']

    def get_class_types(self, obj):
        recent_class_types = obj.class_type.all().order_by('-created_at')[:1]
        serializer = ClassDetailModelSerializer(recent_class_types, many=True)
        return serializer.data


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'


class RecentImageCategoryModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ImageCategoryModel
        fields = ['id', 'category_title', 'slug', 'image']

    def get_image(self, obj):
        images = obj.image.all()[:2]
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
