import controlP5.*;
import processing.serial.*;

ControlP5 cp5;
Serial myPort;

// Number of sliders (6 servos: 5 joints + 1 gripper)
int numSliders = 6;
Slider[] sliders = new Slider[numSliders];
int[] servoAngles = new int[numSliders]; // Store slider values

void setup() {
  size(400, 300); // Window size
  
  // Initialize ControlP5 for GUI
  cp5 = new ControlP5(this);
  
  // Create sliders for each servo
  for (int i = 0; i < numSliders; i++) {
    sliders[i] = cp5.addSlider("Servo " + i)
      .setPosition(50, 30 + i * 40)
      .setSize(300, 20)
      .setRange(0, 180) // Servo angle range
      .setValue(90)     // Default position (middle)
      .plugTo(this, "updateServo" + i);
  }

  // Establish Serial Communication
  String portName = Serial.list()[0]; // Adjust the index as needed
  myPort = new Serial(this, portName, 9600);
}

void draw() {
  background(200);
  fill(0);
  text("Servo Control GUI", 140, 20);
}

void sendServoData() {
  // Send servo angles as a comma-separated string
  String data = "";
  for (int i = 0; i < numSliders; i++) {
    data += servoAngles[i];
    if (i < numSliders - 1) data += ",";
  }
  myPort.write(data + "\n"); // Send data over serial with newline
}

// Update methods for sliders
void updateServo0(float val) {
  servoAngles[0] = int(val);
  sendServoData();
}

void updateServo1(float val) {
  servoAngles[1] = int(val);
  sendServoData();
}

void updateServo2(float val) {
  servoAngles[2] = int(val);
  sendServoData();
}

void updateServo3(float val) {
  servoAngles[3] = int(val);
  sendServoData();
}

void updateServo4(float val) {
  servoAngles[4] = int(val);
  sendServoData();
}

void updateServo5(float val) {
  servoAngles[5] = int(val);
  sendServoData();
}
