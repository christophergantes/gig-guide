from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField(max_length=511)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.title}"

    def is_event(self):
        return hasattr(self, "eventpost")

    def is_forum(self):
        return hasattr(self, "forumpost")
