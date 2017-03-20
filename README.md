# Pi-Cam-NeoPixel
Crude script written to be utilized by OctoPrint events

How to use
----------
Place the pi_cam_neopixel_control.py file where ever you like. Then for the
different effects, I just create a link to the python file with the name of
effect I want.

For instance, to have an effect of turning the camera LEDs on to full white:
    ln -s pi_cam_neopixel_control.py camon

Then I can run it as:
    sudo ./camon

If you look through the hokey if statements at the bottom, you should be able to
figure out how to create your links.
