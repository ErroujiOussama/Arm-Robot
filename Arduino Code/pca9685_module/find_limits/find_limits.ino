#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pca = Adafruit_PWMServoDriver(0x40);       // called this way, it uses the default address 0x40   


int ServoPins[]={0,1,2,4,6,8};

short SERVOMIN[]={125,125,125};
short SERVOMAX[]={620,400,620};

enum Servo_Type{
  sg90 = 1,
  mg90s = 2,
  mg996r = 3
};

void setup() {
  Serial.begin(9600);
  Serial.println("Start!");
  pca.begin();
  pca.setPWMFreq(60);                  // Analog servos run at ~60 Hz updates
}


void loop() 
  {  
  //  for(int i : ServoPins){
  //  Set_To_Zero(0);
  //  }
 ;
  
  
  Set_To_Meduim(0);
  delay(2000);

  
  Set_To_Meduim(1);
  Set_To_Meduim(2);
  delay(2000);
  Set_To_Max(1);
  Set_To_Max(2);
  delay(2000);
  Set_To_Zero(1);
  Set_To_Zero(2);
  delay(2000);

  }

//coversion
int angleToPulse(int ang,int Servo_num)                             //gets angle in degree and returns the pulse width
  {  int pulse = map(ang,0, 180, SERVOMIN[Servo_num],SERVOMAX[Servo_num]);  // map angle of 0 to 180 to Servo min and Servo max 
     Serial.print("Angle: ");Serial.print(ang);
     Serial.print(" pulse: ");Serial.println(pulse);
     return pulse;
  }

//SET
void Set_To_Zero(int Servo_num){
 int angle = 0;
 pca.setPWM(Servo_num, 0, angleToPulse(angle,Servo_num));
}

void Set_To_Max(int Servo_num){
  int angle = 179;
  pca.setPWM(Servo_num, 0, angleToPulse(angle,Servo_num));
}

void Set_To_Meduim(int Servo_num){
  int angle = 90;
  pca.setPWM(Servo_num, 0, angleToPulse(angle,Servo_num));
}
