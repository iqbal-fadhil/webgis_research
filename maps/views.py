from django.shortcuts import render
from .models import Region, Location

def map_view(request):
    regions = Region.objects.all()
    locations = Location.objects.all()
    return render(request, 'maps/map.html', {'regions': regions, 'locations': locations})
