import time
from micro_interface import SerialInterface
from keyboard_interface import KeyboardInterface, keyboard

micro_interface = SerialInterface('/dev/ttyUSB0', 9600, debug=True)
keyboard_interface = KeyboardInterface()
servo1 = 90     # Set initial servo positions (0-180)
servo2 = 90     # Set initial servo positions (0-180)
laser = 0       # Set initial laser state (0 or 1)

if __name__ == "__main__":
    keyboard_interface.start()
    try:
        print("Press 'esc' to exit...")
        while True:
            if keyboard.is_pressed('esc'):
                print("Exiting...")
                break
            
            if keyboard_interface.is_key_pressed('up'):
                # print("Up key is pressed!")
                servo1 = min(180, servo1 + 1)
            if keyboard_interface.is_key_pressed('down'):
                # print("Down key is pressed!")
                servo1 = max(0, servo1 - 1)
            if keyboard_interface.is_key_pressed('left'):
                # print("Left key is pressed!")
                servo2 = max(0, servo2 - 1)
            if keyboard_interface.is_key_pressed('right'):
                # print("Right key is pressed!")
                servo2 = min(180, servo2 + 1)
            if keyboard_interface.is_key_pressed('center'):
                # print("Center (space) key is pressed!")
                laser = 1 - laser
            
            micro_interface.send_nmea_sentence(servo1, servo2, laser)
            time.sleep(0.05)  # Small delay to prevent excessive CPU usage
    finally:
        micro_interface.close()
        keyboard_interface.stop()
