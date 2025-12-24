#define MQ2_PIN 34 

void setup() {
  Serial.begin(9600);
  Serial.println("MQ-2 Gas & Smoke Sensor Ready");
  delay(20000);    
}

void loop() {
  int gasValue = analogRead(MQ2_PIN);

  Serial.print("Gas or Smoke Value:");
  Serial.println(gasValue);

  if (gasValue > 5000) {
    Serial.println("GAS or SMOKE DETECTED");
  } else {
    Serial.println("Air is clean");
  }

  Serial.println("---");
  delay(2000);
}

