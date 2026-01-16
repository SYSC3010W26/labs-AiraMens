from sense_hat import SenseHat
import sqlite3
import time
from datetime import datetime

sense = SenseHat()
sense.clear()

database_db = sqlite3.connect("sensorDB")
cursor = database_db.cursor()

try:
    while True:
        pressure = sense.get_pressure()
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("""
            INSERT INTO sensordata (datetime, temperature, humidity, pressure) VALUES (?, ?, ?, ?)
        """, (date_time, temperature, humidity, pressure))
        
        database_db.commit()
        
        
        print(f"{date_time} | Temp: {temperature} | Humidity: {humidity} | Pressure: {pressure}")
        
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nData logging stopped.")
    
    
finally:
    database_db.close()