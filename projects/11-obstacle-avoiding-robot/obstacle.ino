// Obstacle-Spotting Robot: HC-SR04 + SG90 servo
#include <Servo.h>
const int TRIG = 9, ECHO = 10;
Servo head;

long distanceCm() {
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long t = pulseIn(ECHO, HIGH, 30000);
  return t / 58;            // microseconds -> cm
}

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  head.attach(6);
  Serial.begin(9600);
}

void loop() {
  long d = distanceCm();
  Serial.println(d);
  if (d > 0 && d < 15) head.write(160);   // too close: look away
  else head.write(90);                    // all clear: look ahead
  delay(150);
}
