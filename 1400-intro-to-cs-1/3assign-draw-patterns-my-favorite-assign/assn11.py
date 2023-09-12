'''
    Jethro Watson
    CS 1400
    ASSN 11
'''

# import pattern and all its functions
import pattern


def main():
    # Setup pattern
    pattern.setup()

    # Play again loop
    playAgain = True

    # enter loop
    while playAgain:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle Patterns'
        if mode == 1:
            ### inputs ###
            # center position
            centerX, centerY = eval(input("Enter the center position: "))

            # offset
            offset = eval(input("Enter the offset: "))

            # height
            height = eval(input("Enter the height: "))

            # width
            width = eval(input("Enter the width: "))

            # count
            count = eval(input("Enter the number of rectangles: "))

            # rotation
            rotation = eval(input("Enter the rotation: "))

            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            ### inputs ###
            # center position
            centerX, centerY = eval(input("Enter the center position: "))

            # offset
            offset = eval(input("Enter the offset: "))

            # radius
            radius = eval(input("Enter the radius: "))

            # count
            count = eval(input("Enter the number of circles: "))

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:

            num = input("Enter number of spirals: ")

            if num == "":
                pattern.drawSuperPattern()
            else:
                pattern.drawSuperPattern(eval(num))

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        #### Add Statement(s) to clear drawings and play again ####
        if response == 1:
            playAgain = True
        elif response == 2:
            playAgain = True
            pattern.reset()
        elif response == 3:
            playAgain = False
        #### End Add Inputs Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()
