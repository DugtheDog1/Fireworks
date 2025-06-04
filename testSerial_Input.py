import serial
import time

# Change 'COM3' to your Arduino's serial port
ser = serial.Serial('COM9', 9600)
time.sleep(2)  # Wait for Arduino reset

def send_led_command(led_index, state):
    """
    led_index: 0-based LED index (0 to 51)
    state: True for ON, False for OFF
    """
    if 0 <= led_index < 52:
        ser.write(bytes([led_index]))
        ser.write(bytes([1 if state else 0]))
        print(f"Sent command: LED {led_index + 1} {'ON' if state else 'OFF'}")
    else:
        print(f"Invalid LED index: {led_index}")

print("Enter commands in the format: <LED number> <ON/OFF>")
print("Example: 5 ON  (turns LED 5 on)")
print("Type 'exit' to quit")

try:
    while True:
        user_input = input("Command: ").strip()
        if user_input.lower() == 'exit':
            break

        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid format. Please enter: <LED number> <ON/OFF>")
            continue

        led_str, state_str = parts
        if not led_str.isdigit():
            print("LED number must be a digit.")
            continue

        led_num = int(led_str)
        if not (1 <= led_num <= 52):
            print("LED number must be between 1 and 52.")
            continue

        state_str = state_str.lower()
        if state_str not in ['on', 'off']:
            print("State must be 'ON' or 'OFF'.")
            continue

        led_index = led_num - 1
        state = True if state_str == 'on' else False

        send_led_command(led_index, state)

finally:
    ser.close()
    print("Serial connection closed.")
