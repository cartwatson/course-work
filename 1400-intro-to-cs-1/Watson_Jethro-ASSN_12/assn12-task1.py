import turtle

global tr
tr = turtle.Turtle()


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def drawFace(self):
        tr.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    def changeMouth(self):
        # self.__smile = False if self.__smile else True
        if self.__smile:
            self.__smile = False
        else:
            self.__smile = True
        self.drawFace()

    def changeEmotion(self):
        self.__happy = False if self.__happy else True
        self.drawFace()

    def changeEyes(self):
        self.__darkEyes = False if self.__darkEyes else True
        self.drawFace()

    def __drawHead(self):
        tr.goto(0, 0)
        if self.__happy:
            tr.fillcolor("Yellow")
        else:
            tr.fillcolor("Red")
        tr.pu()
        tr.seth(270)
        tr.fd(100)
        tr.seth(0)
        tr.pd()
        tr.begin_fill()
        tr.circle(100)
        tr.end_fill()
        tr.pu()

    def __drawMouth(self):
        tr.pensize(8)
        if self.__smile:
            tr.pu()
            tr.goto(-55, -50)
            tr.seth(315)
            tr.pd()
            tr.circle(80, 90)
            tr.pu()
        else:
            tr.pu()
            tr.goto(55, -50)
            tr.seth(135)
            tr.pd()
            tr.circle(80, 90)
            tr.pu()
        tr.pensize(1)

    def __drawEyes(self):
        tr.pu()
        tr.goto(-40, 30)
        tr.seth(0)
        if self.__darkEyes:
            tr.fillcolor("Black")
        else:
            tr.fillcolor("Blue")
        tr.pd()
        tr.begin_fill()
        tr.circle(10)
        tr.end_fill()
        tr.pu()
        tr.goto(40, 30)
        tr.seth(0)
        tr.pd()
        tr.begin_fill()
        tr.circle(10)
        tr.end_fill()
        tr.pu()
        tr.fillcolor("Black")


def main():
    face = Face()
    face.drawFace()

    done = False
    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    tr.hideturtle()
    turtle.done()


main()
