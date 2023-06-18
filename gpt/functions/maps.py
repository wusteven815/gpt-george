from ._utils import create_arg
from ._utils import create_config
import smtplib
from env import maps_api
import googlemaps

class LocationsGet:

    config = create_config(
        name="locations_get",
        desc="Finds nearby locations of restaurants or stores",
        required=["keyword"],
        keyword=create_arg(
            desc="The restaurant or store that the user would like to find. If the keyword is not valid, reprompt the user."
        ),
     )

    @staticmethod
    def run(keyword):
        gmaps = googlemaps.Client(key=maps_api)
        latitude = 37.8635105
        longitude = -122.2767202
        places_result = gmaps.places_nearby(
        location=(latitude, longitude),
        radius=5000,  
        keyword=keyword,
        )
        if (len(places_result['results']) == 0):
            return f"Sorry, there are no places named {keyword} nearby"
        return f"There's a {places_result['results'][0]['name']} at {places_result['results'][0]['vicinity']}"
