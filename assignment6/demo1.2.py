#delete
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

    id = int(input("Enter ID to delete: "))

    query = "DELETE FROM sensor_reading WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Data deleted successfully from sensor_reading")
    else:
        print("No record found with given ID")

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
