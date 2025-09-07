from django.contrib.auth.models import User
from django.db import models

from core.models import Post


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", blank=True
    )
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", blank=True, null=True
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} on {self.post}"
