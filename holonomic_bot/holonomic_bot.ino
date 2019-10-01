/*
 Example sketch for the PS4 USB library - developed by Kristian Lauszus
 For more information visit my blog: http://blog.tkjelectronics.dk/ or
 send me an e-mail:  kristianl@tkjelectronics.com
 */

#include<MatrixMath.h>


#include <PS4USB.h>

// Satisfy the IDE, which needs to see the include statment in the ino too.
#ifdef dobogusinclude
#include <spi4teensy3.h>
#endif
#include <SPI.h>


int x;
int y;
int w;


#define dir_1 25
#define pwm_1 3
#define dir_2 27
#define pwm_2 4
#define dir_3 29
#define pwm_3 5


mtx_type A_inverse[3][3];  //inverse matrix
mtx_type B_position[3];  //POSITION VECTOR
mtx_type C_speed[3];  //speed matrix

class Motor{
  int enablePin;
  int directionPin;

  public:
  Motor(int ENPin, int dPin){
    enablePin=ENPin;
    directionPin=dPin;
  };

  void Drive(int speed){
    
    if(speed>=0){
      digitalWrite(directionPin,HIGH);
    }

    else{
      digitalWrite(directionPin,LOW);
      speed=-speed;
    }

    analogWrite(enablePin, speed);
  }
};


Motor motor1= Motor(pwm_1,dir_1);

Motor motor2= Motor(pwm_2,dir_2);

Motor motor3= Motor(pwm_3,dir_3);


USB Usb;
PS4USB PS4(&Usb);

bool printAngle, printTouch;
uint8_t oldL2Value, oldR2Value;

void setup() {
  Serial.begin(115200);
#if !defined(__MIPSEL__)
  while (!Serial); // Wait for serial port to connect - used on Leonardo, Teensy and other boards with built-in USB CDC serial connection
#endif
  if (Usb.Init() == -1) {
    //Serial.print(F("\r\nOSC did not start"));
    while (1); // Halt
  }
  //Serial.print(F("\r\nPS4 USB Library Started"));

 
  A_inverse[0][0]=-0.33;
  A_inverse[0][1]=0.58;
  A_inverse[0][2]=0.33;
  A_inverse[1][0]=-0.33;
  A_inverse[1][1]=-0.58;
  A_inverse[1][2]=0.33;
  A_inverse[2][0]=0.67;
  A_inverse[2][1]=0;
  A_inverse[2][2]=0.33;


}

void loop() {
  Usb.Task();
  int s1,s2,s3;
  if (PS4.connected()) {
    if (PS4.getAnalogHat(LeftHatX) > 137 || PS4.getAnalogHat(LeftHatX) < 117 || PS4.getAnalogHat(LeftHatY) > 137 || PS4.getAnalogHat(LeftHatY) < 117 || PS4.getAnalogHat(RightHatX) > 137 || PS4.getAnalogHat(RightHatX) < 117 || PS4.getAnalogHat(RightHatY) > 137 || PS4.getAnalogHat(RightHatY) < 117) {
    x=PS4.getAnalogHat(LeftHatX);
    y=PS4.getAnalogHat(LeftHatY);
    w=PS4.getAnalogHat(RightHatX);

    x=map(x,0,255,-127,127);
    y=map(y,0,255,-127,127);
    w=map(w,0,255,-127,127);

  s1=((A_inverse[0][0]*x)+(A_inverse[0][1]*y)+(A_inverse[0][2]*w));
  
  s2=((A_inverse[1][0]*x)+(A_inverse[1][1]*y)+(A_inverse[1][2]*w));
  
  s3=((A_inverse[2][0]*x)+(A_inverse[2][1]*y)+(A_inverse[2][2]*w));    
////  POSITION VECTOR IS OBTAINED FROM PS4
//  B_position[0]=x;
//  B_position[1]=y;
//  B_position[2]=w;
//
//
//  Matrix.Multiply((mtx_type*)A,(mtx_type*)B,3,3,3,(mtx_type*)C);

  motor1.Drive(s1);
  motor2.Drive(s2);
  motor3.Drive(s3);
    } 
  }
}
