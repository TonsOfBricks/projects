"""
Author: Nikita Sinkha
File: inscribe_poly.py
Date: 09/20/2017
"""

import math as m
import turtle as t

Polys = int(input("Number of polygons(0 to quit):"))#Takes the number of sides for the first polygon

def main():
	"""
	func: main()
	Executes the program in ordered steps to produce a favorable
	outcome
	"""
	if Polys == 0:
		exit()
	else:
		init()
		print("The total distance traveled by the turtle is:", "%.2f" %  drawPolys(150,Polys), "units.") # "%.2f" % Helps format the number of decimal places
		t.done()

def init():
	"""
	func: init()
	Initializes the canvas and sets the turtles speed for easier and faster drawing.
	"""
	t.setworldcoordinates(-getWorldBorder(), -getWorldBorder(), getWorldBorder(),  getWorldBorder())
	t.up()

def getWorldBorder():
	"""
	func: getWorldBorder():
	Returns a value of 200 which is used to define a border for the ruetle window
	"""
	return 200

def color(n):
	"""
	func: color():
	This function assigns different colors to different shapes using the modulus function
	param1 = n -> The number of polygon, which decides its color	
	"""
	if not(n%3):
		t.pencolor('green')
	elif not(n%2):
		t.pencolor('light blue')
	else:
		t.pencolor('magenta')

def newRad(r, N):
	"""
	func: newRad():
	Generates a new radius for the inner circles by using the cosines law
	param1 = r
	param2 = N
	"""
	c = m.sqrt((r*r)+(r*r)-2.0*r*r*m.cos((2*m.pi)/N))
	return m.sqrt((r*r)-((c/2)*(c/2)))


def drawPoly(r, N):
	"""
	func: drawPoly():
	Draws a polygon inside a circle using iteration
	param1 = r -> radius
	param2 = N -> Number of iterations to be made
	"""
	n = N 
	c = m.sqrt((r*r)+(r*r)-2.0*r*r*m.cos((2*m.pi)/N))
	t.forward(r)
	t.left(180-(180*((N-2)/N))/2)   
	t.down()
	while n > 0:
		t.forward(c)
		t.left(360/N)
		n -= 1
	t.right(180-(180*((N-2)/N))/2)
	t.pencolor('black')
	t.left(90)
	t.circle(r)
	t.right(90)
	t.up()
	t.back(r)
	return c*N

def drawPolys(r, N, s = 0):
	"""
	func: drawPolys():
	Draws the final figure with the polygons drawn in the circles of correct radii and return the distance traveled by the turtle
	param1 = r
	param2 = N
	param3 = s = 0 -> s is the distance traveled by turtle. It is 0 at the start.
	"""
	if N < 3:
		return s
	else:
		color(N)
	return drawPolys(newRad(r, N), N-1, s+drawPoly(r,N))  	

if __name__ == '__main__':
	main()


"""
Thank You
"""
