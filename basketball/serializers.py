# serializers.py
from rest_framework import serializers

from .models import NewsModel, NoticeModel, ImagesModel, BaseModel


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ['context', 'created_at', 'updated_at']


class NewsModelSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = NewsModel


class NoticeModelSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = NoticeModel


class ImagesModelSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = ImagesModel
        fields = ['context', 'created_at', 'updated_at', 'image', 'notice', 'news']
