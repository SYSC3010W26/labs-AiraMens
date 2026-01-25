# Lab 3 – Pyrebase 
import pyrebase 
import random 
import time 
from sense_hat import SenseHat

# Config will contain the information needed to connect to your firebase 
#   The API KEY and Project ID are found in your project settings 
#   The DB URL can be found under the Realtime Database tab 
config = { 
  "apiKey": "BM8ZK5mdjs2s6WtW21Zz26oANrJD-8hqssQy-iXpuAPGsACd3HhJOGPy3hg5DRoj4ewKG4TCHpWNSyliu6IS_hk", 
  "authDomain": "sysc3010-lab3-40cc8.firebaseapp.com", 
  "databaseURL": "https://sysc3010-lab-3-40cc8-default-rtdb.firebaseio.com/", 
  "storageBucket": "sysc3010-lab3-40cc8.appspot.com" 
} 

# Connect using your configuration 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 
dataset = "sensor1" 
USERNAME = "AyraMensah"   


sense = SenseHat()

timestamp = int(time.time())

print("\nSending 10 sensor readings...")

for key in range(10):

    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    db.child(USERNAME).child("sensorTemperature").child(key).set(temperature)
    db.child(USERNAME).child("sensorHumidity").child(key).set(humidity)
    db.child(USERNAME).child("sensorPressure").child(key).set(pressure)

    print(f"{key}: T={temperature}, H={humidity}, P={pressure}")

    time.sleep(1)


print("\nReading teammates' latest 3 sensor values...\n")

all_users = db.get()

if all_users.each():

    for user in all_users.each():

        uname = user.key()

        print("===================================")
        print("User:", uname)

        for sensor in ["sensorTemperature", "sensorHumidity", "sensorPressure"]:

            print("\n", sensor.upper())

            data = db.child(uname).child(sensor).get()

            if data.val() is None:
                print("  No data.")
                continue

            readings = data.each()

            # Sort by timestamp key
            readings.sort(key=lambda x: int(x.key()))

            # Last 3
            last_three = readings[-3:]

            for r in last_three:
                print(f"  {r.key()} -> {r.val()}")

        print("\n")

else:
    print("No users found in DB.")
