from django.contrib import admin
from .models import Region, Location

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

admin.site.register(Region, RegionAdmin)
admin.site.register(Location, LocationAdmin)
