import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(broker, 1883, 60)

while True:
    pulse = random.randint(50, 120)
    spo2 = random.randint(90, 100)

    data = f"{pulse},{spo2}"
    client.publish("health/monitor", data)

    print("Published Pulse:", pulse, "SpO2:", spo2)
    time.sleep(5)