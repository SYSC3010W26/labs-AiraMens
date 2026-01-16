'''
Script to access weather data from openweathermap.org using a REST API
Data are returned as a JSON string
The JSON string is then deserialized/parsed into a Python dictionary
Sample data fields are printed.

See http://openweathermap.org/current#current for the API

Originally written by Cheryl Schramm ~2015
Updated by James Green Jan-2023
'''

from urllib.request import urlopen 
from urllib.parse import urlencode
import json
import sqlite3
from datetime import datetime

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# Prof Schramm created this API key several years ago. If it doesn’t work, get your own.
apiKey = "a808bbf30202728efca23e099a4eecc7"   
# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"metric", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print(f"Requesting data from URL: {url}")
webData = urlopen(url)
results = webData.read().decode('utf-8')  # results is a JSON string
webData.close()


print("The raw JSON string returned by the query is")
print(results)

# Deserialize/parse the JSON string into a Python Dictionary data structure
# See https://www.geeksforgeeks.org/json-loads-in-python/ for loads details
data = json.loads(results)


wind_speed = data["wind"]["speed"]
date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


print("\nWind Speed:", wind_speed, "m/s")

dbconnect = sqlite3.connect("sensorDB")
cursor = dbconnect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Winds ( City TEXT NOT NULL, Date TEXT NOT NULL, WindSpeed REAL NOT NULL)

""")

cursor.execute("""
    SELECT WindSpeed FROM Winds WHERE City = ? ORDER BY Date DESC LIMIT 1
""", (city,))

result = cursor.fetchone()

if result is None:
    print("\nNo previous wind data for this city.")
else:
    previous_wspeed = result[0]
    if wind_speed > previous_wspeed:
        print("\nWind speed is higher than the previous recorded speed.")
    elif wind_speed < previous_wspeed:
        print("\nWind speed is lower than the previous recorded speed.")
    else:
        print("\nWind speed is the same as the previous recorded speed.")

cursor.execute("""
    INSERT INTO Winds (City, Date, WindSpeed) VALUES (?, ?, ?)

""", (city, date_now, wind_speed))

dbconnect.commit()
dbconnect.close()


# Use the Dictionary to print specific fields from the data
print ("Temperature: %d%sC" % (data["main"]["temp"], chr(176) ))
print ("Humidity: %d%%" % data["main"]["humidity"])
print ("Pressure: %d" % data["main"]["pressure"] )
print ("Wind : %d" % data["wind"]["speed"])
