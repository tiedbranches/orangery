#include <SPI.h>
#include <AccelStepper.h>

AccelStepper stepper(1,3,2);
AccelStepper stepper2(1,5,4);
AccelStepper stepper3(1,7,6);
AccelStepper stepper4(1,9,8);
AccelStepper stepper5(1,11,10);


const byte buffSize = 40;
char inputBuffer[buffSize];
const char startMarker = '<';
const char endMarker = '>';
const char incMarker = '.';
const char commMarker = ')';
const char testMarker = 'a';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newDataFromPC = false;

char messageFromPC[buffSize] = {0};
char dest;
int stepDest = 0;
int stepDest2 = 0;
int stepDest3 = 0;
int stepDest4 = 0;
int stepDest5 = 0;
int maxspeed = 2000;
int accel = 2000;

unsigned long curMillis;

unsigned long prevReplyToPCmillis = 0;
unsigned long replyToPCinterval = 1000;




void getDataFromPC() {

    // receive data from PC and save it into inputBuffer
    
  if(Serial.available() > 0) {

    char x = Serial.read();

      // the order of these IF clauses is significant
      
    if (x == endMarker) {
      readInProgress = false;
      newDataFromPC = true;
      inputBuffer[bytesRecvd] = 0;
      Serial.println("Dest");
      parseDest();
    }

    else if (x == incMarker) {
      readInProgress = false;
      newDataFromPC = true;
      inputBuffer[bytesRecvd] = 0;
      Serial.println("Inc");
      parseInc();
    }

    else if (x == commMarker) {
      readInProgress = false;
      newDataFromPC = true;
      inputBuffer[bytesRecvd] = 0;
      Serial.println("Comm");
      parseComm();
      Serial.println("Comm2");
    }
    
    if(readInProgress) {
      inputBuffer[bytesRecvd] = x;
      bytesRecvd ++;
      if (bytesRecvd == buffSize) {
        bytesRecvd = buffSize - 1;
      }
    }

    if (x == startMarker) { 
      bytesRecvd = 0; 
      readInProgress = true;
    }
  }
}


void parseInc() {

  Serial.println("Inside INC");
    
  char * strtokIndx; // this is used by strtok() as an index
  
  strtokIndx = strtok(inputBuffer,",");      // get the first part - the destination
  dest = atoi(strtokIndx); //

  if (dest == 5) {
    stepDest2 -= 100;
  }

  else if (dest == 8) {
    stepDest2 += 100;
  }
  
  else if (dest == 4) {
    stepDest += 100;
  }
  
  else if (dest == 7) {
    stepDest -= 100;
  }

  else if (dest == 9) {
    stepDest3 += 100;
  }
  
  else if (dest == 6) {
    stepDest3 -= 100;
  }

  else if (dest == 1) {
    stepDest4 += 100;
  }

    else if (dest == 0) {
     stepDest4 -= 100;

  }

    else if (dest == 2) {
    stepDest5 += 100;
  }

    else if (dest == 3) {
    stepDest5 -= 100;
  }


}

void zeroSteppers() {
  stepper.setCurrentPosition(0);
  stepper2.setCurrentPosition(0);
  stepper3.setCurrentPosition(0);
  stepper4.setCurrentPosition(0);
  stepper5.setCurrentPosition(0);

  stepDest = 0;
  stepDest2 = 0;
  stepDest3 = 0;
  stepDest4 = 0;
  stepDest5 = 0;
  Serial.println("Zeroed in ZeroSteppers");
  delay(2000);
  Serial.println("Zeroed in ZeroSteppers after wait");
}

void parseComm() {

  Serial.println("Zeroed in parseComm MEGAOBEN");
    
  char * strtokIndx; // this is used by strtok() as an index
  
  strtokIndx = strtok(inputBuffer,",");      // get the first part - the destination
  dest = atoi(strtokIndx); //
  Serial.println("Zeroed in parseComm OBEN");
  if (dest == 0) {
    zeroSteppers();
    Serial.println("Zeroed in parseComm");
  }
}


void parseDest() {

    // split the data into its parts
    
  char * strtokIndx; // this is used by strtok() as an index
  
  strtokIndx = strtok(inputBuffer,",");      // get the first part - the destination
  stepDest=atoi(strtokIndx); // 
  
  strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
  stepDest2 = atoi(strtokIndx);     // convert this part to an integer
  
  strtokIndx = strtok(NULL, ","); 
  stepDest3 = atoi(strtokIndx);     // convert this part to another int

  strtokIndx = strtok(NULL, ","); 
  stepDest4 = atoi(strtokIndx);     // convert this part to another int

  strtokIndx = strtok(NULL, ","); 
  stepDest5 = atoi(strtokIndx);     // convert this part to another int
}


void replyToPC() {

  if (newDataFromPC) {
    newDataFromPC = false;
    Serial.print("<Msg ");
    Serial.print(messageFromPC);
    Serial.print(" New Speed ");
    Serial.print(maxspeed);
    Serial.print(" Stepper Dest ");
    Serial.print(stepDest);
    Serial.print(" StepperDest2 ");
    Serial.print(stepDest2);
    Serial.print(" Time ");
    Serial.print(curMillis >> 9); // divide by 512 is approx = half-seconds
    Serial.println(">");
  }
}


void updateSpeedAndAccel() {
  stepper.setMaxSpeed(maxspeed);
  stepper.setAcceleration(accel);

  stepper2.setMaxSpeed(maxspeed);
  stepper2.setAcceleration(accel);

  stepper3.setMaxSpeed(maxspeed);
  stepper3.setAcceleration(accel);

  stepper4.setMaxSpeed(maxspeed);
  stepper4.setAcceleration(accel);

  stepper5.setMaxSpeed(maxspeed);
  stepper5.setAcceleration(accel);
}


void updateStepperPos() {

  stepper.moveTo(stepDest);
  stepper2.moveTo(stepDest2);
  stepper3.moveTo(stepDest3);
  stepper4.moveTo(stepDest4);
  stepper5.moveTo(stepDest5);
  

}



void moveStepper() {
  stepper.run();
  stepper2.run();
  stepper3.run();
  stepper4.run();
  stepper5.run();

  }


void setup() {
  Serial.begin(115200);

  delay(500);
  stepper.setCurrentPosition(0);
  stepper2.setCurrentPosition(0);
  stepper3.setCurrentPosition(0);
  stepper4.setCurrentPosition(0);
  stepper5.setCurrentPosition(0);

}

void loop() {

  curMillis = millis();
 
  getDataFromPC();
  
  updateSpeedAndAccel();
  updateStepperPos();
  
  //replyToPC(); //unread replies cause trouble i.e full buffer

  moveStepper();
  //moveStepper();
  //moveStepper();
  //moveStepper();
  //moveStepper();
  
  
}
