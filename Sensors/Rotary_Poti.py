HOST = "localhost"
PORT = 4223
UID = "y5q" # Change XYZ to the UID of your Rotary Poti Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_poti import BrickletRotaryPoti

ipcon = IPConnection() # Create IP connection
rp = BrickletRotaryPoti(UID, ipcon) # Create device object

ipcon.connect(HOST, PORT) # Connect to brickd
# Don't use device before ipcon is connected

def get_value():
    

    # Get current position
    position = rp.get_position()
    return (position + 150) / 300 # Range: -150 to 150
