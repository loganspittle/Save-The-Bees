#include <ESP32Servo.h>

// Define servo objects
Servo servo1;
Servo servo2;

// Define servo pins
const int servo1Pin = 18;  // Adjust as needed
const int servo2Pin = 17;  // Adjust as needed

void setup() {
    // Attach servos to their respective pins
    servo1.attach(servo1Pin);
    servo2.attach(servo2Pin);
}

void loop() {
    // Sweep from 0 to 180 degrees
    for (int angle = 0; angle <= 180; angle++) {
        servo1.write(angle);
        servo2.write(angle);
        delay(20); // Adjust delay for smoother motion
    }

    // Sweep from 180 to 0 degrees
    for (int angle = 180; angle >= 0; angle--) {
        servo1.write(angle);
        servo2.write(angle);
        delay(20);
    }
}