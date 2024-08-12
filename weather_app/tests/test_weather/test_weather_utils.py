import pytest

from weather.models import City
from weather.utils import (
    convert_data_to_dataframe, get_city_coordinates, get_weather_info,
    save_city_to_db
)


def test_get_coordinates_with_correct_city():
    city = 'kineshma'
    response = get_city_coordinates(city)
    for item in response:
        assert isinstance(item, float)


def test_get_weather_info():
    # Test data
    latitude = 57.442959
    longitude = 42.149399

    response = get_weather_info(latitude, longitude)
    assert isinstance(response, dict)


def test_convert_data_to_dataframe():
    # Test data
    data = {
        'hourly_units': {
            'time': 'iso8601',
            'temperature_2m': '°C',
            'relative_humidity_2m': '%',
            'rain': 'mm',
            'wind_speed_10m': 'km/h'
        },
        'hourly': {
            'time': [
                '2024-08-12T00:00', '2024-08-12T01:00', '2024-08-12T02:00'
            ],
            'temperature_2m': [12.9, 12.5, 12.4],
            'relative_humidity_2m': [94, 95, 96],
            'rain': [0.00, 0.00, 0.00],
            'wind_speed_10m': [6.8, 6.5, 6.8]
        }
    }

    result = convert_data_to_dataframe(data)
    assert isinstance(result, str)


@pytest.mark.django_db
def test_save_city_to_db(admin_user):
    all_cities = City.objects.all()
    assert len(all_cities) == 0
    city = 'kineshma'
    save_city_to_db(city, admin_user)
    all_cities = City.objects.all()
    assert len(all_cities) == 1
    assert all_cities[0].city_title == 'Kineshma'
    assert all_cities[0].user.first() == admin_user
