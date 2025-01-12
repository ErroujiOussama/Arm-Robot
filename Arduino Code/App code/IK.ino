#include <Servo.h>

int ServoPins[] = {3, 5, 6, 9, 10, 11};
Servo Servos[6];
String inputString = "";
int servoAngles[6];

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 6; i++) {
    Servos[i].attach(ServoPins[i]);
    servoAngles[i] = 90; // Default position
    Servos[i].write(servoAngles[i]);
  }
}

void loop() {
  if (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      parseData();
    } else {
      inputString += inChar;
    }
  }
}

void parseData() {
  int index = 0;
  char *token = strtok((char *)inputString.c_str(), ",");
  while (token != NULL && index < 6) {
    servoAngles[index] = constrain(atoi(token), 0, 180);
    Servos[index].write(servoAngles[index]);
    token = strtok(NULL, ",");
    index++;
  }
  inputString = "";
}





