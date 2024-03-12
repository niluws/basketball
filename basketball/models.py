from django.db import models


class NewsModel(models.Model):
    image = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name="عکس")
    title = models.CharField(max_length=225, null=True, blank=True, verbose_name="موضوع")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "خبر ها"
        verbose_name = "خبر"


class ClassModel(models.Model):
    class_name = models.CharField(max_length=225, null=True, blank=True, verbose_name="نام کلاس")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "کلاس ها"
        verbose_name = "کلاس"


class ClassDetailModel(models.Model):
    STATUS_CHOICES = (
        ("A", "پذیرش"),
        ("E", "پایان"),
    )
    GENDER_CHOICES = (
        ("M", "اقایان"),
        ("F", "بانوان"),
    )
    class_type = models.ForeignKey(ClassModel, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=225, null=True, blank=True, verbose_name="شاخه ی دوره")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True, verbose_name="وضعیت")
    deadline = models.DateField(null=True, blank=True, verbose_name="مهلت")
    capacity = models.IntegerField(null=True, blank=True, verbose_name="ظرفیت")
    city = models.CharField(max_length=225, null=True, blank=True, verbose_name="شهر")
    location = models.CharField(max_length=225, null=True, blank=True, verbose_name="ادرس")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, verbose_name="جنسیت")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    class_time = models.CharField(max_length=225, null=True, blank=True, verbose_name="ساعت کلاس")
    start_date = models.DateField(null=True, blank=True, verbose_name="شروع کلاس")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "جزییات"
        verbose_name = "جزییات"


class BlogModel(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True, verbose_name="موضوع")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")

    class Meta:
        verbose_name_plural = "بلاگ"
        verbose_name = "بلاگ"


class ImagesModel(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="عکس")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "عکس ها"
        verbose_name = "عکس"


class StaffMemberModel(models.Model):
    GENDER_CHOICES = (
        ("M", "اقا"),
        ("F", "خانم"),
    )
    image = models.ImageField(upload_to='staff/', null=True, blank=True, verbose_name="عکس")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, verbose_name="جنسیت")
    full_name = models.CharField(max_length=225, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "اعضا"
        verbose_name = "اعضا"


class BossModel(models.Model):
    image = models.ImageField(upload_to='boss/', null=True, blank=True, verbose_name="عکس")
    full_name = models.CharField(max_length=225, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "روسا"
        verbose_name = "رییس"


class CommitteeMemberModel(models.Model):
    image = models.ImageField(upload_to='committee/', null=True, blank=True, verbose_name="عکس")
    full_name = models.CharField(max_length=225, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "اعضای کمیته"


class AboutModel(ImagesModel):
    class Meta:
        verbose_name_plural = "درباره ی ما"
        verbose_name = "درباره ی ما"


class LeagueModel(models.Model):
    league_name = models.CharField(max_length=225, null=True, blank=True, verbose_name="نام لیگ")
    # available = models.BooleanField(null=True, blank=True, verbose_name="")

    class Meta:
        verbose_name_plural = "لیگ ها"
        verbose_name = "لیگ"


class LeagueTableModel(models.Model):
    GENDER_CHOICES = (
        ("M", "اقایان"),
        ("F", "بانوان"),
    )
    league = models.ForeignKey(LeagueModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name="لیگ")
    team_name = models.CharField(max_length=225, null=True, blank=True, verbose_name="نام تیم")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, verbose_name="جنسیت")
    games = models.IntegerField(null=True, blank=True, verbose_name="بازی ها")
    wins = models.IntegerField(null=True, blank=True, verbose_name="برد")
    fails = models.IntegerField(null=True, blank=True, verbose_name="باخت")
    draws = models.IntegerField(null=True, blank=True, verbose_name="مساوی")
    goals = models.IntegerField(null=True, blank=True, verbose_name="گل ها")
    differences = models.IntegerField(null=True, blank=True, verbose_name="تفاضل")
    scores = models.IntegerField(null=True, blank=True, verbose_name="امیتاز ها")

    class Meta:
        verbose_name_plural = "جداول لیگ"
        verbose_name = "جدول لیگ"
