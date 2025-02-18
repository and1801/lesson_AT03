import requests
#
# def get_weather(api_key, city):
#     url = f'[<http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}>](<http://api.openweathermap.org/data/2.5/weather?q=%7Bcity%7D&appid=%7Bapi_key%7D>)'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

def get_catapi_url(URL):
    url = f'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
