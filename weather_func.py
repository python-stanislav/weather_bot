import requests, bs4


def data_to_string(weather_data):
    
    date = weather_data.select('#bd1 .date')
    month = weather_data.select('#bd1 .month')
    temperature_max = weather_data.select('#bd1 .max span')
    temperature_min = weather_data.select('#bd1 .min span')
    try:
        data = '\nДата: ' + date[0].getText() + ' ' + month[0].getText()
        data += '\nМаксимальная температура: ' + temperature_max[0].getText()
        data += '\nМинимальная температура: ' + temperature_min[0].getText()
    except IndexError:
        return None
    return data

def get_weather(city):
    sinoptik_url = 'https://sinoptik.ua/погода-'
    if city.find(' '):
        sinoptik_url += city.replace(' ', '-').lower()
    res = requests.get(sinoptik_url)
    weather_data = bs4.BeautifulSoup(res.text, 'lxml')
    weather_msg = '\nПрогноз погоды в городе ' + city.title() + '\n'
    if data_to_string(weather_data) == None:
        return None
    else:
        return weather_msg + str(data_to_string(weather_data))


        
