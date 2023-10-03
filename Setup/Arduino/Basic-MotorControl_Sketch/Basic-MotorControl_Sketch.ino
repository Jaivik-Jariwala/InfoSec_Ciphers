#include <Adafruit_MotorShield.h>
#include <AFMotor.h>
/*
this will state the motor is sync-properly to all movements
install&Include Adafruit Motor Shield V2 Library
*/

// instance for motor var (pin)
AF_DCMotor m3(3);
AF_DCMotor m4(4);


void setup() {
  // put your setup code here, to run once:

//speed of motor here var(speed in rpm)
m3.setSpeed(300);
m4.setSpeed(300);
m3.run(RELEASE);
m4.run(RELEASE);
}

void loop() {
  // put your main code here, to run repeatedly:

front();
halt();
Right();
halt();
back();
halt();
Left();
}

//front(), back(), Right(), Left()
void front(){
  m3.run(FORWARD);
  m4.run(FORWARD);
  delay(100);
  m3.run(RELEASE);
  m4.run(RELEASE);
  delay(1);
}
void Back(){
  m3.run(BACKWARD);
  m4.run(BACKWARD);
  delay(100);
  m3.run(RELEASE);
  m4.run(RELEASE);
  delay(1);
}
void right(){
  m3.run(FORWARD);
  m4.run(BACKWARD);
  delay(100);
  m3.run(RELEASE);
  m4.run(RELEASE);
  delay(1);
}
void left(){
  m3.run(BACKWARD);
  m4.run(FORWARD);
  delay(100);
  m3.run(RELEASE);
  m4.run(RELEASE);
  delay(1);
}
void halt()
{
  m3.run(RELEASE)
  m4.run(RELEASE)
  delay(10)
}