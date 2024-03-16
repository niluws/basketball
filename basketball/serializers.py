from rest_framework import serializers

from .models import NewsModel, ClassModel, ImagesModel, StaffModel, BlogModel, AboutModel, LeagueModel, BossModel, \
    CommitteeModel, ClassDetailModel, ImageCategoryModel, AboutImagesModel


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
        fields = ['class_name', 'class_type']


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'


class ImageCategoryModelSerializer(serializers.ModelSerializer):
    image = ImageModelSerializer(many=True, read_only=True)

    class Meta:
        model = ImageCategoryModel
        fields = ['id', 'category_title', 'image']


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
        fields = '__all__'


class AboutImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImagesModel
        fields = '__all__'


class AboutModelSerializer(serializers.ModelSerializer):
    image = AboutImageModelSerializer(many=True, read_only=True)

    class Meta:
        model = AboutModel
        fields = ['description', 'image']


class LeagueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueModel
        fields = '__all__'


class LeagueTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueModel
        fields = '__all__'
