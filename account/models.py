from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# todo max for INTs
class RegisterFormModel(models.Model):
    CLASS_CHOICES = (
        ("A", "پذیرش"),
        ("E", "پایان"),
    )
    GENDER_CHOICES = (
        ("M", "اقایان"),
        ("F", "بانوان"),
    )
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    class_range = models.CharField(max_length=1, choices=CLASS_CHOICES, verbose_name="رده سنی ثبت نام")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="جنسیت")
    id_cart = models.IntegerField(verbose_name="شماره ملی")
    birth_date = models.DateTimeField()
    birth_place = models.CharField(max_length=50, verbose_name="محل تولد")
    father_name = models.CharField(max_length=50, verbose_name="نام پدر")
    height = models.IntegerField(verbose_name="قد")
    weight = models.IntegerField(verbose_name="وزن")
    degree = models.CharField(max_length=50, verbose_name="مدرک تحصیلی")
    school_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="نام مدرسه")
    school_address = models.CharField(max_length=50, null=True, blank=True, verbose_name="ادرس مدرسه")
    address_home = models.CharField(max_length=100, verbose_name="ادرس منزل")
    phone_number = models.CharField(_('phone number'), max_length=11, unique=True,
                                    validators=[
                                        RegexValidator(regex='^09\d{9}$',
                                                       message='Phone number must be entered in the format: "09xxxxxxxxx".')
                                    ])
    father_job = models.CharField(max_length=50, verbose_name="شغل پدر")
    father_job_address = models.CharField(max_length=100, verbose_name="محل کار پدر")
    father_phone_number = models.CharField(_('phone number'), max_length=11, unique=True,
                                           validators=[
                                               RegexValidator(regex='^09\d{9}$',
                                                              message='Phone number must be entered in the format: "09xxxxxxxxx".')
                                           ])

    mother_job = models.CharField(max_length=50, verbose_name="شغل مادر")
    mother_job_address = models.CharField(max_length=100, verbose_name="محل کار مادر")
    mother_phone_number = models.CharField(_('phone number'), max_length=11, unique=True,
                                           validators=[
                                               RegexValidator(regex='^09\d{9}$',
                                                              message='Phone number must be entered in the format: "09xxxxxxxxx".')
                                           ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_name = models.CharField(max_length=50, verbose_name="نام والد ی که تعهد را امضا کرده")
    basketball_learner_name = models.CharField(max_length=50, verbose_name="نام بسکتبال اموز در بخش تعهد")
    basketball_gym_name = models.CharField(max_length=50, verbose_name="نام مدرسه ی بسکتبال")
    signature = models.BooleanField(verbose_name="امضا")
    explanation = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "فرم های ثبت نام"
        verbose_name = "فرم ثبت نام"
