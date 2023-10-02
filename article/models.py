from django.db import models
from django.contrib.auth.models import User
from . managers import CategoryManager, ArticleManager, CommentManager


class Category(models.Model):

    title = models.CharField(max_length=35, unique=True, verbose_name="عنوان")
    slug = models.SlugField(max_length=30, verbose_name="url", primary_key=True)
    sidebar = models.BooleanField(default=False, help_text="نشان دادن در سایدبار")
    created = models.DateTimeField(auto_now_add=True)
    objects = CategoryManager()

    class Meta:
        ordering = ["-sidebar"]
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=120, verbose_name="عنوان")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", verbose_name="نویسنده")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی های مقاله")
    slug = models.SlugField(max_length=30, verbose_name="url", primary_key=True)
    main_image = models.ImageField(upload_to="articles_images/", verbose_name="تصویر اصلی")
    body = models.TextField(verbose_name="متن مقاله")

    views = models.IntegerField(default=0, verbose_name="تعداد بازدید ها")
    banner = models.BooleanField(default=False, verbose_name="Home Banner", help_text="نشان دادن درون بنر اصلی سایت درون صغحه خانه")
    home_item = models.BooleanField(default=False, help_text="قرار گرفتن در مقاله های خانه")
    published = models.BooleanField(default=False, verbose_name="انتشار", help_text="تا وقتی دکمه انتشار تیک نخورد این مقاله در هیچ کدام از صفحات وبسایت قابل رؤیت نخواهد بود")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ArticleManager()

    class Meta:
        ordering = ["published", "-updated"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return f"{self.author.username} : {self.title[:40]}"


class ArticleView(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="requests", verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_requests", null=True, verbose_name="حساب کاربری")
    client_ip = models.GenericIPAddressField(verbose_name="IP")
    device = models.CharField(max_length=40, verbose_name="دستگاه")
    os = models.CharField(max_length=40, verbose_name="سیستم عامل")
    os_version = models.CharField(max_length=20, verbose_name="نسخه سیستم عامل")
    browser = models.CharField(max_length=40, verbose_name="مرورگر")
    browser_version = models.CharField(max_length=20, verbose_name="نسخه مرورگر")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "بازدید مقاله"
        verbose_name_plural = "بازدید های مقالات"

    def __str__(self):
        return f"{self.article.slug} requested by {self.client_ip}"


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="حساب کاربری")
    body = models.TextField(max_length=300, verbose_name="متن کامنت")
    published = models.BooleanField(default=False, verbose_name="انتشار", help_text="تا وقتی دکمه انتشار تیک نخورد این کامنت در هیچ کدام از صفحات وبسایت قابل رؤیت نخواهد بود")
    created = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()

    class Meta:
        ordering = ["-created"]
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return f"{self.user.username} : {self.body[:30]} "
