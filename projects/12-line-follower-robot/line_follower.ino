// Line-Follower Robot: 2 IR sensors + L298N/L9110 driver
const int LEFT_SENSOR = 2, RIGHT_SENSOR = 3;   // LOW/HIGH depends on sensor: test first!
const int L_FWD = 5, L_BACK = 6, R_FWD = 9, R_BACK = 10;
const int SPEED = 150;                          // 0..255

void drive(int left, int right) {
  analogWrite(L_FWD, left);  analogWrite(L_BACK, 0);
  analogWrite(R_FWD, right); analogWrite(R_BACK, 0);
}

void setup() {
  pinMode(LEFT_SENSOR, INPUT);
  pinMode(RIGHT_SENSOR, INPUT);
  pinMode(L_FWD, OUTPUT); pinMode(L_BACK, OUTPUT);
  pinMode(R_FWD, OUTPUT); pinMode(R_BACK, OUTPUT);
}

void loop() {
  bool leftOnLine  = digitalRead(LEFT_SENSOR)  == HIGH;  // most TCRT5000 boards: HIGH = black
  bool rightOnLine = digitalRead(RIGHT_SENSOR) == HIGH;
  if (leftOnLine && !rightOnLine)      drive(0, SPEED);      // turn left
  else if (rightOnLine && !leftOnLine) drive(SPEED, 0);      // turn right
  else if (!leftOnLine && !rightOnLine) drive(SPEED, SPEED); // line in middle: go
  else drive(0, 0);                                          // both black: stop (finish line)
}
