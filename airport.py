import requests
import json

def airportInfo(code):

    url = "https://aviation-reference-data.p.rapidapi.com/airports/"+code

    headers = {
	"X-RapidAPI-Key": "329f0f0717msh310027eea320ceep130734jsned84bd0e8cb4",
	"X-RapidAPI-Host": "aviation-reference-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    parsed = response.json()
    print("############################")
    print("Name of Airport: " + parsed['name'])
    print("Airport Code:    " + parsed['iataCode'])
    print("############################")

