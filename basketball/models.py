from django.db import models


class BaseModel(models.Model):
    context = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NewsModel(BaseModel):
    def __str__(self):
        return f"News: {self.context[:50]}..."


class NoticeModel(BaseModel):
    def __str__(self):
        return f"Notice: {self.context[:50]}..."


class ImagesModel(BaseModel):
    image = models.ImageField(upload_to='images/')
    notice = models.ForeignKey(NoticeModel, on_delete=models.CASCADE, null=True, blank=True, related_name='images')
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, null=True, blank=True, related_name='images')

    def __str__(self):
        return f"Image: {self.context[:50]}..."
