#!/usr/bin/env python

import os
import time
from neopixel import Adafruit_NeoPixel, Color, ws

COUNT = 12
PIN = 18  # GPIO Pin 18 for Data In
FREQ = 800000  # LED signal frequency in hertz (usually 800khz)
DMA = 5  # DMA channel to use for generating signal
BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
INVERT = False  # Invert signal if using NPN transistor level shift
CHANNEL = 0
#STRIP = ws.SK6812_STRIP_RGBW
STRIP = ws.SK6812W_STRIP


def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=1000):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


if __name__ == '__main__':
    strip = Adafruit_NeoPixel(
        COUNT,
        PIN,
        FREQ,
        DMA,
        INVERT,
        BRIGHTNESS,
        CHANNEL,
        STRIP
    )
    strip.begin()
    runtype = os.path.basename(__file__)
    if runtype == 'off':
        colorWipe(strip, Color(0, 0, 0, 0), 0)
        colorWipe(strip, Color(0, 0, 0), 0)
    elif runtype == 'camon':  # Turn on WHITE for camera
        strip.setBrightness(75)
        colorWipe(strip, Color(255, 255, 255, 255), 0)
    elif runtype == 'heating':
        theaterChase(strip, Color(127, 0, 0))
    elif runtype == 'cooling':
        theaterChase(strip, Color(0, 0, 127))
    elif runtype == 'rainbow':
        rainbow(strip)
    elif runtype == 'cycle':
        rainbowCycle(strip)
    elif runtype == 'chase':
        theaterChaseRainbow(strip)
