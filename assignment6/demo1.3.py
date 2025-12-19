#select or retrive data
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="iot_data"
    )

    cursor = connection.cursor()

    id = int(input("Enter ID to retrieve data: "))

    query = "SELECT * FROM sensor_reading WHERE id = %s"
    cursor.execute(query, (id,))

    record = cursor.fetchone()

    if record:
        print("ID:", record[0])
        print("Temperature:", record[1])
        print("Humidity:", record[2])
        print("Timestamp:", record[3])
    else:
        print("No record found for given ID")

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()