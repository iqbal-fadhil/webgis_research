# serializers.py
from rest_framework import serializers
from .models import Region, Location

class RegionGeoJSONSerializer(serializers.ModelSerializer):
    polygon = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ['id', 'name', 'color', 'polygon']

    def get_polygon(self, obj):
        return obj.polygon.geojson  # Convert to GeoJSON

class LocationGeoJSONSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'name', 'point']

    def get_point(self, obj):
        return obj.point.geojson  # Convert to GeoJSON

from rest_framework import serializers
from .models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'slug', 'content', 'created_at', 'updated_at']

# serializers.py

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    region_coords = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'updated_at', 'region_coords']

    def get_region_coords(self, obj):
        if obj.region and obj.region.polygon:
            return obj.region.polygon.coords[0]  # Returning the coordinates
        return []
