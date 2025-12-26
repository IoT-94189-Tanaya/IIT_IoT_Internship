#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

const char* ssid = "Tanaya's S24";
const char* password = "Tanaya@2911";

const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;

#define DHTPIN 4
#define DHTTYPE DHT11   

DHT dht(DHTPIN, DHTTYPE);

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected");
}


void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  char tempStr[8];
  char humStr[8];

  dtostrf(temperature, 1, 2, tempStr);
  dtostrf(humidity, 1, 2, humStr);

  client.publish("esp32/temperature", tempStr);
  client.publish("esp32/humidity", humStr);

  Serial.print("Temperature: ");
  Serial.println(tempStr);
  Serial.print("Humidity: ");
  Serial.println(humStr);

  delay(5000); 
}