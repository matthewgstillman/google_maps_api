from django.shortcuts import render, redirect
import googlemaps
import requests
from .forms import TripForm
from .models import Trip
from datetime import datetime
from api_key import api_key

# Create your views here.

def index(request):
    session_formatted_starting_address = request.session['formatted_starting_address']
    session_formatted_ending_address = request.session['formatted_ending_address']
    print("Formatted Ending Address: " + str(session_formatted_ending_address))
    session_geocode_ending_address = request.session['geocode_ending_address']
    print("Session Geocode Ending Address: " + str(session_geocode_ending_address))
    latitude = session_geocode_ending_address[0]['geometry']['location']['lat']
    longitude = session_geocode_ending_address[0]['geometry']['location']['lng']
    lat_lon = str(latitude) + "," + str(longitude)
    key2 = api_key['api_key2']
    print("Key 2: " + str(key2))
    starting_address = request.session['starting_address']
    print("Starting Address: " + str(starting_address))
    ending_address = request.session['ending_address']
    print("Ending Address: " + str(ending_address))
    key = api_key['api_key']
    gmaps = googlemaps.Client(key=key)
    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(starting_address,
                                     ending_address,
                                     mode="driving",
                                     departure_time=now)
    context = {
        'starting_address': starting_address,
        'ending_address': ending_address,
        'directions_result': directions_result,
        'geocode_result': geocode_result,
        'key2': key2,
        'lat_lon': lat_lon,
        'gmaps': gmaps,
        'now': now,
        'reverse_geocode_result': reverse_geocode_result,
        'session_formatted_starting_address': session_formatted_starting_address,
        'session_formatted_ending_address': session_formatted_ending_address,
        'session_geocode_ending_address': session_geocode_ending_address,
    }
    return render(request, 'google_maps_api/index.html', context)

def enter_trip(request):
    if request.method == 'GET':
        key = api_key['api_key']
        gmaps = googlemaps.Client(key=key)
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
        context = {
            'directions_result': directions_result,
            'geocode_result': geocode_result,
            'gmaps': gmaps,
            'key': key,
            'now': now,
            'reverse_geocode_result': reverse_geocode_result,
        }
        return render(request, 'google_maps_api/enter_trip.html', context)
    if request.method == 'POST':
        key = api_key['api_key']
        print request.POST
        starting_address = request.POST['starting_address']
        request.session['starting_address'] = starting_address
        session_starting_address = request.session['starting_address']
        formatted_starting_address = ""
        for i in session_starting_address:
            if i == " " or i == "  ":
                formatted_starting_address += '%20'
            else:
                formatted_starting_address += i
        print("Formatted Starting Address: " + str(formatted_starting_address))
        request.session['formatted_starting_address'] = formatted_starting_address
        session_formatted_starting_address = request.session['formatted_starting_address']
        ending_address = request.POST['ending_address']
        request.session['ending_address'] = ending_address
        session_ending_address = request.session['ending_address']
        print("Session Ending Address:\n " + str(session_ending_address) + "\n")
        formatted_ending_address = ""
        for i in session_ending_address:
            if i == " " or i == "  ":
                formatted_ending_address += '%20'
            else:
                formatted_ending_address += i
        print("Formatted Ending Address: \n" + str(formatted_ending_address) + str("\n"))
        request.session['formatted_ending_address'] = formatted_ending_address
        session_formatted_ending_address = request.session['formatted_ending_address']
        print("Session Formatted Ending Address: " + str(session_formatted_ending_address))
        trip = Trip.objects.create_trip(request.POST)
        gmaps = googlemaps.Client(key=key)
        # Geocoding an address
        geocode_starting_address = gmaps.geocode(starting_address)
        print("Starting Address Geocode: " + str(geocode_starting_address))
        geocode_ending_address = gmaps.geocode(ending_address)
        print("Ending Address Geocode: " + str(geocode_ending_address))
        request.session['geocode_ending_address'] = geocode_ending_address
        session_geocode_ending_address = request.session['geocode_ending_address']
        print("Session Geocode Ending Address: " + str(session_geocode_ending_address))
        # Look up an address with reverse geocoding
        reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
        now = datetime.now()
        directions_result = gmaps.directions(starting_address,
        ending_address,
        mode="driving",
        departure_time=now)
        context = {
            'directions_result': directions_result,
            'formatted_ending_address': formatted_ending_address,
            'ending_address': ending_address,
            'session_formatted_starting_address': session_formatted_starting_address,
            'session_formatted_ending_address': session_formatted_ending_address,
            'session_geocode_ending_address': session_geocode_ending_address,
            'geocode_starting_address': geocode_starting_address,
            'geocode_ending_address': geocode_ending_address,
            'reverse_geocode_result': reverse_geocode_result,
            'gmaps': gmaps,
            'now': now,
            'starting_address': starting_address,
            'trip': trip,
        }
        return redirect("/", context)

def new_trip(request):
    if request.method == 'POST':
        starting_address = request.POST['starting_address']
        request.session['starting_address'] = starting_address
        ending_address = request.POST['ending_address']
        request.session['ending_address'] = ending_address
        print starting_address, ending_address
        context = {
            'starting_address': starting_address,
            'ending_address': ending_address,
        }
        return render(request, "google_maps_api/new_trip.html", context)
    else:
        starting_address = request.session['starting_address']
        ending_address = request.session['ending_address']
        print starting_address, ending_address
        context = {
            'starting_address': starting_address,
            'ending_address': ending_address
        }
        return render(request, "google_maps_api/new_trip.ht,ml", context)

