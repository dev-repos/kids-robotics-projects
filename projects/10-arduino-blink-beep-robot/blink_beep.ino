// Arduino Blink and Beep Robot
const int LEFT_EYE = 12, RIGHT_EYE = 13, BUZZER = 8;

void setup() {
  pinMode(LEFT_EYE, OUTPUT);
  pinMode(RIGHT_EYE, OUTPUT);
  pinMode(BUZZER, OUTPUT);
}

void loop() {
  digitalWrite(LEFT_EYE, HIGH);
  digitalWrite(RIGHT_EYE, LOW);
  tone(BUZZER, 523, 150);   // C
  delay(400);
  digitalWrite(LEFT_EYE, LOW);
  digitalWrite(RIGHT_EYE, HIGH);
  tone(BUZZER, 659, 150);   // E
  delay(400);
}
