/* Algorithm : 
*/


#include <Adafruit_MotorShield.h>
#include <AFMotor.h>
/*
this will state the motor is sync-properly to all movements
install&Include Adafruit Motor Shield V2 Library
*/

// instance for motor var (pin)
AF_DCMotor m3(3);
AF_DCMotor m4(4);

//instance for LED
const int greenLEdPin = ;
const int redLEDPin = ;

String path;

void setup() {
// put your setup code here, to run once:
  Serial.begin(9600);
  // Adding LED
  pinMode(greenLEDPin, OUTPUT);
  pinMode(redLEDPin, OUTPUT);
  
  // function for setting up pinmode for Motor from 14 to 20
  for (int i = 14; i<20; i++){
    pinMode(i, INPUT);
  }

  //speed of motor here var(speed in rpm)
  m3.setSpeed(300);
  m4.setSpeed(300);
  m3.run(RELEASE);
  m4.run(RELEASE);
}
void loop(){
  //Sensor Position with PinID
  /*                  16
    14        15                18        19                      
                      17                               */
 
// Scan the path for Various Conditions of the Maze
  // FORWARD CONDITION [0 0 1 1 0 0] - SINGLE CONDITION-------------------------
  if (!digitalRead(15) && digitalRead(17) && !digitalRead(18)){
    
    Serial.println("Move Forward")
    path += 'S'
    front(1);
    GreenLightArea();
  }

  // BACKWARD CONDITION [0 x 1 0 x 0] - SINGLE CONDITION-------------------------
  if (!digitalRead(15) && !digitalRead(17) && !digitalRead(18) )){
    m3.run(FORWARD);
    m4.run(BACKWARD);
    delay(1000);
    if (digitalRead(15) && !digitalRead(17) && digitalRead(18) )){
    Serial.println("Move Backward")
    path +='B'
    back(1);
    GreenLightArea();
    } else{
    m3.run(BACKWARD);
    m4.run(BACKWARD);
    delay(1000);      // do something
    }
  }

  // RIGHT/RIGHT-T CONDITION [0 0 1 1 1 1] - SINGLE CONDITION-------------------------
  if ( digitalRead(16) && digitalRead(17) && digitalRead(18) && digitalRead(19)){
    Serial.println("Move Left")
    path += 'R';
    Right(1);
    GreenLightArea();
  }

  // LEFT/LEFT-T CONDITION [1 1 1 1 0 0] - SINGLE CONDITION-------------------------
  if (digitalRead(14) && digitalRead(15) && digitalRead(16) && digitalRead(17) ){
    if
    Serial.println("Move Left")
    path += 'L';
    Left(1);
    GreenLightArea();
  }

  // CROSS CONDITION [1 1 1 1 1 1] - SINGLE CONDITION-------------------------
  if (digitalRead(14) && digitalRead(15) && digitalRead(16) && digitalRead(17) && digitalRead(18) && digitalRead(19)){
    Serial.println("Move Forward")
    front(1);
    GreenLightArea();
  }

  // HALT CONDITION [1 0 0 0 0 1] - SINGLE CONDITION-------------------------
  if (digitalRead(14) && !digitalRead(15) && !digitalRead(16) && !digitalRead(17) && !digitalRead(18) && digitalRead(19)){
    Serial.println("Stop")
    halt(2);
    RedLightArea();
  }

  // U-TURN CONDITION [0 0 0 0 0 0] - SINGLE CONDITION-------------------------
  if (!digitalRead(14) && !digitalRead(15) && !digitalRead(16) && !digitalRead(17) && !digitalRead(18) && !digitalRead(19)){
    Serial.println("Performing U-Turn");
    uTurn(1);
    GreenLightArea();
  }

  // Move SLIGHT RIGHT CONDITION 
  if(digitalRead(14) || digitalRead(15)){
    Serial.println("move slight left")
    Left();
  }
  // Move SLIGHT LEFT CONDITION
    if(digitalRead(18) || digitalRead(19)){
    Serial.println("move slight right")
    Right();
  }

}