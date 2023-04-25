'''
    Jethro C Watson
    CS 1400 - 3
    Assn 10
'''

# Add Import Statement(s) as needed #

from chessboard import drawChessboard

# End Add Import Statement(s) #


def main():
    # Add Code to get input from user #

    startX, startY = eval(input("Enter starting coordinates: "))

    width = input("Enter width: ")
    height = input("Enter height: ")

    # End Add Code to get input from user #

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()
