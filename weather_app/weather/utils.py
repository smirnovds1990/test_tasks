from datetime import timedelta
from typing import Any

import pandas as pd
import requests
import requests_cache
from django.contrib.auth.models import User


from .constants import (
    COORDINATES_FORMAT, COORDINATES_LIMIT, COORDINATES_URL, WEATHER_DETAILS,
    WEATHER_URL
)
from .models import City


requests_cache.install_cache(
    'city_coordinates_cache', expire_after=timedelta(hours=24)
)


def get_city_coordinates(city: str) -> tuple[float | None, float | None]:
    params = {
        'q': city,
        'format': COORDINATES_FORMAT,
        'limit': COORDINATES_LIMIT
    }
    headers = {
        'User-Agent': 'MyWeatherApp/1.0 (smirnovds1990@gmail.com)'
    }
    response = requests.get(COORDINATES_URL, params=params, headers=headers)
    data = response.json()
    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return float(latitude), float(longitude)
    return None, None


def get_weather_info(
        latitude: float | None, longitude: float | None
) -> dict[str, Any]:
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': WEATHER_DETAILS
    }
    response = requests.get(WEATHER_URL, params=params)
    return response.json()


def convert_data_to_dataframe(data: dict[str, Any]) -> str:
    """
    Convert weather data to Pandas dataframe to be able to
    show user-friendly on the page.
    """
    hourly_data = data['hourly']
    units = data['hourly_units']
    dataframe = pd.DataFrame(hourly_data)
    dataframe.columns = [f'{col} ({units[col]})' for col in dataframe.columns]
    return dataframe.to_html(index=False)


def save_city_to_db(city: str, user: User) -> None:
    new_city = City(city_title=city.title())
    new_city.save()
    new_city.user.add(user)
