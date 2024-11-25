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


def get_geojson(request, slug):
    # Fetch the post using slug
    post = get_object_or_404(Post, slug=slug)

    region_geojson = None
    location_geojson = None

    if post.region and post.region.polygon:
        region_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": list(post.region.polygon.coords),  # Region as GeoJSON
            },
            "properties": {
                "name": post.region.name,
                "color": post.region.color,
            },
        }

    if post.location and post.location.point:
        location_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [post.location.point.x, post.location.point.y],  # Location as GeoJSON
            },
            "properties": {
                "name": post.location.name,
            },
        }

    if not region_geojson and not location_geojson:
        return JsonResponse({"error": "Region or location missing for this post"}, status=400)

    return JsonResponse({
        "region": region_geojson,
        "location": location_geojson,
    })
