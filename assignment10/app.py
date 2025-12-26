from flask import Flask, request
import mysql.connector
import datetime
import paho.mqtt.client as mqtt

app = Flask(__name__)

# DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_data"
)
cursor = db.cursor()

# MQTT SETTINGS
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "iit/moisture/alert"

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# MOISTURE THRESHOLD
THRESHOLD = 300

@app.route('/add_moisture')
def add_moisture():
    sensor_id = request.args.get('sensor_id')
    moisture = int(request.args.get('moisture'))

    now = datetime.datetime.now()
    date = now.date()
    time = now.time()

    sql = """INSERT INTO moisture_data
             (sensor_id, moisture_level, date, time)
             VALUES (%s, %s, %s, %s)"""
    values = (sensor_id, moisture, date, time)
    cursor.execute(sql, values)
    db.commit()

    if moisture < THRESHOLD:
        alert = f"ALERT! Sensor {sensor_id} Moisture LOW ({moisture})"
        mqtt_client.publish(MQTT_TOPIC, alert)
        return alert + " | Stored + MQTT Alert Sent"

    return "Moisture Stored Successfully"

if __name__ == '__main__':
    app.run(debug=True)
