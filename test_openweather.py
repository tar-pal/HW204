from openweather import get_weather_dict, get_description, get_main_data, get_wind, API_KEY
import pytest

@pytest.mark.parametrize(
    'city, api_key',
    [
        ('Kyiv', API_KEY)
    ]
)
def test_get_weather_dict(city, api_key):
    assert isinstance(get_weather_dict(city, api_key), dict), "Expected a dictionary"

