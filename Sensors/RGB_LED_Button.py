HOST = "localhost"
PORT = 4223
UID = "Do7" # Change XYZ to the UID of your RGB LED Button Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_button import BrickletRGBLEDButton

ipcon = IPConnection() # Create IP connection
rlb = BrickletRGBLEDButton(UID, ipcon) # Create device object

ipcon.connect(HOST, PORT) # Connect to brickd
# Don't use device before ipcon is connected

def set_value(r,g,b):
    # Set light blue color
    rlb.set_color(r, g, b)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_value():
    state = rlb.get_button_state()
    if state == rlb.BUTTON_STATE_PRESSED:
        return 1
    elif state == rlb.BUTTON_STATE_RELEASED:
        return 0
