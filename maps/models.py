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
