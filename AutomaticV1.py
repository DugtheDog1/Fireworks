import time
import serial
from sacn import sACNreceiver

# --- Setup Serial to Arduino ---
# Change 'COM3' to your Arduino's serial port
ser = serial.Serial('COM9', 9600)
time.sleep(2)  # Wait for Arduino reset

num_leds = 52
last_state = [0] * num_leds  # Track last known LED state (0=OFF,1=ON)

def send_led_command(led_index, state):
    """
    led_index: 0-based LED index (0 to 51)
    state: True for ON, False for OFF
    """
    if 0 <= led_index < num_leds:
        ser.write(bytes([led_index]))
        ser.write(bytes([1 if state else 0]))
        print(f"Sent command: LED {led_index + 1} {'ON' if state else 'OFF'}")
    else:
        print(f"Invalid LED index: {led_index}")

# --- Setup sACN receiver ---
receiver = sACNreceiver()
receiver.start()
receiver.join_multicast(1)  # Listen on Universe 1

@receiver.listen_on('universe', universe=1)
def callback(packet):
    data = packet.dmxData
    # Limit data length to num_leds
    data = data[:num_leds]

    print("Received DMX data for Universe 1:")
    for i, val in enumerate(data):
        new_state = 1 if val > 127 else 0
        if new_state != last_state[i]:
            state_str = "ON" if new_state == 1 else "OFF"
            print(f"  Channel {i+1}: {val} → {state_str}")
            last_state[i] = new_state
            send_led_command(i, new_state == 1)

print("Listening for E1.31 data on Universe 1... Press Ctrl+C to quit.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    receiver.stop()
    ser.close()
    print("\nStopped listening and closed serial connection.")
