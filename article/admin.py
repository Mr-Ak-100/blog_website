from django.contrib import admin
from . models import Category, Article, ArticleView, Comment

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(ArticleView)
admin.site.register(Comment)
