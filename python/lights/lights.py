
import random

def randomColor():
	r = random.randint(0,255) 
	g = random.randint(0,255)
	b = random.randint(0,255)

	return Color(r,g,b)