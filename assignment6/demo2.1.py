#insert data

import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="iot_data"
)

cursor = connection.cursor()

sensor_id = int(input("Enter Sensor ID: "))
moisture = float(input("Enter Moisture Level: "))
date_time = datetime.now()

query = """
INSERT INTO sensor_data (sensor_id, moisture_level, date_time)
VALUES (%s, %s, %s)
"""

cursor.execute(query, (sensor_id, moisture, date_time))
connection.commit()

print("Record inserted successfully")

cursor.close()
connection.close()
