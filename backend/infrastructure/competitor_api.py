import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPID_KEY = os.getenv("RAPID_API_KEY")

# Step 1: Hard-coded search inputs
departure_id  = "LHR"
arrival_id    = "CDG"
outbound_date = "2025-06-20"
return_date   = "2025-06-27"
adults        = "1"
travel_class  = "ECONOMY"

# Step 2: Build query parameters
params = {
    "departure_id":  departure_id,
    "arrival_id":    arrival_id,
    "outbound_date": outbound_date,
    "return_date":   return_date,
    "adults":        adults,
    "travel_class":  travel_class,
    "currency":      "USD",
    "language_code": "en-US",
    "country_code":  "US",
    "show_hidden":   "0",
}

# Step 3: Send request
url = "https://google-flights2.p.rapidapi.com/api/v1/searchFlights"
headers = {
    "x-rapidapi-host": "google-flights2.p.rapidapi.com",
    "x-rapidapi-key": RAPID_KEY
}
response = requests.get(url, headers=headers, params=params)
data = response.json()

prices = []
for flight in data.get("data", []):  # Assuming response format is { "data": [...] }
    price_str = flight.get("price", "").replace("$", "").replace(",", "").strip()
    if price_str:
        try:
            price = float(price_str)
            prices.append(price)
        except ValueError:
            continue

# Step 5: Calculate and print summary statistics
if prices:
    avg_price = sum(prices) / len(prices)
    min_price = min(prices)
    max_price = max(prices)

