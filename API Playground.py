import requests
import json

positionstack_apikey = "eb3a8269f916521b7c4875580c2bae19"

location_readable = "705 Hood Blvd, Fairless Hills, PA 19030"

geocode_data = requests.get("https://api.positionstack.com/v1/forward?access_key=" + positionstack_apikey + "&query=" + location_readable).json()

print(geocode_data)

def lat(geocode_data):
    latitude = geocode_data["data"][0]["latitude"]
    return latitude

def lon(geocode_data):
    longitude = geocode_data["data"][0]["longitude"]
    return longitude

print(lat(geocode_data))
print(lon(geocode_data))