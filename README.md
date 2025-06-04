# Fireworks


DMX to Arduino LED Control - Setup & Requirements
=================================================
----------------------
1. Python Installation
- Install Python 3.7 or newer:
  https://www.python.org/downloads/
----------------------
2. Python Package Dependencies
- Open a command prompt or terminal and run:
  pip install pyserial sacn

  Packages:
  - pyserial : For serial communication with Arduino
  - sacn     : To listen for E1.31 (sACN) DMX data streams
----------------------
3. Arduino IDE
- Download and install Arduino IDE:
  https://www.arduino.cc/en/software
----------------------
4. Arduino Drivers
- Make sure Arduino USB drivers are installed.
- For most Arduino boards, drivers install automatically with the IDE.
- If not, check Arduino's official website for your board's drivers.
----------------------
5. Hardware Setup
- Use an Arduino Uno or compatible board.
- Connect LEDs to digital pins 2 through 53 as per your sketch.
- Connect Arduino to PC via USB cable.
----------------------
6. COM Port Configuration
- Find your Arduino COM port on the new PC (Windows Device Manager or equivalent).
- Update the Python script serial port (e.g., 'COM3', 'COM9') accordingly.
----------------------
7. Network Setup for sACN (E1.31) Data
- Ensure multicast UDP port 5568 is allowed through your firewall.
- Use xLights or compatible software to send DMX data to Universe 1.
- The Python script listens to Universe 1 multicast to receive DMX data.
----------------------
8. Running the Project
- Upload the Arduino sketch to your Arduino board via the Arduino IDE.
- Run the Python script on your PC.
- The Python script receives DMX data and sends corresponding serial commands to Arduino.
- Arduino turns LEDs ON/OFF according to received commands.
----------------------
9. Troubleshooting Tips
- Confirm correct COM port and baud rate (9600) in Python script.
- Check USB cable and connections.
- Verify LEDs wired to correct Arduino pins matching the sketch.
- Allow multicast traffic on your network.
- Restart Arduino IDE and Python script if connection issues occur.

---


