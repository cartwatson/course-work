'''
    Jethro C Watson
    CS 1400 - 3
    Assn 10
'''

# Add Import Statement(s) as needed #

import turtle
from chessboardOOP import Chessboard

# End Add Import Statement(s) #


def main():
    # Add Code to get input from user #

    startX, startY = eval(input("Enter starting coordinates: "))

    width = input("Enter width: ")
    height = input("Enter height: ")

    # End Add Code to get input from user #
    tr = turtle.Turtle()

    if width == "" and height == "":
        chessboard = Chessboard(tr, startX, startY)
    elif height == "":
        chessboard = Chessboard(tr, startX, startY, width=eval(width))
    elif width == "":
        chessboard = Chessboard(tr, startX, startY, height=eval(height))
    else:
        chessboard = Chessboard(tr, startX, startY, eval(width), eval(height))

    chessboard.draw()


main()
