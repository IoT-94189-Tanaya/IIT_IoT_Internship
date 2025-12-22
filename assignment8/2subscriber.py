import paho.mqtt.client as mqtt
import sqlite3

broker = "localhost"

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("home/control")

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    appliance, status = data.split(",")

    print(f"{appliance} turned {status}")

    conn = sqlite3.connect("home.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO appliance_status (appliance_name, status) VALUES (?, ?)",
        (appliance, status)
    )

    conn.commit()
    conn.close()

    print("Status updated in database")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_forever()