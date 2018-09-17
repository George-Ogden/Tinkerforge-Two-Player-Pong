HOST = "localhost"
PORT = 4223
UID = "A1k" # Change XYZ to the UID of your Linear Poti Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_linear_poti import BrickletLinearPoti

ipcon = IPConnection() # Create IP connection
lp = BrickletLinearPoti(UID, ipcon) # Create device object

ipcon.connect(HOST, PORT) # Connect to brickd
# Don't use device before ipcon is connected

def get_value():
    
    # Get current position
    position = lp.get_position()
    return position / 100 # Range: 0 to 100
