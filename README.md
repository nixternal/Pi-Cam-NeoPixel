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

Look at the lines in the python script that say "runtype == 'xxxx'". The 'xxxx'
part is what you want to name your links. Yeah, cheap hack, I know. Was just
being quick to test the NeoPixel and never got around to doing this properly. It
works, and I forgot about it :)

If you look through the hokey if statements at the bottom, you should be able to
figure out how to create your links.

OctoPrint config.yaml events
----------------------------
    events:
      enabled: true
      subscriptions:
      - command: sudo ~/myscripts/off && sudo ~/myscripts/camon
        event: PrintStarted
        type: system
      - command: sudo ~/myscripts/off && sudo ~/myscripts/chase
        event: MovieRendering
        type: system
      - command: sudo ~/myscripts/off && sudo ~/myscripts/off
        event: MovieDone
        type: system
      - command: sudo ~/myscripts/off && sudo ~/myscripts/off
        event: Shutdown
        type: system
      - command: sudo ~/myscripts/off && sudo ~/myscripts/off
        event: Disconnected
        type: system
      - command: sudo ~/myscripts/off && sudo ~/myscripts/off
        event: Startup
        type: system
