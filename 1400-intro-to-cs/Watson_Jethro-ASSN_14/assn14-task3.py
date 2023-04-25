from circle import circle
from rectangle import rectangle


def main():
    done = False
    shapes = list()

    while not done:
        menu = eval(input("1: Enter Circle\n2: Enter Rectangle\n3: Remove shape\n4: Draw Shapes\n5: Exit\nSelection: "))
        if menu == 1:
            posX, posY = eval(input("Enter starting pos: "))
            radius = eval(input("Enter radius: "))
            color = "black"
            while color != "red" or "yellow" or "green" or "blue":
                color = input("Enter color: ").lower()
                if color == "red":
                    break
                elif color == "yellow":
                    break
                elif color == "green":
                    break
                elif color == "blue":
                    break
                else:
                    print("Invalid color selection. Valid colors include: red, yellow, blue, and green.")
            shapes.append(circle(radius, posX, posY, color))
        elif menu == 2:
            posX, posY = eval(input("Enter starting pos: "))
            height = eval(input("Enter height: "))
            width = eval(input("Enter width: "))
            color = "black"
            while color != "red" or "yellow" or "green" or "blue":
                color = input("Enter color: ").lower()
                if color == "red":
                    break
                elif color == "yellow":
                    break
                elif color == "green":
                    break
                elif color == "blue":
                    break
                else:
                    print("Invalid color selection. Valid colors include: red, yellow, blue, and green.")
            shapes.append(rectangle(height, width, posX, posY, color))
        elif menu == 3:
            print("Shapes in Queue: ", end="")
            print(len(shapes))
            removeMenu = eval(input("To remove a shape input it's placement: "))
            removeMenu -= 1
            shapes[removeMenu].clear()
            del shapes[removeMenu]
        elif menu == 4:
            shapeCount = len(shapes)
            for i in range(shapeCount):
                shapes[i].clear()
            for i in range(shapeCount):
                shapes[i].draw()
        elif menu == 5:
            print("Thanks for Drawing!")
            done = True
        else:
            print("Invalid Selection")


main()