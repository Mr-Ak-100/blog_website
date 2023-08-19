from django.db import models


class CategoryManager(models.Manager):

    def sidebar_items(self):
        return self.filter(sidebar=True)


class ArticleManager(models.Manager):

    def published(self):
        return self.filter(published=True)

    def banner_items(self):
        return self.filter(banner=True).exclude(published=False)

    def home_items(self):
        return self.filter(home_item=True).exclude(published=False)


class CommentManager(models.Manager):

    def published(self):
        return self.filter(published=True)

