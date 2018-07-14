from django.shortcuts import render, redirect
import googlemaps
from datetime import datetime

# Create your views here.

def index(request):
    gmaps = googlemaps.Client(key='AIzaSyBCpcT3_3H3Qd7dZ05uK_HqoQ2id7fz8M8')
    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
    print(now)
    print(directions_result)
    # print(geocode_result)
    # print(gmaps)
    # print(reverse_geocode_result)
    context = {
        'directions_result': directions_result,
        'geocode_result': geocode_result,
        'gmaps': gmaps,
        'now': now,
        'reverse_geocode_result': reverse_geocode_result,
    }
    return render(request, 'google_maps_api/index.html', context)