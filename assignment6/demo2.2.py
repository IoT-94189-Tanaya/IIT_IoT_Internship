#retrive
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="iot_data"
)

cursor = connection.cursor()

query = "SELECT * FROM sensor_data"
cursor.execute(query)

records = cursor.fetchall()

for row in records:
    print(row)

cursor.close()
connection.close()
