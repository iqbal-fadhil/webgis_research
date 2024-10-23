from django.db import models
from django.contrib.gis.db import models as geomodels  # for geographic fields

class Region(models.Model):
    name = models.CharField(max_length=100)
    geometry = geomodels.PolygonField()  # For choropleth
    color = models.CharField(max_length=7)  # e.g., '#ff0000' for red

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
