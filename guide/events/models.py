from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=127)
    postal_code = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name}, {self.address}, {self.city}"


class Event(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(max_length=511)
    date = models.DateField()
    start_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to="event_images", blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    custom_address = models.CharField(max_length=255, blank=True, null=True)
    custom_city = models.CharField(max_length=127, blank=True, null=True)
    custom_state = models.CharField(max_length=127, blank=True, null=True)
    custom_postal_code = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.venue if self.venue else self.date}"
