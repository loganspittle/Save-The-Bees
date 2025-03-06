import serial 
from serial import Serial

class SerialInterface:
    def __init__(self, port, baudrate, debug=False):
        self.port = port
        self.baudrate = baudrate
        self.debug = debug
        if debug:
            print(f"Opening serial port {port} with baud rate {baudrate}")
        else:
            self.ser = Serial(port, baudrate, timeout=1)

    def send_nmea_sentence(self, servo1, servo2, laser):
        # Create NMEA sentence
        sentence = f"${servo1},{servo2},{laser}*"
        
        # Send NMEA sentence
        if self.debug:
            print(f"Sending NMEA sentence: {sentence}")
        else:
            self.ser.write(sentence.encode('ascii'))

    def close(self):
        # Close serial port
        if self.debug: 
            print("Closing serial port")
        else:
            self.ser.close()

# # Example usage
# if __name__ == "__main__":
#     port = '/dev/ttyUSB0'  # Replace with your serial port
#     baudrate = 9600  # Replace with your baud rate
#     servo1 = 123
#     servo2 = 456
#     laser = 789
    
#     interface = SerialInterface(port, baudrate)
#     interface.send_nmea_sentence(servo1, servo2, laser)
#     interface.close()