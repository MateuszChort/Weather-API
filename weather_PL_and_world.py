from requests import get
from json import loads
from terminaltables import AsciiTable
import requests
from datetime import datetime

city = input("Podaj nazwę miasta/miast w Polsce (po przecinku): ")


def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = (get(url))
    rows = [
        ['City', 'date', 'Hour', 'Temperature']
    ]
    for row in loads(response.text):
        if row['stacja'] in city:
            rows.append([
                row['stacja'],
                row['data_pomiaru'],
                row['godzina_pomiaru'],
                row['temperatura']
            ])
    table = AsciiTable(rows)
    print(table.table)


if __name__ == '__main__':
    print('Pogodynka')
    main()

user_api = '4b3c45f1128c27d62c6d04f784696f2c'
location = input("Enter the city name (all over the world): ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']

date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.1f} deg C".format(temp_city))
print("Current weather description  :", weather_desc)
