from django.db import models


class BaseModel(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    context = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NewsModel(BaseModel):
    title = models.CharField(max_length=500, null=True, blank=True)
    pass


class NoticeModel(BaseModel):
    title = models.CharField(max_length=500, null=True, blank=True)
    pass


class ImagesModel(BaseModel):
    pass


class MemberModel(BaseModel):
    full_name = models.CharField(max_length=225)
    pass
