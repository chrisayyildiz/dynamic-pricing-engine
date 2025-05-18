# backend/scraper/batch_scraper.py
import sys
print("sys.path:", sys.path)

import csv
from .amadeus_scraper import get_prices

routes = [
    {"origin": "LHR", "destination": "JFK", "departure_date": "2025-05-19", "return_date": "2025-05-26"},
    # Add more routes as needed
]

all_results = []
for route in routes:
    results = get_prices(**route)
    all_results.extend(results)

csv_file = "data/competitor_prices.csv"
fieldnames = ["timestamp", "competitor", "origin", "destination", "departure_date", "return_date", "price", "currency"]
with open(csv_file, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # Write header only if file is empty
    f.seek(0, 2)
    if f.tell() == 0:
        writer.writeheader()
    writer.writerows(all_results)
