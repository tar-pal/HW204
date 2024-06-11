import requests

API_KEY = 'bb162c28be60f5bf4afb31a045255ad2'



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

def get_description(data_dict):
    return data_dict['weather'][0]['description']

def get_main_data(data_dict):
    return data_dict['main']

def get_wind(data_dict):
    return data_dict['wind']

if __name__ == 'main':
    city = input('Enter city name:')
    data_dict = get_weather_dict(city, API_KEY)
    print(get_description)