from django.db import models
from core.models import Post


# Create your models here.
class ForumPost(Post):
    labels = [("sell", "Sell/Buy"), ("members", "Find Members"), ("general", "General")]
    category = models.CharField(max_length=100, choices=labels)
