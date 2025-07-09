import random
#import requests
from datetime import datetime

DELHI_BOUNDS = {
    "min_lat": 28.4,
    "max_lat": 28.9,
    "min_lng": 76.9,
    "max_lng": 77.4
}

crime_types = ['theft', 'assault', 'burglary', 'murder']
severities = ['low', 'medium', 'high']

API_ENDPOINT = "https://your-api-gateway-url/crime"

def random_coordinates():
    lat = random.uniform(DELHI_BOUNDS["min_lat"], DELHI_BOUNDS["max_lat"])
    lng = random.uniform(DELHI_BOUNDS["min_lng"], DELHI_BOUNDS["max_lng"])
    return lat, lng

def simulate_crime():
    lat, lng = random_coordinates()
    payload = {
        "latitude": lat,
        "longitude": lng,
        "type": random.choice(crime_types),
        "severity": random.choice(severities),
        "timestamp": datetime.utcnow().isoformat()
    }
    return payload

# Send 500 simulated reports
for _ in range(500):
    event = simulate_crime()
    print(event)
    # try:
    #     response = requests.post(API_ENDPOINT, json=event)
    #     print(f"Sent: {event} | Response: {response.status_code}")
    # except Exception as e:
    #     print(f"Error sending event: {e}")
