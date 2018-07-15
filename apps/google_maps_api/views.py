from django.shortcuts import render, redirect
import googlemaps
import requests
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
    directions_result = gmaps.directions("245 N 11th St, San Jose, CA 95112",
                                     "711 2nd Ave, Salt Lake City, UT, 84103",
                                     mode="driving",
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

def enter_trip(request):
    if request.method == 'GET':
        gmaps = googlemaps.Client(key='AIzaSyBCpcT3_3H3Qd7dZ05uK_HqoQ2id7fz8M8')
        # Geocoding an address
        geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
        # Look up an address with reverse geocoding
        reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
        # Request directions via public transit
        now = datetime.now()
        directions_result = gmaps.directions("Sydney Town Hall",
                                        "Parramatta, NSW",
                                        mode="driving",
                                        departure_time=now)
        # print(now)
        # print(directions_result)
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
        return render(request, 'google_maps_api/enter_trip.html', context)
    if request.method == 'POST':
        print request.POST
        User.objects.create_trip(request.POST)
        # starting_address = request.POST['starting_address']
        # print starting_address
        # ending_address = request.POST['ending_address']
        # print ending_address
        context = {
            'trip': trip,
        }
    return render(request, 'google_maps_api/enter_trip.html', context)
