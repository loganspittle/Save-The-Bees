#include <ESP32Servo.h>
#include <HardwareSerial.h>

// Define servo objects
Servo servo1;
Servo servo2;

// Define buffer for incoming NMEA sentences
const int BUFFER_SIZE = 100;
char nmeaBuffer[BUFFER_SIZE];
int bufferIndex = 0;

// Define servo pins
const int servo1Pin = 18;  // Adjust as needed
const int servo2Pin = 17;  // Adjust as needed
const int laserPin = 14;  // Adjust as needed

// Function to parse NMEA sentence and control servos
void parseNMEA(char* sentence) {
    if (sentence[0] == '$' && strchr(sentence, '*') != NULL) {
        int int1, int2, int3;
        if (sscanf(sentence + 1, "%d,%d,%d*", &int1, &int2, &int3) == 3) {
            // Ensure values are within servo range (0-180)
            int1 = constrain(int1, 0, 180);
            int2 = constrain(int2, 0, 180);
            int3 = constrain(int3, 0, 1);
            
            servo1.write(int1);
            servo2.write(int2);
            digitalWrite(laserPin, int3);

            Serial.print("Servo 1 set to: ");
            Serial.println(int1);
            Serial.print("Servo 2 set to: ");
            Serial.println(int2);
        } else {
            Serial.println("Error: Invalid NMEA format");
        }
    } else {
        Serial.println("Error: Invalid NMEA sentence");
    }
}

void setup() {
    // Initialize serial communication
    Serial.begin(9600);
    
    // Attach servos to their respective pins
    servo1.attach(servo1Pin);
    servo2.attach(servo2Pin);
    
    // Initialize servos to middle position
    servo1.write(90);
    servo2.write(90);

    // Initialize laser pin
    pinMode(laserPin, OUTPUT);
    digitalWrite(laserPin, LOW);
    
    Serial.println("System ready. Waiting for NMEA sentences...");
}

void loop() {
    while (Serial.available() > 0) {
        char inChar = Serial.read();
        if (inChar == '$') {
            // Start of a new NMEA sentence
            bufferIndex = 0;
        }
        
        if (bufferIndex < BUFFER_SIZE - 1) {
            nmeaBuffer[bufferIndex++] = inChar;
            nmeaBuffer[bufferIndex] = '\0';  // Null-terminate the string
        }
        
        if (inChar == '*') {
            // End of NMEA sentence, parse it
            parseNMEA(nmeaBuffer);
            bufferIndex = 0;  // Reset buffer
        }
    }
}
