#!/usr/bin/python3

import lights
import argparse
import signal

# LED strip configuration:
LED_COUNT = 297        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def exit_handler(signum,frame):
    print('Leaving')
    exit(0)


# Process arguments
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
parser.add_argument('-l', '--loop', action='store_true', help='loop')

args = parser.parse_args()

signal.signal(signal.SIGTERM,exit_handler)

colour = lights.randomColor()

print(colour)

