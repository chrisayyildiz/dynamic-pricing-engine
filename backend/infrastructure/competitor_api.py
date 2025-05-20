import requests
import os

url = "https://google-flights2.p.rapidapi.com/api/v1/searchFlights"

querystring = {"departure_id":"LHR","arrival_id":"ABZ","outbound_date":"2025-05-20","return_date":"2025-05-27","travel_class":"ECONOMY","adults":"1","show_hidden":"0","currency":"GBP","language_code":"en-US","country_code":"GB"}

headers = {
	"x-rapidapi-key": os.getenv("x-rapidapi-key"),
	"x-rapidapi-host": "google-flights2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

