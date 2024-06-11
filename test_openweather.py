from openweather import get_weather_dict, get_description, get_main_data, get_wind, API_KEY
import pytest

def test_get_weather_dict():
    assert isinstance(get_weather_dict('Kyiv', API_KEY), dict), "Expected a dictionary"

