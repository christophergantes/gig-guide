from core.models import Post
from django.db import models


# Create your models here.
class ForumPost(Post):
    labels = [("sell", "Sell/Buy"), ("members", "Find Members"), ("general", "General")]
    category = models.CharField(max_length=100, choices=labels)
