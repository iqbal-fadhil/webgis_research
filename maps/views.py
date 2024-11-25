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

def post_detail(request, slug):
    # Fetch the post using slug or return 404 if not found
    post = get_object_or_404(Post, slug=slug)
    
    # Render the detail page with the post data
    return render(request, 'maps/post_detail.html', {'post': post})

from django.shortcuts import render, get_object_or_404
from .models import Post

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return render(request, 'maps/post_detail.html', {'post': post})

# def region_coords(region):
#     if region and region.polygon:
#         return region.polygon.coords[0]  # Assuming the polygon has a list of coordinates
#     return []

# def post_detail(request, slug):
#     post = Post.objects.get(slug=slug)
#     region_coordinates = region_coords(post.region)
#     context = {
#         'post': post,
#         'region_coordinates': region_coordinates,
#     }
#     return render(request, 'maps/post_detail.html', context)

