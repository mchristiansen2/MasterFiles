# DSC 510
# Week 12
# Programming Assignment Week 12
# Author: Madison Christiansen
# 11/15/2022
# Description: Weather lookup.

import json
import requests

weatherAPI = 'https://api.openweathermap.org/data/2.5/weather'
geoAPI = 'http://api.openweathermap.org/geo/1.0/direct'

print("Welcome to the Weather Locator!")


def get_latLong(location, standard):
    """Asking for the user input, zip code and city works from one url and question"""
    if location.isdigit() is True:
        params = {'zip': location, 'APPID': 'fdaec6c0c00e945a4bb9ab0b6cc2c91c'}
    else:
        params = {'q': location, 'APPID': 'fdaec6c0c00e945a4bb9ab0b6cc2c91c'}
    location_resp = requests.get(geoAPI, params=params)
    data = json.loads(location_resp.text)
    lon = data[0]['lon']
    lat = data[0]['lat']
    """Getting weather data from lat and long passing unit type"""
    data_fromLatLong(lat, lon, standard)


def data_fromLatLong(lat, lon, unit):
    params = {'lat' : lat, 'lon': lon, 'APPID': 'fdaec6c0c00e945a4bb9ab0b6cc2c91c', 'units': unit}
    location_resp = requests.get(weatherAPI, params=params)
    data = json.loads(location_resp.text)
    show_data(data, unit)


def show_data(data, unit):
    """Organizing the output to look neat, for the user to see"""
    temp = data['main']['temp']
    high_temp = data['main']['temp_max']
    low_temp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    tempUnit = 'F' if unit == 'imperial' else 'C'
    speedUnit = 'MPH' if unit == 'imperial' else 'M/S'

    print('Current Temperature', temp, tempUnit)
    print('High Temperature', high_temp, tempUnit)
    print('Low Temperature', low_temp, tempUnit)
    print('Wind Speed : {} '.format(wind_speed), speedUnit)
    print('Humidity : {} %'.format(humidity))
    print('Description : {}'.format(description))


def another_one():
    """Asks the user if they want to enter another location"""""
    question = input('Do you want to do another search? Type Yes or No: ')
    if question == 'Yes' or question == 'yes':
        main()
    if question == 'No' or question == 'no':
        print("Thank you for using the Weather Locator!")
        exit()


def main():
    """Main function preforms and pulls the info needed to display"""

    location = input('Enter a city or zip code you would like to lookup:').lower()
    standard = input('Imperial or Metric units?').lower()

    '''Prompt user for units until correct answer is provided'''
    while standard != 'imperial' and standard != 'metric':
        print("Please enter 'Imperial' or 'Metric'")
        standard = input('Imperial or Metric units?').lower()
    while True:
        try:
            get_latLong(location, standard)
            another_one()
            break
        except LookupError:
            print("Enter a correct response.")
            another_one()
            break


if __name__ == "__main__":
    main()


#   Change#:1
#   Change(s) Made: added main, and three def functions
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
#   Change#:2
#   Change(s) Made: added urls and inputs
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
#   Change#:3
#   Change(s) Made: added temperature function details to the show data function
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
#   Change#:4
#   Change(s) Made: added only one url for both zip and city lookup, added api to get location. works for both lookups
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
#   Change#:5
#   Change(s) Made: redid API, finally works!!!
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
#   Change#:6
#   Change(s) Made: except error block in main
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
#   Change#:7
#   Change(s) Made: created another one function, and added too main
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
#   Change#:8
#   Change(s) Made: took out hard coded F and C, changed to if else
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
#   Change#:9
#   Change(s) Made: added geo url and changed to lat and lon lookup
#   Date of Change: 11/15/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/19/2022
