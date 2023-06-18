import googlemaps
API_KEY='AIzaSyAr-ClypgVViP6m5dpyM_1aDQYey0Dy9po'

gmaps = googlemaps.Client(key=API_KEY)

def locate():
    location = gmaps.geolocate()
    # latitude = location['location']['lat']
    # longitude = location['location']['lng']
    latitude = 37.8635105
    longitude = -122.2767202
    return latitude, longitude

def get_nearby_places(keyword):

    latitude, longitude = locate()
    places_result = gmaps.places_nearby(
        location=(latitude, longitude),
        radius=5000,  
        keyword=keyword,
    )
    return places_result['results'][0]['name'], places_result['results'][0]['vicinity']


def get_directions(keyword):
    latitude, longitude = locate()
    places_result = gmaps.places_nearby(
        location=(latitude, longitude),
        radius=5000,  
        keyword=keyword,
    )
    place_id = places_result['results'][0]['place_id']
    print(latitude, longitude, place_id)

    directions_result = gmaps.directions(
        origin=(latitude, longitude),
        destination=place_id,
        mode='walking'
    )
    return directions_result[0]['legs'][0]['steps'][0]['html_instructions']

print(get_directions('starbucks'))