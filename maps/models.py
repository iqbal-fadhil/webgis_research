from django.db import models
from django.contrib.gis.db import models as gis_models

class Region(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)
    polygon = gis_models.PolygonField()  # For polygon data

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    # latitude = models.FloatField()  # Optional, but can use for display
    # longitude = models.FloatField()  # Optional, but can use for display
    point = gis_models.PointField()  # For point data

    def __str__(self):
        return self.name

from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

