import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="iot_data"
)
cursor = conn.cursor()


id = int(input("Enter ID: "))
temperature = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
timestamp = datetime.strptime(input("Enter timestamp (YYYY-MM-DD HH:MM:SS): "), "%Y-%m-%d %H:%M:%S")

cursor.execute("INSERT INTO sensor_reading (id, temperature, humidity, timestamp) VALUES (%s, %s, %s, %s)",
               (id, temperature, humidity, timestamp))
conn.commit()

print("Data inserted successfully")

cursor.close()
conn.close()
