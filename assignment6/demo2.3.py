#update
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="iot_data"
)

cursor = connection.cursor()

sensor_id = int(input("Enter Sensor ID to update: "))
new_moisture = float(input("Enter new Moisture Level: "))

query = """
UPDATE sensor_data
SET moisture_level = %s
WHERE sensor_id = %s
"""

cursor.execute(query, (new_moisture, sensor_id))
connection.commit()

print("Record updated successfully")

cursor.close()
connection.close()
