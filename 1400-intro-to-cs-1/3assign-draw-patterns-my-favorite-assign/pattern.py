# import turtle and random modules
import turtle
import random


def setup():
    # create global turtle
    global tr
    tr = turtle.Turtle()
    # create global turtle screen
    global sc
    sc = turtle.Screen()

    # turtle go fast
    tr.speed(0)
    # turtle window 1000 x 800
    sc.screensize(1000, 800, "#000000")
    # pen up
    tr.pu()
    # bye bye turtle
    tr.hideturtle()


def reset():
    # clear screen
    tr.clear()
    # reset turtle
    tr.reset()
    # pen up
    tr.pu()
    # bye bye turtle
    tr.hideturtle()
    # turtle go fast
    tr.speed(0)


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    angle = 0
    for i in range(count):
        # random color
        clr = setRandomColor()
        tr.pencolor(clr)

        # move to center
        tr.goto(centerX, centerY)
        tr.seth(0)

        # adjust for next circle
        angle += 360 / count
        tr.seth(angle)

        # adjust offset
        tr.fd(offset)

        # adjust rotation
        tr.left(rotation)

        # call drawRectangle
        drawRectangle(width, height)


def drawRectangle(width, height):
    tr.pd()
    # draw a single rectangle
    for i in range(2):
        tr.fd(width)
        tr.left(90)
        tr.fd(height)
        tr.left(90)
    tr.pu()


def drawCirclePattern(centerX, centerY, offset, radius, count):
    angle = 0
    for i in range(count):
        # random color
        color = setRandomColor()
        tr.pencolor(color)

        # move to center
        tr.goto(centerX, centerY)
        tr.seth(0)

        # adjust for next circle
        angle += 360 / count
        tr.seth(angle)

        # adjust offset
        tr.fd(offset)

        # draw circle
        drawCircle(radius)


def drawCircle(radius):
    tr.pd()
    tr.circle(radius)
    tr.pu()


def drawSuperPattern(num=1):
    for i in range(num):
        # randomly draw rectangle and circle patterns
        shape = random.randint(1, 2)
        if shape == 1:
            # generate random valid rectangle values
            centerX = random.randint(-400, 400)
            centerY = random.randint(-300, 300)
            offset = random.randint(-100, 100)
            width = random.randint(0, 200)
            height = random.randint(0, 200)
            count = random.randint(0, 100)
            rotation = random.randint(-180, 180)
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        if shape == 2:
            # generate random valid circle values
            centerX = random.randint(-400, 400)
            centerY = random.randint(-300, 300)
            offset = random.randint(-100, 100)
            radius = random.randint(0, 100)
            count = random.randint(0, 100)
            drawCirclePattern(centerX, centerY, offset, radius, count)


def setRandomColor():
    # no parameters
    # at least three colors
    clr = random.randint(1, 3)
    if clr == 1:
        # light blue
        return "#0a47b2"
    elif clr == 2:
        # light pink
        return "#f266bd"
    elif clr == 3:
        # dark blue
        return "#ffffff"


def done():
    turtle.done()
