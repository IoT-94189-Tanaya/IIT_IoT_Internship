import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(broker, 1883, 60)

while True:
    ldr = random.randint(100, 900)
    temp = round(random.uniform(20, 40), 2)

    client.publish("sensor/ldr", ldr)
    client.publish("sensor/lm35", temp)

    print("Published LDR:", ldr)
    print("Published Temp:", temp)

    time.sleep(5)