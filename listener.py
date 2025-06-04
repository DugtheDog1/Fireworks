import time
from sacn import sACNreceiver

receiver = sACNreceiver()
receiver.start()
receiver.join_multicast(1)  # Universe 1

last_state = [0] * 5

@receiver.listen_on('universe', universe=1)
def callback(packet):
    data = packet.dmxData
    print("Received DMX data for Universe 1:")
    
    for i in range(5):
        val = data[i]
        state = "ON" if val > 127 else "OFF"
        
        # Print if the state changed
        if (val > 127 and last_state[i] == 0) or (val <= 127 and last_state[i] == 1):
            print(f"  Channel {i+1}: {val} → {state}")
            last_state[i] = 1 if val > 127 else 0

print("Listening for E1.31 data on Universe 1... Press Ctrl+C to quit.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    receiver.stop()
    print("\nStopped listening.")
