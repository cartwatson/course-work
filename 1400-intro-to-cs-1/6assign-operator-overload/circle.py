import turtle


class circle:
    def __init__(self, radius, posX, posY, color):
        self.__radius = radius
        self.__X = posX
        self.__Y = posY
        self.__color = color
        self.__tr = turtle.Turtle()

    def draw(self):
        self.__tr.ht()
        self.__tr.pu()
        self.__tr.goto(self.__X, self.__Y)
        self.__tr.seth(270)
        self.__tr.fd(self.__radius)
        self.__tr.seth(0)
        self.__tr.fillcolor(self.__color)
        self.__tr.color(self.__color)
        self.__tr.pd()
        self.__tr.begin_fill()
        self.__tr.circle(self.__radius)
        self.__tr.end_fill()
        self.__tr.pu()

    def clear(self):
        self.__tr.reset()
