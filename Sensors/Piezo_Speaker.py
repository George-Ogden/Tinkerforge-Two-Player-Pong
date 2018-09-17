HOST = "localhost"
PORT = 4223
UID = "C5K" # Change XYZ to the UID of your Piezo Speaker Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_piezo_speaker import BrickletPiezoSpeaker

ipcon = IPConnection() # Create IP connection
ps = BrickletPiezoSpeaker(UID, ipcon) # Create device object

ipcon.connect(HOST, PORT) # Connect to brickd
# Don't use device before ipcon is connected
def set_value(time):
    # Make 2 second beep with a frequency of 1kHz
    ps.beep(time*1000, 1000)
