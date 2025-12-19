#insert
import mysql.connector
from datetime import datetime

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="iot_data",
    )

    cursor = connection.cursor()

    id = int(input("Enter ID: "))
    temperature = float(input("Enter temperature: "))
    humidity = float(input("Enter humidity: "))
    timestamp_str = input("Enter timestamp (YYYY-MM-DD HH:MM:SS): ")

    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    query = """
        INSERT INTO sensor_reading (id, temperature, humidity, timestamp)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (id, temperature, humidity, timestamp))
    connection.commit()  

    print("Data inserted successfully into sensor_reading")

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()