# backend/scraper/amadeus_scraper.py

from amadeus import Client, ResponseError
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()  # Loads .env file

AMADEUS_CLIENT_ID = os.getenv('AMADEUS_API_KEY')
AMADEUS_CLIENT_SECRET = os.getenv('AMADEUS_API_SECRET')

amadeus = Client(
    client_id=AMADEUS_CLIENT_ID,
    client_secret=AMADEUS_CLIENT_SECRET
)

def get_prices(origin, destination, departure_date, return_date=None, adults=1, currency='GBP'):
    """Searches for flight prices using Amadeus Flight Offers API."""
    try:
        params = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            'departureDate': departure_date,
            'adults': adults,
            'currencyCode': currency,
            'max': 5  # Limit results for demonstration; increase as needed
        }
        if return_date:
            params['returnDate'] = return_date

        response = amadeus.shopping.flight_offers_search.get(**params)
        results = []
        for offer in response.data:
            results.append({
                "timestamp": datetime.utcnow().isoformat(),
                "competitor": "Amadeus",
                "origin": origin,
                "destination": destination,
                "departure_date": departure_date,
                "return_date": return_date,
                "price": offer["price"]["total"],
                "currency": offer["price"]["currency"]
            })
        return results

    except ResponseError as error:
        print(f"Amadeus API error: {error}")
        return []
