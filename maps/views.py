from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import Region, Location
from .serializers import RegionGeoJSONSerializer, LocationGeoJSONSerializer

def map_view(request):
    regions = Region.objects.all()
    locations = Location.objects.all()

    # Serialize regions
    regions_geojson = RegionGeoJSONSerializer(regions, many=True).data
    regions_geojson_json = JSONRenderer().render(regions_geojson)

    # Serialize locations
    locations_geojson = LocationGeoJSONSerializer(locations, many=True).data
    locations_geojson_json = JSONRenderer().render(locations_geojson)

    return render(request, 'maps/map.html', {
        'regions_geojson': regions_geojson_json.decode('utf-8'),
        'locations_geojson': locations_geojson_json.decode('utf-8'),
    })

# views.py
from rest_framework.generics import ListAPIView
from .models import Region, Location
from .serializers import RegionGeoJSONSerializer, LocationGeoJSONSerializer

class RegionListCreateView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionGeoJSONSerializer

class LocationListCreateView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationGeoJSONSerializer

from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
