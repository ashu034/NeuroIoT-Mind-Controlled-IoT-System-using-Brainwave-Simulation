// === NeuroIoT ESP32 Receiver ===
// Receives brainwave states from Python via Serial
// Controls LED and Relay accordingly

#define LED_PIN 2      // Onboard LED
#define RELAY_PIN 5    // Relay signal pin
#define BUZZER_PIN 4   // Optional buzzer

String command = "";

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  digitalWrite(RELAY_PIN, LOW);
  digitalWrite(BUZZER_PIN, LOW);
  Serial.println("✅ ESP32 ready to receive NeuroIoT signals...");
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      command.trim();
      Serial.print("Command received: ");
      Serial.println(command);

      if (command == "FOCUS") {
        digitalWrite(LED_PIN, HIGH);
        digitalWrite(RELAY_PIN, HIGH);
        digitalWrite(BUZZER_PIN, LOW);
        Serial.println("💡 Focus Mode ON: Devices Activated");
      }
      else if (command == "RELAX") {
        digitalWrite(LED_PIN, LOW);
        digitalWrite(RELAY_PIN, LOW);
        digitalWrite(BUZZER_PIN, HIGH);
        Serial.println("💤 Relax Mode: Devices OFF, Buzzer ON");
        delay(300);
        digitalWrite(BUZZER_PIN, LOW);
      }
      else if (command == "NEUTRAL") {
        digitalWrite(LED_PIN, LOW);
        digitalWrite(RELAY_PIN, LOW);
        digitalWrite(BUZZER_PIN, LOW);
        Serial.println("😐 Neutral Mode: All Devices OFF");
      }

      command = "";  // reset
    } 
    else {
      command += c;
    }
  }
}
