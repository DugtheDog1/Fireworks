const int numLeds = 52;

// Pins array (starting from pin 2, avoid pins 0 and 1 because of Serial)
const int ledPins[numLeds] = {
  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
  14, 15, 16, 17, 18, 19,
  20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
  30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
  40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51
};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);  // Start with all LEDs OFF
  }
  Serial.println("Arduino ready for commands.");
}

void loop() {
  if (Serial.available() >= 2) {
    int ledIndex = Serial.read();    // 0-based LED index (0 to 51)
    int state = Serial.read();       // 0=OFF, 1=ON

    if (ledIndex >= 0 && ledIndex < numLeds) {
      digitalWrite(ledPins[ledIndex], state == 1 ? HIGH : LOW);
      Serial.print("LED ");
      Serial.print(ledIndex + 1);
      Serial.println(state == 1 ? " ON" : " OFF");
    } else {
      Serial.print("Invalid LED index: ");
      Serial.println(ledIndex);
    }
  }
}
