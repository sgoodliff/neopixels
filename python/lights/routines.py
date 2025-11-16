
import random
import time
from rpi_ws281x import Color

def test():
	print("test")
	
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


def testing(strip,gap=20,wait_ms=1000):

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

def explosion(strip, wait_ms=100):
    print('explosion')

    left = randomColor()
    right = randomColor()
    length = strip.numPixels()

    for l in range(strip.numPixels()):
       # print('led:' + str(l))
        print('left led ' + str(length - l) + ' right led '+ str(l))

        strip.setPixelColor( (length - l) , left)
        strip.setPixelColor( l,right)

        strip.show()


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

