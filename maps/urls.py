from django.urls import path
from .views import map_view, RegionListCreateView, LocationListCreateView

urlpatterns = [
    path('regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('map/', map_view, name='map_view'),
]
