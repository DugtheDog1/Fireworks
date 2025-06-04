import serial
import time

SERIAL_PORT = 'COM9'  # Change this to your Arduino's port
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2)  # Wait for Arduino to reset
    print(f"Successfully opened serial port {SERIAL_PORT} at {BAUD_RATE} baud.")
    ser.close()
except serial.SerialException as e:
    print(f"SerialException: Could not open port {SERIAL_PORT}: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
