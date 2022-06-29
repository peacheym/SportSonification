
/*
  
*/

#include <SPI.h>
#include <SD.h>
#include <Arduino_LSM6DS3.h>

// Pin 10 for Adafruit breakout board.
const int chipSelect = 10;

void setup() {
  Serial.begin(9600);
  while (!Serial);
  
  Serial.println("Initializing IMU...");
  
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }


  Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);
  }
  Serial.println("card initialized.");

}

void loop() {
  float x, y, z;

  // make a string for assembling the data to log:
  String dataString = "0,0,0";


  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
    dataString = String(x) + "," + String(y) + "," + String(z);
    Serial.println(dataString);
  }

  File dataFile = SD.open("datalog.txt", FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    // print to the serial port too:
    Serial.println(dataString);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  }

  
}
