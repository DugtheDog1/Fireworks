import serial
import time

SERIAL_PORT = 'COM9'  # Change this to your Arduino port
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2)  # Wait for Arduino reset
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
except Exception as e:
    print(f"Error opening serial port: {e}")
    exit(1)

print("Type a letter to send to Arduino (e.g., 'A' to turn LED1 ON, 'a' to turn LED1 OFF). Type 'q' to quit.")

try:
    while True:
        cmd = input("Send command: ").strip()
        if cmd.lower() == 'q':
            break
        if len(cmd) != 1 or not cmd.isalpha():
            print("Please enter a single letter (A-Z or a-z).")
            continue
        ser.write(cmd.encode())
        print(f"Sent '{cmd}'")
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser.close()
    print("Serial port closed.")
