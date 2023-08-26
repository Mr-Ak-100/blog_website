from django.contrib import admin
from . models import Category, Article, ArticleView, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("body",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ArticleView)
admin.site.register(Comment)
