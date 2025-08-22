from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(default="no_pfp.png", upload_to="pfp", blank=True)
    bio = models.TextField(max_length=127, blank=True)
