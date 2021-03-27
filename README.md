# huion_setup
A python script to configure the Huion Inspiroy H610PROv2 to a single monitor.

COORDINATES
The coordinates selected are specific for my setup, so modifying the arguments
passed to the xinput command to match a given display configuration is solely 
the responsibility of the user of the script.

XINPUT ERROR: DEVICE NOT FOUND
If the stylus hasn't been placed close enough to the Huion tablet to activate
it since the last time it was connected, xinput will not be able to locate the
stylus.  The solution is to place the tip of the stylus very close to the
Huion drawing tablet and run the script again.
