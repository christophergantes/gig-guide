# Generated by Django 5.2.4 on 2025-07-26 23:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="image",
            field=models.ImageField(blank=True, upload_to="event_images"),
        ),
    ]
