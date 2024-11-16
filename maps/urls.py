from django.urls import path
from .views import map_view, RegionListCreateView, LocationListCreateView, PostListView

urlpatterns = [
    path('regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('posts/', PostListView.as_view(), name='post-list-create'),
    path('', map_view, name='map_view'),
]
