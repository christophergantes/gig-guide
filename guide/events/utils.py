import requests


def get_coordinates(address: str, city: str, state: str):
    url = f"https://geocoding.geo.census.gov/geocoder/locations/address?street={address}&city={city}&state={state}&benchmark=4&format=json"
    response = requests.get(url)
    data = response.json()

    return data["coordinates"]["x"], data["coordinates"]["y"]
