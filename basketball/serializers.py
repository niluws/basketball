from rest_framework import serializers

from .models import NewsModel, NoticeModel, ImagesModel, MemberModel


class ImagesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


class NoticeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeModel
        fields = '__all__'


class MemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = '__all__'
