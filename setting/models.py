from django.db import models


class SettingsModel(models.Model):
    website_name = models.CharField(max_length=50, verbose_name="نام وب سایت")
    phone_number = models.CharField(max_length=50, verbose_name="شماره تلفن")
    fax = models.CharField(max_length=50, verbose_name="فکس")
    post_code = models.CharField(max_length=50, verbose_name="کد پستی")
    whatsapp = models.CharField(max_length=50, verbose_name="واتس اپ")
    instagram = models.CharField(max_length=50, verbose_name="اینستاگرام")

    def __str__(self):
        return self.website_name

    class Meta:
        verbose_name_plural = "تنظیمات"
        verbose_name = "تنظیمات"
