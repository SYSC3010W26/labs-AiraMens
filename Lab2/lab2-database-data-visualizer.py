import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


connect_db = sqlite3.connect("sensorDB")

query = """
SELECT datetime, temperature, humidity, pressure FROM sensordata ORDER BY datetime
"""

df = pd.read_sql_query(query, connect_db)

connect_db.close()

df['datetime'] = pd.to_datetime(df['datetime'])

fig, ax1 = plt.subplots()

ax1.scatter(df['datetime'], df['temperature'], color='tab:blue', label='Temperature [deg C]')
ax1.scatter(df['datetime'], df['humidity'], color='tab:green', label='Humidity [%]')
ax1.set_xlabel("Time [%H:%M:%S]")
ax1.set_ylabel("Temperature [deg C], Humidity [%]")

ax2 = ax1.twinx()
ax2.scatter(df['datetime'], df['pressure'], color='tab:red', label='Pressure [millibars]')
ax2.set_ylabel("Pressure [millibars]")

plt.title("Sensor data over time")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

