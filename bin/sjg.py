#!/usr/bin/env python3

import time
import os
import signal
import random
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 297        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def exit_handler(signum,frame):
    print('Leaving')
    colorWipe(strip, Color(0, 0, 0), 10)
    exit(0)


def randomColor():
	r = random.randint(0,255) 
	g = random.randint(0,255)
	b = random.randint(0,255)
	#print(str(r) + '/' + str(g) + '/' + str(b) )
	return Color(r,g,b)

# Define functions which animate LEDs in various ways.

def doubleWhoosh(strip,color,wait_ms=50):
   gap = 10
   a = randomColor()
   b = randomColor()
   c = randomColor()
   for i in range(strip.numPixels()):


       strip.setPixelColor(i, a)
       strip.setPixelColor( gap + i, b)
       strip.setPixelColor( gap + gap +i , c)  

       strip.show()
       time.sleep(wait_ms / 1000.0)

       strip.setPixelColor(i - 1, Color(0,0,0))
       strip.setPixelColor( (gap + i) -  1, Color(0,0,0)) 
       strip.setPixelColor( (gap + gap + i) -  1, Color(0,0,0))


def test(strip,gap=20,wait_ms=20):

    for i in range(strip.numPixels()):

        strip.setPixelColor(i,randomColor())    
        strip.setPixelColor(gap + i,randomColor())
        strip.setPixelColor(gap + gap + i,randomColor()) 
       
        strip.show() 
        time.sleep(wait_ms / 1000.0)

        strip.setPixelColor(i - 1, Color(0,0,0))
        strip.setPixelColor( (gap + i) -  1, Color(0,0,0))
        strip.setPixelColor( (gap + gap + i) -  1, Color(0,0,0))
        print("finish")

def whoosh(strip,color,reverse=False,wait_ms=50):

   if reverse == False:
        for i in range(strip.numPixels()):
             strip.setPixelColor(i, color)
             strip.setPixelColor(i + 1,color)

             strip.show()
             time.sleep(wait_ms / 1000.0)
             strip.setPixelColor(i - 1, Color(0, 0, 0))

   else:
       for i in reversed(range(strip.numPixels())):
             strip.setPixelColor(i, color)
             strip.setPixelColor(i - 1,color)
             strip.show()
             time.sleep(wait_ms / 1000.0)
             strip.setPixelColor(i + 1, Color(0, 0, 0))

def stripe(strip, color_low,color_high, wait_ms=50):

	leds = strip.numPixels()		
	for i in range(strip.numPixels()):

		strip.setPixelColor(i, color_low)
		strip.show()

		strip.setPixelColor(leds - i,color_high)
		strip.show()

		time.sleep(wait_ms / 1000.0)

def stripeBrightness(strip, wait_ms=100):

    leds = strip.numPixels()

    for i in range(strip.numPixels()):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        #print(str(r) + '/' + str(g) + '/' + str(b) )

        strip.setPixelColor(i, Color(r,g,b))
        strip.show()

        strip.setPixelColor(leds - i,Color(r,g,b))
        strip.show()
        time.sleep(wait_ms / 1000.0) 

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50,reverse=False):
    """Wipe color across display a pixel at a time."""
    if reverse == True:
        for i in reversed(range(strip.numPixels())):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
    else:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(
                (int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def routine():

	print('whoosh')
	doubleWhoosh(strip,randomColor(),25)
	whoosh(strip,randomColor(),False,25)
	whoosh(strip,randomColor(),True,25)

	print('stripe animation')
	stripe(strip,randomColor(),randomColor())

	print('Color wipe animations.')
	colorWipe(strip, Color(255, 0, 0),100)  # Red wipe
	colorWipe(strip, Color(0,255,0),100,True)

	colorWipe(strip, Color(0, 0, 255),100)  # Green wipe
	colorWipe(strip, Color(255, 0, 0),100,True)  # Blue wipe

	print('Theater chase animations.')
	theaterChase(strip, Color(127, 127, 127),100)  # White theater chase
	theaterChase(strip,Color(0,0,127),100)

	theaterChase(strip, Color(127, 0, 0))  # Red theater chase
	theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
	print('Rainbow animations.')
	rainbow(strip)
	rainbowCycle(strip)
	theaterChaseRainbow(strip)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('-l', '--loop', action='store_true', help='loop')

    args = parser.parse_args()

    signal.signal(signal.SIGTERM,exit_handler)

    pid = str(os.getppid())
    with open('/var/run/sjg.pid','w') as file:
          file.write(pid)

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        if args.loop:
            while True:
                 print("looping")
                 routine()
        else:
            stripeBrightness(strip)
            #test(strip)

    except KeyboardInterrupt:
        if args.clear:
           colorWipe(strip, Color(0, 0, 0), 10)
