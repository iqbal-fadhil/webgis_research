# from django.contrib import admin
# from .models import Region, Location

# class RegionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'color')

# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'latitude', 'longitude')

# admin.site.register(Region, RegionAdmin)
# admin.site.register(Location, LocationAdmin)

# from django.contrib import admin
# from django import forms
# from .models import Region, Location

# class RegionForm(forms.ModelForm):
#     class Meta:
#         model = Region
#         fields = ['name', 'color', 'polygon']

#     class Media:
#         css = {
#             'all': ('https://unpkg.com/leaflet@1.7.1/dist/leaflet.css',),
#         }
#         js = ('https://unpkg.com/leaflet@1.7.1/dist/leaflet.js', 'js/region_map.js')  # Custom JS for handling map

# class LocationForm(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields = ['name', 'latitude', 'longitude', 'point']

#     class Media:
#         css = {
#             'all': ('https://unpkg.com/leaflet@1.7.1/dist/leaflet.css',),
#         }
#         js = ('https://unpkg.com/leaflet@1.7.1/dist/leaflet.js', 'js/location_map.js')  # Custom JS for handling map

# class RegionAdmin(admin.ModelAdmin):
#     form = RegionForm
#     list_display = ('name', 'color')

# class LocationAdmin(admin.ModelAdmin):
#     form = LocationForm
#     list_display = ('name', 'latitude', 'longitude')

# admin.site.register(Region, RegionAdmin)
# admin.site.register(Location, LocationAdmin)


from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Region, Location, Post, MapChanges

class RegionAdmin(LeafletGeoAdmin):
    list_display = ('name', 'color')

class LocationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'point')

class PostAdmin(LeafletGeoAdmin):
    list_display = ('title', 'slug')    

class MapChangesAdmin(LeafletGeoAdmin):
    list_display = ('animation_url', 'slug')    



admin.site.register(Region, RegionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(MapChanges, MapChangesAdmin)
