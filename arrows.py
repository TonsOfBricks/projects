"""
Author: Nikita Sinkha
File: arroes.py
Date:3/2/2018
"""


import turtle as t
import random as r
import math as m

def border():
        """
        func: border()
        Draws a border of size 500x500.
        """
        t.pencolor("blue")
        t.forward(500)
        t.left(90)
        t.forward(500)
        t.left(90)
        t.forward(500)
        t.left(90)
        t.forward(500)
        t.pencolor("black")

def init():
        """
        func: init()
        Initializes the canvas for the turtle to draw.
        """
        t.speed(0)
        t.home()
        t.setworldcoordinates(-250, -250, 250, 250)
        t.up()
        t.goto(-250, -250)
        t.down()
        border()
        t.up()
        t.home()
        t.down()

def triangles(s):
        """
        func: traingles()
        A function made to draw triangles with a side s.
        param1: s -> Side of the triangles
        """
        t.forward(s)
        t.left(120)
        t.forward(2*s)
        t.left(120)
        t.forward(2*s)
        t.left(120)
        t.forward(s)

def size():
        """
        func: size()
        Function made to randomize the length of the triangles side.
        """
        s = r.randint(1, 30)
        return s

def angle():
        """
        func: angle()
        Gives a random angle for the turtle to move after every
        recursive call
        """
        a = r.randint(0, 360)
        return a

def length():
        """
        func: length()
        Length function desides the amount that the turtle moves forward
        after every recursive call
        """
        l = r.randint(1, 100)
        return l

def colors():
        """
        func: colors()
        Randomizes the colors for the triangles after every recursive call
        """
        c = r.random()
        return c

def max_num():
        """
        func: max_num():
        Returns a value of 500 for using as a limit of maximum user input
        """
        return 500

def drawFigureRec(n, area=0):
        """
        func: drawFigureRec():
        Draws triangles recursively one after the other at different angles and
        distnaces
        param1: n -> number of triangles
        param2: area = 0 -> Area counter
        """
        t.down()
        s = size()
        if n > 0:
                t.begin_fill()
                t.color(colors(), colors(), colors())
                triangles(s)
                temp = ((m.sqrt(3)/4)*s**2)
                t.end_fill()
                t.up()
                t.forward(length())
                t.left(angle())
                if (t.xcor() > 200 or t.ycor() > 200 or t.xcor()
                    < -200 or t.ycor() < -200):
                        t.home()
                        t.forward(length())
                        t.left(angle())
                        return drawFigureRec(n-1, area+temp)
                else:
                        return drawFigureRec(n-1, area+temp)
        else:
                return area

def main():
        """
        func: main()
        This function executes the program in order to produce favorable
        outcome
        """
        area = 0
        lim = max_num()
        num = int(input("Enter the number of triangles to be drawn (0-500):"))
        if num <= lim:
                init()
                print("Total area covered by the turtle:",
                drawFigureRec(num, area), "square units.")
                print("Number of triangles:", num)
                print("Thank you!")
                t.done()
        else:
                print("Enter a number less than 500")
                return main()


if __name__ == '__main__' :
        main()
