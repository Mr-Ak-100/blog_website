from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="messages", null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["read", "-created"]

    def __str__(self):
        if self.user is not None:
            return f" {self.read} | {self.user.username} > {self.title[:30]}"
        else:
            return f" {self.read} | {self.name} > {self.title[:30]}"
