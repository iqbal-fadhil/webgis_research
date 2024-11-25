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
    point = gis_models.PointField(null=True, blank=True)  # For point data

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
    featured_image = models.ImageField(upload_to='featured_images/', null=True, blank=True)  # Featured Image Field
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )  # Optional reference to a specific location
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )  # Optional reference to a region


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# models.py (Updated)
from django.db import models
from django.utils.text import slugify
from django.contrib.gis.db import models as gis_models

class MapChanges(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    animation_url = models.URLField(help_text="URL to GIF or video that shows the map changes")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.location.name}-{self.region.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        location_name = self.location.name if self.location else "No location"
        region_name = self.region.name if self.region else "No region"
        return f"Map Changes for {location_name} in {region_name}"