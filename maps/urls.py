from django.urls import path
from .views import map_view, RegionListCreateView, LocationListCreateView, PostListView, post_detail, get_geojson
from . import views

urlpatterns = [
    path('regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('posts/', PostListView.as_view(), name='post-list-create'),
    path('', map_view, name='map_view'),
    path('all-posts/', views.posts, name='posts'),
    path('all-posts/<str:slug>/', views.post_detail, name='post_detail'),
    path('geojson/<slug:slug>/', views.get_geojson, name='get_geojson'),
]
