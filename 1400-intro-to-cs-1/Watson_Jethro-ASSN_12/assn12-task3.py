from Blobber import Blobber
import time


def main():
    name = input("name: ")
    color = input("color: ")
    radius = input("radius: ")
    height = input("height: ")
    if radius == "" and height == "":
        blobber = Blobber(name, color)
    elif radius == "":
        height = eval(height)
        blobber = Blobber(n=name, c=color, h=height)
    elif height == "":
        radius = eval(radius)
        blobber = Blobber(name, color, radius)
    else:
        radius = eval(radius)
        height = eval(height)
        blobber = Blobber(name, color, radius, height)

    startTime = time.time()
    done = False
    while not done:
        print("Main Menu")
        print("\t(1): Display Name")
        print("\t(2): Change Name")
        print("\t(3): Display Color")
        print("\t(4): Change Color")
        print("\t(5): Feed Blobber")
        print("\t(6): Blobber Speak")
        print("\t(7): Exit")
        menu = eval(input("Make a selection please: "))

        if menu == 1:
            print("My name is " + blobber.getName())
        elif menu == 2:
            new = input("Input new name: ")
            blobber.setName(new)
        elif menu == 3:
            print("My color is " + blobber.getColor())
        elif menu == 4:
            new = input("Input new color: ")
            blobber.setColor(new)
        elif menu == 5:
            food = eval(input("How much would you like to feed " + blobber.getName() + "? "))
            blobber.feedBlobber(food)
            if blobber.vitalsOk(startTime):
                continue
            else:
                print("You over fed your blobber and it died")
                break
        elif menu == 6:
            print(blobber.blobberSpeak(startTime))
        elif menu == 7:
            break

        # check vitals after decision
        if blobber.vitalsOk(startTime):
            startTime = time.time()
        else:
            print("Your blobber starved and died")
            break


main()