#delect
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="iot_data"
)

cursor = connection.cursor()

sensor_id = int(input("Enter Sensor ID to delete: "))

query = "DELETE FROM sensor_data WHERE sensor_id = %s"
cursor.execute(query, (sensor_id,))
connection.commit()

print("Record deleted successfully")

cursor.close()
connection.close()
