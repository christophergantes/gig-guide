from django import forms
from .models import EventPost

from django.core.exceptions import ValidationError


class EventForm(forms.ModelForm):
    class Meta:
        model = EventPost
        fields = [
            "title",
            "content",
            "image",
            "date",
            "start_time",
            "venue",
            "custom_location",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        venue = cleaned_data.get("venue")
        location = cleaned_data.get("custom_location")

        if not venue and not location:
            raise ValidationError("You must porvide either a venue or location.")
        if venue and location:
            raise ValidationError("You cannot provide both a venue and a location.")

        return cleaned_data
