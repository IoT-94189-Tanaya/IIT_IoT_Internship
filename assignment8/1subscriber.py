import paho.mqtt.client as mqtt

broker = "localhost"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("sensor/#")

def on_message(client, userdata, msg):
    print("Topic:", msg.topic, "| Message:", msg.payload.decode())

# 👇 FIX IS HERE
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
print("Waiting for messages...")
client.loop_forever()