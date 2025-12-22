import paho.mqtt.client as mqtt
import time

broker = "localhost"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(broker, 1883, 60)

while True:
    appliance = input("Enter appliance (Light/Fan): ")
    status = input("Enter status (ON/OFF): ")

    msg = appliance + "," + status
    client.publish("home/control", msg)

    print("Command sent:", msg)
    time.sleep(1)