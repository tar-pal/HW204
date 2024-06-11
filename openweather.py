import requests

API_KEY = 'bb162c28be60f5bf4afb31a045255ad2'

city = input('Enter city name:')

def get_weather_dict(city, API_KEY):
    try:
        request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&language=ua"
        data = requests.get(request)
        data_dict = data.json()
    except:
        exception = Exception
        print(exception.mro())
        data_dict = {'Exception':exception.mro()[1]}

    return data_dict

