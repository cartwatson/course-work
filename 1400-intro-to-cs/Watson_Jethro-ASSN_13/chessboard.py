class Chessboard:
    def __init__(self, tr, startX, startY, width=250, height=250):
        self.__tr = tr
        self.__startX = startX
        self.__startY = startY
        self.__width = width
        self.__height = height

    def draw(self):
        self.__tr.hideturtle()
        self.__tr.speed(0)
        self.__tr.pu()
        self.__tr.setpos(self.__startX, self.__startY)
        self.__tr.pd()
        self.__tr.pos()
        # draw outside of chessboard
        self.__tr.seth(0)
        self.__tr.fd(self.__width)
        self.__tr.right(90)
        self.__tr.fd(self.__height)
        self.__tr.right(90)
        self.__tr.fd(self.__width)
        self.__tr.right(90)
        self.__tr.fd(self.__height)
        self.__tr.right(90)
        # draw mini squares
        self.__drawAll()

    def __drawAll(self):
        smallW = self.__width / 8
        smallH = self.__height / 8
        self.__tr.pu()
        self.__tr.home()
        self.__tr.setpos(self.__startX, self.__startY - self.__height)
        # draw all rectangles
        for x in range(2):
            # draw rectangle
            for h in range(4):
                # draw columns
                for w in range(4):
                    # draw rows
                    self.__drawRectangle()
                self.__tr.seth(90)
                self.__tr.fd(smallH * 2)
                self.__tr.seth(180)
                self.__tr.fd(self.__width)
            self.__tr.setpos(self.__startX + smallW, self.__startY - smallH * 7)

    def __drawRectangle(self):
        smallW = self.__width / 8
        smallH = self.__height / 8
        self.__tr.seth(0)
        self.__tr.begin_fill()
        self.__tr.fd(smallW)
        self.__tr.left(90)
        self.__tr.fd(smallH)
        self.__tr.left(90)
        self.__tr.fd(smallW)
        self.__tr.left(90)
        self.__tr.fd(smallH)
        self.__tr.left(90)
        self.__tr.end_fill()
        self.__tr.fd(smallW * 2)
