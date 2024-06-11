from openweather import get_weather_dict, get_description, get_main_data, get_wind, API_KEY
import pytest

def my_mock():
    with open('mock.txt', 'r') as file:
        data = file.read()
    data_dict = eval(data)
    return data_dict
@pytest.mark.parametrize(
    'city, api_key',
    [
        ('Kyiv', API_KEY)
    ]
)
def test_get_weather_dict(city, api_key):
    assert isinstance(get_weather_dict(city, api_key), dict), "Expected a dictionary"

def test_get_description():
    expected = {'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}
    data_dict = my_mock()
    assert get_description(data_dict) == expected
def test_get_main_data():
    expected = {'temp': 29.55, 'feels_like': 31.15, 'temp_min': 26.45, 'temp_max': 30.96, 'pressure': 993, 'humidity': 55}
    data_dict = my_mock()
    assert get_main_data(data_dict) == expected

def test_get_wind():
    expected = {'speed': 0.89, 'deg': 207, 'gust': 2.24}
    data_dict = my_mock()
    assert get_wind(data_dict) == expected

