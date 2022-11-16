import requests
import json

def airlineInfo(code):
    url = "https://aviation-reference-data.p.rapidapi.com/airline/"+code

    headers = {
	    "X-RapidAPI-Key": "329f0f0717msh310027eea320ceep130734jsned84bd0e8cb4",
	    "X-RapidAPI-Host": "aviation-reference-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    parsed = response.json()
    print("############################")
    print("Name of Airline: " + parsed['name'])
    print("Country Code:    " + parsed['alpha3countryCode'])
    print("############################")
    print("The Collegue was here")
    print("############################")
    print("This is the last edit")
