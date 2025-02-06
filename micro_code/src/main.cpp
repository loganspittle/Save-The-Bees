#include <ESP32Servo.h>

// Create a Servo object
Servo myServo;

// Define the servo pin
const int servoPin = 25;

// Define positions
const int servoStartPosition = 0;  // Start position in degrees
const int servoEndPosition = 90;  // End position in degrees

void setup() {
  // Attach the servo to the pin and define the PWM frequency range
  myServo.attach(servoPin, 500, 2400); // Attach pin with min and max pulse widths in microseconds
  
  // Move servo to the start position
  myServo.write(servoStartPosition);
  delay(1000);  // Wait for 1 second
}

void loop() {
  // Move servo to the end position
  myServo.write(servoEndPosition);
  delay(1000);  // Wait for 1 second

  // Move servo back to the start position
  myServo.write(servoStartPosition);
  delay(1000);  // Wait for 1 second
}