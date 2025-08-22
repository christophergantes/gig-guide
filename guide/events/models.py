from core.models import Post
from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=127)
    postal_code = models.CharField(max_length=63)
    lattitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name}, {self.address}, {self.city}"


class EventPost(Post):
    date = models.DateField()
    start_time = models.TimeField()
    image = models.ImageField(upload_to="event_images", blank=True)

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    custom_location = models.CharField(max_length=255, blank=True)

    def get_address(self):
        if self.venue:
            return self.venue
        return self.custom_location
