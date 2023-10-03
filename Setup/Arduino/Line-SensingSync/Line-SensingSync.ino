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
// function for setting up pinmode from 14 to 20
for (int i = 14; i<20; i++)
{
  pinMode(i, INPUT);
}

//speed of motor here var(speed in rpm)
m3.setSpeed(300);
m4.setSpeed(300);
m3.run(RELEASE);
m4.run(RELEASE);
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.begin(9600);//initalise serial monitor
for(int i=14; i<20; i++)
{
  Serial.print("Pin");
  Serial.println("i");
  Serial.println(" = ");
  Serial.println(digitalRead(i));
}
//output of above code-block will be Pin 14 = 1/0


//front(), Right(), back(), Left(), halt();
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