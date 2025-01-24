import requests
from bs4 import BeautifulSoup as bs

url = "https://api.open-meteo.com/v1/forecast?latitude=22&longitude=77&current=temperature_2m,wind_speed_10m"

api_data_response = requests.get(url)

if api_data_response.status_code == 200:
    # print(api_data_response.json())
    print(f"Time:{api_data_response.json()['current']['time']}\nTemperature:{api_data_response.json()['current']['temperature_2m']}\nWindspeed:{api_data_response.json()['current']['wind_speed_10m']}")
