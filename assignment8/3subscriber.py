import paho.mqtt.client as mqtt

broker = "localhost"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe("health/monitor")

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    pulse, spo2 = map(int, data.split(","))

    print(f"Pulse: {pulse} bpm | SpO2: {spo2}%")

    if pulse < 60 or pulse > 100:
        print("ALERT: Pulse rate abnormal! Notify Doctor")

    if spo2 < 95:
        print("ALERT: Blood Oxygen level low! Notify Doctor")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_forever()