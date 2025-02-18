import pytest
from main import get_catapi_url
# from main import get_github_user
# from main import get_weather
#
#
# def test_get_weather(mocker):
#     mo_get = mocker.patch('main.requests.get')
#     mo_get.return_value.status_code = 200
#     mo_get.return_value.json.return_value = {
#         'weather' : [{'description': 'clear sky'}],
#         'main' : {'temp': 273.15}
#     }
#
#     api_key = '05cbad7e5559260998ca03318c73cacd'
#     city = 'London'
#
#     weather_data = get_weather(api_key, city)
#
#     assert weather_data == {
#         'weather' : [{'description': 'clear sky'}],
#         'main' : {'temp': 273.15}
#     }
#
# def test_get_weather_with_error(mocker):
#     mo_get = mocker.patch('main.requests.get')
#     mo_get.return_value.status_code = 404
#
#     api_key = '05cbad7e5559260998ca03318c73cacd'
#     city = 'London'
#
#     weather_data = get_weather(api_key, city)
#
#     assert weather_data == None

def test_get_catapi_url(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'URL' : 'https://api.thecatapi.com/v1/images/search',
    }

    URL = get_catapi_url('https://api.thecatapi.com/v1/images/search')
    assert URL == {
        'URL' : 'https://api.thecatapi.com/v1/images/search',
    }

def test_get_catapi_with_err(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500


    URL = get_catapi_url('https://api.thecatapi.com/v1/images/search')
    assert URL == None