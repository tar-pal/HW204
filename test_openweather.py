from types import SimpleNamespace
import json
from openweather import get_weather_dict, get_description, get_main_data, get_wind, API_KEY
from unittest import mock
import pytest

def my_mock():
    with open('mock.json', 'r') as file:
        data_dict = file.read()
    return data_dict
@pytest.mark.parametrize(
    'city, api_key',
    [
        ('Kyiv', API_KEY)
    ]
)
def test_get_weather_dict(city, api_key):
    mock_response = SimpleNamespace()
    mock_response.json = lambda: json.loads(my_mock())
    expected_value = mock_response.json()
    with mock.patch('requests.get', return_value=mock_response):
        response = get_weather_dict(city, api_key)
    assert response == expected_value

def test_get_description():
    expected = {'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}
    data_dict = json.loads(my_mock())
    assert get_description(data_dict) == expected
def test_get_main_data():
    expected = {'temp': 29.55, 'feels_like': 31.15, 'temp_min': 26.45, 'temp_max': 30.96, 'pressure': 993, 'humidity': 55}
    data_dict = json.loads(my_mock())
    assert get_main_data(data_dict) == expected

def test_get_wind():
    expected = {'speed': 0.89, 'deg': 207, 'gust': 2.24}
    data_dict = json.loads(my_mock())
    assert get_wind(data_dict) == expected

