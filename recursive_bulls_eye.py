"""
Author: Nikita Sinkha
File: bulls_eye.py
Date: 1/22/2018
"""
import turtle as t

def init(r):
    """
    func: init()
    This function initializes the canvas for drawing the desired figures.
    param1: r -> distance to be traveled to centralize the figure
    """
    t.hideturtle()
    t.speed(0)
    t.up()
    t.home()
    t.right(90)
    t.forward(r)
    t.left(90)

def bulls_eye(r, n):
    """
    func: bulls_eye()
    Function draws a bullseye using the method of recursion.
    param1: r -> radius
    param2: n -> number of concentric circles
    """
    init(r)
    if n != 0:
        width = r/n
        t.down()
        if n%2 == 0:
            t.begin_fill()
            t.circle(r)
            t.color('red')
            t.end_fill()
        else:
            t.begin_fill()
            t.circle(r)
            t.color('black')
            t.end_fill()
        bulls_eye(r-width, n-1)
    else:
        pass

def drawSquare(r):
    """
    func: drawSquare(r)
    A helper function that is used to draw squares used in bulls_eye_square()
    function.
    param1: r -> half length of a side
    """
    t.forward(r)
    t.left(90)
    t.forward(2*r)
    t.left(90)
    t.forward(2*r)
    t.left(90)
    t.forward(2*r)
    t.left(90)
    t.forward(r)

def bulls_eye_square(r, n):
    """
    func: bulls_eye_square()
    Function draws a square bullseye using the method of recursion.
    param1: r -> length of side
    param2: n -> number of concentric squares
    """
    init(r)
    if n != 0:
        width = r/n
        t.down()
        if n%2 == 0:
            t.begin_fill()
            drawSquare(r)
            t.color('red')
            t.end_fill()
        else:
            t.begin_fill()
            drawSquare(r)
            t.color('black')
            t.end_fill()
        bulls_eye_square(r-width, n-1)
    else:
        pass

def main():
    """
    func: main()
    The main function contains the sequence in which commands
    have to be executed.
    """
    r = float(input("Enter the raduis of bullseye:"))
    n = int(input("Number of concentric circles:"))
    bulls_eye(r, n)
    cont = str(input("Press Enter key to continue"))
    if cont is "":
        t.reset()
        t.hideturtle()
        r = float(input("Enter the length of bullseye:"))
        n = int(input("Number of concentric squares:"))
        bulls_eye_square(r, n)
        close = str(input("Press Enter key to exit"))
        if close is "":
            exit()
        else:
            t.done()
    else:
        t.done()

if __name__ == '__main__':
    """
    Main Function is executed when called.
    """
    main()
