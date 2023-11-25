#include <WiFi.h>
#include <PubSubClient.h>
#include <ESP32Servo.h>

const char* ssid = "MeFoun 11";
const char* password = "005memenet";
const char* mqtt_server = "172.20.10.5";
const char* mqtt_topic = "servo_control";

WiFiClient espClient;
PubSubClient client(espClient);
Servo myServo;

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  String message = "";

  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
    message += (char)payload[i];
  }
  Serial.println();

  // Check the received message 
  if (message == "true") {
    // Rotate the servo to angle
    myServo.write(90);  // 90 degrees
    Serial.println("Servo turned to 90 degrees");
  } else if (message == "false") {
    // Rotate the servo to another angle (adjust as needed)
    myServo.write(0);  // 0 degrees 
    Serial.println("Servo turned to 0 degrees");
  } else {
    Serial.println("Invalid message");
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      client.subscribe(mqtt_topic);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  myServo.attach(13);  // Attach the servo to pin 13, 
  myServo.write(0);    // Initially set the servo to 0
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Additional loop logic goes here
}

