#include <AccelStepper.h>

const int numVariables = 3;
int variables[numVariables];


//AccelStepper Xaxis(1, 2, 5); // pin 2 = step, pin 5 = direction
//AccelStepper Yaxis(1, 3, 6); // pin 3 = step, pin 6 = direction
//AccelStepper Zaxis(1, 4, 7); // pin 4 = step, pin 7 = direction

AccelStepper Xaxis(1, 2, 5); // pin 3 = step, pin 6 = direction
AccelStepper Yaxis(1, 3, 6); // pin 4 = step, pin 7 = direction
AccelStepper Zaxis(1, 4, 7); // pin 5 = step, pin 8 = direction

int xTarget, yTarget, zTarget;

void setup() {
  Serial.begin(9600);  // Set the baud rate to match the Python script
  Xaxis.setMaxSpeed(150);
  Yaxis.setMaxSpeed(1200);
  Zaxis.setMaxSpeed(1200);
  Xaxis.setAcceleration(50);
  Yaxis.setAcceleration(50);
  Zaxis.setAcceleration(1000);

  Xaxis.setSpeed(550);
  Yaxis.setSpeed(500);
  Zaxis.setSpeed(500);
  Xaxis.moveTo(0);
  Yaxis.moveTo(0);
  Zaxis.moveTo(0);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming data until a newline character is received
    String data = Serial.readStringUntil('\n');
    
    // Split the received data into individual variables
    int index = 0;
    int start = 0;
    for (int i = 0; i < data.length(); i++) {
      if (data.charAt(i) == ',') {
        variables[index] = data.substring(start, i).toInt();
        start = i + 1;
        index++;
      }
    }
    // Assign the last variable
    variables[index] = data.substring(start).toInt();
    Xaxis.moveTo(variables[0]);
    Yaxis.moveTo(variables[1]);
    Zaxis.moveTo(variables[2]);
    
    // Process the received variables as needed
    // Example: Print the received variables

  }
  Xaxis.run();
  Yaxis.run();
  Zaxis.run();
}
