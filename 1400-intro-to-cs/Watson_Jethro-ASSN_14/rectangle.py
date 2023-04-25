import turtle


class rectangle:
    def __init__(self, height, width, posX, posY, color):
        self.__height = height
        self.__width = width
        self.__X = posX
        self.__Y = posY
        self.__color = color
        self.__tr = turtle.Turtle()

    def draw(self):
        self.__tr.ht()
        self.__tr.pu()
        self.__tr.goto(self.__X, self.__Y)
        self.__tr.fillcolor(self.__color)
        self.__tr.color(self.__color)
        self.__tr.pd()
        self.__tr.begin_fill()
        self.__tr.seth(0)
        for i in range(2):
            self.__tr.fd(self.__width)
            self.__tr.left(90)
            self.__tr.fd(self.__height)
            self.__tr.left(90)
        self.__tr.end_fill()
        self.__tr.pu()

    def clear(self):
        self.__tr.reset()
