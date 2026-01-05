import os
import requests

# Example Mapbox Static API image fetcher
# This script demonstrates how satellite images were downloaded
# using latitude and longitude coordinates.

MAPBOX_TOKEN = "YOUR_MAPBOX_TOKEN"

def fetch_satellite_image(lat, lon, save_path):
    url = (
        f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
        f"{lon},{lat},18/256x256"
        f"?access_token={MAPBOX_TOKEN}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
