from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import Region, Location, Post
from django.shortcuts import render, get_object_or_404
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

def posts(request):
    return render(request, 'maps/posts.html')     

# def post_detail(request, slug):
#     # Fetch the post using slug or return 404 if not found
#     post = get_object_or_404(Post, slug=slug)
    
#     # Render the detail page with the post data
#     return render(request, 'maps/post_detail.html', {'post': post})


from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Post

def post_detail(request, slug):
    # Fetch the post using slug or return 404 if not found
    post = get_object_or_404(Post, slug=slug)
    region = post.region
    location = post.location

    return render(request, 'maps/post_detail.html', {
        'post': post,
        'region': region,
        'location': location,
    })


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post

def get_geojson(request, slug):
    # Fetch the post using slug
    post = get_object_or_404(Post, slug=slug)

    # Initialize empty GeoJSON structures
    region_geojson = None
    location_geojson = None

    # Generate GeoJSON for the region if it exists and has a polygon
    if post.region and post.region.polygon:
        region_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": list(post.region.polygon.coords),  # Ensure the polygon is in GeoJSON format
            },
            "properties": {
                "name": post.region.name,
                "color": post.region.color,  # Include region-specific styling
            },
        }

    # Generate GeoJSON for the location if it exists and has a point
    if post.location and post.location.point:
        location_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [post.location.point.x, post.location.point.y],  # Ensure the point is in GeoJSON format
            },
            "properties": {
                "name": post.location.name,  # Include location-specific data
            },
        }

    # Return an error if neither region nor location is available
    if not region_geojson and not location_geojson:
        return JsonResponse({"error": "Region or location missing for this post"}, status=400)

    # Return the GeoJSON data for the region and location
    return JsonResponse({
        "region": region_geojson,
        "location": location_geojson,
    })

# views.py
# from django.shortcuts import render, get_object_or_404
from .models import MapChanges

# def map_changes_detail(request, slug):
#     map_change = get_object_or_404(MapChanges, slug=slug)
#     return render(request, 'maps/map_changes_detail.html', {'map_change': map_change})

def map_changes_detail(request, slug):
    # Fetch the MapChanges object using the slug
    map_change = get_object_or_404(MapChanges, slug=slug)
    
    return render(request, 'maps/map_changes_detail.html', {
        'map_change': map_change,
    })

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import MapChanges

def geojson_view(request, slug):
    # Get the MapChange object by slug
    map_change = get_object_or_404(MapChanges, slug=slug)

    # Prepare GeoJSON data for region and location
    geojson_data = {
        'location': None,
        'region': None,
    }

    if map_change.location:
        geojson_data['location'] = {
            "type": "Point",
            "coordinates": [map_change.location.point.x, map_change.location.point.y],
            "properties": {
                "name": map_change.location.name,
                "description": map_change.location.description,
            }
        }

    if map_change.region:
        geojson_data['region'] = {
            "type": "Polygon",
            "coordinates": map_change.region.polygon.coords,
            "properties": {
                "name": map_change.region.name,
                "color": map_change.region.color,
            }
        }

    return JsonResponse(geojson_data)
