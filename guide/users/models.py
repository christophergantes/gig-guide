from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to="pfp", default="pfp/no_pfp.png", blank=True)
    bio = models.TextField(max_length=127, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
