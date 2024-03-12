from rest_framework import serializers

from .models import NewsModel, ClassModel, ImagesModel, StaffMemberModel, BlogModel, AboutModel, LeagueModel


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


class ClassModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = '__all__'


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'


class StaffMemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMemberModel
        fields = '__all__'


class AboutModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = '__all__'


class LeagueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueModel
        fields = '__all__'


class LeagueTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueModel
        fields = '__all__'
